'''is word inside list?'''
#caught from thinkpython2

import bisect

def is_inside_list(word_list, word):
    i = bisect.bisect_left(word_list, word):
        if len(word_list) == i:
            return False
        return word_list[i] == word
