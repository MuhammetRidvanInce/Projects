
public class Oyun {
    
    public static void musabaka(Nesne nesne1, Nesne nesne2)
    {   
        double etki1 = nesne1.etkiHesapla(nesne2);
        nesne1.durumGuncelle(nesne2);
        double etki2 = nesne2.etkiHesapla(nesne1);
        nesne2.durumGuncelle(nesne1);           
    }
    
    
    public static void dayaniklilik_kontrol(Nesne[] array){
        
        int arrayLenght;

        for (arrayLenght = 0; arrayLenght<array.length;arrayLenght++ )
            if (array[arrayLenght] == null)
                    break;
        
        
        int kontrol_gereklimi = 0;
        for (Nesne array1 : array) {
            if (array1 == null)
                break;
            if (array1.dayaniklilik < 0) {
                kontrol_gereklimi = 1;
                break;
            }
        }
        
        
        if (kontrol_gereklimi == 1)
        {
        int i;
        for (i = 0; i < arrayLenght; i++) {

            if (array[i].dayaniklilik < 0)
            {
                array[i] = null;
                break;
            }   
        }

        for (int j = i; j<arrayLenght-1; j++)
            array[j] = array[j+1];
        array[arrayLenght - 1] = null;  
        
        }

        
  
    }
    
    public static int null_karakter_say(Nesne[] array)
    {
        int hepsi_nulmu = 1;
        for (Nesne array1 : array) {
            if (array1 != null) {
                hepsi_nulmu = 0;
                break;
            }  
        }
        return hepsi_nulmu;
    }
    
    public static void terfi_kontrol(Nesne[] nesneListesi, Nesne[] tumListe, int baraj)
    {
        for(int i = 0; i< nesneListesi.length; i++)
        {
            if(nesneListesi[i] == null)
                continue;
            
            String nesneAdi = nesneListesi[i].getClass().getName();
            if(nesneListesi[i] == null ||
                    "AgirTas".equals(nesneAdi) || 
                    "OzelKagit".equals(nesneAdi) || 
                    "UstaMakas".equals(nesneAdi))
                continue;
            
            if (nesneListesi[i].seviyePuani >= baraj)
            {
                int indis = nesneListesi[i].id;
                nesneListesi[i] = tumListe[indis + 15];
              
            }
            
        }
            
    }

   
 
    public static void main(String[] args) {
     
          Arayuz oyunubaslat = new Arayuz();


    }
  
}
