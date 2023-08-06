# DicTok

A dictionary-based tokenizer.
It tokenizes a text based on known tokens defined in a given file.

## Installation

```
pip install dictok
```

## Usage

1. Create your dic-file with a list of tokens e.g. `tokens.dic`:

```
super
man
note
book
store
...
```

2. Import `dictok` and pass it the dictionary file as main parameter:

```
>>> import dictok
>>> dt = dictok.DicTok('tokens.dic')
```

3. You are ready to use it:

```
>>> sent = "Superman bought a notebook in the bookstore."
>>> dt.tokenize(sent)
['Super', 'man', 'bought', 'a', 'note', 'book', 'in', 'the', 'book', 'store', '.']
```
