
public abstract class Oyuncu {
    
    int oyuncuID;
    String OyuncuAdi;
    double skor;
    Nesne[] nesneler;
    Nesne[] nesneListesi = new Nesne[5];

    public Oyuncu(int oyuncuID, String OyuncuAdi, double skor) {
        this.oyuncuID = oyuncuID;
        this.OyuncuAdi = OyuncuAdi;
        this.skor = skor;

    }

    public Oyuncu() {
        
    }

    abstract Nesne nesneSec(Nesne[] nesnelistesi);
    abstract void nesneListesiOlustur(); 
    double skorGoster(){
        
        if (nesneListesi[0] == null)
            skor = 0;
        else
        {
            double toplam = 0;
            int i = 0;
            while(true)
            {
                double dayaniklilik = nesneListesi[i].dayaniklilik;
                toplam +=dayaniklilik;
                i++;
                if ( (i==5) || nesneListesi[i] == null )
                    break;
            }
            skor = toplam;
        }
        
        return skor;
    } 
}
