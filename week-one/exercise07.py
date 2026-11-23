def is_palindrome(text):
    text = text.replace(" ", "").lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text) -1 -i]:
             return False
    return True

assert is_palindrome("oso"), "oso should be a palindrome"