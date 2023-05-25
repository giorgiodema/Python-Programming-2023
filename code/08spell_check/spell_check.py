from typing import List,Tuple,Callable
import sys
from pathlib import Path
from search import *

# name of the dictionary (it is 
# assumed to be in the same directory
# as the module)
_DICT_NAME = "italian.dic"

# helper function that computes the 
# hamming_distance between two strings
def _hamming_distance(a:str,b:str)->int:
    if len(a)!=len(b):
        raise ValueError("lengths must be equal")
    d = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            d +=1
    return d

def _insert_in_order(l:List[Tuple[str,int]],e:Tuple[str,int],max_len:int)->None:
    if len(l)==0:
        l.append(e)
        return
    if len(l)==max_len and e[1] > l[-1][1]:
        return
    if len(l)<max_len and e[1] <= l[-1][1]:
        l.append(e)
        return
    for i in range(len(l)):
        if e[1] < l[i][1]:
            l.insert(i,e)
            break
    if len(l) > max_len:
        l.pop()

def _length_cmp(s1:str,s2:str)->int:
    if len(s1)==len(s2): return 0
    elif len(s1)<len(s2): return -1
    else: return 1

def _str_cmp(s1:str,s2:str)->int:
    if s1==s1: return 0
    elif s1 < s2: return -1
    else: return 1

class SpellChecker:
    """
    Instantiate the object SpellChecker and call the 
    method object.get_hints(prompt,n_hints) to get some
    hints.
    """

    def __init__(self):
        self.__dic = []
        f = open(Path(__file__).with_name(_DICT_NAME),"r",encoding="utf-8")
        for line in f:
            line = line.strip().split("/")[0]
            line = line.lower()
            self.__dic.append(line)
        # sort the list by the length of the 
        # words in ascending order
        self.__dic.sort(
            key=lambda x:len(x)
        )

    def get_hints(self,prompt:str,n_hints:int=10)->List[Tuple[str,int]]:
        """
        returns a list of hints for the received prompt. The list contains
        tuples where the first element is the hint and the second is the 
        hamming distance between the hint and the prompt.
        """
        # retrieve the words with the same length
        # as prompt
        min_id = find_first_binary_search(
            self.__dic,
            prompt,
            _length_cmp
        )
        max_id = find_last_binary_search(
            self.__dic,
            prompt,
            _length_cmp
        )
        # if prompt is in the list, then return no hints
        if prompt in self.__dic[min_id:max_id]:
            return []
        # otherwise find the 10 words with the minimum 
        # distance and return these words
        hints = []
        for w in self.__dic[min_id:max_id]:
            d = _hamming_distance(w,prompt)
            _insert_in_order(hints,(w,d),max_len=n_hints)
        return hints