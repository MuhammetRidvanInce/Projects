public class Kullanici extends Oyuncu{
    
    
    public Kullanici(int oyuncuID, String OyuncuAdi, double skor) {
        super(oyuncuID, OyuncuAdi,skor); 
        
        nesneler = new Nesne[]{
                new Tas(0), new Tas(1), new Tas(2), new Tas(3), new Tas(4), 
                new Makas(5), new Makas(6),new Makas(7),new Makas(8),new Makas(9),
                new Kagit(10),new Kagit(11),new Kagit(12),new Kagit(13),new Kagit(14),
                new AgirTas(15), new AgirTas(16), new AgirTas(17), new AgirTas(18), new AgirTas(19), 
                new UstaMakas(20), new UstaMakas(21),new UstaMakas(22),new UstaMakas(23),new UstaMakas(24),
                new OzelKagit(25),new OzelKagit(26),new OzelKagit(27),new OzelKagit(28),new OzelKagit(29),
                };
    }
    
    
    void nesneListesiOlustur()
    {
        // Arayüzde manuel olarak liste oluşturulduğunda bu fonksiyon işlevsiz kalmaktadır.
    }
 
    @Override
    Nesne nesneSec(Nesne[] nesnelistesi) {
        // Arayüzde manuel olarak seçim yapıldığından bu fonksiyon işlevsiz kalmaktadır.
        return nesnelistesi[1]; 
    }
    
  
}
