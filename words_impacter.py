import re


def word_swap(txt,word, new_word,):
    return re.sub(word, new_word, txt)

def word_del(txt,word):
    return re.sub(word,"", txt)

txt="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida ligula vitae " \
    "ante cursus varius. Nulla nec fermentum tellus. Aliquam molestie condimentum ante, " \
    "at pulvinar nisl pharetra ac. Suspendisse tempus sed orci nec porta. Sed sit amet ipsum " \
    "lacinia, luctus erat eu, facilisis lectus. Sed maximus ligula non ipsum maximus, sagittis " \
    "pretium odio ultricies. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed tincidunt commodo ullamcorper."

print(word_del(txt,'Sed'))
print(word_swap(txt,'Sed', 'xxxx'))
