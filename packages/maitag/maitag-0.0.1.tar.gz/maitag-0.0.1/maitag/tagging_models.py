import numpy as np
import matplotlib.pyplot as plt

from sklearn.multiclass import OneVsRestClassifier
from sklean.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA

import seaborn as sns
sns.set_style()


def plot_hyperplane(binary_classifier, min_x, max_x, linestyle, label):
    # get the separating hyperplane
    w = binary_classifier.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(min_x - 5, max_x + 5)  # make sure the line is long enough
    yy = a * xx - (binary_classifier.intercept_[0]) / w[1]
    plt.plot(xx, yy, linestyle, label=label)


def plot_examples(model, X, Y):
    plt.figure(figsize=(12, 8))

    plot_subplot(model, X, Y, 1, "CCA", XCA=CCA)
    plot_subplot(model, X, Y, 2, "PCA", XCA=PCA)

    # plt.subplots_adjust(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
    plt.show()


def plot_subplot(tagger, X, Y, subplot, title):
    min_x = np.min(X[:, 0])
    max_x = np.max(X[:, 0])

    min_y = np.min(X[:, 1])
    max_y = np.max(X[:, 1])

    plt.subplot(1, 2, subplot)
    plt.title(title)

    tag0 = np.where(Y[:, 0])
    tag1 = np.where(Y[:, 1])
    plt.scatter(X[:, 0], X[:, 1], s=40, c="gray", edgecolors=(0, 0, 0))
    plt.scatter(
        X[tag0, 0],
        X[tag0, 1],
        s=160,
        edgecolors="b",
        facecolors="none",
        linewidths=2,
        label="Class 1",
    )
    plt.scatter(
        X[tag1, 0],
        X[tag1, 1],
        s=80,
        edgecolors="orange",
        facecolors="none",
        linewidths=2,
        label="Class 2",
    )

    plot_hyperplane(
        tagger.estimators_[0], min_x, max_x, "k--", "Boundary\nfor class 1"
    )
    plot_hyperplane(
        tagger.estimators_[1], min_x, max_x, "k-.", "Boundary\nfor class 2"
    )
    plt.xticks(())
    plt.yticks(())

    plt.xlim(min_x - 0.5 * max_x, max_x + 0.5 * max_x)
    plt.ylim(min_y - 0.5 * max_y, max_y + 0.5 * max_y)

    plt.xlabel("First component")
    plt.ylabel("Second component")
    plt.legend(loc="upper left")


def train_pii_detector(X, y):
    hyperparams = dict(
        C=1, class_weight='balanced', random_state=1, max_iter=10000, multi_class='auto')
    model = LogisticRegression(**hyperparams)
    model.fit(X_train, y_train)
    return model


if __name__ == '__main__':
    from sklearn.datasets import make_multilabel_classification

    X, Y = make_multilabel_classification(
        n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
    )

    tagger = OneVsRestClassifier(SVC(kernel="linear", class_weight='balanced'))

    Xpca = PCA(n_components=2).fit(X, Y).transform(X)
    tagger.fit(Xpca, Y)

    Xcca = CCA(n_components=2).fit(X, Y).transform(X)
    tagger.fit(Xcca, Y)

    plt.figure(figsize=(16, 6))
    plot_subplot(tagger, Xpca, Y, 1, "With unlabeled samples + CCA")
    plot_subplot(tagger, Xcca, Y, 2, "With unlabeled samples + PCA")

    # plt.subplots_adjust(0.04, 0.02, 0.97, 0.94, 0.09, 0.2)
    plt.show(block=False)
