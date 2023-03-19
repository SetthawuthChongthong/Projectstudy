WM=0
for k in range(1,4):
    weight = int(input("ใส่น้ำหนัก >>> "))
    if weight > WM:
        weight = WM

print("น้ำหนักมากที่สุด >>> {} ".format(weight))