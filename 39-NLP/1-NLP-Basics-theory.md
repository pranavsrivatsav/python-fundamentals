#### NLP Basic theory
- What is NLP?
- Steps in NLP Text preprocessing.
    - Tokenization: Breaking down text into smaller units (words, subwords, characters).
    - Cleaning: Removing noise (e.g., punctuation, stop words, HTML tags).
    - Normalization: Converting text to a consistent format (e.g., lowercasing, stemming, lemmatization).

- What are stop words?
    - Stop words are words that are commonly used in the language, but have little meaning. So these are removed during text preprocessing.

- What is lemmatization?
    - Lemmatization is a normalization process. It involves getting the root unit of a word, by removing the stem (i.e part of the word or context of the word) that does not add value to preprocessing.
    
    - How it works?
        - It analyzes the context of a word, including its part of speech, meaning, and use in the sentence.
        - It removes inflectional endings like "s", "ed", and "ing".
        - It ensures that post the removal, the resulting word is a word in the dictionary.
    - Examples 
        - The word "better" would be reduced to its lemma, "good".
        - The verb "running" would be identified as "run".
        - The word "saw" would return as "see" or "saw" depending on its context.
        - The word "ponies" would return "pony".

- What is stemming?
    - stemming is similar to Lemmatization, it uses a pre-defined logic/algorithm to remove suffixes from a word.
    - porter stemmer is a popular stemming algorithm that was created in 1980s, which is used widely for stemming.
    - It removes suffiexes like 'ed', 'ing' etc from a word.

- Difference between lemmatization and stemming
    
    |   | Lemmatization | Stemming |
    |---|---|---|
    | Speed | Comparitively slower | Faster |
    | Precision | More Precise | Less Precise |
    | Context | Context where the word is used, is taken into account | Context does not play a role in stemming |
    | Dictionary | Lemmatization ensures that the resulting root is a word in the language dictionary | The resulting word in stemming might not possibly be a valid word on its own |
    | Usage | text categorization, chat bots, semantic analysis | search engines, text mining |
