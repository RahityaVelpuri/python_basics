def is_palindrome(num):
    temp=num
    reverse_num=0
    while(temp>0):
        reminder=temp%10
        reverse_num=reverse_num*10+reminder
        temp=int(temp/10)
    if(reverse_num==num):
        print("%d is a palindrome" %num)
    else:
        print("%d is not a palindrome" %num)

is_palindrome(1232)
    
        
