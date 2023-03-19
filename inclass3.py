check=0
while check != 'Q'and check !='q':
        name = str(input("ระบุชื่อ-นามสกุล>>>"))
        age  = int(input("ระบุอายุ>>>>"))
        sex = str(input("โปรดระบุเพศของท่าน>>>"))
        check=str(input("Press Q and q to Exit>>>>>>>>>>"))
        print("Name : {}, อายุ {},เพศ {}".format(name,age,sex))