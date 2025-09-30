def create_phone_number(numbers):

    return"({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

print(create_phone_number([1,1,1,1,1,1,1,1,1,1])) 
print(create_phone_number([0,2,3,0,5,6,0,8,9,0]))  
print(create_phone_number([0,0,0,0,0,0,0,0,0,0]))