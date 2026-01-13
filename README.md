Kurulum
Projeyi yerel ortamınıza klonlamak ve bağımlılıkları yüklemek için aşağıdaki adımları izleyin:

Bash

# 1. Repoyu klonlayın
git clone [https://github.com/yarennaksuu/PortScanner.git](https://github.com/yarennaksuu/PortScanner.git)

# 2. Proje dizinine geçiş yapın
cd PortScanner

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt
💻 <a name="usage"></a>Kullanım
PortScanner, komut satırı argümanları ile yönetilir.

Sözdizimi:

Bash

python Scanner.py -t <HEDEF_IP>
Parametreler: | Argüman | Açıklama | Zorunlu | | :--- | :--- | :---: | | -t, --target | Taranacak Hedef IP Adresi veya Hostname | ✅ |

Örnek Senaryo
Bir hedef üzerindeki servisleri ve versiyonları tespit etmek için:

Bash

python Scanner.py -t scanme.nmap.org
Beklenen Çıktı:

Plaintext

------------------------------------------------------------
[*] Scanning Target: 45.33.32.156
[*] Scanning ports 1-1000 with 100 threads...
[*] Start Time: 2026-01-13 16:45:12
------------------------------------------------------------
[+] Port 22    (ssh) OPEN : SSH-2.0-OpenSSH_7.4
[+] Port 80    (http) is OPEN
[+] Port 9929  (nping-echo) is OPEN
------------------------------------------------------------
[*] Scan Completed: 2026-01-13 16:45:22
⚠️ <a name="disclaimer"></a>Yasal Uyarı (Disclaimer)
Lütfen Dikkatle Okuyunuz:

Bu yazılım yalnızca eğitim amaçlı ve yasal izinlerin alındığı ağlarda güvenlik testleri gerçekleştirmek amacıyla geliştirilmiştir.

İzniniz olmayan bir ağa veya sisteme tarama yapmak, 5237 Sayılı Türk Ceza Kanunu (TCK) Bilişim Suçları maddeleri ve uluslararası yasalar uyarınca suç teşkil edebilir.

Geliştirici (Yaren Naksu), bu aracın kötü niyetli kullanımından doğabilecek maddi/manevi zararlardan sorumlu tutulamaz.

Bu aracı indirerek ve kullanarak, tüm yasal sorumluluğu kabul etmiş sayılırsınız.

<div align="center">

Geliştirici: Yaren Naksu

Cybersecurity Researcher & Developer

</div>
