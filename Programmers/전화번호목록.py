def solution(phone_book):   
    phone_book.sort()
    print(phone_book)
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            print(f"흠 {phone_book[i]}, 와 {phone_book[i+1]}")
            return False
    return True




phone_book = ["119", "97674223", "1195524421"]


print(solution(phone_book))


# 정렬을 하면 같은 글자가 있다면 그 순서대로 정렬되기 때문에 바로 뒤에 값만으로 참거짓판별가능
'''
a = "123"
b = "12345"

#print(bool(a in b))


a = "가나다"
b = "가나다라"

print(bool(a in b))

'''