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

## 🚀 <a name="features"></a>Temel Özellikler

* **Eşzamanlı Tarama Motoru:** `concurrent.futures` kütüphanesi ile optimize edilmiş Thread Havuzu.
* **Servis Parmak İzi:** Açık portlarda çalışan servislerin versiyon tespiti.
* **Düşük Yanlış Pozitif:** Optimize edilmiş soket zaman aşımı yönetimi.
* **Platform Bağımsız:** Windows, Linux ve macOS üzerinde çalışır.
* **Renkli Arayüz:** `Colorama` ile okunabilir terminal çıktıları.

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

Taramayı başlatmak için -t parametresini kullanın.Komut:
```text
Bashpython Scanner.py -t <HEDEF_IP>
```
✅Örnek Senaryo: 
```text
python Scanner.py -t scanme.nmap.org
```
Beklenen Çıktı:
```text
Plaintext------------------------------------------------------------
[*] Scanning Target: 45.33.32.156
[*] Scanning ports 1-1000 with 100 threads...
------------------------------------------------------------
[+] Port 22    (ssh) OPEN : SSH-2.0-OpenSSH_7.4
[+] Port 80    (http) is OPEN
------------------------------------------------------------
```
## ⚠️ <a name="disclaimer"></a>Yasal Uyarı
Bu yazılım yalnızca eğitim amaçlı ve yasal izinlerin alındığı ağlarda güvenlik testleri gerçekleştirmek amacıyla geliştirilmiştir. İzinsiz tarama yapmak suç teşkil edebilir. Geliştirici, kötü niyetli kullanımlardan sorumlu değildir.

<div align="center">Geliştirici: Yaren AksuCybersecurity Researcher & Developer</div>
