import tkinter as tk


# --- FUNGSI LOGIKA ---
def hitung_jumlah():
    try:
        bil1 = float(entry_bil1.get())
        bil2 = float(entry_bil2.get())
        hasil = bil1 + bil2
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        label_hasil.config(text="Error: Masukkan bilangan!")


# --- SETUP JENDELA UTAMA ---
jendela = tk.Tk()
jendela.title("Kalkulator Jumlah")
jendela.geometry("300x200")  # Mengatur ukuran jendela

# --- WIDGET UNTUK BILANGAN PERTAMA ---
label_bil1 = tk.Label(jendela, text="Bilangan Pertama:")
label_bil1.pack()
entry_bil1 = tk.Entry(jendela)
entry_bil1.pack()

# --- WIDGET UNTUK BILANGAN KEDUA ---
label_bil2 = tk.Label(jendela, text="Bilangan Kedua:")
label_bil2.pack()
entry_bil2 = tk.Entry(jendela)
entry_bil2.pack()

# --- TOMBOL DAN LABEL HASIL ---
tombol_hitung = tk.Button(jendela, text="Jumlahkan", command=hitung_jumlah)
tombol_hitung.pack(pady=10)  # pady memberi sedikit jarak vertikal

label_hasil = tk.Label(jendela, text="Hasil: ")
label_hasil.pack()

# --- MEMULAI APLIKASI ---
jendela.mainloop()
