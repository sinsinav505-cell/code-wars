#Your task is to make a function that can take any non-negative integer as an argument and 
# return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    l=list(str(num))
    for i in range(len(l)):
        for i in range(len(l)-1):
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    return(int(''.join(l)))
print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))
