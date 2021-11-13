#To check the given word is palindrome or not
#Palindrome = reverse of the word also same

word = input("Enter a word to check the palindrome: ").lower()

string = word[::-1]

if word == string:
    print(f"The given word {word} is Palindrome")
else:
    print(f"The given word {word} is not Palindrome")
    
