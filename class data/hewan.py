class Data_Pendaftaran:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat

    def __str__(self):
        return f"Nama: {self.nama}, Jenis: {self.jenis}, Habitat: {self.habitat}"
