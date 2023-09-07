public class AgirTas extends Tas {
    

    public AgirTas(int id_){
        super(0);
        id = id_;
        sicaklik = 2;
    }
    
    @Override
    public double etkiHesapla(Nesne nesne)
    {
        etkipuani = 0;
        etkipuani = katilik * sicaklik / (alpha*nesne.keskinlik* nesne.direnc + (1-alpha)*nesne.nufuz * nesne.kalinlik); 
        if (etkipuani == Double.POSITIVE_INFINITY & !"Tas".equals(nesne.getClass().getName()))
            etkipuani = beta1;
        else if (etkipuani == Double.POSITIVE_INFINITY & "Tas".equals(nesne.getClass().getName()))
            etkipuani = beta2;
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
