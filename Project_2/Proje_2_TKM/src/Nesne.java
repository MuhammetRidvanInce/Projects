public abstract class Nesne {
    
    double alpha = 0.2;
    // 1 - Terfi etmemis iki aynı nesne karşılasırsa birbirlerinin dayanıklılık puanından düşecek değer.
    // 2 - İki aynı nesne karşılaşırsa karşılıklı düşecek puan.
    double beta1 = 3.125; 
    // 2 - Biri terfi etmis diğeri etmemis iki aynı nesne karşılaşırsa terfi etmeyenden düşecek puan.
    double beta2 = 5;
    double dayaniklilik = 20;
    double seviyePuani = 0;
    
    
    double katilik = 0;
    double nufuz = 0;
    double keskinlik = 0;
    double sicaklik = 0;
    double kalinlik = 0;
    double direnc = 0;
    int id = 0;
    
    public Nesne(double alpha, double beta1, double beta2, 
            double dayaniklilik, double seviyePuani, 
            double katilik, double nufuz, double  keskinlik,
            double sicaklik, double kalinlik, double direnc,
            int id){
        this.alpha = alpha;
        this.beta1 = beta1;
        this.beta2 = beta2;
        this.dayaniklilik = dayaniklilik;
        this.seviyePuani = seviyePuani;
        this.katilik = katilik;
        this.nufuz = nufuz;
        this.keskinlik = keskinlik;
        this.sicaklik = sicaklik;
        this.kalinlik = kalinlik;
        this.direnc = direnc;
        this.id = id;
    }
    
    public Nesne(){
        
    }

    public void setAlpha(double alpha) {
        this.alpha = alpha;
    }

    public void setBeta1(double beta1) {
        this.beta1 = beta1;
    }

    public void setBeta2(double beta2) {
        this.beta2 = beta2;
    }

    public void setDayaniklilik(double dayaniklilik) {
        this.dayaniklilik = dayaniklilik;
    }

    public void setSeviyePuani(double seviyePuani) {
        this.seviyePuani = seviyePuani;
    }

    public void setKatilik(double katilik) {
        this.katilik = katilik;
    }

    public void setNufuz(double nufuz) {
        this.nufuz = nufuz;
    }

    public void setKeskinlik(double keskinlik) {
        this.keskinlik = keskinlik;
    }

    public void setSicaklik(double sicaklik) {
        this.sicaklik = sicaklik;
    }

    public void setKalinlik(double kalinlik) {
        this.kalinlik = kalinlik;
    }

    public void setDirenc(double direnc) {
        this.direnc = direnc;
    }

    public void setId(int id) {
        this.id = id;
    }

    //abstract double etkiHesapla(Nesne nesne);
    abstract void durumGuncelle(Nesne nesne);
    abstract void nesnePuaniGoster();
  
}
