# Adım 1: Temel Olarak Ne Kullanacağız?
# Docker'ın resmi deposundan, Python 3.11'in 'slim' (hafifletilmiş) versiyonunu temel al.
# Bu, içinde Python'un hazır kurulu olduğu bir mini-Linux işletim sistemi gibidir.
FROM python:3.11-slim

# Adım 2: Çalışma Dizini Oluştur
# Konteynerin İÇİNDE, kodumuzun yaşayacağı bir klasör oluştur.
WORKDIR /app

# Adım 3: Malzeme Listesini Kopyala
# Yerel bilgisayarımızdaki 'requirements.txt' dosyasını,
# konteynerin içindeki '/app' klasörüne kopyala.
COPY requirements.txt .

# Adım 4: Malzemeleri Kur
# Konteynerin içinde, kopyaladığımız listeyi kullanarak pip ile kurulum yap.
RUN pip install -r requirements.txt

# Adım 5: Kodumuzu Kopyala
# Yerel klasörümüzdeki HER ŞEYİ (.), konteynerin içindeki '/app' klasörüne kopyala.
COPY . .

# Adım 6: Kapıyı (Port) Dış Dünyaya Aç
# Konteynere gelen 5000 numaralı porttaki trafiği dinleyeceğini söyle.
EXPOSE 5000

# Adım 7: Konteyner Başladığında Ne Çalışacak?
# Konteyner çalıştığı anda, terminalde 'python main.py' komutunu işlet.
CMD ["python", "main.py"]