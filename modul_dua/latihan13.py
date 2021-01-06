#13

buah = { 
    "apel" : 25000,
    "mangga" : 15000,
    "kiwi": 20000,
    "alpukat": 30000,
}


keys_list = list(buah) 

uang = input("Masukan Uang Pembeli : ") 
uang_pembeli = uang
k = 0 
print("="*30)
while True  : 
    print(""" 
       -Daftar Buah-buahan-
        apel   : Rp.25000
        mangga : Rp.15000
        kiwi   : Rp.20000
        alpukat: Rp.30000 
    """)
    print("uang anda ada : Rp."+str(uang_pembeli)) 



    masukan_nama_buah = input("masukan nama buah yg ingin di beli: ")
    nama_buah = masukan_nama_buah.lower()
    for i in range(len(keys_list)): 
        if nama_buah in keys_list[i]: 
            continue 
        else: 
            k = k + 1
            k = k
    if k >= len(keys_list): 
        print("-- Toko ini tidak menjual buah yang anda sebutkan tadi -- ")
        break 



    masukan_kg_buah = input("berapa kilo : ")
    print("anda akan membeli ",masukan_kg_buah+'kg ',nama_buah)
    if int(masukan_kg_buah) > 5 : 
        if nama_buah == "kiwi":
           dis = 7
           penjulanan = int(masukan_kg_buah) * buah[nama_buah]
           diskon = 0.07 * penjulanan
           harga_diskon = int(diskon)
           total = int(penjulanan) - int(harga_diskon)

        elif nama_buah == "mangga":
            dis = 7
            penjulanan = int(masukan_kg_buah) * buah[nama_buah]
            diskon = 0.07 * penjulanan
            harga_diskon = int(diskon)
            total = int(penjulanan) - int(harga_diskon)
        elif nama_buah == "apel":
           dis = 5
           penjulanan = int(masukan_kg_buah) * buah[nama_buah]
           diskon = 0.05 * penjulanan
           harga_diskon = int(diskon)
           total = int(penjulanan) - int(harga_diskon)
        elif nama_buah == "alpukat":
            dis = 5
            penjulanan = int(masukan_kg_buah) * buah[nama_buah]
            diskon = 0.05 * penjulanan
            harga_diskon = int(diskon)
            total = int(penjulanan) - int(harga_diskon)
    else: 
        penjulanan = int(masukan_kg_buah) * buah[nama_buah]
        total = penjulanan



    print("\t\t--NOTA--")
    print("Nama buah \t\t\t: ",masukan_nama_buah)
    print("Harga per-kilo Buah :  Rp."+str(buah[nama_buah]))
    print("anda membeli \t\t: ",masukan_kg_buah+"kg buah ",masukan_nama_buah)
    uang_pembeli = int(uang_pembeli) - total
    uang_pembeli = int(uang_pembeli)
    if uang_pembeli > 0 : 
        if int(masukan_kg_buah) > 5:
            print("anda mendapatkan diskon ",str(dis)+"% dari total penjualan sebesar = Rp."+str(harga_diskon))
            print("Total belanja anda adalah Rp."+str(total)," ini sudah termasuk potongan diskon")
        else:
            print("Total belanja anda adalah Rp." + str(total))
    else:
        if int(masukan_kg_buah) > 5:
            print("anda mendapatkan diskon ",str(dis)+"% dari total penjualan sebesar = Rp."+str(harga_diskon))
            print("Total belanja anda adalah Rp."+str(total)," ini sudah termasuk potongan diskon")
        else:
            print("Total belanja anda adalah Rp." + str(total))
        print("Tetapi Uang anda tidak cukup Untuk melakukan pembelian ini")
        break
    if uang_pembeli > 0 :
        print("sisa uang anda adalah = Rp."+str(uang_pembeli))



    k = 0 
    k = k 
    print('\n')
    print('='*30)
    loop_ingin_beli_lagi = input("apakah anda ingin beli buah lagi ?(y/t) : ") 
    loop = loop_ingin_beli_lagi.lower()
    if loop== "y" :
        print('\n')
        continue
    elif loop == "t":
        break
    else:
        print("anda hanya dapat menjawab Y/T , Y untu Ya ,..., T untuk tidak ")
        print("silahkan Ulangi program")
        break










