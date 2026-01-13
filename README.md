<div align="center">

# PortScanner 🛡️
### Network Reconnaissance & Service Discovery Tool

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey?style=flat)
![Type](https://img.shields.io/badge/type-Reconnaissance-red?style=flat)

<p align="center">
  <a href="#about">Proje Hakkında</a> •
  <a href="#features">Özellikler</a> •
  <a href="#installation">Kurulum</a> •
  <a href="#usage">Kullanım</a> •
  <a href="#disclaimer">Yasal Uyarı</a>
</p>

</div>

---

## 📌 <a name="about"></a>Proje Hakkında

**PortScanner**, siber güvenlik uzmanları ve sistem yöneticileri için geliştirilmiş; hafif, hızlı ve çok iş parçacıklı (multi-threaded) bir ağ tarama aracıdır. Standart tek iş parçacıklı tarayıcıların aksine, PortScanner **Python'un eşzamanlılık (concurrency)** yeteneklerini kullanarak yaygın portları saniyeler içinde tarar. Standart port taramasının ötesine geçerek hedef sistem hakkında SSL Analizi, WAF Tespiti ve Kritik Zafiyet Kontrolleri yapar.

Ayrıca içerdiği **Banner Grabbing** (Servis Bilgisi Toplama) özelliği sayesinde, açık portlarda çalışan servislerin versiyon bilgilerini (örneğin: SSH versiyonu, Apache sunucu bilgisi vb.) otomatik olarak tespit eder. Bu özellik, sızma testlerinin keşif (reconnaissance) aşamasında kritik öneme sahiptir.

## 🚀 Özellikler
⚡ Yüksek Hız: Concurrent.futures kullanarak çoklu iş parçacığı (multi-threading) ile saniyeler içinde binlerce portu tarar.
🔍 Akıllı Hedef Çözümleme: Domain adreslerini (örn: google.com) otomatik olarak IP adresine çevirir ve tarar. CIDR desteği (örn: 192.168.1.0/24) mevcuttur.
🛡️ WAF Tespiti: Hedef sistemde Cloudflare, ModSecurity gibi Güvenlik Duvarı (WAF) olup olmadığını analiz eder.
🔒 Gelişmiş SSL/TLS Analizi:
SNI (Server Name Indication) desteği ile sanal hostları doğru analiz eder.
Sertifika otoritesini (Issuer) ve geçerlilik süresini (Expiry Date) UTC uyumlu olarak hesaplar.
Güvensiz/Self-Signed sertifikaları tespit eder.
🐛 Zafiyet Modülleri (Mini-NSE):
FTP: Anonim giriş (Anonymous Login) kontrolü.
HTTP: robots.txt dosyası üzerinden bilgi ifşası (Information Disclosure) kontrolü.
SMTP: VRFY komutu ile kullanıcı numaralandırma (User Enumeration) açığı kontrolü.
Banner Grabbing: Servis versiyonlarını ve işletim sistemi ipuçlarını yakalar.
📊 Raporlama: Sonuçları detaylı bir JSON dosyasına kaydeder.
🎨 Kullanıcı Deneyimi: Renkli terminal çıktıları (colorama) ve ilerleme çubuğu (tqdm).
## 📂 Proje Yapısı

```text
PortScanner/
├── Scanner.py          # Ana tarama motoru
├── requirements.txt    # Kütüphaneler
├── README.md           # Dokümantasyon
└── .gitignore          # Git ayarları
```
## ⚙️ <a name="installation"></a>Kurulum
Projeyi kurmak için şu adımları izleyin:
```text
Bash# 1. Repoyu klonlayın
git clone [https://github.com/yarennaksuu/PortScanner.git](https://github.com/yarennaksuu/PortScanner.git)

# 2. Klasöre girin
cd PortScanner

# 3. Kütüphaneyi yükleyin
pip install -r requirements.txt
```
## 💻 <a name="usage"></a>Kullanım

1. Basit Tarama (Domain veya IP)
```text
Bashpython Scanner.py -t <HEDEF_IP>
```
✅Örnek Senaryo: 
```text
python Scanner.py -t google.com veya python Scanner.py -t 192.168.1.1
```
2. Raporlu Tarama (JSON Çıktısı)
Sonuçları kaydetmek için -o parametresini kullanın:
```text
python Scanner.py -t scanme.nmap.org -o rapor.json
```
Beklenen Çıktı:
```text
[*] Domain resolved: google.com -> 142.250.187.174
------------------------------------------------------------
[*] Target: google.com
[*] Features: Port Scan, SSL SNI Analysis, WAF Detect, Vuln Check
------------------------------------------------------------
[+] 142.250.187.174:80    (http) OPEN [i] robots.txt found (Info Disclosure)
[+] 142.250.187.174:443   (https) OPEN [SSL: *.google.com | Issuer: Google Trust Services | Expires: 42 days]
Scanning: 100%|██████████████████████████████| 1000/1000
```
## ⚠️ <a name="disclaimer"></a>Yasal Uyarı
Bu yazılım yalnızca eğitim amaçlı ve yasal izinlerin alındığı ağlarda güvenlik testleri gerçekleştirmek amacıyla geliştirilmiştir.

İzniniz olmayan bir ağa veya sisteme tarama yapmak, 5237 Sayılı Türk Ceza Kanunu (TCK) Bilişim Suçları maddeleri ve uluslararası yasalar uyarınca suç teşkil edebilir.

Geliştirici, bu aracın kötü niyetli kullanımından doğabilecek maddi/manevi zararlardan sorumlu tutulamaz.

Bu aracı indirerek ve kullanarak, tüm yasal sorumluluğu kabul etmiş sayılırsınız.

<div align="center">Geliştirici: Yaren AksuCybersecurity Researcher & Developer</div>
