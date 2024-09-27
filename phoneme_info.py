import pandas as pd
import pickle as pkl

# Adapted from https://github.com/BrainBehaviorAnalyticsLab/PyPLLRComputer
# by Prad Kadambi

ENGLISH_PHONEME_LIST = [
    "AA",
    "AE",
    "AH",
    "AO",
    "AW",
    "AY",
    "B",
    "CH",
    "D",
    "DH",
    "EH",
    "ER",
    "EY",
    "F",
    "G",
    "HH",
    "IH",
    "IY",
    "JH",
    "K",
    "L",
    "M",
    "N",
    "NG",
    "OW",
    "OY",
    "P",
    "R",
    "S",
    "SH",
    "T",
    "TH",
    "UH",
    "UW",
    "V",
    "W",
    "Y",
    "Z",
]


PHONEME_INFO_DF = pd.DataFrame(
    [
        {
            "phoneme": "AA",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AE",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AO",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AW",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "EH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "ER",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "EY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "IH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "IY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "OW",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "OY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "UH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "UW",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "B",
            "type": "bilabial plosive stop",
            "voiced": "voiced",
        },
        {
            "phoneme": "CH",
            "type": "alveolar affricate fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "D",
            "type": "alveolar plosive",
            "voiced": "voiced",
        },
        {
            "phoneme": "DH",
            "type": "biabial plosive",
            "voiced": "voiced",
        },
        {
            "phoneme": "F",
            "type": "labiodental fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "G",
            "type": "velar plosive",
            "voiced": "voiced",
        },
        {
            "phoneme": "HH",
            "type": "gottal fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "JH",
            "type": "alveolar fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "K",
            "type": "velar plosive stop",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "L",
            "type": "lateral approximant",
            "voiced": "voiced",
        },
        {
            "phoneme": "M",
            "type": "bilabial nasal",
            "voiced": "voiced",
        },
        {
            "phoneme": "N",
            "type": "alveolar nasal",
            "voiced": "voiced",
        },
        {
            "phoneme": "NG",
            "type": "velar nasal",
            "voiced": "voiced",
        },
        {
            "phoneme": "P",
            "type": "bilabial plosive stop",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "R",
            "type": "retroflex approximant",
            "voiced": "voiced",
        },
        {
            "phoneme": "S",
            "type": "alveolar fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "SH",
            "type": "palatoalveolar fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "T",
            "type": "alveolar flap stop",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "TH",
            "type": "dental fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "V",
            "type": "labiodental fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "W",
            "type": "labiovelar approximant",
            "voiced": "voiced",
        },
        {
            "phoneme": "Y",
            "type": "palatal sonorant vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "Z",
            "type": "alveolar fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "ZH",
            "type": "postalveolar fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "[UNK]",
            "type": "sil_unk_pad",
            "voiced": "NA",
        },
        {
            "phoneme": "[PAD]",
            "type": "sil_unk_pad",
            "voiced": "NA",
        },
        {"phoneme": "SIL", "type": "sil_unk_pad", "voiced": "NA"},
    ]
)

# Use a more basic set of 'types' to describe the phonemes
PHONEME_INFO_DF_BASIC = pd.DataFrame(
    [
        {
            "phoneme": "AA",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AE",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AO",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AW",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "AY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "EH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "ER",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "EY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "IH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "IY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "OW",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "OY",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "UH",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "UW",
            "type": "vowel",
            "voiced": "voiced",
        },
        {
            "phoneme": "B",
            "type": "plosive",
            "voiced": "voiced",
        },
        {
            "phoneme": "CH",
            "type": "affricate",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "D",
            "type": "plosive",
            "voiced": "voiced",
        },
        {
            "phoneme": "DH",
            "type": "fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "F",
            "type": "fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "G",
            "type": "plosive",
            "voiced": "voiced",
        },
        {
            "phoneme": "HH",
            "type": "fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "JH",
            "type": "affricate",
            "voiced": "voiced",
        },
        {
            "phoneme": "K",
            "type": "plosive",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "L",
            "type": "liquid",
            "voiced": "voiced",
        },
        {
            "phoneme": "M",
            "type": "nasal",
            "voiced": "voiced",
        },
        {
            "phoneme": "N",
            "type": "nasal",
            "voiced": "voiced",
        },
        {
            "phoneme": "NG",
            "type": "nasal",
            "voiced": "voiced",
        },
        {
            "phoneme": "P",
            "type": "plosive",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "R",
            "type": "liquid",
            "voiced": "voiced",
        },
        {
            "phoneme": "S",
            "type": "fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "SH",
            "type": "fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "T",
            "type": "plosive",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "TH",
            "type": "fricative",
            "voiced": "unvoiced",
        },
        {
            "phoneme": "V",
            "type": "fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "W",
            "type": "glide",
            "voiced": "voiced",
        },
        {
            "phoneme": "Y",
            "type": "glide",
            "voiced": "voiced",
        },
        {
            "phoneme": "Z",
            "type": "fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "ZH",
            "type": "fricative",
            "voiced": "voiced",
        },
        {
            "phoneme": "[UNK]",
            "type": "sil_unk_pad",
            "voiced": "NA",
        },
        {
            "phoneme": "[PAD]",
            "type": "sil_unk_pad",
            "voiced": "NA",
        },
        {"phoneme": "SIL", "type": "sil_unk_pad", "voiced": "NA"},
    ]
)
phone2type_dict_base = dict(
    zip(PHONEME_INFO_DF_BASIC["phoneme"], PHONEME_INFO_DF_BASIC["type"])
)


def get_all_phones_of_type(descriptions, removephones=None):
    from phoneme_info import PHONEME_INFO_DF

    phones = []
    for descrip in descriptions:
        _phns = list(
            PHONEME_INFO_DF[PHONEME_INFO_DF["type"].str.contains(descrip)].phoneme
        )
        phones.extend(_phns)
    phones = set(phones)
    if removephones is not None:
        for rphn in removephones:
            phones.discard(rphn)
    return list(phones)


stops = get_all_phones_of_type(["stop", "plosive"], removephones=["CH"])
stops = set(stops)
stops.discard("CH")
stops = list(stops)
fricatives = get_all_phones_of_type(
    ["fricative"], removephones=["CH"]
) + get_all_phones_of_type(["affricate"], removephones=["CH"])
unvoiced_fricatives = ["F", "TH", "S", "SH"]
voiced_fricatives = ["V", "DH", "Z"]
liquid_approximants = ["R", "L"]
glide_approximants = ["JH", "W"]
nasals = ["NG", "N", "M"]
vowels = get_all_phones_of_type(["vowel"])
obstruents = stops + fricatives
affricates = ["JH", "CH"]

phone_classes_dct = {
    "Stops": stops,
    "UnvoicedFricatives": unvoiced_fricatives,
    "VoicedFricatives": voiced_fricatives,
    "LiquidApproximants": liquid_approximants,
    "GlideApproximants": glide_approximants,
    "Nasals": nasals,
    "Vowels": vowels,
    "Obstruents": obstruents,
    "Affricates": affricates,
}


def get_phoneid2phone_dict():
    return pkl.load(open("./kaldi_phone_inds.pkl", "rb"))
