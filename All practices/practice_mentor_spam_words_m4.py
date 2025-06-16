# Написати код, який буде аналізувати текст та прибирати в ньому спам слова. - Python 
#"Hello, this is a spam message"
import re
spam_words_list = ["spam", "Python"]    
def remove_spam_words(message:str) -> str:
    for spam_word in spam_words_list:
        message = re.sub(rf"\b{spam_word}\b","*", message)
    return message
assert remove_spam_words("spam") == "*"
assert remove_spam_words("Python") == "*" 
print(remove_spam_words("Hello, this is a spam message"))
print(remove_spam_words("Python is a programming language"))