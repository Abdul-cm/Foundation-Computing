def ispalindrome (j):
        reverse_string = reversed (j)
        if list (j) == list (reverse_string):
             return True
        else:
            return False
x = "Hanna"
answer = ispalindrome (x.lower())
print (answer)
        

