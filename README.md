## 🛡️ SPY CONSOLE TERMUX

Pusat kendali alat keamanan siber berbasis Termux yang menggabungkan berbagai tools pentesting dalam satu interface.

## 📋 Fitur Tersedia
- **SQLmap**: Otomatisasi eksploitasi SQL Injection.
- **Metasploit**: Framework eksploitasi sistem dan jaringan.
- **Nikto**: Pemindaian kerentanan server web.
- **SMS Sender**: Automasi pengiriman pesan via kartu SIM.
- **Nmap**: Pemindaian port dan audit jaringan.
- **OSINT Scraper**: Pengambilan data gambar dari website secara otomatis.

## ⚙️ Cara Instalasi

1.  **Siapkan Izin Termux:**
    Buka Termux dan ketik:
    ```bash
    termux-setup-storage
    ```

2.  **Download Script:**
    Gunakan `nano` untuk membuat file:
    ```bash
    nano spy.sh
    ```
    (Paste kode script yang diberikan, simpan dengan `CTRL+O`, `Enter`, lalu `CTRL+X`)

3.  **Beri Izin Eksekusi:**
    ```bash
    chmod +x spy.sh
    ```

4.  **Install Bahan (Wajib):**
    Jalankan script dan pilih **Opsi 1**:
    ```bash
    ./spy.sh
    ```

## 🚀 Cara Penggunaan
Setiap kali ingin masuk ke dashboard SPY-E, cukup jalankan:
```bash
./spy.sh
```

⚠️ Disclaimer

**​Alat ini dibuat untuk tujuan edukasi, audit keamanan mandiri, dan pengujian penetrasi legal. Penggunaan alat ini terhadap sistem milik orang lain tanpa izin adalah tindakan ilegal. Segala penyalahgunaan adalah tanggung jawab pengguna.**
