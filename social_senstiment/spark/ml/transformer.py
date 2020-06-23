from pyspark.ml.feature import (
    RegexTokenizer, 
    StopWordsRemover, 
    Word2Vec
)


_regex_tokenizer = RegexTokenizer(inputCol= 'tweet' , outputCol= 'tokens', pattern= '\\W')

_stop_word_remover = StopWordsRemover(inputCol= 'tokens', outputCol= 'filtered_words')

_word_2_vec = Word2Vec(inputCol= 'filtered_words', outputCol= 'vector', vectorSize= 100)

TRANSFORMERS = [
    _regex_tokenizer,
    _stop_word_remover,
    _word_2_vec
]
