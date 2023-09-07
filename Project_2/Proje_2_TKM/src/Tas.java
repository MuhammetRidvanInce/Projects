public class Tas extends Nesne{

    double etkipuani;
    public Tas(int id_){
        super();
        this.katilik = 2;
        this.sicaklik = 1;
        id = id_;
    }

    @Override
    public void setKatilik(double katilik) {
        this.katilik = katilik;
    }
    

   
    public double etkiHesapla(Tas tas)
    {
        etkipuani = beta1;
        return etkipuani;
    }
    
    public double etkiHesapla(Makas makas)
    {
        etkipuani = 0;
        etkipuani = katilik * sicaklik / (alpha*makas.keskinlik* makas.direnc); 
        return etkipuani;
    }
        
    public double etkiHesapla(Kagit kagit)
    {
        etkipuani = 0;
        etkipuani = katilik * sicaklik / ((1-alpha)*kagit.nufuz * kagit.kalinlik); 
        return etkipuani;
    }
    

    @Override
    public void durumGuncelle(Nesne nesne)
    {
       dayaniklilik =  dayaniklilik - nesne.etkiHesapla(this);
        if (etkipuani > nesne.etkiHesapla(this))
            seviyePuani +=20;
    }
    
    @Override
    public void nesnePuaniGoster()
    {
        System.out.println(this.getClass().getName()+ "[" + id + "]" + " Nesnesi Puan Durumu");
        System.out.println("Dayanıklılık: "  + dayaniklilik);
        System.out.println("Seviye Puanı: "  + seviyePuani); 
        System.out.println("-----------------");
    }


    
}
