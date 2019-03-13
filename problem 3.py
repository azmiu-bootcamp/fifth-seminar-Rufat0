a = int(input("a-ni daxil edin-> "))
b = int(input("b-ni daxil edin-> "))
c = int(input("c-ni daxil edin-> "))




def lone_sum(a , b , c):
    if a != b and a != c and b != c:
        print(a+b+c)
    elif a == b == c:
        print(a)
    elif a == b and a != c:
        print(a + c)
    elif a == c and a != b:
        print(a + b)
    elif b == c and b != a:
        print(b + a)





lone_sum(a,b,c)
