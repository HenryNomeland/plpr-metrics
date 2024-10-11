import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from phoneme_info import PHONEME_INFO_DF_BASIC

# Implementation of the _plot_phoneme_confusion_matrix function is adapted from
# https://github.com/BrainBehaviorAnalyticsLab/PyPLLRComputer
# by Prad Kadambi


def plot_phoneme_confusion_matrix(
    per_frame_df, title=None, save=True, name="PhonemePlot"
):
    _plot_two_category_confusion_matrix(
        per_frame_df,
        groupingCategory="ExpectedPhoneme",
        outcomeCategory="MostLikelyPhoneme",
        title=title,
    )
    if save:
        plt.savefig(f".\\plots\\{name}")
    plt.show()


def plot_type_confusion_matrix(per_frame_df, title=None, save=True, name="PhonemePlot"):
    _plot_two_category_confusion_matrix(
        per_frame_df,
        groupingCategory="ExpectedType",
        outcomeCategory="MostLikelyType",
        title=title,
    )
    if save:
        plt.savefig(f".\\plots\\{name}")
    plt.show()


def plot_phoneme_vs_type_confusion_matrix(
    per_frame_df, title=None, save=True, name="PhonemePlot"
):
    _plot_two_category_confusion_matrix(
        per_frame_df,
        groupingCategory="ExpectedPhoneme",
        outcomeCategory="MostLikelyType",
        title=title,
    )
    if save:
        plt.savefig(f".\\plots\\{name}")
    plt.show()


def _plot_two_category_confusion_matrix(
    per_frame_df, groupingCategory, outcomeCategory, title=None
):
    crosstab = pd.crosstab(
        per_frame_df[groupingCategory], per_frame_df[outcomeCategory]
    )
    fracmatrix = crosstab.div(crosstab.sum(axis=1), axis=0) * 100
    plt.figure(figsize=(6.4 * 2, 4.8 * 2))

    # If the outcome category is phoneme, group the phonemes by voicing and type
    if "phoneme" in outcomeCategory.lower():
        phonemes = PHONEME_INFO_DF_BASIC.sort_values(["type", "voiced"]).phoneme.values
        if "AH" not in per_frame_df[outcomeCategory].unique():
            phonemes = np.delete(phonemes, np.where(phonemes == "AH"))
        keeplocs = ~np.logical_or(
            np.logical_or(
                np.logical_or(phonemes == "[PAD]", phonemes == "ZH"),
                phonemes == "SIL",
            ),
            phonemes == "[UNK]",
        )
        outcomecategories = phonemes[keeplocs]

        fracmatrix = fracmatrix.round().loc[outcomecategories]

        fracmatrix = fracmatrix[list(outcomecategories) + ["SIL", "[UNK]"]]
    else:
        outcomecategories = list(fracmatrix.index)
        fracmatrix = fracmatrix.round().loc[outcomecategories]

    sns.heatmap(
        fracmatrix, annot=True, xticklabels=True, yticklabels=True, cmap="Greys"
    )

    if title is None:
        plt.title("Phoneme Confusion Matrix")
    else:
        plt.title(title)
    plt.show()
