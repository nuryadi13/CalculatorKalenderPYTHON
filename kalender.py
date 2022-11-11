import calendar

#Menampilan Header Kalender
print ("Kalender Header 3")
print (calendar.weekheader(3))
print (" ")
print ("Kalender Header 2")
print (calendar.weekheader(2))
print (" ")
zz = int(input("Masukkan Tahun : "))
mm = int(input("Masukkan Bulan : "))
    # Kalender Bulanan
print (" ")
print ("Kalender Pada Bulan ke {} Tahun {} :".format(mm,zz))
print (" ")
print(calendar.month(zz,mm))
yy = int (input ("Masukkan Tahun : "))
    # Kalender Tahunan
print(calendar.calendar(yy))
    
    #Mengecek Apakah Merupakan Tahun Kabisat Atau Tidak
    # #Tahun Kabisat = 4 Tahun 1x Seperti 2012, 2016, 2020
    # #Bulan Februari Menjadi 29 Hari
print (" ")
print ("Apakah Tahun {} Merupakan Tahun Kabisat : ".format(yy))
print (calendar.isleap(yy))
print (" ")
    #Menentukan Hari Berdasarkan Tanggal,Bulan,Tahun
    # #Dimulai Dari Monday(Senin) = 0 - Sunday(Minggu)= 6
print ("Program Menentukan Hari")
print (" ")
thn= int(input("Masukkan Tahun : "))
bln= int (input("Masukkan Bulan : "))
tgl= int(input("Masukkan Tanggal : "))
day_week_day= calendar.weekday(thn,bln,tgl)
print (" ")
if day_week_day == 0:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Senin".format(tgl,bln,thn))
        if day_week_day == 1:
            print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Selesa".format(tgl,bln,thn))
            if day_week_day == 2:
                print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Rabu".format(tgl,bln,thn))
                if day_week_day == 3:
                    print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Kamis".format(tgl,bln,thn))
                    if day_week_day == 4:
                        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Jumat".format(tgl,bln,thn))
                        if day_week_day == 5:
                            print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Sabtu".format(tgl,bln,thn))
                            if day_week_day == 6:
                                print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Minggu".format(tgl,bln,thn))