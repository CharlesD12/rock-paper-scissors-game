# rock-paper-scissors-game
Ini merupakan game gunting, kertas, batu sederhana dengan menggunakan Function dan Import module. Kode script.py berfungsi mengimpor modul utils dan random. Modul utils kemungkinan berisi fungsi yang digunakan dalam permainan, seperti validate, print_hand, dan judge. Modul random digunakan untuk menghasilkan pilihan tangan komputer secara acak.

Pertama, program mencetak pesan untuk memulai permainan dan meminta pemain untuk memasukkan nama mereka. Kemudian, program memasuki loop while yang akan terus berjalan sampai pemain memutuskan untuk berhenti bermain. Di dalam loop, program meminta pemain untuk memilih tangan mereka dengan memasukkan nomor antara 0-2, di mana 0 mewakili batu, 1 mewakili kertas, dan 2 mewakili gunting.

Setelah pemain memasukkan pilihan tangan mereka, program memeriksa apakah pilihan tersebut valid dengan menggunakan fungsi validate dari modul utils. Jika pilihan tersebut valid, program kemudian menetapkan pilihan tangan komputer secara acak menggunakan fungsi randint dari modul random. Kemudian, program mencetak pilihan tangan pemain dan komputer menggunakan fungsi print_hand dari modul utils.

Setelah itu, program menentukan hasil permainan dengan menggunakan fungsi judge dari modul utils dan mencetak hasilnya. Program kemudian meminta pemain apakah mereka ingin bermain lagi atau tidak. Jika pemain ingin bermain lagi, loop akan terus berjalan. Jika tidak, program akan mencetak pesan terima kasih dan keluar dari loop.

Jika pilihan tangan pemain tidak valid, program akan mencetak pesan kesalahan dan meminta pemain untuk memasukkan nomor yang benar. Loop akan terus berjalan sampai pemain memutuskan untuk berhenti bermain atau memasukkan pilihan tangan yang valid.

Kode utils.py mendefinisikan tiga fungsi yang digunakan dalam permainan gunting, kertas, batu yang dijelaskan sebelumnya.

Fungsi pertama adalah validate(hand), yang menerima satu argumen hand yang merupakan pilihan tangan pemain. Fungsi ini memeriksa apakah pilihan tangan tersebut valid atau tidak. Jika pilihan tangan kurang dari 0 atau lebih dari 2, fungsi akan mengembalikan False yang menunjukkan bahwa pilihan tangan tidak valid. Jika tidak, fungsi akan mengembalikan True yang menunjukkan bahwa pilihan tangan valid.

Fungsi kedua adalah print_hand(hand, name='Tamu'), yang menerima dua argumen: hand yang merupakan pilihan tangan dan name yang merupakan nama pemain. Argumen name bersifat opsional dan memiliki nilai default 'Tamu'. Fungsi ini mencetak pilihan tangan pemain dalam bentuk teks. Pertama, fungsi mendefinisikan daftar hands yang berisi teks untuk setiap pilihan tangan: 'Batu', 'Kertas', dan 'Gunting'. Kemudian, fungsi mencetak nama pemain dan pilihan tangan mereka dengan mengakses elemen daftar hands yang sesuai dengan indeks hand.

Fungsi ketiga adalah judge(player, computer), yang menerima dua argumen: player yang merupakan pilihan tangan pemain dan computer yang merupakan pilihan tangan komputer. Fungsi ini menentukan hasil permainan dan mengembalikan teks yang sesuai: 'Seri', 'Kalah', atau 'Menang'. Fungsi ini menggunakan logika sederhana untuk menentukan hasil permainan: jika pilihan tangan pemain sama dengan pilihan tangan komputer, hasilnya seri; jika pemain memilih batu dan komputer memilih kertas, atau pemain memilih kertas dan komputer memilih gunting, atau pemain memilih gunting dan komputer memilih batu, maka hasilnya kalah; selain itu, hasilnya menang.

Berikut output programnya :
<img width="889" alt="image" src="https://github.com/CharlesD12/rock-paper-scissors-game/assets/78160523/398df63f-e8e6-4da7-836f-8d27b7e6421f">
