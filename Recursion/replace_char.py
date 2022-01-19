def replace_char(s,a,b):
    if len(s) == 0:
        return s
    small_output = replace_char(s[1:],a,b)
    if s[0] == a:
        return str(b)+ str(small_output)
    else :
        return str(s[0]) + str(small_output)
    
s = "Bhanu Pratap"
a = "a"
b = "b"
print(replace_char(s,a,b))