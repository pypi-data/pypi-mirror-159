# Sinophone (三耨風)

`sinophone` is a python package that helps to manipulate Chinese phonology. It is divided into two submodules, `sinophone.phonetics` and `sinophone.phonology`. The former is a general abstraction of IPA symbols and distinctive features which could well be applied to other languages, while the latter is designed specifically to suit the purpose of working with the phonologies of Chinese languages.

## Install

`pip install sinophone`

## Example of use

In the following example, I simulated a tiny portion of Shanghainese phonology. Observe how `sinophone` can collocate phonemes to create a list of hypothetical syllables, and then pick out the ones that contradict the phonotactic constraint `pc`. It also applied a phonological rule when printing the syllable in phonetic transcription as `bʊ̃ŋ˥˥`, instead of the phonemic one, `boŋ˥˥`.

```python
from sinophone.phonetics import *
from sinophone.phonology import *

# Syllable 音節
kuaq = Syllable(
    Initial("k"),
    Final(
        medial=Medial("ʷ"),
        nucleus=Nucleus("ɐ"),
        coda=Coda("ʔ"),
    ),
    Tone("˥˥"),
)
kuaq  # <Syllable [<Initial 'k'> <Final [<Medial 'ʷ'> <Nucleus 'ɐ'> <Coda 'ʔ'>]> <Tone '˥˥'>]>

lon = Syllable(Initial("l"), Final(nucleus=Nucleus("o"), coda=Coda("ŋ")), Tone("˨˧"))

bo = Syllable(Initial("b"), Final(nucleus=Nucleus("o")), Tone("˨˧"))


# PhonologicalRule 音韻規則
pr = PhonologicalRule(
    Nucleus("o"),
    IPAString("ʊ̃"),
    SyllableFeatures({"Final": {IPAFeatureGroup("+nasal")}}),
)
pr  # <PhonologicalRule "o -> ʊ̃ / {'Final': '+nasal'}">


# PhonotacticConstraint 音位排列制約
pc = PhonotacticConstraint(
    SyllableFeatures(
        {
            "Initial": {IPAFeatureGroup("+stop +voiced")},
            "Tone": {IPAFeatureGroup("+extra-high-level")},
        }
    ),
    PhonotacticAcceptability(False, False),
)
pc  # <PhonotacticConstraint {'Initial': '+plosive +voiced', 'Tone': '+extra-high-level'}: {'existent': False, 'grammatical': False}>


# Phonology 音系
phonology = Phonology(
    syllables={kuaq, bo, lon},
    phonotactics={pc},
    phonological_rules=[pr],
)

phonology.initials  # {<Initial 'k'>, <Initial 'l'>, <Initial 'b'>}

# automatically collocate to create hypothetical syllables
phonology.collocations

# list of hypothetical syllables contradicting phonotactics
[
    syllable.phonetic_ipa_str
    for syllable in phonology.collocations
    if phonology.render_syllable(syllable).acceptability
    != PhonotacticAcceptability(True, True)
]  # [<IPAString 'bo˥˥'>, <IPAString 'bʷɐʔ˥˥'>, <IPAString 'bʊ̃ŋ˥˥'>]
```
