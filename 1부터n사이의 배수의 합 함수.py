def print_baesu(a,b,c):
    n=0
    i=a
    while i <= b:
        if i%c==0:
            n=n+i
        i=i+1
    return n

a=int(input("시작 값을 입력하시오: "))
b=int(input("끝 값을 입력하시오: "))
c=int(input("배수로 정할 값을 입력하시오: "))
p_baesu=print_baesu(a,b,c)
print(p_baesu)
