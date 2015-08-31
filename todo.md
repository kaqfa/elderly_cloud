<!-- 
Yang perlu dikerjain saat ini
NB: 
- yang udah selesai ditandain v ya....
- latihan sementara bisa diimplementasikan di halaman admin
- tampilane asal aja, nanti yang bagian desain aku
- kalo udah implementasikan juga di rest framework
-->

## Models
- Lengkapin atribut di model kalau boleh
- Untuk query yang berhubungan dengan list of respective model, dibuat method static
- Untuk query yang berhubungan dengan attributes / relations dibuat method biasa

## User Modifications
- Pengennya ada 2 cara user login, yaitu login biasa dan login dengan kode  aja (elder)

## REST
- Simulasikan client consumption masing2 service penting (boleh pake POSTman)

## Testing
- Baca dan nyoba bikin testing, sampe pake fixture
- Nggak harus TDD, tapi pelajari (dan praktekkan) bukunya Percival boleh juga

## Per halaman
[ ] Pilihan orang tua yang sedang dirawat disimpan dalam session

### Halaman Dashboard (siapin query di model-nya aja)
[ ] Tampilkan semua elder yang dirawat user
[ ] Tampilkan 10 info & tips terbaru
[ ] Tampilkan 10 POI terdekat dengan lokasi user
[ ]

### Halaman Orang Tua
[ ] Tampilkan semua elder yang dirawat user
[ ] Tampilkan kondisi harian terakhir masing2 elder
[ ] Tampilkan jumlah perawat masing2 elder
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Kondisi Harian
[ ] Hanya menampilkan data kondisi harian orang tua aktif saja
[ ] CBV ListView
[ ] CBV ShowView
[ ] Tambah note untuk setiap kondisi

### Riwayat Penyakit
[ ] Hanya menampilkan data riwayat penyakit orang tua aktif saja
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Riwayat Perawatan Medis
[ ] Hanya menampilkan data riwayat perawatan medis orang tua aktif saja
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Catatan Kondisi
[ ] Hanya menampilkan catatan orang tua aktif saja
[ ] Tambahkan komentar untuk setiap catatan
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Kontak Penting
[ ] Hanya menampilkan kontak penting dari orang tuag aktif saja
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Informasi
[ ] User selain user yang punya permission add, change, & delete hanya bisa list & show saja
[ ] User dengan permission add, change, & delete bisa CRUD
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Tips dan Trik
[ ] User selain user yang punya permission add, change, & delete hanya bisa list & show saja
[ ] User dengan permission add, change, & delete bisa CRUD
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView

### Lokasi Penting
- nanti dulu

### Feedback
[ ] Selain admin bisa CRUD + komentar
[ ] Selain admin hanya menampilkan feedback yang telah diberikan user tersebut
[ ] Admin bisa menampilkan semua feedback yang ada
[ ] Admin bisa list, show, dan komentar
[ ] CBV ListView
[ ] CBV ShowView
[ ] CBV EditView
[ ] CBV AddView