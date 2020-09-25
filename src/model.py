import tensorflow as tf
import torch
import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


class Summarization:
    def __init__(self, device: str, pretrained: str = 't5-base'):
        self.model = T5ForConditionalGeneration.from_pretrained(pretrained)
        self.tokenizer = T5Tokenizer.from_pretrained(pretrained)
        self.device = torch.device(device)
        self.text = ''

    def set_text(self, text: str) -> 'Summarization':
        self.text = text
        return self

    def summarize(self, verbose: bool = False) -> str:
        preprocess_text = self.text.strip().replace('\n', '')
        if self.text is '':
            raise Exception('Empty text')
        if verbose:
            print('Original text preprocessed: ' + preprocess_text)

        t5_prepared_text = 'summarize: ' + preprocess_text
        tokenized_text = self.tokenizer.encode(t5_prepared_text,
                return_tensors='pt').to(self.device)

        summary_ids = self.model.generate(tokenized_text,
                num_beams=4,
                no_repeat_ngram_size=2,
                min_length=30,
                max_length=100,
                early_stopping=True)

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
