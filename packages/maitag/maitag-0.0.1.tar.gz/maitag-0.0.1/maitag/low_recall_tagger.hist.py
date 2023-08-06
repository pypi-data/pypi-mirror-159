from collections import Counter
from anonymize import *

pii_tag_rows = load_pii_tag_rows()
df = load_utterances()
df['tags']
counts = [Counter(x) for x in df['tags']]
pd.DataFrame(counts)
pd.DataFrame(counts).astype(int).T.sum()
pd.DataFrame(counts).fillna(0).astype(int).T.sum()
num_tags = pd.DataFrame(counts).fillna(0).astype(int).T.sum()
num_tags[num_tags > 1]
df[num_tags > 1]
len(num_tags[num_tags > 1])
Y
Ytags = pd.DataFrame(counts).fillna(0).astype(int)
Y
Ytags
X
len(Y)
len(Ytags)
Xtags = X
tagger = OneVsRestClassifier(SVC(kernel="linear"))
tagger.fit(Xtags, Ytags)
tagger.score(Xtags, Ytags)
Xcca = CCA(n_components=2).fit(Xtags, Y).transform(Xtags)
tagger
Xcca = CCA(n_components=2).fit(Xtags, Ytags).transform(Xtags)
tagger_cca = tagger.fit(Xcca, Ytags)
plot_subplot(tagger_cca, Xcca, Ytags, 1, "With unlabeled samples + CCA")
plot_subplot(tagger_cca, Xcca, Ytags.values, 1, "With unlabeled samples + CCA")
plt.show()
plot_subplot(tagger_cca, Xcca, Ytags.values, 1, "With unlabeled samples + CCA")
plt.figure(figsize=(16, 6))
plot_subplot(tagger_cca, Xcca, Ytags.values, 1, "With unlabeled samples + CCA")
plt.show()
examples = pd.DataFrame([sbert.encode(s)
                        for s in ["Hi I'm Vishvesh Bhat and OK"]])
tagger.predict(examples)
tagger
tagger = OneVsRestClassifier(SVC(kernel="linear"))
tagger = tagger.fit(Xtags, Ytags)
tagger_cca = tagger_cca.fit(Xcca, Ytags)
tagger_cca = OneVsRestClassifier(SVC(kernel="linear"))
tagger_cca = tagger_cca.fit(Xcca, Ytags)
plt.figure(figsize=(16, 6))
plot_subplot(tagger_cca, Xcca, Ytags.values, 1, "With unlabeled samples + CCA")
plt.show(block=False)
tagger = tagger.fit(Xtags, Ytags)
tagger.predict(examples)
examples
tags
del tags
Ytags
Ytags.columns
pd.DataFrame(tagger.predict(examples), columns=Ytags.columns)
examples_pred = pd.DataFrame(tagger.predict(examples), columns=Ytags.columns)
examples_pred
examples_pred.T
examples = pd.DataFrame([sbert.encode(s) for s in [
                        "Hi I'm Vishvesh Bhat and OK", "My name is Sandeep", "OK", "Can you help me please?"]])
examples_pred = pd.DataFrame(tagger.predict(examples), columns=Ytags.columns)
examples_pred.T
examples_pred.T.sum()
examples_pred = pd.DataFrame(
    tagger.predict_proba(examples), columns=Ytags.columns)
examples_pred = pd.DataFrame(
    tagger.predict_proba(examples), columns=Ytags.columns)
