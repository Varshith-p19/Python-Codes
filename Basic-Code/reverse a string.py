#reverse a string without using built in function 

def reverse_of_string(a):
    rev = ''
    for i in a:
        rev = i + rev
    print(rev)
    
n = input("Enter the string to reverse ")   
reverse_of_string(n)

