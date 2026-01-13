\# 🛡️ PyScanner - Multi-Threaded Port Tarayıcı



!\[Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)

!\[License](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)

!\[Durum](https://img.shields.io/badge/Durum-Aktif-green.svg?style=for-the-badge)



\## 📌 Proje Hakkında

\*\*PyScanner\*\*, siber güvenlik uzmanları ve sistem yöneticileri için geliştirilmiş; hafif, hızlı ve çok iş parçacıklı (multi-threaded) bir ağ tarama aracıdır. Standart tek iş parçacıklı tarayıcıların aksine, PyScanner \*\*Python'un eşzamanlılık (concurrency)\*\* yeteneklerini kullanarak yaygın portları saniyeler içinde tarar.



Ayrıca içerdiği \*\*Banner Grabbing\*\* (Servis Bilgisi Toplama) özelliği sayesinde, açık portlarda çalışan servislerin versiyon bilgilerini (örneğin: SSH versiyonu, Apache sunucu bilgisi vb.) otomatik olarak tespit eder. Bu özellik, sızma testlerinin keşif (reconnaissance) aşamasında kritik öneme sahiptir.



\## 🚀 Özellikler

\* \*\*Yüksek Hız (Multi-Threading):\*\* 100 eşzamanlı iş parçacığı (thread) kullanarak 1000 portu yaklaşık 10 saniyede tarar.

\* \*\*Banner Grabbing:\*\* Açık portlardaki servislerin versiyon bilgilerini ve karşılama mesajlarını yakalar.

\* \*\*Akıllı Zaman Aşımı:\*\* Filtrelenmiş veya cevap vermeyen portlarda vakit kaybetmemek için optimize edilmiş soket yönetimi.

\* \*\*Renkli Arayüz:\*\* Sonuçları analiz etmeyi kolaylaştıran, okunaklı ve renkli komut satırı çıktıları.

\* \*\*Bağımlılıksız:\*\* Çalışmak için ağır kütüphanelere ihtiyaç duymaz.



\## ⚙️ Kurulum



1\. Repoyu klonlayın:

&nbsp;  ```bash

&nbsp;  git clone \[https://github.com/yarennaksuu/PyScanner.git](https://github.com/yarennaksuu/PyScanner.git)

