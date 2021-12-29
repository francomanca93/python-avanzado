def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
    """
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(is_palindrome(1000))
    
if __name__ == "__main__":
    run()