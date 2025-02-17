# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah berhasil mencetak lulusan berkualitas yang berkontribusi dalam berbagai sektor industri. Namun, meskipun memiliki reputasi yang baik, Jaya Jaya Institut menghadapi tantangan besar dalam hal tingginya angka dropout mahasiswa.

Dropout atau putus kuliah merupakan permasalahan serius dalam dunia pendidikan, karena tidak hanya berdampak pada mahasiswa secara individu tetapi juga pada reputasi dan efektivitas institusi pendidikan itu sendiri. Mahasiswa yang tidak menyelesaikan studinya dapat mengalami kerugian dalam bentuk waktu, biaya, serta kesempatan karier. Di sisi lain, bagi institusi, angka dropout yang tinggi dapat menurunkan kredibilitas dan efektivitas program pendidikan yang ditawarkan.

### Permasalahan Bisnis
1. Faktor apa saja yang mempengaruhi banyaknya mahasiswa yang dropout?
2. Belum tersedia nya teknologi yang dapat membantu pihak institusi dalam memprediksi mahasiswa yang berpotensi akan dropout.
3. Menyediakan business dashboard untuk membantu dalam memonitoring berbagai faktor tersebut.



### Cakupan Proyek
1. Menganalisa penyebab banyaknya mahasiswa yang dropout/keluar dari institusi
2. Membangun model machine learning untuk memprediksi penyebab mahasiswa banyak yang dropout
3. Membangun dashboard untuk membantu institusi dalam memonitoring faktor-faktor secara realtime


### Persiapan
Sumber data: dataset yang digunakan merupakan dataset institusi pendidikan perguruan [Jaya Jaya Instut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

Setup environment: Proyek ini membutuhkan lingkungan sederhana untuk menjalankan analisis data dan dashboard. Berikut langkah-langkah untuk mempersiapkan environment:
- Menjalankan `notebook.ipynb`
    - Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file requirements.txt untuk melihat dependensi yang dibutuhkan).
    ```
    pip install -r requirements.txt
    ```
    - Jalankan seluruh isi file notebook.ipynb menggunakan Google Colab/Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
- Setup conda environtment (jika menggunakan conda bisa memakai ini):
    ```
    conda create --name myenv python=3.9
    conda activate myenv #MacOS
    conda activate myenv  # Windows
    ```

## Business Dashboard
Hasil dari analisis dan model prediktif dapat divisualisasikan dalam bentuk dashboard untuk membantu institusi dalam memantau dan memahami status siswa secara real-time. Berikut adalah elemen-elemen yang dapat disertakan dalam dashboard:

- Tren Status: Distribusi status siswa berdasarkan fitur seperti Curricular_units_2nd_sem_approved, Curricular_units_1st_sem_approved, Curricular_units_2nd_sem_enrolled, Curricular_units_1st_sem_enrolled, Admission_grade, Displaced.

- Feature Importance: Visualisasi kontribusi semua fitur dengan berdasarkan status dari siswa.

- Kemudahan dalam penggunaan Dashboard. [Link Dashboard](https://lookerstudio.google.com/u/0/reporting/084fce4e-59b1-416d-9266-cbdbfe8f20ee/page/4JatE)  

## Menjalankan Sistem Machine Learning
Pada proyek ini menggunakan model Random Forest yang sudah dilatih untuk memprediksi dropout siswa pada set data training dan test. Prediksi ini dilakukan berdasarkan fitur-fitur yang berkolerasi paling tinggi terhadap fitur status siswa.

link Prototype :  [Dashboard](https://subproyek2-penerapandatascience-rizkaindahp.streamlit.app/)

Untuk menjalankan sistem di lingkungan lokal, ikuti langkah-langkah berikut:

1. Clone repository di bawah ini:
    ```
    git clone https://github.com/rizkaindahp/sub_proyek_2_pds.git
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Jalankan aplikasi Streamlit:
    ```
    streamlit run app.py
    ```

## Conclusion
1. Dari data yang telah kita analisa, beberapa faktor penyebab tingginya dropout antara lain:
    - Faktor akademik (jumlah mata kuliah yang disetujui, nilai semester, dan nilai masuk) sangat berpengaruh terhadap apakah mahasiswa akan graduate atau dropout.
    - Faktor finansial (biaya kuliah yang terbayar dan status beasiswa) dapat menjadi indikator utama risiko dropout, terutama bagi mahasiswa yang kesulitan membayar biaya kuliah.
    - Faktor sosial dan ekonomi (misalnya mahasiswa yang berasal dari luar kota atau daerah lain) bisa meningkatkan risiko dropout jika tidak ada dukungan yang cukup.
2. Pembuatan sistem machine learning yang dapat membantu dalam memprediksi status siswa.


### Rekomendasi Action Items
1. Intervensi Akademik
- Menyediakan kelas tambahan bagi mahasiswa dengan nilai rendah pada semester pertama dan kedua.
- Menyediakan tutor sebaya atau mentor dari dosen untuk mahasiswa dengan IPK rendah.
- Meninjau ulang kurikulum dan metode pengajaran agar lebih sesuai dengan kebutuhan mahasiswa.
- Menyediakan pelatihan untuk dosen dalam penggunaan metode pembelajaran inovatif.
2. Dukungan Finansial

- Beasiswa & Bantuan Keuangan
- Sistem Cicilan atau Bantuan Pembayaran
- Edukasi Keuangan untuk Mahasiswa

3. Meningkatkan keterlibatan mahasiswa melalui komunitas dan mentoring.
4. Implementasi sistem peringatan dini berbasis data.

















