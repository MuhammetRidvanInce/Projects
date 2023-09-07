public class Bilgisayar extends Oyuncu{
    

    public Bilgisayar(int oyuncuID, String OyuncuAdi, double skor) {
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
        int[] secimler  = new int[5];
        int indis = 0;
        while (true)
        {
            int secim = (int)(Math.random()*(15)+0);
            if (icindemi(secim, secimler) == 1)
                continue;
            else
            {
                secimler[indis] = secim;
                indis++;
            }
            if (indis == 5)
                break;
        }
        
        for (int i = 0; i<secimler.length; i++ )
            nesneListesi[i] = nesneler[secimler[i]];  
    }
    @Override
    Nesne nesneSec(Nesne[] nesnelistesi) {
        
        int nesneSayisi;
        int secim=-1;
        for (nesneSayisi = 0; nesneSayisi<nesnelistesi.length;nesneSayisi++ )
            if (nesnelistesi[nesneSayisi] == null)
                    break;
        
        if (nesneSayisi == 0)
            System.out.println("Nesne Listesinde Nesne Yok!");
        else
            secim = (int)(Math.random()*(nesneSayisi)+0);

        return nesnelistesi[secim];
        
    }
    final int icindemi(int X, int[] array){
        int uzunluk = array.length;
        int icinde = 0;
        
        for (int i = 0; i<uzunluk; i++ )
        {
            if (array[i] == X )
            {
                icinde =1;
                break;
            }
        }
        
        return icinde;
    }
  
}
