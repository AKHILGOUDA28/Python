text = input("Enter text: ").lower()
vowels = "aeiou"
v_count = c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count, "Consonants:", c_count)
