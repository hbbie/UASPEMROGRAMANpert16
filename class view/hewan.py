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
