import pandas as pd
import numpy as np


def drop_schwa(df):
    other_columns = list(df.columns[3:28]) + list(df.columns[29:45])
    print(other_columns)
    modified_columns = [col.split("_")[1] for col in other_columns]
    dropped_df = df.drop(columns=["Phoneme_AH"])
    remaining_prob_distribution = dropped_df[other_columns].sum(axis=1)
    normalized_other_columns = dropped_df[other_columns].div(
        remaining_prob_distribution, axis=0
    )
    dropped_df = dropped_df[dropped_df["Phone"] != "AH"]
    mask = dropped_df["MostLikelyPhoneme"] == "AH"
    dropped_df.loc[mask, "MostLikelyPhoneme"] = (
        dropped_df.loc[mask, other_columns]
        .idxmax(axis=1)
        .apply(lambda col: col.split("_")[1])
    )
    dropped_df["MostLikelyPhonemeProb"] = dropped_df[other_columns].max(axis=1)
    dropped_df["ExpectedPhonemeProb"] = dropped_df.apply(
        lambda row: (
            row["Phoneme_" + row["Phoneme"]]
            if row["Phoneme"] in modified_columns
            else None
        ),
        axis=1,
    )
    result = pd.concat(
        [
            dropped_df[df.columns[0:3]],
            normalized_other_columns,
            dropped_df[df.columns[45:-24]],
        ],
        axis=1,
    )
    return result
