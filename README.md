Advanced Port Scanner with Banner Grabbing
Bu proje, Python kullanılarak geliştirilmiş, yüksek performanslı ve çok iş parçacıklı (multi-threaded) bir ağ port tarayıcısıdır. Hedef sistem üzerindeki açık portları tespit eder, çalışan servislerin isimlerini çözümler ve mümkünse servis versiyon bilgilerini (Banner Grabbing) yakalar.

🚀 Özellikler
Çok İş Parçacıklı Tarama (Multi-threading): concurrent.futures kullanılarak aynı anda 100 thread ile hızlı tarama yapar.

Banner Grabbing: Açık portlara bağlanarak çalışan servisin sürüm ve başlık bilgilerini çeker.

Servis Tanımlama: Port numarasına göre standart servis isimlerini (HTTP, SSH, FTP vb.) tanımlar.

Renkli Çıktı: colorama kütüphanesi ile sonuçları okunabilir ve renkli bir formatta sunar.

CLI Desteği: Komut satırı argümanları ile kolay kullanım sağlar.

Hata Yönetimi: Bağlantı zaman aşımı ve soket hatalarını yöneterek taramanın kesilmesini engeller.

📋 Gereksinimler
Bu projeyi çalıştırmak için bilgisayarınızda Python 3.x yüklü olmalıdır. Ayrıca renklendirme için colorama kütüphanesine ihtiyaç duyar.

Bash

pip install colorama
cd 🛠️ Kurulum
Projeyi yerel makinenize klonlayın:

Bash

git clone https://github.com/kullaniciadi/port-scanner.git
cd port-scanner
Gerekli kütüphaneyi yükleyin:

Bash

pip install -r requirements.txt
# Veya manuel olarak:
pip install colorama
💻 Kullanım
Programı terminal veya komut satırı üzerinden aşağıdaki formatta çalıştırabilirsiniz:

Temel Kullanım:

Bash

python Scanner.py -t <HEDEF_IP>
Örnek:

Bash

python Scanner.py -t 192.168.1.10
📸 Örnek Çıktı
Program çalıştığında aşağıdaki gibi bir çıktı üretecektir:

Plaintext

------------------------------------------------------------
[*] Scanning Target: 192.168.1.10
[*] Scanning ports 1-1000 with 100 threads...
[*] Start Time: 2023-10-27 14:30:00.123456
------------------------------------------------------------
[+] Port 21    (ftp) OPEN : vsFTPd 3.0.3
[+] Port 22    (ssh) OPEN : SSH-2.0-OpenSSH_8.2p1
[+] Port 80    (http) OPEN : Apache/2.4.41 (Ubuntu)
[+] Port 443   (https) is OPEN
------------------------------------------------------------
[*] Scan Completed: 2023-10-27 14:30:05.654321
⚠️ Yasal Uyarı (Disclaimer)
Bu araç yalnızca eğitim amaçlı ve yasal izinlere sahip olduğunuz ağlarda güvenlik testi yapmak üzere tasarlanmıştır. Sahibi olmadığınız veya test izniniz olmayan sistemlerde kullanılması yasa dışıdır. Geliştirici, bu aracın kötüye kullanımından doğacak hiçbir sorumluluğu kabul etmez.

🤝 Katkıda Bulunma
Bu depoyu Fork'layın.

Yeni bir özellik dalı oluşturun (git checkout -b feature/YeniOzellik).

Değişikliklerinizi commit edin (git commit -m 'Yeni özellik eklendi').

Dalınızı Push edin (git push origin feature/YeniOzellik).

Bir Pull Request oluşturun.

📝 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
