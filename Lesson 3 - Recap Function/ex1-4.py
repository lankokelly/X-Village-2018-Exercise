a_score=91
a_hour=20
pay_a=200*a_hour
if a_score>90:
    pay_a=pay_a+8000
elif a_score<70:
    pay_a=pay_a+4000
else:
    pay_a=pay_a+6000
print(pay_a)

b_score=75
b_hour=15
pay_b=200*b_hour
if b_score>90:
    pay_b=pay_b+8000
elif a_score<70:
    pay_b=pay_b+4000
else:
    pay_b=pay_b+6000
print(pay_b)

c_score=60
c_hour=25
pay_c=200*c_hour
if c_score>90:
    pay_c=pay_c+8000
elif c_score<70:
    pay_c=pay_c+4000
else:
    pay_c=pay_c+6000
print(pay_c)

d_score=75
d_hour=10
pay_d=200*d_hour
if d_score>90:
    pay_d=pay_d+8000
elif d_score<70:
    pay_d=pay_d+4000
else:
    pay_d=pay_d+6000
print(pay_d)

e_score=80
e_hour=12
pay_e=200*e_hour
if e_score>90:
    pay_e=pay_e+8000
elif e_score<70:
    pay_e=pay_e+4000
else:
    pay_e=pay_e+6000
print(pay_e)

f_score=90
f_hour=25
pay_f=200*f_hour
if f_score>90:
    pay_f=pay_f+8000
elif e_score<70:
    pay_f=pay_f+4000
else:
    pay_f=pay_f+6000
print(pay_f)

g_score=45
g_hour=14
pay_g=200*g_hour
if g_score>90:
    pay_g=pay_g+8000
elif e_score<70:
    pay_g=pay_g+4000
else:
    pay_g=pay_g+6000
print(pay_g)

h_score=95
h_hour=13
pay_h=200*h_hour
if h_score>90:
    pay_h=pay_h+8000
elif h_score<70:
    pay_h=pay_h+4000
else:
    pay_h=pay_h+6000
print(pay_h)

i_score=88
i_hour=2
pay_i=200*i_hour
if i_score>90:
    pay_i=pay_i+8000
elif i_score<70:
    pay_i=pay_i+4000
else:
    pay_i=pay_i+6000
print(pay_i)

def pay(score,hour):
    pay=200*hour
    if score>90:
        pay=pay+8000
    elif score<70:
        pay=pay+4000
    else:
        pay=pay+6000
    print(pay)

pay(91,20)
pay(75,15)
pay(60,25)
pay(75,10)
pay(80,12)
pay(90,25)
pay(45,14)
pay(95,13)
pay(88,2)