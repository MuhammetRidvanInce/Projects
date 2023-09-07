# include <stdio.h>
# include <dirent.h>
# include <locale.h>
# include <string.h>


// SABIT DEGISKENLERE VERILERIN CEKILECEGI DOSYANIN DIZINI VERILMELIDIR...
# define UNIVERSITE_DIZIN  "C:/Users/ER/Desktop/Deneme"
# define UNIVERSITE_DIZIN2 "C:/Users/ER/Desktop/Deneme/"

int  uni_klasor_sayisi    = 0;
int  uni_dizin_sayisi     = 0;
int  txt_dosya_sayisi     = 0;
int  txt_dizin_sayisi     = 0;
int  etiket_sayisi        = 0;
int yetim_etiket_sayisi   = 0;
int istenen_etiket_sayisi = 0;

char uni_klasor[30][100]          = {"",""};
char uni_dizin[30][200]           = {"",""};
char txt_dosya[100][100]          = {"",""};
char txt_dizin[100][200]          = {"",""};
char txt_icerik[100][5000]        = {"",""};
char etiket_listesi[100][100]     = {"",""};
char yetim_etiketler[100][100]    = {"",""};
char istenen_etiketler[100][100]  = {"",""};


// TXT DOSYASINDAN CEKILEN VERILER ICIN....
void tr_karakter_kontrol(char *str1)
{
    for (int i = 0; i<strlen(str1); i++)
    {
        if ((str1[i] == -61 && str1[i+1] == -89) || (str1[i] == -25))
               str1[i] = 'c';
        else if ((str1[i] == -60 && str1[i+1] == -79) || (str1[i] == -3))
               str1[i] = 'i';
        else if ((str1[i] == -61 && str1[i+1] == -68)|| (str1[i] == -4))
               str1[i] = 'u';
        else if ((str1[i] == -60 && str1[i+1] == -97)|| (str1[i] == -16))
               str1[i] = 'g';
        else if ((str1[i] == -61 && str1[i+1] == -74)|| (str1[i] == -10))
               str1[i] = 'o';
        else if ((str1[i] == -59 && str1[i+1] == -97)|| (str1[i] == -2))
               str1[i] = 's';
        else if ((str1[i] == -60 && str1[i+1] == -80)|| (str1[i] == -35))
               str1[i] = 'I';
        else if ((str1[i] == -60 && str1[i+1] == -98)|| (str1[i] == -48))
               str1[i] = 'G';
        else if ((str1[i] == -61 && str1[i+1] == -100)|| (str1[i] == -36))
               str1[i] = 'U';
        else if ((str1[i] == -61 && str1[i+1] == -106)|| (str1[i] == -42))
               str1[i] = 'O';
        else if ((str1[i] == -59 && str1[i+1] == -98)|| (str1[i] == -34))
               str1[i] = 'S';
        else if ((str1[i] == -61 && str1[i+1] == -121)|| (str1[i] == -57))
               str1[i] = 'C';
        else
               str1[i] = str1[i];
    }

    for (int j = 0; j < strlen(str1); j++)
    {
        if (str1[j] < 0)
            memmove(&str1[j],&str1[j+1],strlen(str1)-j);
    }
}

// KULLANICIDAN ALINAN VERILER ICIN
void tr_karakter_kontrol_2(char *str)
{
    for (int i = 0; i<strlen(str); i++)
    {
        if (str[i] == -121)
            str[i] = 'c';
        else if (str[i] == -115)
            str[i] = 'i';
        else if (str[i] == -127)
            str[i] = 'u';
        else if (str[i] == -89)
            str[i] = 'g';
        else if (str[i] == -108)
            str[i] = 'o';
        else if (str[i] == -97)
            str[i] = 's';
        else if (str[i] == -104)
            str[i] = 'I';
        else if (str[i] == -90)
            str[i] = 'G';
        else if (str[i] == -102)
            str[i] = 'U';
        else if (str[i] == -103)
            str[i] = 'O';
        else if (str[i] == -98)
            str[i] = 'S';
        else if (str[i] == -128)
            str[i] = 'C';
    }

}

// KOD ICERISINDE TANIMLANAN STRINGLER ICIN
void tr_karakter_kontrol_3(char *str)
{
    for (int i = 0; i<strlen(str); i++)
    {
        if (str[i] == -25)
            str[i] = 'c';
        else if (str[i] == -3)
            str[i] = 'i';
        else if (str[i] == -4)
            str[i] = 'u';
        else if (str[i] == -16)
            str[i] = 'g';
        else if (str[i] == -10)
            str[i] = 'o';
        else if (str[i] == -2)
            str[i] = 's';
        else if (str[i] == -35)
            str[i] = 'I';
        else if (str[i] == -48)
            str[i] = 'G';
        else if (str[i] == -36)
            str[i] = 'U';
        else if (str[i] == -42)
            str[i] = 'O';
        else if (str[i] == -34)
            str[i] = 'S';
        else if (str[i] == -57)
            str[i] = 'C';
    }

}

void VerileriGuncelle()
{
    uni_klasor[30][100];
    uni_dizin[30][200];
    txt_dosya[100][100];
    txt_dizin[100][200];
    txt_icerik[100][5000];
    etiket_listesi[100][100];
    yetim_etiketler[100][100];
    istenen_etiketler[100][100];

    uni_klasor_sayisi    = 0;
    uni_dizin_sayisi     = 0;
    txt_dosya_sayisi     = 0;
    txt_dizin_sayisi     = 0;
    etiket_sayisi        = 0;
    yetim_etiket_sayisi   = 0;
    istenen_etiket_sayisi = 0;

    char universite_klasorler[1000] = "";
    char universite_dizinler[1000] = "";
    char txt_dosya_isimleri[1000] = "";
    char txt_dosya_dizinleri[1000] = "";
    char txt_icerikleri[5000] = "";
    char etiketler[1000] = "";


    DIR *dizin;
    struct dirent *klasor;
    dizin = opendir(UNIVERSITE_DIZIN);

    while ((klasor = readdir(dizin)) != NULL)
    {

        if (strchr(klasor->d_name, '.') == NULL)
        {

            strcat(universite_klasorler, klasor ->d_name);
            strcat(universite_klasorler, "|");

            char gecici_dizin[100] = "";
            strcpy(gecici_dizin,UNIVERSITE_DIZIN2);
            strcat(gecici_dizin,klasor ->d_name);
            strcat(universite_dizinler, gecici_dizin);
            strcat(universite_dizinler, "|");
            uni_klasor_sayisi++;
            uni_dizin_sayisi++;

            //--------------------------------------------------------------
            DIR *dizin2;
            struct dirent *klasor2;
            dizin2 = opendir(gecici_dizin);

            while ((klasor2 = readdir(dizin2)) != NULL)
            {
                if (strstr(klasor2->d_name, ".txt"))
                {
                    char gecisi_dizin2[100] = "";
                    strcpy(gecisi_dizin2, gecici_dizin);
                    strcat(gecisi_dizin2, "/");
                    strcat(gecisi_dizin2,klasor2->d_name);
                    strcat(txt_dosya_dizinleri,gecisi_dizin2);
                    strcat(txt_dosya_dizinleri,"|");

                    tr_karakter_kontrol_3(klasor2->d_name);
                    strcat(txt_dosya_isimleri, klasor2->d_name);
                    strcat(txt_dosya_isimleri, "|");
                    txt_dosya_sayisi++;
                    txt_dizin_sayisi++;

                    //--------------------------------------------------------------

                    char *p;
                    FILE *dosya = fopen(gecisi_dizin2, "r");
                    char buf[2000];
                    char gecici_icerik[5000] = "";

                    while (fgets(buf, 2000, dosya) != NULL)
                        strcat(gecici_icerik, buf);

                    fclose(dosya);
                    strcat(gecici_icerik, "|");
                    strcat(gecici_icerik, "\n");
                    strcat(gecici_icerik, "\0");
                    tr_karakter_kontrol(gecici_icerik);

                    //--------------------------------------------------------------


                    char *aranan1 = "[[";
                    char *aranan2 = "]]";

                    char *ara_ptr1 = strstr(gecici_icerik, aranan1);
                    char *ara_ptr2 = strstr(gecici_icerik, aranan2);


                    while (ara_ptr1 != NULL && ara_ptr2 != NULL)
                    {
                        int len = ara_ptr2 - ara_ptr1 - 3;
                        char temp[len];

                        int k = 0;
                        for (int j = ara_ptr1-gecici_icerik + 2; j<= ara_ptr2-gecici_icerik-1; j++)
                        {
                            temp[k] = gecici_icerik[j];
                            k++;
                        }
                        temp[k] = '\0';

                        //----------------ETIKET OLMA SARTLARI---------------------------

                        // 1- Etiketteki bosluk sayisinin kontrolu
                        char *aranan3 = ' ';
                        char *ara_ptr3 = strchr(temp, aranan3);
                        int bosluk_sayisi = 0;

                        while (ara_ptr3 != NULL)
                        {
                            bosluk_sayisi++;
                            ara_ptr3 = strchr(ara_ptr3+1, aranan3);
                        }

                        // 2 - Etiket tekrarinin kontrolu
                        int kontrol = 0;
                        char kontrol_str[1000];
                        strcpy(kontrol_str,etiketler);
                        char *token = strtok(kontrol_str, "|");
                        while (token != NULL)
                        {
                            if (strcmp(token, temp) ==0)
                            {
                                kontrol = 1;
                                break;
                            }
                            token = strtok(NULL, "|");
                        }

                        // 3 - Etiket icinin tamaminin alfabetik olmasinin kontrolu
                        // Alfabe haricisinde bosluk ve alttire (_) karakteri icerebilir...
                        int alfabetik = 1;
                        for (int i = 0; i<strlen(temp); i++)
                        {
                            if (isalpha(temp[i]) == 0 && temp[i] != 32 && temp[i] != 95)
                            {
                                alfabetik = 0;
                                break;
                            }
                        }

                        // Tum sartlari sagladiysa etiketler listesine yerlestir....
                        if (kontrol == 0 && bosluk_sayisi < 2 && alfabetik == 1)
                        {
                            tr_karakter_kontrol_2(temp);
                            strcat(temp, "|");
                            strcat(etiketler, temp);
                            etiket_sayisi++;
                        }

                        ara_ptr1 = strstr(ara_ptr1+1, aranan1);
                        ara_ptr2 = strstr(ara_ptr2+1, aranan2);
                    }

                    //-----------------------------------------------------------

                    strcat(txt_icerikleri, gecici_icerik);

                }

            }
            closedir(dizin2);

        }

    }
    closedir(dizin);


    //-------------------------------------

    char *token1;
    token1 = strtok(universite_klasorler, "|");
    int indis1 = 0;
    while(token1 != NULL)
    {
        strcpy(uni_klasor[indis1],token1);
        token1 = strtok(NULL, "|" );
        indis1++;
    }
    //----------------------------------------

    char *token2;
    token2 = strtok(universite_dizinler, "|");
    int indis2 = 0;
    while(token2 != NULL )
    {
        strcpy(uni_dizin[indis2],token2);
        token2 = strtok(NULL, "|" );
        indis2++;
    }
//------------------------------------------------
    char *token3;
    token3 = strtok(txt_dosya_isimleri, "|");
    int indis3 = 0;
    while(token3 != NULL )
    {
        strcpy(txt_dosya[indis3],token3);
        token3 = strtok(NULL, "|" );
        indis3++;
    }

//-------------------------------------------
    char *token4;
    token4 = strtok(txt_dosya_dizinleri, "|");
    int indis4 = 0;
    while(token4 != NULL )
    {
        strcpy(txt_dizin[indis4],token4);
        token4 = strtok(NULL, "|" );
        indis4++;
    }
//------------------------------------------------

    char *token5;
    token5 = strtok(txt_icerikleri, "|");
    int indis5 = 0;
    while(token5 != NULL )
    {
        strcpy(txt_icerik[indis5],token5);
        token5 = strtok(NULL, "|" );
        indis5++;
    }

//--------------------------------------------
    char *token6;
    token6 = strtok(etiketler, "|");
    int indis6 = 0;
    while(token6 != NULL )
    {
        strcpy(etiket_listesi[indis6],token6);
        token6 = strtok(NULL, "|" );
        indis6++;
    }
//---------------------------------------------
    int indis7 = 0;
    for (int i = 0; i<etiket_sayisi; i++)
    {
        int yetim = 1;
        for (int j = 0; j < txt_dosya_sayisi; j++)
        {
            char *token = strtok(txt_dosya[j], ".");
            if (strcmp(etiket_listesi[i], token) == 0)
                yetim = 0;
        }

        if(yetim)
        {
           strcpy(yetim_etiketler[indis7], etiket_listesi[i]);
           indis7++;
           yetim_etiket_sayisi++;
        }

    }


    int indis8 = 0;
    for (int i = 0; i<txt_dosya_sayisi; i++)
    {
        int istenen = 1;
        for (int j = 0; j < etiket_sayisi; j++)
        {
            char *token = strtok(txt_dosya[i], ".");
            if (strcmp(token, etiket_listesi[j]) == 0)
                istenen = 0;
        }

        if(istenen)
        {
           strcpy(istenen_etiketler[indis8], txt_dosya[i]);
           indis8++;
           istenen_etiket_sayisi++;
        }

    }
}



// GUNCELLEME FONKSIYONU I ERISINDE DEGISTIRILECEK
// IFADENIN KELIMEMI, ETIKETMI, YETIM ETIKETMI OLDUGUNU
// KONTROL EDIYOR.....
int kelime_kontrol(char *kelime)
{
    for (int i = 0; i< etiket_sayisi; i++)
    {
        if (strcmp(etiket_listesi[i], kelime) == 0)
        {
            for (int j = 0; j < yetim_etiket_sayisi; j++)
            {
                if (strcmp(yetim_etiketler[j],kelime)  == 0)
                    return 2;
            }
            return 1;
        }
    }
    return 0;
}


void kelime_degistir(char *eski, char *yeni)
{
    for (int i = 0; i < txt_dizin_sayisi; i++)
    {
        char *cumle = (char*)malloc(5000);
        strcpy(cumle, txt_icerik[i]);

        char *ptr = strstr(cumle, eski);
        int sayac = 0;
        while(ptr != NULL)
        {
            sayac++;
            ptr = strstr(ptr+1, eski);
        }

        int eskiLen = strlen(eski);
        int yeniLen = strlen(yeni);
        char *yenistr = (char*)malloc(5000);

        int indis = 0;
        while (*cumle)
        {
            if (strstr(cumle, eski) != cumle)
            {
                yenistr[indis] = *cumle;
                indis++;
                *cumle++;
            }

            else
            {
                strcpy(&yenistr[indis], yeni);
                indis += yeniLen;
                cumle += eskiLen;
            }
        }

        yenistr[indis] = '\0';
        if (yenistr[0] == '\n')
            yenistr = yenistr+1;


        remove(txt_dizin[i]);
        FILE *dosya = fopen(txt_dizin[i], "w");
        fputs(yenistr, dosya);
        fclose(dosya);
    }

}


void dosya_ismi_degistir(char *eski_dosya_adi, char *yeni_dosya_adi)
{

    for (int i = 0; i< txt_dosya_sayisi; i++)
    {

        if (strcmp(eski_dosya_adi,txt_dosya[i]) == 0)
        {
            char *mevcut_dizin = (char*)malloc(strlen(txt_dosya[i]) + strlen(yeni_dosya_adi) - strlen(eski_dosya_adi) +1);
            char g_dizin[100] = "";
            strcpy(mevcut_dizin, txt_dizin[i]);
            char *token;
            token = strtok(mevcut_dizin, "/");
            while(token != NULL)
            {
                if (strstr(token, ".txt"))
                    strcat(g_dizin, yeni_dosya_adi);
                else
                {
                   strcat(g_dizin, token);
                   strcat(g_dizin, "/");
                }
                token = strtok(NULL, "/");
            }
            strcat(g_dizin, ".txt");
            rename(txt_dizin[i], g_dizin);

        }
    }
}


void etiket__dosya_listesi_yazdir()
{
    VerileriGuncelle();
    printf("\nNORMAL ETIKETLER (Dosya ve Etiket Var!!)\n");
    int indis1 = 1;
    for (int i = 0; i<txt_dosya_sayisi; i++)
    {
        int istenen = 1;
        for (int j = 0; j < etiket_sayisi; j++)
        {
            char *token = strtok(txt_dosya[i], ".");
            if (strcmp(token, etiket_listesi[j]) == 0)
                istenen = 0;
        }

        if (!istenen)
        {
            printf("   %d ->%s\n", indis1, txt_dosya[i]);
            indis1++;
        }
    }

    printf("\nYETIM ETIKETLER (Etiket Var Dosya Yok!!)\n");
    for (int i = 0; i<yetim_etiket_sayisi; i++)
        printf("    %d ->%s\n",i+1, yetim_etiketler[i]);



    printf("\nISTENEN ETIKETLER (Dosya Var Etiket Yok!!) \n");
    for (int i = 0; i<istenen_etiket_sayisi; i++)
        printf("    %d ->%s\n",i+1, istenen_etiketler[i]);

    printf("\n\n");



}

int ders_kodu()
{
    VerileriGuncelle();
    int enbuyuk = 0;
    for (int i = 0; i < txt_dizin_sayisi; i++)
    {
        FILE *dosya = fopen(txt_dizin[i], "r");
        char buf[100] = "";
        char kod[10] = "";

        fgets(buf, 100, dosya);

        for (int j = 0; j < strlen(buf); j++)
        {
            if (isdigit(buf[j]))
            {
                int indis = 0;
                for (int k = j; k < strlen(buf); k++)
                {
                    kod[indis] = buf[k];
                    indis++;
                }
            int kod_int = atoi(kod);
            if (kod_int > enbuyuk)
                enbuyuk = kod_int;
            break;
            }

        }

    }
    return enbuyuk;
}


void MENU()
{
  while(1)
    {
        VerileriGuncelle();
        printf("\t\tDOKUWIKI KOCAELI UNIVERSITESI UYGULAMA MENUSU\n");
        printf("\t\t---------------------------------------------\n\n");
        printf("%d\t: %s\n",1, "Arama()");
        printf("%d\t: %s\n",2, "Guncelleme()");
        printf("%d\t: %s\n",3, "Dosyaya Yazma()");
        printf("%d\t: %s\n",4, "Tum Etiketler");
        printf("%d\t: %s\n",5, "Tum Alt Klasorler");
        printf("%d\t: %s\n",6, "Tum (.txt) dosyalari");
        printf("%d\t: %s\n",7, "Tum Icerikler");
        printf("%d\t: %s\n",8, "Cikis");
        printf("\n\nYapmak istediginiz islem icin (1 - 7) arasinda bir rakam seciniz: ");
        char kontrol[10];
        gets(kontrol);
        if (!strcmp(kontrol, "1"))
            Arama();
        else if (!strcmp(kontrol, "2"))
            Guncelleme();
        else if (!strcmp(kontrol, "3"))
            Dosyaya_Yazma();
        else if (!strcmp(kontrol, "4"))
        {
           printf("\n\n\n\t\t-----TUM ETIKETLER-----");
           etiket__dosya_listesi_yazdir();
        }
        else if (!strcmp(kontrol, "5"))
        {
           printf("\n\n\n\t\t-----TUM ALT KLASORLER-----\n");
           for (int i = 0; i< uni_klasor_sayisi; i++)
                printf("%d ->%s\n",i+1, uni_klasor[i]);
           printf("\n");
        }
        else if (!strcmp(kontrol, "6"))
        {
           printf("\n\n\n\t\t-----TUM TXT DOSYALARI-----\n");
           for (int i = 0; i< txt_dosya_sayisi; i++)
                printf("%d ->%s\n",i+1, txt_dosya[i]);
           printf("\n");
        }

        else if (!strcmp(kontrol, "7"))
        {
           printf("\n\n\n\t\t-----TUM ICERIKLER-----\n");
           for (int i = 0; i< txt_dosya_sayisi; i++)
           {
             printf("%s\n", txt_icerik[i]);
             printf("----------------------------------------------------------------\n");
           }

           printf("\n");
        }
        else if (!strcmp(kontrol, "8"))
            break;
        else
            printf("\n\nLutfen verilen aralikta bir rakam giriniz!!\n\n");

    }
}

int main()
{
    setlocale(LC_ALL, "Turkish");
    MENU();
    return 0;
}

void Arama()
{
    system("cls");
    printf("\n\n\n------------------------------------------------------\n");
    printf("Arama() FONKSIYONU CALISIYOR.......\n\n");
    char aranacak_kelime[60];
    printf("Aranacak Kelimeyi Giriniz: ");
    fgets(aranacak_kelime, 60, stdin);
    aranacak_kelime[strlen(aranacak_kelime)-1] = '\0';
    tr_karakter_kontrol_2(aranacak_kelime);

    int etiketmi = 0;
    for (int j = 0; j < etiket_sayisi; j++)
    {
        if (strcmp(etiket_listesi[j], aranacak_kelime) == 0)
        {
            etiketmi = 1;
            break;
        }
    }

    if (etiketmi)
    {
        char *aranacak_kelime2 = (char*)malloc(strlen(aranacak_kelime)+4);
        strcpy(aranacak_kelime2, "[[");
        strcat(aranacak_kelime2, aranacak_kelime);
        strcat(aranacak_kelime2, "]]");
        strcpy(aranacak_kelime, aranacak_kelime2);
        printf("    SONUC 1: %s KELIMESI [[ETIKETTIR!]]\n\n\n");
        printf("    SONUC 2: %s ETIKETININ GECTIGI DOSYALAR\n");
    }

    else
    {
       printf("     SONUC 1: |%s| KELIMESI |ETIKET DEGILDIR!|\n\n\n");
       printf("     SONUC 2: |%s| KELIMESININ GECTIGI DOSYALAR\n");
    }

printf("------------------------------------------------------\n");


    int toplam_kac_kere_geciyor1 = 0;
    for (int i = 0; i < txt_dizin_sayisi; i++)
    {
        printf("Klasor Adi: %s\n", txt_dosya[i]);

        int satir_sayisi = 1;
        char *token;
        char temp[3000] = "";
        strcpy(temp, txt_icerik[i]);
        token = strtok(temp, "\n");

        int dosyada_kackere_geciyor = 0;
        while(token != NULL)
        {
            char *ara_ptr = strstr(token, aranacak_kelime);
            int  kac_kere_geciyor = 0;
            while(ara_ptr !=NULL)
            {
                kac_kere_geciyor++;
                toplam_kac_kere_geciyor1++;
                dosyada_kackere_geciyor++;
                ara_ptr = strstr(ara_ptr+1, aranacak_kelime);
            }
            if(kac_kere_geciyor)
                printf("    Satir: %d --> Adet: %d\n", satir_sayisi, kac_kere_geciyor);

            token = strtok(NULL, "\n");
            satir_sayisi++;

        }

        if(dosyada_kackere_geciyor)
            printf("        TOPLAM: %d\n", dosyada_kackere_geciyor);
        else
            printf("    Yukaridaki Dosyada '%s' kelimesi gecmiyor!\n\n", aranacak_kelime);

    }

    if (toplam_kac_kere_geciyor1)
        printf("'%s' kelimesi tum dosyalarda toplam |%d| kere geciyor!!\n", aranacak_kelime, toplam_kac_kere_geciyor1);
    else
        printf("'%s' kelimesi hicbir dosyada gecmiyor!!\n\n");

    printf("------------------------------------------------------\n\n\n");
    printf("    SONUC 3 YETIM ve ISTENEN ETIKETLER\n");
    printf("------------------------------------------------------\n\n");
    printf("TUM ETIKET ve DOSYALAR:\n");
    etiket__dosya_listesi_yazdir();
}

void Guncelleme()
{
    printf("\n\n\n------------------------------------------------------\n");
    printf("Guncelleme() FONKSIYONU CALISIYOR!!!.......\n\n");

    printf("GUNCELLEME ONCESI ETIKET ve DOSYA LISTESI\n");
    printf("------------------------------------------------------\n");
    etiket__dosya_listesi_yazdir();


    /*Degistirilecek ifade /kelime/normal etiket / yetim etiket olabilir.
    Kelime ise tum dosyalar dolasilip ilgili kelime degistirilecek. Normal etiket
    (hem etiketi hem de dosyasi olan etiketler) ise hem metin icerisindeki ifadeler hem de
    dosya adi degistirilecek. Yetim etiket ise metin icerisindeki ifadeler degistirilecek
    ve kullaniciya txt dosyasi olusturup olusturmak istemedigi sorulacak. Olusturmak isterse
    ilgili islemler yapilacak*/

    char mevcut_deger[50] = "";
    char yeni_deger[50] = "";
    char hata_d;

    printf("Degistirmek istediginiz ifadeyi giriniz: ");
    gets(mevcut_deger);
    tr_karakter_kontrol_2(mevcut_deger);
    printf("Yeni ifadeyi giriniz: ");
    gets(yeni_deger);
    tr_karakter_kontrol_2(yeni_deger);


    int kontrol = kelime_kontrol(mevcut_deger); // 0 = Kelime, 1 = Normal Etiket, 2 = Yetim Etiket//

    printf("%d\n\n", kontrol);

   if (kontrol == 0) // Kelime olma durumu
    {
        kelime_degistir(mevcut_deger, yeni_deger);
        for (int i = 0; i<istenen_etiket_sayisi; i++)
        {
            if (strcmp(mevcut_deger, istenen_etiketler[i]))
                dosya_ismi_degistir(mevcut_deger, yeni_deger);
        }
    }
    else if (kontrol == 1) // Normal etiket olma durumu
    {
        char *mevcut_deger2 = (char*)malloc(strlen(mevcut_deger)+4);
        strcpy(mevcut_deger2, "[[");
        strcat(mevcut_deger2, mevcut_deger);
        strcat(mevcut_deger2, "]]");

        char *yeni_deger2 = (char*)malloc(strlen(yeni_deger)+4);
        strcpy(yeni_deger2, "[[");
        strcat(yeni_deger2, yeni_deger);
        strcat(yeni_deger2, "]]");

        kelime_degistir(mevcut_deger2, yeni_deger2);
        dosya_ismi_degistir(mevcut_deger, yeni_deger);

    }
    else if (kontrol == 2) // Yetim Etiket olma durumu
    {
        char *mevcut_deger2 = (char*)malloc(strlen(mevcut_deger)+4);
        strcpy(mevcut_deger2, "[[");
        strcat(mevcut_deger2, mevcut_deger);
        strcat(mevcut_deger2, "]]");

        char *yeni_deger2 = (char*)malloc(strlen(yeni_deger)+4);
        strcpy(yeni_deger2, "[[");
        strcat(yeni_deger2, yeni_deger);
        strcat(yeni_deger2, "]]");

        kelime_degistir(mevcut_deger2, yeni_deger2);
        printf("\n\n\n%s yetim etiketi %s olarak degistirildi\n" \
               "%s yeni etiketimne ait dosya olusturma istiyor musunuz?\n\n", mevcut_deger, yeni_deger, yeni_deger);

        int dosya_kontrol;
        printf("\n\nDosya Olusturmak Icin '1' Bu Asamayi gecmek icin '0': ");


        while(1)
        {
            scanf("%d", &dosya_kontrol);

            if (dosya_kontrol !=1 && dosya_kontrol !=0)
            {
                printf("\n\nLutfen 1 ya da 0 giriniz!: ");
                continue;
            }
            else
            {
                if (dosya_kontrol ==1)
                {
                   printf("\nDosya hangi alt klasorde olusturulsun?\n");
                   printf("-----------------------------------------\n");

                   int dosya_numarasi = 1;
                   for(int i = 0; i<uni_klasor_sayisi; i++)
                   {
                       printf("     %20s:  %d\n", uni_klasor[i], dosya_numarasi);
                       dosya_numarasi++;
                   }

                   char dizin[100];
                   strcpy(dizin, UNIVERSITE_DIZIN2);
                   int dosya_numarasi2;
                   printf("\nLutfen 1 ile %d arasinda rakam giriniz: ", dosya_numarasi-1);

                   while(1)
                   {
                       scanf("%d", &dosya_numarasi2);
                       if (dosya_numarasi2 < 1 || dosya_numarasi2 > dosya_numarasi)
                       {
                            printf("\n\nGirdiginiz Numara Hatali\nLutfen 1 ile %d arasinda rakam giriniz: ", dosya_numarasi-1);
                            continue;
                       }
                       else
                       {
                           strcat(dizin, uni_klasor[dosya_numarasi2-1]);
                           strcat(dizin, "/");
                           strcat(dizin, yeni_deger);
                           strcat(dizin, ".txt");
                           break;
                       }
                   }

                   printf("%s\n", dizin);

                   char ders_bilgileri[250];
                   int kod = ders_kodu();
                   if (kod < 200)
                        sprintf(ders_bilgileri, "Dersin Kodu         : BLM%d\n\nDersin Adi          : [[%s]]\n\nDersin Icerikleri   :", 200, yeni_deger);
                   else
                        sprintf(ders_bilgileri, "Dersin Kodu         : BLM%d\n\nDersin Adi          : [[%s]]\n\nDersin Icerikleri   :", kod+1, yeni_deger);
                   FILE *fp = fopen(dizin, "w");
                   fputs(ders_bilgileri, fp);
                   fclose(fp);
                   printf("\n\nDosya Olusturuldu!!\n");
                   scanf("%c",&hata_d);
                }

                else
                {
                    scanf("%c",&hata_d);
                    system("cls");
                    printf("\n\nDosya olusuturulmadi!!\n");
                }

                break;
            }

        }


    }

    VerileriGuncelle();

    printf("\n\nGUNCELLEME SONRASI ETIKET ve DOSYA LISTESI\n");
    printf("------------------------------------------------------\n\n");
    etiket__dosya_listesi_yazdir();

}

void Dosyaya_Yazma()
{
   system("cls");
   char dosyaya_yazdir[10000];
   char baslik[100];
   sprintf(baslik, "\n\nEtiket Listesi - %30s", "Tekrar Sayisi\n");
   strcat(dosyaya_yazdir, baslik);

   for (int i = 0; i<etiket_sayisi; i++)
   {
       char aranan[50] = "[[";
       strcat(aranan, etiket_listesi[i]);
       strcat(aranan, "]]");
       int tekrar_sayisi = 0;
       for (int j = 0; j<txt_dizin_sayisi; j++)
       {
           char *ara_ptr = strstr(txt_icerik[j], aranan);

           while(ara_ptr !=NULL)
           {
               tekrar_sayisi++;
               ara_ptr = strstr(ara_ptr+1, aranan);
           }
       }

       char temp[100];
       sprintf(temp,"%-30s %10d\n",etiket_listesi[i], tekrar_sayisi);
       strcat(dosyaya_yazdir, temp);
   }

   strcat(dosyaya_yazdir, "\nYetim Etiketler\n");
   for (int i = 0; i<yetim_etiket_sayisi; i++)
   {
       char temp[300];
       sprintf(temp, "%s\n", yetim_etiketler[i]);
       strcat(dosyaya_yazdir, temp);

   }
   strcat(dosyaya_yazdir, "------------------------------\n");
   printf("Son");
   printf("%s",dosyaya_yazdir);
   char dizin[100];
   strcpy(dizin, UNIVERSITE_DIZIN2);
   strcat(dizin, "output.txt");
   FILE *dosya = fopen(dizin, "a");
   fputs(dosyaya_yazdir, dosya);
   fclose(dosya);
}






































