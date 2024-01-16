from compiler.tokenizer import tokenize

def test_tokenizer_basics() -> None:
    assert tokenize("if  3\nwhile") == ['if', '3', 'while']

def test_tokenizer_no_specials() -> None:
    assert tokenize("for X 3 @a") == ['for', 'X', '3', 'a']