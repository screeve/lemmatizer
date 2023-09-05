# Lemmatizer
Lemmatization functionality for Georgian language. screeve-postagger is a small encoder-decoder (sequence-to-sequence) model trained on Georgian National Corpus for lemmatizing Georgian senteces. We provide you with two types of lemmatizer. 

You can use basic Lemmatizer in the following manner:


```python
from transformers import BartForConditionalGeneration, AutoTokenizer, pipeline

model = BartForConditionalGeneration.from_pretrained("Nargizi/screeve-lemmatizer")
tokenizer = AutoTokenizer.from_pretrained("Nargizi/screeve-lemmatizer")

tagger = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

ka_word = "დამიწერია"
result = tagger(ka_word)
print(result)
```

For the Lemmatizer with POS tags as additional input use the following code:


```python
from transformers import BartForConditionalGeneration, AutoTokenizer, pipeline

model = BartForConditionalGeneration.from_pretrained("Nargizi/screeve-pos-lemmatizer")
tokenizer = AutoTokenizer.from_pretrained("Nargizi/screeve-pos-lemmatizer")

ka_word = "დამიწერია"
pos_tag = "V"

encoded_ka_word = tokenizer(ka_word, text_pair=pos_tag, return_tensors="pt")
generated_tokens = model.generate(**encoded_ka_word)
result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print(result)
```

Label descriptions:

Abbreviation|Description
-|-
V| Verb
N | Noun
Pron | Pronoun
Interj | Interjection
A |Person’s name
Adv | Adverb
Cj | Conjunction
Punct | Punctuation
Num | Number
Pp |Preposition
