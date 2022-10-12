# Iterating through a string

string = 'taco cat'

def palindrome(string_to_check):
    if string.lower().replace(' ', '') == string.lower().replace(' ', '')[::-1]:
        print("You found a palindrome!")
    else:
        print("Your string isn't a palindrome")

palindrome(string)