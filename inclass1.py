sale = float(input("กรุณาป้อนยอดขาย : "))
print("ยอดขายเท่ากับ {:.2f} บาท".format(sale))
com = 0.0
if sale<=  6000:
    vat = 0.5
    com = sale * vat/100
elif sale<6000:
    vat = 1
    com = sale * vat/100
elif sale<8000:
    vat = 1.5
    com = sale * vat/100
else: 
    vat = 2
    com = sale * vat/100
print("ค่าคอมมิขชั่น{}% เท่ากับ {:.2f} บาท".format(vat,com))


