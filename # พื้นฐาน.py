# พื้นฐาน
# 1. การคอมเมนต์
''' 1 Line
> 1 Lines '''

# 2. แสดงผลออกทางจอภาพอย่างง่าย
# print('Hello')
# print("Hello")

# print('Hello')
# print('Pasapitch')
# print('Chujai')

# print('''Hello
# Pasapitch
# Chujai''')

# print("""Hello
# Pasapitch
# Chujai""")
# 3. การสร้างและเรียกใช้ตัวแปร
#ชื่อตัวแปร = ค่าที่กำหนดให้กับตัวแปร
''' v = 6
print(type(v))
v = v * 5.0
print(type(v))
_v = 5
first_Name = 'P'
last_Name = 'Chujai'
print(type(first_Name))
print(type(last_Name))
print('first_Name')
print(last_Name) '''
# 3.2 การแปลงชนิดข้อมูล
# v = 7
# print(type(v), v)
# v = oct(v)
# print(type(v), v)
# 4. นิพจน์
# num1 = 3
# num2 = {3, 5}  # 0000 0101
# output = 7 in num2
# print(output)

# 5. แสดงผลออกทางจอภาพระดับสูง
# กำหนดข้อมูลความกว้าง เป็น 10 ความยาวเป็น 1.5 จงหาพื้นที่สี่เหลี่ยมผืนผ้า พร้อมทั้งแสดงผลพื้นที่
# พท = ก * ย
''' w = 10
l = 1.5
a = w*l
print('พื้นที่ =' + str(a))  # + , '''
''' P 5000 ครั้ง

-Loop
-print 500 ครั้ง
print(arg * n) '''
# print('P\n'*5)
# %c %d
# print("%f %.2f %d" % (5, 5.455, 5))
# print("L = {:*<20,.2f} W = {:*^20,.2f} Area ={:*>20,.2f}".format(1.5, 10, 1.5*10))

# print(1, 3, 5, 7, sep='\t', end='\t****')
# print(str(w)+str(w))  # 1010
# number => string => str

# 6. การรับข้อมูล
# 6.1 รับค่ามา 1 ค่า
# age = int(input("Enter your age : "))
# print(age, "type = ", type(age))
# ข้อมูลที่รับเข้ามาจะเป็นตัวอักษร
# ถ้าจะเอาไปคำนวณ จะต้องทำการแปลงข้อมูลนั้นให้เป็นตัวเลข
# if age > 50:
#     print('Old')
# else:
#     print('Y')
# 6.2 รับค่ามา > 1 ค่า
var1, var2, var3 = [v for v in input(
    "Enter three characters (รับข้อมูลแล้วกดปุ่ม space bar เมื่อรับตัวสุดท้ายให้กดปุ่ม Enter): ").split()]
print("Var1 : {} Var2 : {} Var3 : {}".format(var1, var2, var3))

# การบ้าน
# ให้สร้างรูปอะไรก็ได้ โดยใช้คำสั่งที่เรียนมาวันนี้