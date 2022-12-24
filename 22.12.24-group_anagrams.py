
import collections
from typing import List


word_list = ["eat", "tea", "tan", "ate", "nat", "bat"] 
"""
Output:
-> [["ate","eat","tea"], ["nat","tan"], ["bat"]]
"""
def group_anagrams(word_list: List[str]) :
    """
    defaultdict는 dict의 서브클래스로,
    defaultdict()으 ㅣ인자로 주어진 객체를 기본값으로 가지는 딕셔너리값의 초기값으로 지정할 수 있다. 
    숫자, 리스트, set등으로 초기화 가능하다 
    
    """

    anagrams = collections.defaultdict(list)

    for word in word_list:
        # print('?', ''.join(sorted(word))) # aet, aet, ant, aet, ant ....
        # anagrams['정렬된 단어(키값)'].append(원래 단어)
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
