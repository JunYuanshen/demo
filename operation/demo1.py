print("hello world!")
def cal(a,b,s):
    if s == 'add':
        return a+b
    elif s == 'sub':
        temp = a-b
        if temp < 0:
            return -temp
        else:        
            return temp
    elif s == 'mul':
        return a*b
    else :
        if a > b:
            return a/b
        else :
            return b/a
a = input()
b = input()
s = input()
print(cal(a,b,s))

            