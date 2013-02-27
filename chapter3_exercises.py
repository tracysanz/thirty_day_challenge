# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Tamar Schanfeld
# 3.1 Traceback (most recent call last):
#  File "C:/Users/Tamar/Documents/program/thirty_day_challenge/test2", line 1, in <module>
#    repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined
# 3.2 NameError: global name 'print_lyrics' is not defined
# 3.3
def right_justify(word):
    print (' '*(70-len(word)))+word
# 3.4  1) spam appears twice 
# 3.4 2)
def do_twice(f, word):
    f(word)
    f(word)

# 3.4 3) 
def print_twice(word):
    print word
    print word
    
# 3.4 4)
 def do_twice(f, word):
    f(word)
    f(word)

def print_twice(word):
    print word

do_twice(print_twice,'spam')

# 3.4 5)
def do_twice(f, word):
    f(word)
    f(word)

def print_twice(word):
    print word
    print word

def do_four(f, word):
    do_twice(f, word)
    do_twice(f, word)

do_four(print_twice, 'spam')