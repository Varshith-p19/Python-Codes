#Check the number is palindrome and not a palindrome


def is_polindrome(a):
    a = str(a)
    c = a[::-1]
    if c == a:
        print("Polindrome")
    else:
        print("Not a polindrome")
n = int(input("Enter the number "))        
is_polindrome(n)
