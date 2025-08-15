str1 = input("Enter first word: ").replace(" ", "").lower()
str2 = input("Enter second word: ").replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Anagrams!")
else:
    print("Not anagrams.")
