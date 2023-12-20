from collections import deque


def is_palindrome(string):
    string = "".join(el.lower() for el in string if el.isalnum())

    string_deque = deque(string)

    while len(string_deque) > 1:
        first = string_deque.popleft()
        last = string_deque.pop()
        if first != last:
            return False
    return True
