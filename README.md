# Sentiment-Analysis-on-X

Bu proje, Twitter API kullanarak belirli bir hashtag ile toplanan tweetlerin duygu analizini gerçekleştirir. Veriler analiz edildikten sonra grafik ile görselleştirilir ve CSV dosyası olarak kaydedilir.


Özellikler

-Twitter API ile veri çekme (Tweepy kullanılarak)

-NLTK SentimentIntensityAnalyzer ile duygu analizi

-Seaborn ve Matplotlib ile görselleştirme

-Sonuçları CSV formatında kaydetme


Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki bağımlılıkların yüklü olduğundan emin olun:

pip install tweepy pandas matplotlib seaborn nltk python-dotenv


API Anahtarlarını Tanımlama
Twitter API erişimi için .env dosyanızın içinde aşağıdaki satır bulunmalıdır:

TWITTER_BEARER_TOKEN=your_bearer_token_here

Anahtarların gizliliği açısından .env dosyası kullanmak daha doğrudur.


Kullanım

Kod içinde gerekli alanla analiz etmek istediğiniz hashtagi yazarak çalıştırdığınızda karşınıza analiz edilmiş ve görselleştirilmiş bir grafik çıkacak.
