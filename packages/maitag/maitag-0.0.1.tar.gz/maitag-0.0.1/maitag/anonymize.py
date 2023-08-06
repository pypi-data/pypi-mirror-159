import copy
import json
import logging
import re
import yaml
import random

from sentence_transformers import SentenceTransformer
from sklearn.metrics import confusion_matrix
# from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import numpy as np
import pandas as pd
from pathlib import Path

from .fake_identities import generate_nationality_names
from .spacy_language_model import nlp

log = logging.getLogger(globals().get("__file__", "__main__.ipynb"))
log.setLevel(logging.WARNING)

pd.options.display.max_columns = 1048


sns.set_style("white")
sns.set_theme("notebook")

# FIXME: move to constants.py
BASE_DIR = Path(globals().get("__file__", ".")).resolve().absolute().parent
while not BASE_DIR.name.startswith("mait") and len(str(BASE_DIR)) > 3:
    BASE_DIR = BASE_DIR.parent
DATA_DIR = BASE_DIR.parent / "mait_private" / "data"
DATA_DIR_PRIVATE = DATA_DIR / "private"
DATA_DIR_PUBLIC = DATA_DIR / "public"

FILEPATH = DATA_DIR_PRIVATE / "utterance_intent_pairs_revised.csv"
ANON_FILEPATH = DATA_DIR_PUBLIC / "utterance_intent_pairs_anonymized.csv"

# SBERT used for encoding/embedding sentences/utterances
# https://www.sbert.net/
sbert = SentenceTransformer("paraphrase-MiniLM-L6-v2")


PII_TAG_ROWS = {}  # PII_TAG_ROWS = load_pii_tag_rows() updates this below


def load_pii_tag_rows(filepath=FILEPATH, expected_num_tags=9, expected_num_rows=194):
    """Maria and Hobson found some PII by manually reviewing the first Maya utterance dataset

    Returns:
      pii_tag_rows (dict): dictionary of tag: list_of_row(utterance)_ids
    """
    pii_tag_rows = {}
    filepath = Path(filepath).with_suffix(".yaml")

    for attempts in range(2):
        if filepath:
            if filepath.is_file():
                with filepath.open("rt") as fin:
                    pii_tag_rows = yaml.full_load(fin)
        else:
            filepath = Path(FILEPATH).with_suffix(".yaml")

        num_rows_tagged = sum(len(v) for v in pii_tag_rows.values())
        if (
            len(pii_tag_rows) >= expected_num_tags
            and num_rows_tagged >= expected_num_rows
        ):
            print("The pii_tag_rows database seems to be up to date with {num_rows_tagged} tagged rows.")
            return pii_tag_rows

        print("TAGGED ROWS DATABASE SEEMS TO BE OUT OF DATE")
        print(f"Tags in file: {list(pii_tag_rows.keys())}")
        print(f"Total number of tagged rows: {num_rows_tagged}")
        # maria found these in the small (1098-row) dataset
        name_rows = [189, 536, 665]
        # maria found these in the small (1098-row) dataset
        name_rows += [1018, 910, 916, 1047, 884, 801, 1035, 487]
        # found on 2nd review by Hobson and Maria
        name_rows += [885, 728]
        phone_rows = [801]
        url_rows = list(range(278, 333))

        age_rows = [1079]

        location_rows = []
        birthday_rows = []
        email_rows = []

        pii_tag_rows = {
            "pii": [],
            "person name": name_rows,
            "spam": url_rows,
            "url": url_rows,
            "phone number": phone_rows,
            "location": location_rows,
            "birthday": birthday_rows,
            "age": age_rows,
            "email": email_rows,
        }

        pii_tag_rows["pii"] = set(pii_tag_rows.get("pii") or set())
        for tag_str, row_ids in pii_tag_rows.items():
            pii_tag_rows["pii"] = sorted(set(pii_tag_rows["pii"]).union(set(row_ids)))
        print("SAVING AN UPDATED TAG DATABASE")
        print(f"Tags in file: {list(pii_tag_rows.keys())}")
        print(f"Total number of tagged rows: {num_rows_tagged}")

        with filepath.open("wt") as fout:
            yaml.dump(pii_tag_rows, fout)
    return pii_tag_rows


PII_TAG_ROWS = load_pii_tag_rows()


def interactively_tag_rows(df, batch_size=10, tag_str="pii", weights=None):
    """Samples the df and ask the labeler (human) to identify row numbers that should be tagged

    Use `weights` to focus your sampling on likely candidates for the tag.
    Outputs a list of row ids (index values) that the user would like to tag.

    >>> interactively_tag_rows(df, weights=model.predict_proba(df['utterance'])
    [42, ...]

    """
    tagged_rows = []
    while True:
        print("=" * 10 + "ROWS ALREADY TAGGED {tag_str}" + "=" * 10)
        print(json.dumps(df.iloc[tagged_rows].to_dict(), indent=2))
        print("=" * 10 + "random rows" + "=" * 10)
        print(json.dumps(df.sample(batch_size, weights=weights).to_dict(), indent=2))
        resp = input(
            r"Enter an int row number that looks like PII (negative value to remove row, [ENTER] to resample, x or exit to exit):\n"
        )
        if "x" in resp:
            break
        tagged_rows.extend([int(s) for s in resp.split()])
        tagged_rows = sorted(set(tagged_rows))
    return tagged_rows


def tag_rows(df, row_ids, tag_str):
    tags = [
        sorted(set(x).union({tag_str})) if i in row_ids else sorted(set(x))
        for i, x in zip(df.index, df["tags"])
    ]
    df["tags"] = tags
    return df


def encode(s):
    return sbert.encode(s)


def add_pii_tags(df, pii_tag_rows):
    # # Human:
    # ## Skim utterances and find row numbers for utterances that contain PII (name, age, phone, SSN, URLs)

    # ### Skip this if you already have a list of rows with PII (names & phone numbers)

    #
    # Skim utterances and find row numbers for utterances that contain PII (name, age, phone, SSN, URLs)
    # ## create dict containing tag_name: row_nums for each PII type

    # all tags are for PII
    pii_rows = set()
    for tag_str, row_ids in pii_tag_rows.items():
        pii_rows = pii_rows.union(set(row_ids))
        df = tag_rows(df, row_ids=row_ids, tag_str=tag_str)

    pii_rows = sorted(pii_rows)

    # if no pii_rows predefined then run the interactive tagger
    if not len(pii_rows) or len(df) != 1094:
        pii_rows = interactively_tag_rows(df, pii_rows)

    pii_tag_rows["pii"] = pii_rows
    # before dumping to json or yaml, need to convert sets to list
    pii_tag_rows = {k: sorted(set(v)) for k, v in pii_tag_rows.items()}

    df = tag_rows(df, row_ids=pii_tag_rows['pii'], tag_str="pii")

    return df


def print_tag_examples(df, pii_tag_rows):
    # display example PII utterances for each tag
    for tag_str, row_ids in pii_tag_rows.items():
        print("=" * 10 + " TAG: " + tag_str + " " + "=" * 10)
        for u in df["utterance"].loc[row_ids]:
            print(u)

    # display the PII rows of the DataFrame
    print(df.loc[pii_tag_rows["pii"]])


def load_utterances(filepath=FILEPATH):
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"FILEPATH: {FILEPATH}")
    print(f"FILEPATH.is_file(): {FILEPATH.is_file()}")
    # data/private/utterance_intent_pairs_revised.csv
    df = pd.read_csv(filepath)
    df = df[["utterance", "intent"]].copy()
    df["intent"] = (
        df["intent"].str.lower().str.strip().str.replace(" ", "_").str.replace("-", "_")
    )
    # print(df.shape)
    df["utterance"] = df["utterance"].fillna("")
    df["intent"] = df["intent"].fillna("unknown")
    df["tags"] = df["intent"].str.split(",")
    df["tags"] = df["tags"].apply(
        lambda x: sorted(set([str.strip(t).lower().replace("_", " ") for t in x]))
    )
    # counts = pd.Series(Counter(df["intent"].values)).sort_values()
    # print(counts)
    # df

    if "contains_pii" in df.columns:
        df = df.drop("contains_pii", axis=1)
    if "contains_name" in df.columns:
        df = df.drop("contains_name", axis=1)

    name_rows = sorted(set(PII_TAG_ROWS["person name"]))
    contains_name = np.array([False] * len(df))
    contains_name[name_rows] = True
    df["contains_name"] = contains_name
    df.iloc[name_rows]
    return df


def suggest_rows(df=None, pii_tag_rows=PII_TAG_ROWS, tag_str='person name'):
    r""" Machine assisted intent tagging (curation = utterance tag CRUD) """
    if df is None:
        df = load_utterances()
    print(df.tail())

    # ### Skip this if you already have a list of rows with PII (names & phone numbers)
    X = pd.DataFrame([sbert.encode(s) for s in df["utterance"]])
    X.shape

    print(X[:10])

    y = df["contains_name"].astype(bool)
    print(y[:10])

    num_names = y.sum()
    num_nonnames = num_names * 5
    X_train = pd.concat([X[y], X[~y].sample(num_nonnames)])
    y_train = [True] * num_names + [False] * num_nonnames
    X_train.shape, len(y_train)

    model = LogisticRegression(class_weight="balanced")
    model.fit(X_train, y_train)
    model.score(X, y)

    y_pred = model.predict(X)
    for i, row in df[y_pred & ~df["contains_name"]].iterrows():
        print(f"{i:6}:  {row['utterance']}")


def add_contains_column(df, pii_tag_rows=PII_TAG_ROWS, tag_str='person name'):

    # # Skim the list above to find additional PII

    tag_str = tag_str if tag_str in pii_tag_rows else list(pii_tag_rows.keys())[0]
    name_rows = pii_tag_rows[tag_str]
    for i in name_rows:
        print(f"{i:6}:  {df.iloc[i]['utterance']}")

    contains_name = [False] * len(df)
    for i in name_rows:
        print(i, df["utterance"].iloc[i])
        contains_name[i] = True
    df[f"contains_{tag_str.replace(' ', '_')}"] = contains_name
    print(df.iloc[name_rows])
    return df


# # URLs found using a liberal regex

URL_REGEX = r"[hH]?[tTfF][tT][pP][sS]?:[/]{1,4}[^)\s]+"


def regex_row_ids(series_or_df, tag_regex=URL_REGEX, tag_str='url'):
    if isinstance(series_or_df, pd.DataFrame):
        series = series_or_df["utterance"]
    else:
        series = series_or_df
    is_match = series.str.contains(tag_regex)
    match_row_ids = list(series_or_df.index.values[is_match])
    return match_row_ids


def curate_urls(df=None, filepath=FILEPATH, pii_tag_rows=None, tag_regex=URL_REGEX, tag_str='url'):
    df = load_utterances(filepath) if df is None else df
    pii_tag_rows = load_pii_tag_rows(filepath) if pii_tag_rows is None else pii_tag_rows
    df = add_contains_column(df, pii_tag_rows=pii_tag_rows, tag_str='person name')
    url_row_ids = regex_row_ids(df['utterance'], tag_regex=tag_regex, tag_str=tag_str)
    tag_rows(df, url_row_ids, tag_str='url')
    print(url_row_ids)
    return df

    # df['intent'].iloc[url_rows] = [
    #     f'url_len_{url_len}' for url_len
    #     in df['utterance'].iloc[url_rows].str.extract(r'(' + URL_REGEX + r')')[0].str.len()
    # ]
    # df.iloc[url_rows]

    # # Find names similar to human-labeled PII


META = {'pii_tag_rows': PII_TAG_ROWS, 'names': ['Dimitri', 'Raj']}


def load_private_meta(filepath=FILEPATH, meta=META):
    filepath = Path(filepath).with_suffix('.meta.yaml')
    meta = copy.deepcopy(meta)
    if filepath.is_file():
        with open(filepath) as fin:
            meta.update(yaml.full_load(fin))
    else:
        with open(filepath, 'wt') as fout:
            yaml.dump(meta, fout)
    return meta


META = load_private_meta()

NAMES = META.get('names', [])

ORGANIZATIONS = ("Human Rights Organization",)
ORGANIZATIONS = META.get('ORGANIZATIONS', ORGANIZATIONS)

TITLES = ("Municipal Coordinator",)
TITLES = META.get('ORGANIZATIONS', TITLES)

STR_FUNS = (str, str.lower, str.title, str.upper)


def anonymize_names(
        series=None,
        names=None,
        generate_names=iter(generate_nationality_names()),
        full_given_sur="sur"):
    if names is None:
        names = NAMES

    full_given_sur = str(full_given_sur).lower().strip()
    if full_given_sur[:3] in ("sur", "las"):  # surname or last name
        full_given_sur = -1
    elif full_given_sur[:3] in ("giv", "fir"):  # given or first name
        full_given_sur = 0
    elif full_given_sur[:3] in ("bot",):  # first last
        full_given_sur = slice(0, 2)
    elif full_given_sur[:3] in ("ful", "all"):  # first last
        full_given_sur = slice(0, None, 1)
    # name_mapping = {}
    name_rows = []
    for name in names:
        for fun in STR_FUNS:
            is_name_row = series.str.contains(fun(name))
            this_name_rows = list(series.index.values[is_name_row])
            name_rows += this_name_rows
            for i, new_name in zip(this_name_rows, generate_names()):
                new_name = " ".join(new_name.split()[full_given_sur])
                name_rows[i].update({name: new_name})
                series.str.replace(name, new_name)
    # TODO: localized name_mapping for each row
    return name_rows


def find_organization_rows(df, titles=TITLES, organizations=ORGANIZATIONS):
    org_rows = []
    is_org_row = pd.Series([False] * len(df), index=df.index)
    for name in titles + organizations:
        for fun in (str, str.lower, str.title, str.upper):
            is_org_row |= df["utterance"].str.contains(name)
        org_rows += list(df.index.values[is_org_row])
        org_rows = list(set(org_rows))
    print(df.iloc[org_rows])


def find_phone_number_rows(df):
    phone_rows = []
    patterns = [r"[0-9]{2}[-_.0123456789]+[0-9]{3}"]
    for pat in patterns:
        is_name_row = df["utterance"].str.contains(pat)
        phone_rows += list(df.index.values[is_name_row])
    print(df.iloc[phone_rows])
    return phone_rows


def anonymize_ages(df, patterns=None, min_age=25, max_age=65, digits_pattern=r'\b[0-9][0-9][0-9]?\b'):
    patterns = patterns if patterns is not None else [
        r"(is|be|age|am|old|'m).*" + digits_pattern,
        digits_pattern + r".*(is|be|age|am|old|'m)",
    ]
    is_age_row = np.array([False] * len(df))
    for pat in patterns:
        is_age_row |= df['utterance'].str.contains(pat)
        df["utterance"] = [
            re.sub(digits_pattern, str(random.randint(min_age, max_age)), s) for s in df["utterance"]
            if re.match(s)
        ]
    return df

    # # Train classifier to find PII


def encode_utterances(df, col_name='utterance'):
    return pd.DataFrame([sbert.encode(s) for s in df[col_name]])


def train_tagger(df, test_size=0.1, random_state=42, model_class=LogisticRegression, **hyperparams):
    # Y_sbert = pd.DataFrame([sbert.encode(s) for s in intents])
    X_sbert = encode_utterances(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X_sbert, df["tag"], test_size=test_size, random_state=random_state
    )
    X_train.shape, len(y_train), X_test.shape, len(y_test)

    if str(model_class) == str(LogisticRegression):
        hyp = dict(
            C=1, class_weight="balanced", random_state=1, max_iter=10000, multi_class="auto"
        )
        hyp.update(hyperparams)
    if str(model_class) == str(SVC):
        hyp = dict(class_weight="balanced", decision_function_shape="ovr")
        hyp.update(hyperparams)

    model = model_class(**hyp)
    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    print(model.score(X_test, y_test))
    print(model.classes_)

    y_test_pred = model.predict(X_test)
    confusion_test = pd.DataFrame(
        confusion_matrix(y_test, y_test_pred, labels=model.classes_),
        index=model.classes_,
        columns=model.classes_,
    )
    print(confusion_test)
    return model


def recognize_names(df, pii_tag_rows=PII_TAG_ROWS):
    pii_rows = pii_tag_rows['pii']
    for s in df["utterance"].iloc[pii_rows]:
        doc = nlp(s)
        print(
            pd.DataFrame([[tok.text, tok.pos_] for tok in doc if tok.pos_ == "PROPN"])
        )

    for s in df["utterance"].iloc[pii_rows]:
        doc = nlp(s)
        print(pd.DataFrame([[tok.text, tok.label] for tok in doc.ents]))

    tok = doc[5]
    tok.ent_type

    # # Redact all PII


def redact_all_names(df, name_lists=(TITLES, ORGANIZATIONS, NAMES), replacement_strs='Maitrole MAITorg Maitperson'.split()):
    assert isinstance(replacement_strs, (list, tuple)), \
        f"type(replacement_strs):{type(replacement_strs)} type(replacement_strs[0]):{type(replacement_strs[0])}\n" \
        "replacement_strs must be a list of strs"
    assert isinstance(name_lists, (list, tuple)), \
        f"type(name_lists):{type(name_lists)} type(name_lists[0]):{type(name_lists[0])}\n" \
        "name_lists must be a list of lists of strs"
    assert len(name_lists) == len(replacement_strs), f"len(name_lists):{len(name_lists)} != len(replacement_strs):{len(replacement_strs)}"
    for names, replacement_str in zip(name_lists, replacement_strs):
        assert isinstance(names, (list, tuple)), "name_lists must be a list of lists of strs"
        print(f'   {len(names)}=>{replacement_str}')
        for name in names:
            print(f'       {name}')
            for fun in STR_FUNS:
                print(f'           {fun}')
                name = fun(name)
                df["utterance"] = df["utterance"].str.replace(name, replacement_str)
    return df


def redact_str_variations(df, str_list, replacement_str, funs=STR_FUNS):
    for name in str_list:
        for fun in funs:
            name = fun(name)
            df["utterance"] = df["utterance"].str.replace(name, replacement_str)
    return df


def redact_pattern(df, pattern, replacement_str):
    df["utterance"] = [
        re.sub(pattern, replacement_str, s) for s in df["utterance"]
    ]
    return df


def redact_urls(df, pattern=URL_REGEX, replacement_str='<URL>'):
    return redact_pattern(df, pattern=URL_REGEX, replacement_str='<URL>')


def load_and_update_utterance_tags(filepath=FILEPATH):
    filepath = Path(filepath)
    df = load_utterances(filepath=filepath)
    df = add_pii_tags(df, pii_tag_rows=PII_TAG_ROWS)
    print_tag_examples(df, pii_tag_rows=PII_TAG_ROWS)
    print(f'UPDATING DB OF UTTERANCES WITH LATEST PII_TAG_ROWS:\n{FILEPATH}')
    with Path(filepath).open('wt') as fout:
        df.to_csv(fout, index=False)
    return df


if __name__ == "__main__":
    df = load_and_update_utterance_tags(filepath=FILEPATH)
    df = redact_all_names(df)
    df = redact_urls(df)

    print('total tags: ', sum(df["tags"].apply(len)))
    print('tail')
    print(df.head())
    print('head')
    print(df.tail())
    print('multiple tag rows')
    print(df[df["tags"].apply(len) > 1])
