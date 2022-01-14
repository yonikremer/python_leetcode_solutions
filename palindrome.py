from typing import List


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    digits: List[int] = []
    while True:
        digits.append(x % 10)
        if x < 10:
            break
        x //= 10
    while len(digits) > 1:
        if digits[0] != digits[-1]:
            return False
        digits.pop(0)
        digits.pop(-1)
    return True


if __name__ == "__main__":
    print(is_palindrome(int(input())))
