import sympy as sp

x = sp.symbols('x')
a = float(input("Nhập cơ số a: "))
f_str = input("Nhập biểu thức f(x): ")
m = float(input("Nhập m: "))
n = float(input("Nhập n: "))

if m > n:
    m, n = n, m

if a <= 0 or a == 1:
    print("Cơ số a phải thỏa mãn 0 < a != 1.")
else:
    f = sp.sympify(f_str)
    f_min = sp.calculus.util.minimum(f, x, sp.Interval(m, n))
    if f_min <= 0:
        print("Hàm số không xác định trên đoạn [m, n].")
    else:
        y = sp.log(f) / sp.log(a)
        df = sp.diff(f, x)
        crit_pts = sp.solve(df, x)
        diem_xet = [m, n]
        for pt in crit_pts:
            if pt.is_real and m <= pt <= n:
                diem_xet.append(float(pt))
        diem_xet = list(set(diem_xet))
        gia_tri = [(t, float(y.subs(x, t))) for t in diem_xet]
        GTLN = max(gia_tri, key=lambda p: p[1])
        GTNN = min(gia_tri, key=lambda p: p[1])
        print("Hàm số: y = log_", a, "(", f, ")")
        print("Các điểm cần xét:", diem_xet)
        print("GTLN =", round(GTLN[1], 4), "đạt tại x =", GTLN[0])
        print("GTNN =", round(GTNN[1], 4), "đạt tại x =", GTNN[0])