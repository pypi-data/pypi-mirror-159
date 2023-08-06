import spacy  # https://spacy.io


try:
    nlp = spacy.load('en_core_web_md')
except OSError:
    spacy.cli.download(nlp)
    nlp = spacy.load(nlp)
