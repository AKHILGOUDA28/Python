def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

word = input("Enter a word or phrase: ")
print("Palindrome!" if is_palindrome(word) else "Not a palindrome.")
