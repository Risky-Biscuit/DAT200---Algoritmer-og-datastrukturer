"""
DAT200 - Assignment 3 (Q1): Palindrome
Two implementations:
- is_palindrome_iter(word): iterative two-pointer
- is_palindrome_rec(word):  recursive helper with indices
"""


def is_palindrome_iter(word: str) -> bool:
    i, j = 0, len(word) - 1  # two pointers: start and end
    while i < j:  # stop when they cross or meet
        if word[i] != word[j]:  # mismatch? not a palindrome
            return False
        i += 1  # move inward
        j -= 1
    return True  # all pairs matched


def is_palindrome_rec(word: str) -> bool:
    def helper(s: str, i: int, j: int) -> bool:
        if i >= j:  # base case: crossed or met -> done, it's a palindrome
            return True
        if s[i] != s[j]:  # mismatch at the ends -> fail
            return False
        return helper(s, i + 1, j - 1)  # shrink toward middle

    return helper(word, 0, len(word) - 1)


if __name__ == "__main__":
    tests = ["rotor", "motor", "", "a", "abba", "abca"]
    for t in tests:
        print(f"{t!r}: iter={is_palindrome_iter(t)}  rec={is_palindrome_rec(t)}")
