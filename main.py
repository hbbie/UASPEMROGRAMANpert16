import re
from data.hewan import Data_Pendaftaran
from view.hewan import view_pendaftaran
from process.hewan import process_pendaftaran

def main():
    data_table = []  # Tempat menyimpan data pendaftaran
    while True:
        print("\nselamat datang!!!")
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
                    row_to_delete = int(input("Masukkan nama hewan yang ingin dihapus: "))
                    if 1 <= row_to_delete <= len(data_table):
                        deleted_data = data_table.pop(row_to_delete - 1)
                        view_pendaftaran.display_message(f"Data '{deleted_data.nama}' berhasil dihapus.")
                    else:
                        view_pendaftaran.display_message("data yang dimasukkan tidak valid.")
                except ValueError:
                    view_pendaftaran.display_message("Input harus berupa huruf.")

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
                        nama = input(f"nama ({data.nama}): ") or data.nama
                        jenis = input(f"jenis ({data.jenis}): ") or data.jenis
                        habitat = input(f"habitat ({data.habitat}): ") or data.habitat

                        updated_data = Data_Pendaftaran(nama, jenis, habitat)
                        process_pendaftaran.validate_data(updated_data)

                        data_table[row_to_edit - 1] = updated_data
                        view_pendaftaran.display_message(f"Data berhasil diperbarui untuk: {nama}")
                    else:
                        view_pendaftaran.display_message("Nomor yang dimasukkan tidak valid.")
                except ValueError as e:
                    view_pendaftaran.display_message(f"Error: {e}")
                except Exception:
                    view_pendaftaran.display_message("Terjadi kesalahan saat mengedit data.")

        elif menu_choice == "4":
            # Lihat Semua Data
            if not data_table:
                view_pendaftaran.display_message("Belum ada data yang terdaftar.")
            else:
                view_pendaftaran.table_view(data_table)

        elif menu_choice == "5":
            # Keluar
            print("Terima kasih telah mendaftar!!!")
            break
        else:
            view_pendaftaran.display_message("Pilihan menu tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
