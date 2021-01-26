
#diketahui
jarak = 150

kecepatan_budi = 60
waktu_budi_berangkat = 05.00

kecepatan_yandi = 40
waktu_yandi_berangkat = 05.15



k1 = kecepatan_budi
k2 = kecepatan_yandi



time1 = '0'+str(waktu_budi_berangkat).replace('.',' ')+'0'
time2 = '0'+str(waktu_yandi_berangkat).replace('.',' ')+'0'

jadikan_list_budi = time1.split()
jadikan_list_yandi = time2.split()

if len(jadikan_list_yandi[1]) > 2 :
    ubah = str(jadikan_list_yandi[1]).replace('0','')
    jadikan_list_yandi[1] = ubah
else:
    jadikan_list_yandi[1] = jadikan_list_yandi[1]



if len(jadikan_list_budi[1]) > 2 :
    ubah = str(jadikan_list_budi[1]).replace('0','')
    jadikan_list_budi[1] = ubah
else:
    jadikan_list_yandi[1] = jadikan_list_yandi[1]


if int(jadikan_list_budi[1]) > int(jadikan_list_yandi[1]) :
    total = int(jadikan_list_budi[1]) - int(jadikan_list_yandi[1])
else:
    total = int(jadikan_list_yandi[1]) - int(jadikan_list_budi[1])

perbedaan_waktu_dalam_jam  = total
selisih_jarak = k1 * perbedaan_waktu_dalam_jam / 60
wp1 = jarak - selisih_jarak
wp2 = k1 + k2
wp3 = wp1/wp2

hilangkan_koma = str(wp3).replace('.',' ')
jadikan_list = hilangkan_koma.split()
gabung = jadikan_list[1]
jadi_0_koma = '0.'+gabung

wp5 = float(jadi_0_koma) * 60
wp6 = int(wp5)
wp7 = jadikan_list[0]+'.'+str(wp6)
wp8 = float(wp7)

waktu1 = waktu_yandi_berangkat + wp8
time3 = str(waktu1).replace('.',' ')
jadikan_list_waktu1 = time3.split()


if len(jadikan_list_waktu1[0]) < 2 :
    if len(jadikan_list_waktu1[1]) < 2:

        print('mereka berdua akan berpapasan pada pukul',"0" + str(waktu1)+"0")

    print('mereka berdua akan berpapasan pada pukul',"0"+str(waktu1))
else:
    if len(jadikan_list_waktu1[1]) < 2:
        print('mereka berdua akan berpapasan pada pukul',str(waktu1) + "0")
    else:
        print('mereka berdua akan berpapasan pada pukul',waktu1)
