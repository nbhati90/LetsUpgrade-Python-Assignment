#!/usr/bin/env python
# coding: utf-8

# # Find sum of n numbers with help of while loop

# In[ ]:


add= 0
num=eval(input("Enter the number to add the sum and 0 for exit "))
while num!=0:
    print(add,"+",num)
    add = add+num
    print(add)
    num=eval(input("Enter the number to add the sum and 0 for exit "))
print("the total sum is :", add)

Enter the number to add the sum and 0 for exit 6
0 + 6
6
Enter the number to add the sum and 0 for exit 9
6 + 9
15
Enter the number to add the sum and 0 for exit 8
15 + 8
23
Enter the number to add the sum and 0 for exit 7
23 + 7
30
Enter the number to add the sum and 0 for exit 1
30 + 1
31
Enter the number to add the sum and 0 for exit 3
31 + 3
34
Enter the number to add the sum and 0 for exit 2
34 + 2
36
Enter the number to add the sum and 0 for exit 0
the total sum is : 36
# # Take an integer and find whether the number is prime or not

# In[ ]:


num=eval(input("Enter the number to given number is prime or not "))
if num > 1: 
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
        else:
            print(num,"is a prime number")      
else:
    print(num,"is not a prime number")

Enter the number to given number is prime or not 2
2 is a prime number
