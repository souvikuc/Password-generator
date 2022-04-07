import os
import string as st
import random as rn
import itertools as it
import more_itertools as mits
import re


def choose(seq, num, repeat=False):
    if repeat == False:
        try:
            return "".join(rn.sample(mits.random_permutation(seq), k=num))
        except ValueError:
            return "The sample size is larger than the population"
    else:
        return "".join(rn.choices(mits.random_permutation(seq), k=num))


def smart_change(string):
    dict1 = {'a': '@', 'A': '@', 'c': '(', 'C': '(', 'h': '#', 'H': '#', 'i': '!',
             'I': '!', 'l': '|', 'L': '|', 'o': '0', 'O': '0', 's': '$', 'S': '$'}
    for i, j in dict1.items():
        if i in string:
            string = string.replace(i, j)
    return string


class generator(object):
    def __init__(self, size=8, method='general'):
        self.size = size
        self.method = method

    def generate_random(self, size=8, case='both', digits=True, punc=False, repeat=False, smart=False, exclude=r'_'):
        if not case in ['upper', 'lower', 'both', None]:
            raise ValueError("case must be one of None, upper, lower or both")
        if case == None and digits == False:
            raise ValueError("letters and digits can't be false simultaneously")
        if smart == False:
            if case == 'both':
                l1 = [st.ascii_letters, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [True, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return choose(list1, size, repeat=True)
                else:
                    return choose(list1, size)
            elif case == 'upper':
                l1 = [st.ascii_uppercase, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [True, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return choose(list1, size, repeat=True)
                else:
                    return choose(list1, size)
            elif case == 'lower':
                l1 = [st.ascii_lowercase, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [True, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return choose(list1, size, repeat=True)
                else:
                    return choose(list1, size)
            else:
                l1 = [st.ascii_letters, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [False, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return choose(list1, size, repeat=True)
                else:
                    return choose(list1, size)
        else:
            if case == 'both':
                l1 = [st.ascii_letters, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [True, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return smart_change(choose(list1, size, repeat=True))
                else:
                    return smart_change(choose(list1, size))
            elif case == 'upper':
                l1 = [st.ascii_uppercase, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [True, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return smart_change(choose(list1, size, repeat=True))
                else:
                    return smart_change(choose(list1, size))
            elif case == 'lower':
                l1 = [st.ascii_lowercase, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [True, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return smart_change(choose(list1, size, repeat=True))
                else:
                    return smart_change(choose(list1, size))
            else:
                l1 = [st.ascii_letters, st.digits, re.sub(exclude, '', st.punctuation)]
                index = [False, digits, punc]
                index1 = [i for i, e in enumerate(index) if e != 0]
                list1 = ''.join([l1[i] for i in index1])
                if repeat == True:
                    return smart_change(choose(list1, size, repeat=True))
                else:
                    return smart_change(choose(list1, size))


a = generator()
print(a.generate_random(10, case='upper', punc=False, repeat=True, smart=False))
