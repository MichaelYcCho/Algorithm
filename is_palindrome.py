def is_palindrome(word):
    word = word.lower()
    filtered_word = "".join(char for char in word if char.isalpha())

    left, right = 0, len(filtered_word) - 1
    while left < right:
        if filtered_word[left] != filtered_word[right]:
            return False
        left += 1
        right -= 1

    return True


# 예시 사용
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("Hello, World!"))
