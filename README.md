![preview1](https://r2.fivemanage.com/WX5Hv6yMgODTgG2WF6rml/images/backgroundgithub.png)

# Export Ordered DataStore - Roblox

Script Python untuk mengekspor seluruh data dari **Ordered DataStore** milik sebuah game Roblox ke dalam file JSON lokal.

---

## Apa Itu Script Ini?

Script ini memanfaatkan **Roblox Open Cloud API** (`ordered-data-stores/v1`) untuk mengambil semua entri dari sebuah Ordered DataStore secara otomatis, lalu menyimpannya ke file `donortotals_export.json`.

Berguna untuk kebutuhan seperti:
- Backup data leaderboard / ranking
- Migrasi data antar game
- Analisis data donor/score pemain

---

## Fungsi-Fungsi dalam Script

| Bagian | Penjelasan |
|---|---|
| **Konfigurasi variabel** | Menyimpan API Key, Universe ID, nama DataStore, dan Scope |
| **Request ke API** | Mengirim GET request ke endpoint Roblox Open Cloud |
| **Pagination otomatis** | Melanjutkan pengambilan data selama masih ada `nextPageToken` |
| **Debug output** | Mencetak status HTTP dan isi response mentah di terminal |
| **Parsing entri** | Mengambil field `id` (key) dan `value` dari setiap entri |
| **Ekspor ke JSON** | Menyimpan semua entri ke file `donortotals_export.json` |
| **Ringkasan akhir** | Mencetak total jumlah entri yang berhasil diekspor |

---

## Prasyarat

- Python 3.x
- Library `requests`

Install library jika belum ada:

```bash
pip install requests
```

---

## Cara Menggunakan

### 1. Dapatkan API Key Roblox

1. Buka [Roblox Creator Hub](https://create.roblox.com/)
2. Pergi ke **Credentials** → **API Keys**
3. Buat API Key baru dengan akses:
   - **Ordered Data Stores** → permission **Read**
4. Salin API Key yang dihasilkan

### 2. Isi Variabel Konfigurasi

Buka file `exportordereddatastore.py` dan isi bagian ini:

```python
API_KEY     = "YOUR_API_KEY_HERE"
UNIVERSE_ID = "YOUR_UNIVERSE_ID_HERE"   # ID numerik game kamu
STORE_NAME  = "YOUR_STORE_NAME_HERE"    # Nama Ordered DataStore
SCOPE       = "global"                  # Scope DataStore (biasanya "global")
```

> **Cara mencari Universe ID:** Buka game di Roblox Studio → klik kanan pada game di Explorer → **Game Settings** → lihat URL, angka setelah `/universes/` adalah Universe ID.

### 3. Jalankan Script

```bash
python exportordereddatastore.py
```

### 4. Hasil Output

Script akan mencetak log seperti:

```
Status: 200
Response: {"entries": [...], "nextPageToken": "..."}
[EXPORT] key=player123 | value=5000
[EXPORT] key=player456 | value=3200
...
[DONE] 250 entries
```

File `donortotals_export.json` akan dibuat di direktori yang sama:

```json
[
  {
    "key": "player123",
    "value": 5000
  },
  {
    "key": "player456",
    "value": 3200
  }
]
```

---

## Catatan Penting

- Data diurutkan **descending** (nilai terbesar duluan) sesuai sifat Ordered DataStore.
- Satu halaman maksimal mengambil **100 entri**; script otomatis memproses semua halaman berikutnya.
- Jangan share `API_KEY` kamu ke publik — simpan dengan aman.
