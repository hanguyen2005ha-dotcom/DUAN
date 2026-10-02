import sympy as sp

x = sp.symbols('x')

a = float(input("Nhập a: "))

if a == 0:
    print("Đây không phải hàm bậc hai.")
else:
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    f = a*x**2 + b*x + c
    x0 = -b/(2*a)
    y0 = f.subs(x, x0)

    print("Hàm số:", f)
    print("Đỉnh I =", (x0, y0))

    if a > 0:
        print("Hàm số có giá trị nhỏ nhất:", y0)
        print("Đạt tại x =", x0)
    else:
        print("Hàm số có giá trị lớn nhất:", y0)
        print("Đạt tại x =", x0)