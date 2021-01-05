
masukan_nama_pegawai = input("Nama Pegawai : ")
masa_kerja_pegawai = input('Masa Kerja : ')
print("masa kerja ",masa_kerja_pegawai," tahun")
gaji_pokok = input("masukan besaran gaji : ")
pegawai = input("apakah pegawai tetap : jawab Y atau T :")
pegawai_1 = pegawai.lower()
status = input("sudah Berkeluarga ? : Y atau T : " )
status_1 =status.lower()

if int(masa_kerja_pegawai) > 5 :
    bonus = 0.15 * int(gaji_pokok)
    bonus = int(bonus)

else:
    bonus = 0

if pegawai_1 == 'y' :
    transport = 150000
    transport = int(transport)

else:
    transport = 0

if status_1 == 'y' :
    tunjangan = 0.1 * int(gaji_pokok)
    tunjangan = int(tunjangan)

else:
    tunjangan = 0

gaji_bersih = int(gaji_pokok) + bonus + tunjangan + transport

print("="*30)
print("\n")

print("\t\t___Penghitungan Gaji Pegawai___ ")
print("Nama :", masukan_nama_pegawai)
print("Sudah Bekerja Selama ",masa_kerja_pegawai," Tahun")
if int(masa_kerja_pegawai) > 5 :
    print("mendapatkan Bonus sebesar Rp.",bonus)
if pegawai_1 == 'y' :
    print("dikarnakan pegawai tetap maka mendapatkan uang transport\n"
          "Sebesar Rp.",transport)

if status_1 == 'y' :
    print("mendapatkan tunjangan sebesar Rp.",tunjangan)
print("Gaji Pokok Sebesar Rp.",gaji_pokok,"per-Bulan")
print("Gaji Bersih adalah Rp.",gaji_bersih)
