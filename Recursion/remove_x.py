def remove_x(s):
    if len(s)==0:
        return s
    small_output = remove_x(s[1:])
    if s[0] == "x":
        return small_output
    else :
        return s[0] + small_output
s = input("Enter the string : ")
print(remove_x(s))