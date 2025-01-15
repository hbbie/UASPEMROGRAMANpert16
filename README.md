# UASPEMROGRAMANpert16
Ujian Akhir Semester

## Biodata
# Nama    : Dhani Naufal Habibie
# Kelas   : TI.24.A4
# Mata Kuliah :Bahasa Pemrogaraman
# Dosen Pengampu : Agung Nugroho, S.Kom., M.Kom

## Project UAS Semester 1

![Screenshot 2025-01-06 133248](https://github.com/user-attachments/assets/feccb230-61aa-4278-b6ab-49bce3d5f2fb)

# dengan kode program
# Data (hewan.py)

```python
class Data_Pendaftaran:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat

    def __str__(self):
        return f"Nama: {self.nama}, Jenis: {self.jenis}, Habitat: {self.habitat}"
```
# view(hewan.py)
```python
from data.hewan import Data_Pendaftaran

class view_pendaftaran:
    def get_input():
        print("tambahkan hewan yang dibeli")
        nama = input("Nama: ")
        jenis = input("jenis: ")
        habitat = input("Habitat hidup: ")
        return nama, jenis, habitat

    def table_view(data_table):
        print("=" * 60)
        print("| NO |           NAMA           |     JENIS     |  HABITAT  |")
        print("=" * 60)

        for i, data in enumerate(data_table, start=1):
            print(f"| {i:<2} | {data.nama:<24} | {data.jenis:<13} | {data.habitat:<8} |")
        print("=" * 60)

    def display_message(message):
        print(message)
```
# Process(hewan.py)
```python
import re
from data.hewan import Data_Pendaftaran
from view.hewan import view_pendaftaran


class process_pendaftaran:
    def validate_nama(nama):
        if not nama.isalpha():
            raise ValueError("Nama hanya boleh berisi huruf.")
        
    def validate_jenis(jenis):
        if not jenis.isalpha():
            raise ValueError("Jenis hewan hanya boleh berisi huruf.")

    def validate_habitat(habitat):
        if not habitat.isalpha():
            raise ValueError("habitat tidak boleh berisi angka.")

   

    def validate_data(data):
        process_pendaftaran.validate_nama(data.nama)
        process_pendaftaran.validate_jenis(data.jenis)
        process_pendaftaran.validate_habitat(data.habitat)
```
# main.py
```python
from data.hewan import Data_Pendaftaran
from view.hewan import view_pendaftaran
from process.hewan import process_pendaftaran

def main():
    data_table = []  # Tempat menyimpan data pendaftaran

    while True:
        print("\nSelamat datang!!!")
        print("Menu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Edit Data")
        print("4. Lihat Semua Data")
        print("5. Keluar")

        menu_choice = input("Pilih menu (1-5): ")

        if menu_choice == "1":
            # Tambah Data
            try:
                nama, jenis, habitat = view_pendaftaran.get_input()
                data = Data_Pendaftaran(nama, jenis, habitat)

                # Validasi data
                process_pendaftaran.validate_data(data)

                # Tambahkan data ke tabel
                data_table.append(data)
                view_pendaftaran.display_message("Pendaftaran berhasil dan valid!")
            except ValueError as e:
                view_pendaftaran.display_message(f"Error: {e}")

        elif menu_choice == "2":
            # Hapus Data
            if not data_table:
                view_pendaftaran.display_message("Tidak ada data untuk dihapus.")
            else:
                view_pendaftaran.table_view(data_table)
                try:
                    row_to_delete = int(input("Masukkan nomor data yang ingin dihapus: "))
                    if 1 <= row_to_delete <= len(data_table):
                        deleted_data = data_table.pop(row_to_delete - 1)
                        view_pendaftaran.display_message(f"Data '{deleted_data.nama}' berhasil dihapus.")
                    else:
                        view_pendaftaran.display_message("Nomor yang dimasukkan tidak valid.")
                except ValueError:
                    view_pendaftaran.display_message("Input harus berupa angka.")

        elif menu_choice == "3":
            # Edit Data
            if not data_table:
                view_pendaftaran.display_message("Tidak ada data untuk diedit.")
            else:
                view_pendaftaran.table_view(data_table)
                try:
                    row_to_edit = int(input("Masukkan nomor data yang ingin diedit: "))
                    if 1 <= row_to_edit <= len(data_table):
                        data = data_table[row_to_edit - 1]
                        print(f"Edit data untuk: {data.nama}")
                        nama = input(f"Nama ({data.nama}): ") or data.nama
                        jenis = input(f"Jenis ({data.jenis}): ") or data.jenis
                        habitat = input(f"Habitat ({data.habitat}): ") or data.habitat

                        updated_data = Data_Pendaftaran(nama, jenis, habitat)
                        process_pendaftaran.validate_data(updated_data)

                        data_table[row_to_edit - 1] = updated_data
                        view_pendaftaran.display_message(f"Data berhasil diperbarui untuk: {nama}")
                    else:
                        view_pendaftaran.display_message("Nomor yang dimasukkan tidak valid.")
                except ValueError as e:
                    view_pendaftaran.display_message(f"Error: {e}")

        elif menu_choice == "4":
            # Lihat Semua Data
            if not data_table:
                view_pendaftaran.display_message("Belum ada data yang terdaftar.")
            else:
                view_pendaftaran.table_view(data_table)

        elif menu_choice == "5":
            # Keluar
            print("Terima kasih telah menggunakan layanan pendaftaran!")
            break
        else:
            view_pendaftaran.display_message("Pilihan menu tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

        
```
# gambaran
![image](https://github.com/user-attachments/assets/d9e42d10-75da-412f-b52b-3c0fb6505865)

# Penjelasan
# __init__
setiap class(data, view, process)harus menambahkan __init__ , agar secara otomatis menginisialisasi objek data dengan atribut nama, jenis, dan habitat.
Keuntungan __init__

    Otomatis: Mengatur atribut langsung saat objek dibuat.
    Lebih Aman: Memastikan bahwa atribut objek diinisialisasi dengan benar.
    Bersih dan Terstruktur: Menjaga kode tetap rapi dengan standar pembuatan objek.
# .venv (Virtual Environment)

Folder .venv adalah direktori untuk virtual environment, yang digunakan untuk:

    Mengisolasi dependensi proyek Python Anda dari sistem global.
    Menghindari konflik antara versi pustaka yang digunakan di berbagai proyek.

Fungsi Virtual Environment:

    Penyimpanan Lokal Dependensi: Semua pustaka yang diinstal menggunakan pip di virtual environment akan disimpan di dalam .venv, sehingga tidak memengaruhi sistem global.
    Manajemen Versi Python: Anda dapat menentukan versi Python tertentu untuk setiap proyek.

Cara Kerja .venv:

    Virtual environment dibuat dengan perintah:

python -m venv .venv

Untuk mengaktifkan:

    Windows:

.venv\Scripts\activate

Linux/Mac:

    source .venv/bin/activate

Setelah aktif, Anda dapat menginstal pustaka dengan pip seperti biasa, dan pustaka akan tersimpan di folder .venv.
## Validasi Input
![image](https://github.com/user-attachments/assets/9c558023-c168-491e-b5dd-8bc161858850)

## Hasil Program
![image](https://github.com/user-attachments/assets/048ed574-d901-4f3c-903b-0547ac601454)



