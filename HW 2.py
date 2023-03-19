
customer = float(input("กรุณาป้อนผู้ใช้บริการต่อวัน : "))
print("ยอดผู้ใช้บริการจำนวน {:.2f} คน".format(customer))
com = 0.0
if customer>50:
    vat = 5
    com = customer * vat/100
elif customer>30 and customer<=40 :
    vat = 4
    com = customer * vat/100
elif customer>20 and customer<=30:
    vat = 3
    com = customer * vat/100

elif customer<10:
    vat = 1
    com = customer * vat/100
else: 
    vat=0
print("ค่าคอมมิขชั่นให้ผู้ขายประกัน{}% เท่ากับ {:.2f} บาท".format(vat,com))


