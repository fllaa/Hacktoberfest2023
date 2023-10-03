def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    if len(s) <= 1:
        return True
    return False if s[0] != s[-1] else is_palindrome(s[1:-1])


# Test cases
test_strings = ["racecar", "level", "python", "A man a plan a canal Panama", "Madam, in Eden, I'm Adam"]

for s in test_strings:
    if result := is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")