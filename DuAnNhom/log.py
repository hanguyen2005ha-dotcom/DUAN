import sympy as sp

x = sp.symbols('x', positive=True)
a = float(input("Nhap a: "))
b = float(input("Nhap co so b: "))
c = float(input("Nhap c: "))

if b <= 0 or b == 1:
    print("Co so b khong hop le")
else:
    f = a*sp.log(x, b) + c
    print("Ham so:", f)

    if a == 0:
        print("GTLN = GTNN =", c)
    else:
        print("Ham so khong co GTLN va GTNN")