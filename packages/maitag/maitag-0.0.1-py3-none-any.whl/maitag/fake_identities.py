# # http://fakenamegenerator.com/
# # https://pypi.org/project/fng-api/
# !pip install fng-api
import json
import logging
from pathlib import Path
import random
import time
import yaml

import pandas as pd
import fng_api

log = logging.getLogger(__name__)

FNG_NAMESETS = dict(
    us='American', ar='Arabic', au='Australian', br='Brazil', celat='Chechen (Latin)', ch='Chinese', zhtw='Traditional Chinese',
    hr='Croatian', cs='Czech', dk='Danish', nl='Dutch', en='England/Wales', er='Eritrean', fi='Finnish', fr='French',
    gr='German', gl='Greenland', sp='Hispanic', hu='Hungarian', ig='Igbo', it='Italian',
    jpja='Japanese', no='Norwegian', fa='Persian', pl='Polish', ru='Russian', rucyr='Russian (Cyrillic)',
    gd='Scottish', sl='Slovenian', sw='Swedish', th='Thai', vn='Vietnamese'
)
FNG_NAMESETS['is'] = 'Icelandic'
FNG_NAMESETS_FICTIONAL = dict(hobbit='Hobbit', tlh='Klingon', ninja='Ninja')

FNG_NAMESET = list(FNG_NAMESETS)

FNG_COUNTRIES = dict(au='Australia', bg='Belgium', br='Brazil', ca='Canada', cyen='Cyprus (Anglicized)',
                     cygk='Cyprus (Greek)', cz='Czech Republic', dk='Denmark', ee='Estonia', fi='Finland', fr='France',
                     gr='Germany', gl='Greenland', hu='Hungary', it='Italy', nl='Netherlands', nz='New Zealand',
                     no='Norway', pl='Poland', pt='Portugal', sl='Slovenia', za='South Africa', sp='Spain', sw='Sweden',
                     sz='Switzerland', tn='Tunisia', uk='United Kingdom', us='United States', uy='Uruguay')
FNG_COUNTRIES.update({'as': 'Austria', 'is': 'Iceland'})  # `as` and `is` are keywords
FNG_COUNTRIES_INCOMPLETE = set(['pt', 'sp', 'tn', 'no', 'sz', 'sl', 'gl', 'bg', 'za', 'nz', 'cz', 'uk',
                                'cygk', 'gr', 'uy', 'br', 'ee', 'nl', 'hu', 'as', 'is', 'au'])
FNG_COUNTRIES_INCOMPLETE = {k: FNG_COUNTRIES.pop(k) for k in FNG_COUNTRIES_INCOMPLETE}
FNG_COUNTRY = list(FNG_COUNTRIES)

FNG_ATTRIBUTES = [
    'address', 'age', 'birthday', 'birthdayDay', 'birthdayMonth', 'birthdayYear', 'blood', 'card', 'city', 'color',
    'company', 'coords', 'countryCode', 'cvv2', 'email', 'expiration', 'guid', 'height', 'heightcm', 'moneygram',
    'motherMaidenName', 'name', 'occupation', 'password', 'phone', 'ssn', 'state',
    'street', 'ups', 'useragent', 'username', 'vehicle', 'website', 'weight', 'weightkg', 'westernunion', 'zip', 'zodiac'
]

FNG_COUNTRY_WITHOUT_NAMESET = [c for c in FNG_COUNTRIES if c not in FNG_NAMESETS]
FNG_COUNTRY_WITH_NAMESET = [c for c in FNG_COUNTRIES if c in FNG_NAMESETS]
FNG_COUNTRY_NAMESET = {c: (c if c in c in FNG_NAMESETS else 'us') for c in FNG_COUNTRIES}
# FNG_COUNTRY_NAMESET.update(dict(bg='gr', za='uk'))
# FNG_COUNTRY_NAMESET.update(dict(uk='ca', nz='au'))
# FNG_COUNTRY_NAMESET.update({'is': 'gl', 'ee': 'ru'})

EXPERIMENTS = []
ENCODER = 'sbert'

DATA_DIR = Path('.') / 'data'
NAMES_DIR = DATA_DIR / 'names'
FILEPATH = DATA_DIR / 'utterance_intent_pairs_revised.csv'
IDENTITIES_YAML_PATH = DATA_DIR / 'identities.yml'
# FILEPATH = DATA_DIR / 'utterance_intent_pairs_augmented.csv'
# FILEPATH = DATA_DIR / 'augumented_utterance_intent_pairs.csv'

# minimum number of example utterance per intent (class label),
#  user will be asked to supply paraphrases to make up the gap
MIN_EXAMPLES = 4


def find_name_rows(
        utterance_series, names, funs=(str, str.lower, str.title, str.upper)):
    """

    >>> name_rows = find_name_rows(series=df["utterance"], names=NAMES)
    >>> print(df.iloc[name_rows])
    """

    name_rows = []
    for name in names:
        for fun in funs:
            is_name_row = utterance_series.str.contains(fun(name))
            name_rows += list(utterance_series.index.values[is_name_row])
    return sorted(set(name_rows))


# # .replace(name, random.choice(list_of_anonymous_names))


def generate_identities(
    min_age=19,
    max_age=75,
    country=FNG_COUNTRY,
    nameset=None,
    pct_male=0.5,
    attributes=FNG_ATTRIBUTES,
):
    country = list(country)
    if isinstance(pct_male, float):
        pct_male = int(pct_male * 100)
    if isinstance(pct_male, int):
        pct_male = str(min(max(int(pct_male * 100), 0), 100))
    pct_male = str(pct_male)
    min_age = str(int(float(min_age)))
    max_age = str(int(float(max_age)))
    attempt = 0
    while True:
        time.sleep(0.67)
        country_choice = random.choice(country)
        if nameset is None:
            nameset_choices = [FNG_COUNTRY_NAMESET[country_choice]]
        else:
            nameset_choices = list(nameset)
        kwargs = dict(
            nameset=nameset_choices,
            country=[country_choice],
            minage=min_age,
            maxage=max_age,
            gender=pct_male,
        )
        everything_dict = {"__kwargs__": json.loads(json.dumps(kwargs))}
        try:
            identity = fng_api.getIdentity(**kwargs)
        except (IndexError, ValueError, RuntimeError) as e:
            identity = None
            log.warning(f"FAILED {attempt} time(s): {e}\nkwargs: {kwargs}")
        if identity is None:
            attempt += 1
            continue
        attempt = 0
        identity_dict = json.loads(json.dumps(vars(identity)))
        everything_dict.update(identity_dict)
        with IDENTITIES_YAML_PATH.open("a") as fout:
            yaml.dump([everything_dict], fout)
        attempt = 0
        yield {k: identity_dict[k] for k in identity_dict if k in attributes}


def get_identity(
        min_age=19, max_age=75, country=FNG_COUNTRY, nameset=FNG_NAMESET, pct_male=0.5):
    """ Get a single identity from FNG API (fakenamegenerator.com)

    TODO: swap the country-nameset for popular countries like 'gr' (germany) and 'br' (belgium)
          country is for the location, nameset is for the nationality/language

    >>> get_identity(nameset=["gr"], country=["us"])
    {'name': '...
    """
    for identity_dict in generate_identities(
        min_age=min_age,
        max_age=max_age,
        country=country,
        nameset=nameset,
        pct_male=pct_male,
    ):
        break
    return identity_dict


def update_cache():
    for i, identity_dict in zip(range(3), generate_identities()):
        print(i, identity_dict)

    cache = yaml.safe_load(IDENTITIES_YAML_PATH.open())
    country_nameset_pairs_that_work = dict(
        [
            (c.get("__kwargs__")["country"][0], c.get("__kwargs__")["nameset"][0])
            for c in cache
            if len(c.get("__kwargs__")["country"]) == 1
        ]
    )
    print(
        f"Cache contains {len(cache)} identities for {len(country_nameset_pairs_that_work)} country_nameset pairs"
    )
    country_nameset_pairs_that_work

    return cache


def generate_fng_names(min_age=19, max_age=75, country=FNG_COUNTRY, nameset=FNG_NAMESET, pct_male=0.5):
    for identity_dict in generate_identities(
            min_age=min_age,
            max_age=max_age,
            country=country,
            nameset=nameset,
            pct_male=pct_male):
        yield identity_dict.get("name", "")


NATIONALITY_NAMES = {}


def load_nationality_names(names_dir=NAMES_DIR):
    """ Load Nation.txt names files """
    nationality_names = {}
    paths = list(Path(names_dir).glob('*.txt'))
    for filepath in paths:
        nation = filepath.with_suffix('').name.lower()
        # filepath = Path(names_dir) / f'{str.title(nation)}.txt'
        if filepath.is_file():
            with filepath.open() as fin:
                names = [s.strip() for s in fin.readlines()]
                nationality_names[nation] = names
        else:
            print(f"ERROR: Can't find the names for nationality {nation} in filepath {filepath}.")
    return nationality_names


NATIONALITY_NAMES.update(load_nationality_names())


def generate_nationality_names(nationality='india', name_type='last'):
    names_df = NATIONALITY_NAMES.get(
        nationality,
        pd.DataFrame([['Smith']], columns=[name_type]))
    while True:
        yield names_df.sample()[name_type]


if __name__ == '__main__':
    CACHE = update_cache
