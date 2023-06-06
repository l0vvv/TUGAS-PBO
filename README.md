# TUGAS-PBO

sebuah program untuk aplikasi pemesanan makanan menggunakan library Tkinter dalam bahasa pemrograman Python. Program ini memiliki beberapa fungsi utama yang dapat digunakan untuk menampilkan daftar menu, memesan makanan, menghapus pesanan, dan menampilkan keranjang pesanan.

Pada bagian awal program, terdapat deklarasi variabel daftar_menu yang berisi daftar makanan beserta harganya. Variabel keranjang digunakan untuk menyimpan pesanan yang dipilih oleh pengguna.

Fungsi tampilkan_menu() digunakan untuk menampilkan daftar menu beserta harganya di konsol. Setiap menu akan ditampilkan dengan nomor urut, nama, dan harga.

Fungsi pesan_makanan() digunakan untuk memasukkan pesanan makanan ke dalam keranjang. Pengguna memasukkan nomor menu yang dipilih, kemudian program akan mencari menu tersebut dalam daftar_menu. Jika ditemukan, menu akan ditambahkan ke keranjang dan pesan sukses akan ditampilkan di konsol. Jika nomor menu tidak valid, pesan error akan ditampilkan.

Fungsi hapus_pesanan() digunakan untuk menghapus pesanan dari keranjang berdasarkan nomor pesanan yang diberikan. Jika nomor pesanan valid, menu akan dihapus dari keranjang dan pesan sukses akan ditampilkan. Jika nomor pesanan tidak valid, pesan error akan ditampilkan.

Fungsi tampilkan_keranjang() digunakan untuk menampilkan isi keranjang pesanan di konsol. Jika keranjang tidak kosong, setiap menu dalam keranjang akan ditampilkan dengan nomor urut, nama, dan harga. Total harga pesanan juga akan ditampilkan. Jika keranjang kosong, pesan keranjang kosong akan ditampilkan.

Fungsi main() merupakan fungsi utama yang akan dieksekusi saat program dijalankan. Di dalam fungsi ini, terdapat pengaturan tampilan GUI menggunakan Tkinter. Program akan membuat jendela aplikasi dengan judul "Aplikasi Pemesanan Makanan" dan latar belakang berwarna biru.

Dalam GUI, terdapat beberapa komponen seperti label, tombol, dan entri yang digunakan untuk menampilkan daftar menu, memesan makanan, menampilkan keranjang pesanan, menghapus pesanan, dan memasukkan nomor menu atau nomor pesanan. Ketika tombol-tombol ditekan, fungsi-fungsi terkait akan dipanggil untuk menjalankan aksi yang sesuai.

Terakhir, program akan menjalankan aplikasi dengan memanggil fungsi main() jika file ini dijalankan langsung (bukan diimpor sebagai modul).

Kode di atas menggabungkan fitur konsol dan GUI. Fungsi-fungsi yang sama ada baik dalam tampilan konsol maupun GUI, namun ditulis dalam format yang sesuai dengan masing-masing tampilan. Hal ini memungkinkan pengguna untuk memilih antara menggunakan antarmuka konsol atau GUI untuk berinteraksi dengan aplikasi.
