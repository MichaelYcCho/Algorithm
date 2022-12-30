"""
    defaultdict는 dict의 서브클래스로,
    defaultdict()으 ㅣ인자로 주어진 객체를 기본값으로 가지는 딕셔너리값의 초기값으로 지정할 수 있다. 
    숫자, 리스트, set등으로 초기화 가능하다 
"""

from collections import defaultdict


def default_dict_example1():
    int_dict = defaultdict(int)
    print(int_dict) # defaultdict(<class 'int'>, {})

    int_dict['test']
    # int_dict['test'] = a 를 작성하면 값은 a가된다. 즉, 타입에 맞는 기본값이 아닌 다른 값을 넣을 수 있다. 
    # 다만 위처럼 키값만 넣으면 value값은 초기에 선언한 타입값이 된다
    print(int_dict) # defaultdict(<class 'int'>, {'test': 0})



def default_dict_example2():
    list_dict = defaultdict(list)
    print(list_dict)

    list_dict['test'].append('test')
    print(list_dict) # defaultdict(<class 'list'>, {'test': ['test']})

    list_dict['test'].append('test2')
    print(list_dict) # defaultdict(<class 'list'>, {'test': ['test', 'test2']})





default_dict_example1()
print()
default_dict_example2()

