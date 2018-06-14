# SearchEngine
A simple example of a SearchEngine made in Python.

This search engine indexes and retrieves the paragraphs of a given text (a book, for instance).

## Generating the corpus

Use extractor.py to convert a .txt file into a set of paragraphs, which is the corpus to be indexed.

## Generating the repository

Use make_repository.py to create the repository from the corpus.

## Generating the index

Use make_index.py to create the inverted index from the repository.

## Retrieval

Use search.py to search the index and retrieve the documents.
