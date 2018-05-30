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
print("합계:", p_baesu)
#print("합계:", baesu(1, 10, 3))하면 한줄로 1에서 10사이의 3의배수의 합계를 구할 수 있음
#print("합계:", print_baesu(a,b,c))하면 p_baesu이걸로 안받고 바로해도된다.
