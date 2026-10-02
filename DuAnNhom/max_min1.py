import sympy as sp

x = sp.symbols('x')
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
m = float(input("Nhập m: "))
n = float(input("Nhập n: "))

if a == 0:
    print("Đây không phải là hàm số bậc hai.")
else:
    if m > n:
        m, n = n, m
    f = a*x**2 + b*x + c
    x0 = -b/(2*a)
    diem_xet = [m, n]
    if m <= x0 <= n:
        diem_xet.append(x0)
    gia_tri = [(t, f.subs(x,t)) for t in diem_xet]
    GTLN = max(gia_tri, key=lambda p: p[1])
    GTNN = min(gia_tri, key=lambda p: p[1])
    print("Hàm số:", f)
    print("Hoành độ đỉnh:", x0)
    print("Các điểm cần xét:", diem_xet)
    print("GTLN =", GTLN[1])
    print("Đạt tại x =", GTLN[0])
    print("GTNN =", GTNN[1])
    print("Đạt tại x =", GTNN[0])