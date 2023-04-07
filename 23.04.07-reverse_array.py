arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)



# 사실 한번에 뒤집기도 가능
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)