from typing import List

import torch
from transformers import pipeline, BartForConditionalGeneration, AutoTokenizer, PreTrainedTokenizerFast


class Lemmatizer:
    def __init__(self):
        self._pipeline = pipeline("text2text-generation", model="Nargizi/screeve-lemmatizer")

    def __call__(self, text: str) -> str:
        lemma = self._pipeline(text)
        return lemma[0]['generated_text']


class POSLemmatizer:
    def __init__(self):
        self._model: BartForConditionalGeneration = BartForConditionalGeneration.from_pretrained(
            "Nargizi/screeve-pos-lemmatizer")

        self._tokenizer: PreTrainedTokenizerFast = AutoTokenizer.from_pretrained("Nargizi/screeve-pos-lemmatizer")

    def __call__(self, text: str, pos_tag: str) -> str:
        input_ids = self._tokenizer(text, text_pair=pos_tag).input_ids
        input_batch = torch.tensor(input_ids).unsqueeze(0)
        generated_lemma = self._model.generate(input_batch)
        decoded_lemma = self._tokenizer.batch_decode(generated_lemma)[0].split()
        # remove start and end tokens
        cleared_lemma = [token for token in decoded_lemma if
                         token not in {self._tokenizer.sep_token, self._tokenizer.cls_token}]
        try:
            return cleared_lemma[0]
        except IndexError:
            return ""