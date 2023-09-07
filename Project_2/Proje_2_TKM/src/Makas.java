
public class Makas extends Nesne {

    double etkipuani;

    public Makas(int id_) {
        super();
        keskinlik = 2;
        direnc = 1;
        id = id_;

    }

    public double etkiHesapla(Makas makas) {

        etkipuani = beta1;
        return etkipuani;
    }

    public double etkiHesapla(Tas tas) {
        etkipuani = 0;
        etkipuani = keskinlik * direnc / ( (1 - alpha) * tas.katilik * tas.sicaklik);
        return etkipuani;
    }

    public double etkiHesapla(Kagit kagit) {
        etkipuani = keskinlik * direnc / (alpha * kagit.nufuz * kagit.kalinlik);
        return etkipuani;
    }

    @Override
    public void durumGuncelle(Nesne nesne) {
        dayaniklilik = dayaniklilik - nesne.etkiHesapla(this);
        if (etkipuani > nesne.etkiHesapla(this)) {
            seviyePuani += 20;
        }
    }

    @Override
    public void nesnePuaniGoster() {
        System.out.println(this.getClass().getName() + "[" + id + "]" + " Nesnesi Puan Durumu");
        System.out.println("Dayanıklılık: " + dayaniklilik);
        System.out.println("Seviye Puanı: " + seviyePuani);
        System.out.println("-----------------");

    }


}
