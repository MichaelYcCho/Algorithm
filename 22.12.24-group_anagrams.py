
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
    defaultdict()의 인자로 주어진 객체를 기본값으로 가지는 딕셔너리값의 초기값으로 지정할 수 있다. 
    숫자, 리스트, set등으로 초기화 가능하다 
    
    """

    anagrams = collections.defaultdict(list)

    for word in word_list:
        # print('?', ''.join(sorted(word))) # aet, aet, ant, aet, ant ....
        # anagrams['정렬된 단어(키값)'].append(원래 단어)
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())



def group_anagrams2(word_list: List[str]) :
    """
    그룹 1을 풀어서? 쓰면 아래와 같다
    """

    new_dict = {}

    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in new_dict:
            new_dict[sorted_word].append(word)
        else:
            new_dict[sorted_word] = [word]

    return list(new_dict.values())


print(group_anagrams(word_list))
print(group_anagrams2(word_list))
