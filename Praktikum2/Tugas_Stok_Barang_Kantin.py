data_stok = "Stok_barang.txt"
def tampil_barang():
    dict_barang = {}
    with open(data_stok,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            idx,barang,jumlah = baris.split(",")
            dict_barang[idx] = {"barang": barang, "jumlah": jumlah}
    return dict_barang

tampil_data = tampil_barang()

def tampil_data_barang(dict_barang):
    print("\n=== DATA STOK BARANG KANTIN ===")
    print(f"{'ID' : <8} | {'barang' : <20} | {'jumlah' : >7}")
    print("-"*40)
    for idx in sorted(dict_barang.keys()):
        barang = dict_barang[idx]['barang']
        jumlah = dict_barang[idx]['jumlah']
        print(f"{idx : <8} | {barang : <20} | {jumlah : >7}")

tampil_data_barang(tampil_data)
