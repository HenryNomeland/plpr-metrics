import pandas as pd
from phoneme_info import *


def drop_schwa(df):
    other_columns = list(df.columns[3:28]) + list(df.columns[29:45])
    type_columns = list(df.columns[50:58])
    modified_columns = [col.split("_")[1] for col in other_columns]
    dropped_df = df.drop(columns=["Phoneme_AH"])
    remaining_prob_distribution = dropped_df[other_columns].sum(axis=1)
    normalized_other_columns = dropped_df[other_columns].div(
        remaining_prob_distribution, axis=0
    )
    dropped_df = dropped_df[dropped_df["ExpectedPhoneme"] != "AH"]
    dropped_df = pd.concat(
        [
            dropped_df[df.columns[0:3]],
            normalized_other_columns,
            dropped_df[df.columns[45:]],
        ],
        axis=1,
    )
    # for rows where the most likely phoneme is AH - recalculate the most likely phoneme
    mask = dropped_df["MostLikelyPhoneme"] == "AH"
    dropped_df.loc[mask, "MostLikelyPhoneme"] = (
        dropped_df.loc[mask, other_columns]
        .idxmax(axis=1)
        .apply(lambda col: col.split("_")[1])
    )
    vowel_phonemes = [
        d["phoneme"]
        for _, d in PHONEME_INFO_DF_BASIC.iterrows()
        if d["type"] == "vowel"
    ]
    vowel_phonemes.remove("AH")
    affricate_phonemes = [
        d["phoneme"]
        for _, d in PHONEME_INFO_DF_BASIC.iterrows()
        if d["type"] == "affricate"
    ]
    fricative_phonemes = [
        d["phoneme"]
        for _, d in PHONEME_INFO_DF_BASIC.iterrows()
        if d["type"] == "fricative"
    ]
    plosive_phonemes = [
        d["phoneme"]
        for _, d in PHONEME_INFO_DF_BASIC.iterrows()
        if d["type"] == "plosive"
    ]
    glide_phonemes = [
        d["phoneme"]
        for _, d in PHONEME_INFO_DF_BASIC.iterrows()
        if d["type"] == "glide"
    ]
    liquid_phonemes = [
        d["phoneme"]
        for _, d in PHONEME_INFO_DF_BASIC.iterrows()
        if d["type"] == "liquid"
    ]
    sil_unk_pad_phonemes = ["SIL", ".PAD.", ".UNK."]

    dropped_df["MostLikelyPhonemeProb"] = dropped_df[other_columns].max(axis=1)
    dropped_df["ExpectedPhonemeProb"] = dropped_df.apply(
        lambda row: (
            row["Phoneme_" + row["ExpectedPhoneme"]]
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["Type_vowel"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in vowel_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["Type_affricate"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in affricate_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["type_fricate"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in fricative_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["type_plosive"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in plosive_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["type_liquid"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in liquid_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["type_glide"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in glide_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df["type_sil_unk_pad"] = dropped_df.apply(
        lambda row: (
            row[[f"Phoneme_{p}" for p in sil_unk_pad_phonemes]].sum()
            if row["ExpectedPhoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    dropped_df.loc[mask, "MostLikelyType"] = (
        dropped_df.loc[mask, type_columns]
        .idxmax(axis=1)
        .apply(lambda col: col.split("_")[1])
    )
    dropped_df["MostLikelyTypeProb"] = dropped_df[type_columns].max(axis=1)
    dropped_df["ExpectedTypeProb"] = dropped_df.apply(
        lambda row: (
            row["Type_" + row["ExpectedType"]]
            if row["ExpectedType"] in modified_columns
            else None
        ),
        axis=1,
    )
    return dropped_df
