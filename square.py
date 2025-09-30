def square_digits(num):
    m=[]
    for i in str(num):
        l=int(i)**2
        m.append(str(l))
    r=int("".join(m))
    return r
print(square_digits(765))