#Complete the method/function so that it 
# converts dash/underscore delimited words into camel casing.
#  The first word within the output should be capitalized 
# only if the original word was capitalized (known as Upper Camel Case, also often
#  referred to as Pascal case). The next words should be always capitalized.

def to_camel_case(s):
    text=list(s)
    for i in range(len(text)-1):
        if text[i]=='-' or text[i]=='_':
            text[i+1]=text[i+1].upper()

    t="".join(text).replace("_","").replace("-","")
    return t

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))
