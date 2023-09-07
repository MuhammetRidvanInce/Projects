public class Kagit extends Nesne{
        
        
        double etkipuani;
        
        public Kagit(int id_){
        super();
        nufuz = 2;
        kalinlik = 1;
        id = id_;
        
    }
        

    public double etkiHesapla(Kagit kagit)
    {

        etkipuani = beta1;
        return etkipuani;
    }
    
    
    public double etkiHesapla(Tas tas)
    {
        etkipuani = 0;
        etkipuani = nufuz * kalinlik / (alpha*tas.katilik* tas.sicaklik); 
        return etkipuani;
    }
       
    
    public double etkiHesapla(Makas makas)
    {

        etkipuani = nufuz * kalinlik / ((1-alpha)*makas.keskinlik * makas.direnc); 
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
