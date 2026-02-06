data_stok = "Stok_barang.txt"
def tampil_barang():
    with open(data_stok,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            idx,barang,jumlah = baris.split(",")
            dict_barang[idx] = {"barang": barang, "jumlah": jumlah}
            