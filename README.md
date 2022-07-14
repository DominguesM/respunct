# 🤗 bert-restore-punctuation-ptbr
🇧🇷 easy-to-use package to restore punctuation of portuguese texts.

* 🪄 [W&B Dashboard](https://wandb.ai/dominguesm/RestorePunctuationPTBR)
* 🤗 [HuggingFace Page](https://huggingface.co/dominguesm/bert-restore-punctuation-ptbr)


This is a [bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) model finetuned for punctuation restoration on [WikiLingua](https://github.com/esdurmus/Wikilingua). 

This model is intended for direct use as a punctuation restoration model for the general Portuguese language. Alternatively, you can use this for further fine-tuning on domain-specific texts for punctuation restoration tasks.

Model restores the following punctuations -- **[! ? . , - : ; ' ]**

The model also restores the upper-casing of words.

-----------------------------------------------
## 🎯 Accuracy

|  label                    |   precision  |  recall | f1-score  | support|
| ------------------------- | -------------|-------- | ----------|--------|
| **Upper            - OU** |      0.89    |  0.91   |   0.90    |  69376
| **None             - OO** |      0.99    |  0.98   |   0.98    | 857659
| **Full stop/period - .O** |      0.86    |  0.93   |   0.89    |  60410
| **Comma            - ,O** |      0.85    |  0.83   |   0.84    |  48608
| **Upper + Comma    - ,U** |      0.73    |  0.76   |   0.75    |   3521
| **Question         - ?O** |      0.68    |  0.78   |   0.73    |   1168
| **Upper + period   - .U** |      0.66    |  0.72   |   0.69    |   1884
| **Upper + colon    - :U** |      0.59    |  0.63   |   0.61    |    352
| **Colon            - :O** |      0.70    |  0.53   |   0.60    |   2420
| **Question Mark    - ?U** |      0.50    |  0.56   |   0.53    |     36
| **Upper + Exclam.  - !U** |      0.38    |  0.32   |   0.34    |     38
| **Exclamation Mark - !O** |      0.30    |  0.05   |   0.08    |    783
| **Semicolon        - ;O** |      0.35    |  0.04   |   0.08    |   1557
| **Apostrophe       - 'O** |      0.00    |  0.00   |   0.00    |      3
| **Hyphen           - -O** |      0.00    |  0.00   |   0.00    |      3
|                           |              |         |           |
| **accuracy**              |              |         |   0.96    | 1047818
| **macro avg**             |      0.57    |  0.54   |   0.54    | 1047818
| **weighted avg**          |      0.96    |  0.96   |   0.96    | 1047818

-----------------------------------------------
## 🤷 Output

Example:

```json
[
  {
    "entity_group": "OU",
    "score": 0.8026431202888489,
    "word": "henrique",
    "start": 0,
    "end": 8
  },
  {
    "entity_group": "OO",
    "score": 0.9925149083137512,
    "word": "foi no lago pescar com o",
    "start": 9,
    "end": 33
  },
  {
    "entity_group": ".U",
    "score": 0.8426014184951782,
    "word": "pedro",
    "start": 34,
    "end": 39
  },
  {
    "entity_group": "OU",
    "score": 0.9519776105880737,
    "word": "mais",
    "start": 40,
    "end": 44
  },
  {
    "entity_group": ",O",
    "score": 0.8551820516586304,
    "word": "tarde",
    "start": 45,
    "end": 50
  },
  {
    "entity_group": "OO",
    "score": 0.9902807474136353,
    "word": "foram para a casa do",
    "start": 51,
    "end": 71
  },
  {
    "entity_group": "OU",
    "score": 0.9227372407913208,
    "word": "pedro",
    "start": 72,
    "end": 77
  },
  {
    "entity_group": "OO",
    "score": 0.9997054934501648,
    "word": "fritar os",
    "start": 78,
    "end": 87
  },
  {
    "entity_group": ".O",
    "score": 0.9813661575317383,
    "word": "peixes",
    "start": 88,
    "end": 94
  }
]
```

This output refers to:

```
Henrique foi no lago pescar com o Pedro. Mais tarde, foram para a casa do Pedro fritar os peixes.
```
-----------------------------------------------

## 🤙 Contact 

[Maicon Domingues](dominguesm@outlook.com) for questions, feedback and/or requests for similar models.