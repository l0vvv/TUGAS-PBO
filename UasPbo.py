import tkinter as tk

daftar_menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama":  "Pecel Lele", "harga": 10000},
    3: {"nama": "Ayam Bakar", "harga": 12000},
    4: {"nama": "Ayam Geprek", "harga": 10000},
    5: {"nama": "Ayam Goreng", "harga": 10000},
    6: {"nama": "Nilla Goreng", "harga": 10000},
    7: {"nama": "Mie Goreng", "harga": 8000},
    8: {"nama": "Mie Rebus", "harga": 8000},
}

keranjang = []

def tampilkan_menu():
    print("Daftar Menu:")
    print("============")
    for key, menu in daftar_menu.items():
        print(f"{key}. {menu['nama']} - Rp{menu['harga']}")

def pesan_makanan(pilihan):
    menu = daftar_menu.get(pilihan)
    if menu:
        keranjang.append(menu)
        print(f"{menu['nama']} telah ditambahkan ke keranjang.")
    else:
        print("Menu tidak valid.")

def hapus_pesanan(pilihan):
    if pilihan > 0 and pilihan <= len(keranjang):
        menu = keranjang.pop(pilihan - 1)
        print(f"{menu['nama']} telah dihapus dari keranjang.")
    else:
        print("Pesanan tidak valid.")

def tampilkan_keranjang():
    print("Keranjang Pesanan:")
    print("==================")
    total_harga = 0
    if len(keranjang) > 0:
        for index, menu in enumerate(keranjang):
            print(f"{index+1}. {menu['nama']} - Rp{menu['harga']}")
            total_harga += menu['harga']
        print("Total Harga: Rp", total_harga)
    else:
        print("Keranjang kosong.")

def main():
    print("Selamat datang di Aplikasi Pemesanan Makanan!")
    print("===========================================")

    root = tk.Tk()
    root.title("Aplikasi Pemesanan Makanan")
    root.configure(background="blue")

    def tampilkan_menu_gui():
        menu_text = "Daftar Menu:\n============\n"
        for key, menu in daftar_menu.items():
            menu_text += f"{key}. {menu['nama']} - Rp{menu['harga']}\n"
        menu_label.configure(text=menu_text)

    def pesan_makanan_gui():
        nomor_menu = int(nomor_menu_entry.get())
        pesan_makanan(nomor_menu)
        tampilkan_keranjang_gui()

    def hapus_pesanan_gui():
        nomor_pesanan = int(nomor_pesanan_entry.get())
        hapus_pesanan(nomor_pesanan)
        tampilkan_keranjang_gui()

    def tampilkan_keranjang_gui():
        keranjang_text = "Keranjang Pesanan:\n==================\n"
        total_harga = 0
        if len(keranjang) > 0:
            for index, menu in enumerate(keranjang):
                keranjang_text += f"{index+1}. {menu['nama']} - Rp{menu['harga']}\n"
                total_harga += menu['harga']
            keranjang_text += "Total Harga: Rp" + str(total_harga)
        else:
            keranjang_text = "Keranjang kosong."
        
        keranjang_label.configure(text=keranjang_text)

        # Membuat tampilan GUI
    main_frame = tk.Frame(root, bg="blue")
    main_frame.pack(padx=20, pady=20)

    # Label Daftar Menu
    menu_label = tk.Label(main_frame, text="Daftar Menu:", font=("Arial", 12), bg="blue", fg="white")
    menu_label.pack()

    # Button Tampilkan Menu
    tampilkan_menu_button = tk.Button(main_frame, text="Tampilkan Menu", command=tampilkan_menu_gui)
    tampilkan_menu_button.pack(pady=5)

    # Entry Nomor Menu
    nomor_menu_label = tk.Label(main_frame, text="Masukkan nomor menu:", font=("Arial", 12), bg="blue", fg="white")
    nomor_menu_label.pack()
    nomor_menu_entry = tk.Entry(main_frame)
    nomor_menu_entry.pack()

    # Button Tambah Pesanan
    pesan_makanan_button = tk.Button(main_frame, text="Pesan Makanan", command=pesan_makanan_gui)
    pesan_makanan_button.pack(pady=5)

    # Label Keranjang Pesanan
    keranjang_label = tk.Label(main_frame, text="Keranjang Pesanan:", font=("Arial", 12), bg="blue", fg="white")
    keranjang_label.pack()

    # Button Tampilkan Keranjang
    tampilkan_keranjang_button = tk.Button(main_frame, text="Tampilkan Keranjang", command=tampilkan_keranjang_gui)
    tampilkan_keranjang_button.pack(pady=5)

    # Entry Nomor Pesanan
    nomor_pesanan_label = tk.Label(main_frame, text="Masukkan nomor pesanan yang akan dihapus:", font=("Arial", 12), bg="blue", fg="white")
    nomor_pesanan_label.pack()
    nomor_pesanan_entry = tk.Entry(main_frame)
    nomor_pesanan_entry.pack()

    # Button Hapus Pesanan
    hapus_pesanan_button = tk.Button(main_frame, text="Hapus Pesanan", command=hapus_pesanan_gui)
    hapus_pesanan_button.pack(pady=5)

    # Menjalankan aplikasi
    root.mainloop()


if __name__ == "__main__":
    main()

