def is_palindrom(s1):
    
    left = 0
    right = len(s1)-1

    while(left<right):

        if(s1[left].isalnum() and s1[right].isalnum()):
            if(s1[left]==s1[right]):
                left +=1 
                right -=1
            else:
                return False
        return True    



print(is_palindrom("cac"))
print(is_palindrom("kayak"))
