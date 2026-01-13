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

**PortScanner**, sızma testlerinin (Penetration Testing) keşif aşamasında kullanılmak üzere tasarlanmış, yüksek performanslı ve asenkron mimariye sahip bir ağ tarama aracıdır.

Geleneksel soket programlamanın limitlerini aşmak için **Multi-Threading (Çoklu İş Parçacığı)** mimarisini kullanır. Bu sayede, TCP el sıkışma (3-way handshake) süreçlerini paralelize ederek hedef sistem üzerindeki açık portları ve çalışan servis versiyonlarını (Banner Grabbing) saniyeler içerisinde tespit eder.

Bu proje, Nmap gibi kapsamlı araçların bulunmadığı veya daha hafif (lightweight) çözümlerin gerektiği kısıtlı ortamlarda (Pivot noktaları, Docker konteynerleri vb.) hızlı keşif yapmak amacıyla geliştirilmiştir.

## 🚀 <a name="features"></a>Temel Özellikler

* **Eşzamanlı Tarama Motoru (Concurrency):** `concurrent.futures` kütüphanesi ile optimize edilmiş Thread Havuzu (ThreadPool) yönetimi.
* **Servis Parmak İzi (Service Fingerprinting):** Açık portlarda çalışan servislerin (SSH, FTP, HTTP vb.) "Banner" bilgilerini yakalayarak versiyon tespiti yapar.
* **Düşük Yanlış Pozitif (Low False Positive):** Ağ gecikmelerini ve zaman aşımlarını (timeouts) dinamik olarak yöneten soket yapılandırması.
* **Platform Bağımsız:** Python 3.x yüklü olan tüm işletim sistemlerinde (Windows, Linux, macOS) ek yetki gerektirmeden çalışır.
* **Renkli CLI Arayüzü:** `Colorama` entegrasyonu ile analiz edilmesi kolay, renk kodlu terminal çıktıları.

## 📂 Proje Yapısı

```text
PortScanner/
├── Scanner.py          # Ana tarama motoru ve iş mantığı
├── requirements.txt    # Proje bağımlılıkları
├── README.md           # Dokümantasyon
└── .gitignore          # Git tarafından izlenmeyecek dosyalar
```
##⚙️ <a name="installation"></a>Kurulum
Projeyi yerel ortamınıza klonlamak ve bağımlılıkları yüklemek için aşağıdaki adımları izleyin:
```text

# 1. Repoyu klonlayın
git clone https://github.com/yarennaksuu/PortScanner.git

# 2. Proje dizinine geçiş yapın
cd PortScanner

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt
```
##💻 <a name="usage"></a>KullanımPortScanner

komut satırı argümanları ile yönetilir.
```text

Sözdizimi: Bashpython Scanner.py -t <HEDEF_IP>
Parametreler:ArgümanAçıklamaZorunlu-t, --targetTaranacak Hedef IP Adresi veya Hostname
```

✅Örnek SenaryoBir hedef üzerindeki servisleri ve versiyonları tespit etmek için:   Bashpython Scanner.py -t scanme.nmap.org
```text
Beklenen Çıktı:Plaintext------------------------------------------------------------
[*] Scanning Target: 45.33.32.156
[*] Scanning ports 1-1000 with 100 threads...
[*] Start Time: 2026-01-13 16:45:12
------------------------------------------------------------
[+] Port 22    (ssh) OPEN : SSH-2.0-OpenSSH_7.4
[+] Port 80    (http) is OPEN
[+] Port 9929  (nping-echo) is OPEN
------------------------------------------------------------
[*] Scan Completed: 2026-01-13 16:45:22
```
