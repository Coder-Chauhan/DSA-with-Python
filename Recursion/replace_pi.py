def replace_pi(s):
    if len(s)==0 or len(s)==1:
        return s
    
    if s[0:2]=="pi":
        small_output = replace_pi(s[2:])
        return "3.14" + small_output
    else :
        small_output = replace_pi(s[1:])
        return s[0] + small_output

s = input("Enter the string : ")
print(replace_pi(s))