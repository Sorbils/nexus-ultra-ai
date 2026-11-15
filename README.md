# NEXUS ULTRA AI — başlangıç paketi

Bu paket telefondan Railway'e yüklenebilecek ilk mobil panel iskeletidir.

## Şu anda çalışanlar
- FastAPI tabanlı web uygulaması
- Türkçe, mobil uyumlu kontrol paneli
- `/api/health` sağlık kontrolü
- `/api/status` sistem durumu
- Railway için başlangıç yapılandırması

## Bilerek henüz eklenmeyenler
- Binance TR API anahtarı ve emir gönderimi
- xAI/Grok API anahtarı
- Otomatik canlı alım-satım

İlk sürüm yalnızca `PAPER` modundadır; canlı emir gönderen bir endpoint yoktur.
Borsa bağlantısı, resmi Binance TR dokümanındaki güncel URL, imza yöntemi,
izinler ve emir kuralları doğrulandıktan sonra ayrı bir aşamada eklenecektir.

## Railway'e telefondan dağıtım
1. ZIP'i açıp içindeki dosyaları bir GitHub deposuna yükleyin.
2. Railway'de New Project → Deploy from GitHub Repo yolunu izleyin.
3. Bu depoyu seçin. Railway `railway.json` ve `requirements.txt` dosyalarını algılar.
4. Deploy tamamlanınca oluşturulan domain'i telefondan açın.
5. `/api/health` adresi `ok: true` döndürmelidir.

## Güvenlik
- API anahtarlarını GitHub'a, ZIP'e veya ChatGPT sohbetine koymayın.
- İleride Binance API anahtarı oluşturulursa para çekme iznini kapalı tutun.
- Önce sanal işlem ve hata testleri; canlı emirler ancak ayrıca onaylanmış güvenlik aşamasından sonra.
