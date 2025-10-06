#Write an algorithm that takes an array and moves all of the zeros to the end,
#  preserving the order of the other elements.

#move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]



def move_zeros(lst):
    #lst=([1,0,1,2,0,1,3])
    a=0
    count=lst.count(a)
    for i in range(count):
        lst.remove(a)
        lst.append(a)
    return lst
print(move_zeros(lst=([1,0,1,2,0,1,3])))