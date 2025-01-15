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
