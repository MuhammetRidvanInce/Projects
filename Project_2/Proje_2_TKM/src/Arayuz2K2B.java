
import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.Border;
import javax.swing.ButtonGroup;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;


public class Arayuz2K2B extends Oyun implements ActionListener{
    
    JFrame frame;
    JLabel lbl_1, nesneAdi, Dayaniklilik,seviyePuani,
           lbl_nesne_1, lbl_nesne_2,lbl_nesne_3,lbl_nesne_4,lbl_nesne_5,
           lbl_2, nesneAdi2, Dayaniklilik2,seviyePuani2,
           lbl_nesne_12, lbl_nesne_22,lbl_nesne_32,lbl_nesne_42,lbl_nesne_52,
           secilenTas, etkiPuani1, etkiPuani2, labelVS, sonuc1, sonuc2, sonuctext1, sonuctext2, roundSayisi;
    
    ButtonGroup bg;
    JRadioButton nesne1Ad,nesne2Ad,nesne3Ad,nesne4Ad,nesne5Ad;
 
    JTextField nesne1Dayaniklilik, nesne2Dayaniklilik, nesne3Dayaniklilik, nesne4Dayaniklilik, nesne5Dayaniklilik,
               nesne1SeviyePuani,nesne2SeviyePuani,nesne3SeviyePuani,nesne4SeviyePuani,nesne5SeviyePuani,
            
               nesne12Ad,nesne22Ad,nesne32Ad,nesne42Ad,nesne52Ad,
               nesne12Dayaniklilik, nesne22Dayaniklilik, nesne32Dayaniklilik, nesne42Dayaniklilik, nesne52Dayaniklilik,
               nesne12SeviyePuani,nesne22SeviyePuani,nesne32SeviyePuani,nesne42SeviyePuani,nesne52SeviyePuani,
            
               secilen1, secilen2, etki1, etki2, roundText;
    
    
    JRadioButton[] radiolist; 
    JRadioButton[] secilenler;
    
    JTextField[] textfieldlist_1 = new JTextField[]{nesne1Dayaniklilik, nesne2Dayaniklilik, nesne3Dayaniklilik, 
                                                    nesne4Dayaniklilik, nesne5Dayaniklilik,
                                                    nesne1SeviyePuani,nesne2SeviyePuani,nesne3SeviyePuani,
                                                    nesne4SeviyePuani,nesne5SeviyePuani};
        
    JTextField[] textfieldlist_2 = new JTextField[]{nesne12Ad,nesne22Ad,nesne32Ad,nesne42Ad,nesne52Ad,
                                                    nesne12Dayaniklilik, nesne22Dayaniklilik, nesne32Dayaniklilik, 
                                                    nesne42Dayaniklilik, nesne52Dayaniklilik,
                                                    nesne12SeviyePuani,nesne22SeviyePuani,nesne32SeviyePuani,
                                                    nesne42SeviyePuani,nesne52SeviyePuani};
    
    Nesne n1;
    Nesne n2;
    ImageIcon loser = new ImageIcon(new ImageIcon("loser.png").getImage().getScaledInstance(100, 100, Image.SCALE_DEFAULT));
    ImageIcon winner = new ImageIcon(new ImageIcon("winner.png").getImage().getScaledInstance(120, 120, Image.SCALE_DEFAULT));
    ImageIcon draw = new ImageIcon(new ImageIcon("draw.png").getImage().getScaledInstance(100, 100, Image.SCALE_DEFAULT));
    
    Oyuncu kullanici;
    Oyuncu bilgisayar;
    int round;
    int round_sayac = 1;
    int indis = 0;
    int barajPuani;
    
    int secilen_sayisi_2 = 0;
    Nesne[] secilenler_2 = new Nesne[5];
    
    JButton nesneSec, musabaka;
    JFrame anaekran;
    
    public Arayuz2K2B(Oyuncu kullanici, Oyuncu bilgisayar, int round, JFrame anaekran, int barajPuani){
        
        this.kullanici = kullanici;
        this.bilgisayar = bilgisayar;
        this.round = round;
        this.anaekran = anaekran;
        this.barajPuani = barajPuani;
        
        frame = new JFrame("KULLANICI BİLGİSAYAR OYUNU");   
        Border border1 = BorderFactory.createLineBorder(Color.black);
        
        JPanel panel1 = new JPanel(); 
        panel1.setBounds(15,15,550,425); 
        panel1.setBackground(Color.white);
        panel1.setBorder(border1);
        panel1.setLayout(null);
        frame.add(panel1);

        JPanel panel2 = new JPanel(); 
        panel2.setBounds(565,15,550,425); 
        panel2.setBackground(Color.white);
        panel2.setBorder(border1);
        panel2.setLayout(null);
        frame.add(panel2);

        JPanel panel3 = new JPanel(); 
        panel3.setBounds(15,450,1100,150); 
        panel3.setBackground(Color.white);
        panel3.setBorder(border1);
        panel3.setLayout(null);
        frame.add(panel3);

        lbl_1 = new JLabel(kullanici.OyuncuAdi.toUpperCase() + " "+ kullanici.oyuncuID + " NESNE LİSTESİ");
        lbl_1.setBounds(100, 50, 350, 50);
        lbl_1.setFont(new Font("Serif", Font.BOLD, 23));
        panel1.add(lbl_1);
        
        lbl_2 = new JLabel(bilgisayar.OyuncuAdi.toUpperCase() + " "+ bilgisayar.oyuncuID + " NESNE LİSTESİ");
        lbl_2.setBounds(100, 50, 350, 50);
        lbl_2.setFont(new Font("Serif", Font.BOLD, 23));
        panel2.add(lbl_2);
         
        //---------------------------KULLANICI----------------------------------
        //-----------------------------LABELS-----------------------------------
        nesneAdi = new JLabel("Nesne Adı");
        nesneAdi.setBounds(170, 100, 100, 75);
        nesneAdi.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(nesneAdi);

        Dayaniklilik = new JLabel("Dayanıklılık");
        Dayaniklilik.setBounds(290, 100, 200, 75);
        Dayaniklilik.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(Dayaniklilik);

        seviyePuani = new JLabel("Seviye Puanı");
        seviyePuani.setBounds(420, 100, 200, 75);
        seviyePuani.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(seviyePuani);

        lbl_nesne_1 = new JLabel("NESNE 1");
        lbl_nesne_1.setBounds(50, 175, 80, 25);
        lbl_nesne_1.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(lbl_nesne_1);

        lbl_nesne_2 = new JLabel("NESNE 2");
        lbl_nesne_2.setBounds(50, 225, 80, 25);
        lbl_nesne_2.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(lbl_nesne_2);

        lbl_nesne_3 = new JLabel("NESNE 3");
        lbl_nesne_3.setBounds(50, 275, 80, 25);
        lbl_nesne_3.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(lbl_nesne_3);

        lbl_nesne_4 = new JLabel("NESNE 4");
        lbl_nesne_4.setBounds(50, 325, 80, 25);
        lbl_nesne_4.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(lbl_nesne_4);

        lbl_nesne_5 = new JLabel("NESNE 5");
        lbl_nesne_5.setBounds(50, 375, 80, 25);
        lbl_nesne_5.setFont(new Font("Serif", Font.BOLD, 20));
        panel1.add(lbl_nesne_5);

        //---------------------------KULLANICI----------------------------------
        //--------------------------RADIOBUTTONS--------------------------------
         
        nesne1Ad = new JRadioButton();
        nesne1Ad.setBounds(142, 175, 140, 25);
        nesne1Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne1Ad.setHorizontalAlignment(0);
        panel1.add(nesne1Ad);

        nesne2Ad = new JRadioButton();
        nesne2Ad.setBounds(142, 225, 140, 25);
        nesne2Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne2Ad.setHorizontalAlignment(0);
        panel1.add(nesne2Ad);

        nesne3Ad = new JRadioButton();
        nesne3Ad.setBounds(142, 275, 140, 25);
        nesne3Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne3Ad.setHorizontalAlignment(0);
        panel1.add(nesne3Ad);

        nesne4Ad = new JRadioButton();
        nesne4Ad.setBounds(142, 325, 140, 25);
        nesne4Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne4Ad.setHorizontalAlignment(0);
        panel1.add(nesne4Ad);

        nesne5Ad = new JRadioButton();
        nesne5Ad.setBounds(142, 375, 140, 25);
        nesne5Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne5Ad.setHorizontalAlignment(0);
        panel1.add(nesne5Ad);

        bg =new ButtonGroup();
        bg.add(nesne1Ad);bg.add(nesne2Ad);bg.add(nesne3Ad);
        bg.add(nesne4Ad);bg.add(nesne5Ad);

        //----------------------------KULLANICI---------------------------------
        //---------------------------TEXTFIELDS---------------------------------
         
        nesne1Dayaniklilik = new JTextField();
        nesne1Dayaniklilik.setBounds(302, 175, 80, 25);
        nesne1Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne1Dayaniklilik.setHorizontalAlignment(0);
        nesne1Dayaniklilik.setEditable(false);
        panel1.add(nesne1Dayaniklilik);

        nesne2Dayaniklilik = new JTextField();
        nesne2Dayaniklilik.setBounds(302, 225, 80, 25);
        nesne2Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne2Dayaniklilik.setHorizontalAlignment(0);
        nesne2Dayaniklilik.setEditable(false);
        panel1.add(nesne2Dayaniklilik);

        nesne3Dayaniklilik = new JTextField();
        nesne3Dayaniklilik.setBounds(302, 275, 80, 25);
        nesne3Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne3Dayaniklilik.setHorizontalAlignment(0);
        nesne3Dayaniklilik.setEditable(false);
        panel1.add(nesne3Dayaniklilik);

        nesne4Dayaniklilik = new JTextField();
        nesne4Dayaniklilik.setBounds(302, 325, 80, 25);
        nesne4Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne4Dayaniklilik.setHorizontalAlignment(0);
        nesne4Dayaniklilik.setEditable(false);
        panel1.add(nesne4Dayaniklilik);

        nesne5Dayaniklilik = new JTextField();
        nesne5Dayaniklilik.setBounds(302, 375, 80, 25);
        nesne5Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne5Dayaniklilik.setHorizontalAlignment(0);
        nesne5Dayaniklilik.setEditable(false);
        panel1.add(nesne5Dayaniklilik);


        nesne1SeviyePuani = new JTextField();
        nesne1SeviyePuani.setBounds(435, 175, 80, 25);
        nesne1SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne1SeviyePuani.setHorizontalAlignment(0);
        nesne1SeviyePuani.setEditable(false);
        panel1.add(nesne1SeviyePuani);

        nesne2SeviyePuani = new JTextField();
        nesne2SeviyePuani.setBounds(435, 225, 80, 25);
        nesne2SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne2SeviyePuani.setHorizontalAlignment(0);
        nesne2SeviyePuani.setEditable(false);
        panel1.add(nesne2SeviyePuani);

        nesne3SeviyePuani = new JTextField();
        nesne3SeviyePuani.setBounds(435, 275, 80, 25);
        nesne3SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne3SeviyePuani.setHorizontalAlignment(0);
        nesne3SeviyePuani.setEditable(false);
        panel1.add(nesne3SeviyePuani);

        nesne4SeviyePuani = new JTextField();
        nesne4SeviyePuani.setBounds(435, 325, 80, 25);
        nesne4SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne4SeviyePuani.setHorizontalAlignment(0);
        nesne4SeviyePuani.setEditable(false);
        panel1.add(nesne4SeviyePuani);

        nesne5SeviyePuani = new JTextField();
        nesne5SeviyePuani.setBounds(435, 375, 80, 25);
        nesne5SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne5SeviyePuani.setHorizontalAlignment(0);
        nesne5SeviyePuani.setEditable(false);
        panel1.add(nesne5SeviyePuani);

        //---------------------------BİLGİSAYAR---------------------------------
        //-----------------------------LABELS-----------------------------------

        nesneAdi2 = new JLabel("Nesne Adı");
        nesneAdi2.setBounds(150, 100, 100, 75);
        nesneAdi2.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(nesneAdi2);

        Dayaniklilik2 = new JLabel("Dayanıklılık");
        Dayaniklilik2.setBounds(290, 100, 200, 75);
        Dayaniklilik2.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(Dayaniklilik2);

        seviyePuani2 = new JLabel("Seviye Puanı");
        seviyePuani2.setBounds(420, 100, 200, 75);
        seviyePuani2.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(seviyePuani2);

        lbl_nesne_12 = new JLabel("NESNE 1");
        lbl_nesne_12.setBounds(50, 175, 80, 25);
        lbl_nesne_12.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(lbl_nesne_12);

        lbl_nesne_22 = new JLabel("NESNE 2");
        lbl_nesne_22.setBounds(50, 225, 80, 25);
        lbl_nesne_22.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(lbl_nesne_22);

        lbl_nesne_32 = new JLabel("NESNE 3");
        lbl_nesne_32.setBounds(50, 275, 80, 25);
        lbl_nesne_32.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(lbl_nesne_32);

        lbl_nesne_42 = new JLabel("NESNE 4");
        lbl_nesne_42.setBounds(50, 325, 80, 25);
        lbl_nesne_42.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(lbl_nesne_42);

        lbl_nesne_52 = new JLabel("NESNE 5");
        lbl_nesne_52.setBounds(50, 375, 80, 25);
        lbl_nesne_52.setFont(new Font("Serif", Font.BOLD, 20));
        panel2.add(lbl_nesne_52);

        //---------------------------BİLGİSAYAR---------------------------------
        //---------------------------TEXTFIELDS---------------------------------
        nesne12Ad = new JTextField();
        nesne12Ad.setBounds(142, 175, 120, 25);
        nesne12Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne12Ad.setHorizontalAlignment(0);
        nesne12Ad.setEditable(false);
        panel2.add(nesne12Ad);

        nesne22Ad = new JTextField();
        nesne22Ad.setBounds(142, 225, 120, 25);
        nesne22Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne22Ad.setHorizontalAlignment(0);
        nesne22Ad.setEditable(false);
        panel2.add(nesne22Ad);

        nesne32Ad = new JTextField();
        nesne32Ad.setBounds(142, 275, 120, 25);
        nesne32Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne32Ad.setHorizontalAlignment(0);
        nesne32Ad.setEditable(false);
        panel2.add(nesne32Ad);

        nesne42Ad = new JTextField();
        nesne42Ad.setBounds(142, 325, 120, 25);
        nesne42Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne42Ad.setHorizontalAlignment(0);
        nesne42Ad.setEditable(false);
        panel2.add(nesne42Ad);

        nesne52Ad = new JTextField();
        nesne52Ad.setBounds(142, 375, 110, 25);
        nesne52Ad.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne52Ad.setHorizontalAlignment(0);
        nesne52Ad.setEditable(false);
        panel2.add(nesne52Ad);

        nesne12Dayaniklilik = new JTextField();
        nesne12Dayaniklilik.setBounds(292, 175, 80, 25);
        nesne12Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne12Dayaniklilik.setHorizontalAlignment(0);
        nesne12Dayaniklilik.setEditable(false);
        panel2.add(nesne12Dayaniklilik);

        nesne22Dayaniklilik = new JTextField();
        nesne22Dayaniklilik.setBounds(292, 225, 80, 25);
        nesne22Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne22Dayaniklilik.setHorizontalAlignment(0);
        nesne22Dayaniklilik.setEditable(false);
        panel2.add(nesne22Dayaniklilik);

        nesne32Dayaniklilik = new JTextField();
        nesne32Dayaniklilik.setBounds(292, 275, 80, 25);
        nesne32Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne32Dayaniklilik.setHorizontalAlignment(0);
        nesne32Dayaniklilik.setEditable(false);
        panel2.add(nesne32Dayaniklilik);

        nesne42Dayaniklilik = new JTextField();
        nesne42Dayaniklilik.setBounds(292, 325, 80, 25);
        nesne42Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne42Dayaniklilik.setHorizontalAlignment(0);
        nesne42Dayaniklilik.setEditable(false);
        panel2.add(nesne42Dayaniklilik);

        nesne52Dayaniklilik = new JTextField();
        nesne52Dayaniklilik.setBounds(292, 375, 80, 25);
        nesne52Dayaniklilik.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne52Dayaniklilik.setHorizontalAlignment(0);
        nesne52Dayaniklilik.setEditable(false);
        panel2.add(nesne52Dayaniklilik);

        nesne12SeviyePuani = new JTextField();
        nesne12SeviyePuani.setBounds(425, 175, 80, 25);
        nesne12SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne12SeviyePuani.setHorizontalAlignment(0);
        nesne12SeviyePuani.setEditable(false);
        panel2.add(nesne12SeviyePuani);

        nesne22SeviyePuani = new JTextField();
        nesne22SeviyePuani.setBounds(425, 225, 80, 25);
        nesne22SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne22SeviyePuani.setHorizontalAlignment(0);
        nesne22SeviyePuani.setEditable(false);
        panel2.add(nesne22SeviyePuani);

        nesne32SeviyePuani = new JTextField();
        nesne32SeviyePuani.setBounds(425, 275, 80, 25);
        nesne32SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne32SeviyePuani.setHorizontalAlignment(0);
        nesne32SeviyePuani.setEditable(false);
        panel2.add(nesne32SeviyePuani);

        nesne42SeviyePuani = new JTextField();
        nesne42SeviyePuani.setBounds(425, 325, 80, 25);
        nesne42SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne42SeviyePuani.setHorizontalAlignment(0);
        nesne42SeviyePuani.setEditable(false);
        panel2.add(nesne42SeviyePuani);

        nesne52SeviyePuani = new JTextField();
        nesne52SeviyePuani.setBounds(425, 375, 80, 25);
        nesne52SeviyePuani.setFont(new Font("SansSerif", Font.BOLD, 16));
        nesne52SeviyePuani.setHorizontalAlignment(0);
        nesne52SeviyePuani.setEditable(false);
        panel2.add(nesne52SeviyePuani);


        //-------------------------MUSABAKA ALANI ------------------------------

        secilenTas = new JLabel("SEÇİLEN TAŞLAR");
        secilenTas.setBounds(445, 0, 250, 30);
        secilenTas.setFont(new Font("DialogInput", Font.BOLD, 25));
        panel3.add(secilenTas); 

        etkiPuani1 = new JLabel("ETKİ PUANI");
        etkiPuani1.setBounds(305, 85, 150, 25);
        etkiPuani1.setFont(new Font("DialogInput", Font.BOLD, 15));
        panel3.add(etkiPuani1); 

        etkiPuani2 = new JLabel("ETKİ PUANI");
        etkiPuani2.setBounds(598, 85, 150, 25);
        etkiPuani2.setFont(new Font("DialogInput", Font.BOLD, 15));
        panel3.add(etkiPuani2); 

        labelVS = new JLabel("VS");
        labelVS.setBounds(510, 25, 150, 50);
        labelVS.setFont(new Font("DialogInput", Font.ITALIC, 60));
        panel3.add(labelVS); 

        secilen1 = new JTextField();
        secilen1.setBounds(305,35,200,40);
        secilen1.setFont(new Font("SansSerif", Font.BOLD, 25));
        secilen1.setHorizontalAlignment(0);
        secilen1.setForeground(Color.red);
        secilen1.setEditable(false);
        panel3.add(secilen1);

        secilen2 = new JTextField();
        secilen2.setBounds(598,35,200,40);
        secilen2.setFont(new Font("SansSerif", Font.BOLD, 25));
        secilen2.setHorizontalAlignment(0);
        secilen2.setForeground(Color.red);
        secilen2.setEditable(false);
        panel3.add(secilen2);

        etki1 = new JTextField();
        etki1.setBounds(410,87,70,25);
        etki1.setFont(new Font("SansSerif", Font.BOLD, 16));
        etki1.setHorizontalAlignment(0);
        etki1.setForeground(Color.blue);
        etki1.setEditable(false);
        panel3.add(etki1);

        etki2 = new JTextField();
        etki2.setBounds(703,87,70,25);
        etki2.setFont(new Font("SansSerif", Font.BOLD, 16));
        etki2.setHorizontalAlignment(0);
        etki2.setForeground(Color.blue);
        etki2.setEditable(false);
        panel3.add(etki2);

        sonuc1 = new JLabel("MÜSABAKA SONUCU");
        sonuc1.setBounds(15, 0, 250, 25);
        sonuc1.setFont(new Font("DialogInput", Font.BOLD, 25));
        panel3.add(sonuc1);

        sonuc2 = new JLabel("MÜSABAKA SONUCU");
        sonuc2.setBounds(850, 0, 250, 25);
        sonuc2.setFont(new Font("DialogInput", Font.BOLD, 25));
        panel3.add(sonuc2); 

        sonuctext1 = new JLabel();
        sonuctext1.setBounds(45,10,150,150);
        sonuctext1.setHorizontalAlignment(0);
        panel3.add(sonuctext1);

        sonuctext2 = new JLabel();
        sonuctext2.setBounds(880,10,150,150);
        sonuctext2.setHorizontalAlignment(0);
        panel3.add(sonuctext2);
         
        nesneSec = new JButton("NESNE SEÇ");
        nesneSec.setBounds(15, 600, 250, 45);
        nesneSec.addActionListener(this);
        nesneSec.setFont(new Font("SansSerif", Font.BOLD, 16));
        frame.add(nesneSec);

        musabaka = new JButton("MÜSABAKA");
        musabaka.setBounds(270, 600, 250, 45);
        musabaka.addActionListener(this);
        musabaka.setFont(new Font("SansSerif", Font.BOLD, 16));
        musabaka.setEnabled(false);
        frame.add(musabaka);

        roundSayisi = new JLabel("ROUND");
        roundSayisi.setBounds(950, 610, 75, 25);
        roundSayisi.setFont(new Font("Serif", Font.BOLD, 20));
        roundSayisi.setForeground(Color.green);
        frame.add(roundSayisi);

        roundText = new JTextField("---");
        roundText.setBounds(1025,610,75,25);
        roundText.setFont(new Font("SansSerif", Font.BOLD, 16));
        roundText.setHorizontalAlignment(0);
        roundText.setForeground(Color.blue);
        roundText.setEditable(false);
        frame.add(roundText);
        frame.setResizable(false);
        
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE );
        frame.setSize(1145, 700);
        frame.getContentPane().setBackground(new Color(68, 100, 125));
        frame.setLayout(null);
        
        frame.setVisible(true); 
            frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                anaekran.setVisible(true);
            }
        });
        
        ArayuzGuncelle();
   
    }
    
    public final void ArayuzGuncelle(){
        
        dayaniklilik_kontrol(kullanici.nesneListesi);
        dayaniklilik_kontrol(bilgisayar.nesneListesi);
        terfi_kontrol(kullanici.nesneListesi, kullanici.nesneler, barajPuani);
        terfi_kontrol(bilgisayar.nesneListesi, bilgisayar.nesneler, barajPuani);

        //----------------------------KULLANICI---------------------------------

        if (kullanici.nesneListesi[0] == null)
        {
            nesne1Ad.setEnabled(false);
            nesne1Ad.setText("ELENDİ");   
        }
        else
            nesne1Ad.setText(kullanici.nesneListesi[0].getClass().getName() + "_" + kullanici.nesneListesi[0].id);
            
        if (kullanici.nesneListesi[1] == null)
        {
            nesne2Ad.setEnabled(false);
            nesne2Ad.setText("ELENDİ");   
        }
        else
            nesne2Ad.setText(kullanici.nesneListesi[1].getClass().getName() + "_" + kullanici.nesneListesi[1].id);
        
        if (kullanici.nesneListesi[2] == null)
        {
            nesne3Ad.setEnabled(false);
            nesne3Ad.setText("ELENDİ");   
        }
        else
            nesne3Ad.setText(kullanici.nesneListesi[2].getClass().getName() + "_" + kullanici.nesneListesi[2].id);
        
        if (kullanici.nesneListesi[3] == null)
        {
            nesne4Ad.setEnabled(false);
            nesne4Ad.setText("ELENDİ");   
        }
        else
            nesne4Ad.setText(kullanici.nesneListesi[3].getClass().getName() + "_" + kullanici.nesneListesi[3].id);
        
        if (kullanici.nesneListesi[4] == null)
        {
            nesne5Ad.setEnabled(false);
            nesne5Ad.setText("ELENDİ");   
        }
        else
            nesne5Ad.setText(kullanici.nesneListesi[4].getClass().getName() + "_" + kullanici.nesneListesi[4].id);
        
        // String.format("%,.3f", n1.etkiHesapla(n2))
        if (kullanici.nesneListesi[0] == null)
            nesne1Dayaniklilik.setText("-");
        else
            nesne1Dayaniklilik.setText(String.format("%,.3f", kullanici.nesneListesi[0].dayaniklilik));
        
        if (kullanici.nesneListesi[1] == null)
            nesne2Dayaniklilik.setText("-");
        else
            nesne2Dayaniklilik.setText(String.format("%,.3f", kullanici.nesneListesi[1].dayaniklilik));
                
        if (kullanici.nesneListesi[2] == null)
            nesne3Dayaniklilik.setText("-");
        else
            nesne3Dayaniklilik.setText(String.format("%,.3f", kullanici.nesneListesi[2].dayaniklilik));
                
        if (kullanici.nesneListesi[3] == null)
            nesne4Dayaniklilik.setText("-");
        else
            nesne4Dayaniklilik.setText(String.format("%,.3f", kullanici.nesneListesi[3].dayaniklilik));
        
        if (kullanici.nesneListesi[4] == null)
            nesne5Dayaniklilik.setText("-");
        else
            nesne5Dayaniklilik.setText(String.format("%,.3f", kullanici.nesneListesi[4].dayaniklilik));
        

        if (kullanici.nesneListesi[0] == null)
            nesne1SeviyePuani.setText("-");
        else
            nesne1SeviyePuani.setText(String.format("%,.1f", kullanici.nesneListesi[0].seviyePuani));
        
        if (kullanici.nesneListesi[1] == null)
            nesne2SeviyePuani.setText("-");
        else
            nesne2SeviyePuani.setText(String.format("%,.1f", kullanici.nesneListesi[1].seviyePuani));
        
        if (kullanici.nesneListesi[2] == null)
            nesne3SeviyePuani.setText("-");
        else
            nesne3SeviyePuani.setText(String.format("%,.1f", kullanici.nesneListesi[2].seviyePuani));
        
        if (kullanici.nesneListesi[3] == null)
            nesne4SeviyePuani.setText("-");
        else
            nesne4SeviyePuani.setText(String.format("%,.1f", kullanici.nesneListesi[3].seviyePuani));
        
        if (kullanici.nesneListesi[4] == null)
            nesne5SeviyePuani.setText("-");
        else
            nesne5SeviyePuani.setText(String.format("%,.1f", kullanici.nesneListesi[4].seviyePuani));
            
        //----------------------------BİLGİSAYAR--------------------------------
        
        if (bilgisayar.nesneListesi[0] == null)
            nesne12Ad.setText("ELENDİ");
        else
            nesne12Ad.setText("*****");
            
        if (bilgisayar.nesneListesi[1] == null)
            nesne22Ad.setText("ELENDİ");
        else
            nesne22Ad.setText("*****");
        
        if (bilgisayar.nesneListesi[2] == null)
            nesne32Ad.setText("ELENDİ");
        else
            nesne32Ad.setText("*****");
        
        if (bilgisayar.nesneListesi[3] == null)
            nesne42Ad.setText("ELENDİ");
        else
            nesne42Ad.setText("*****");
        
        if (bilgisayar.nesneListesi[4] == null)
            nesne52Ad.setText("ELENDİ");
        else
            nesne52Ad.setText("*****");
        
        
        if (bilgisayar.nesneListesi[0] == null)
            nesne12Dayaniklilik.setText("-");
        else
            nesne12Dayaniklilik.setText("*****");
        
        if (bilgisayar.nesneListesi[1] == null)
            nesne22Dayaniklilik.setText("-");
        else
            nesne22Dayaniklilik.setText("*****");
                
        if (bilgisayar.nesneListesi[2] == null)
            nesne32Dayaniklilik.setText("-");
        else
            nesne32Dayaniklilik.setText("*****");
                
        if (bilgisayar.nesneListesi[3] == null)
            nesne42Dayaniklilik.setText("-");
        else
            nesne42Dayaniklilik.setText("*****");
        
        if (bilgisayar.nesneListesi[4] == null)
            nesne52Dayaniklilik.setText("-");
        else
            nesne52Dayaniklilik.setText("*****");
        

        if (bilgisayar.nesneListesi[0] == null)
            nesne12SeviyePuani.setText("-");
        else
            nesne12SeviyePuani.setText("*****");
        
        if (bilgisayar.nesneListesi[1] == null)
            nesne22SeviyePuani.setText("-");
        else
            nesne22SeviyePuani.setText("*****");
        
        if (bilgisayar.nesneListesi[2] == null)
            nesne32SeviyePuani.setText("-");
        else
            nesne32SeviyePuani.setText("*****");
        
        if (bilgisayar.nesneListesi[3] == null)
            nesne42SeviyePuani.setText("-");
        else
            nesne42SeviyePuani.setText("*****");
        
        if (bilgisayar.nesneListesi[4] == null)
            nesne52SeviyePuani.setText("-");
        else
            nesne52SeviyePuani.setText("*****");


    }
    
    public int secilimi()
    {  
        radiolist = new JRadioButton[]{nesne1Ad,nesne2Ad,nesne3Ad,nesne4Ad,nesne5Ad};
        int secili = 0;
        for (JRadioButton radioButton : radiolist) {
            if (radioButton.isSelected()) {
                secili = 1;
                break;  
            }
        }
        return secili;
    }
    
    public int secildimi(Nesne[] secilen_liste, Nesne nesne)
    {
        int secilimi = 0;
        
        for (Nesne var : secilen_liste) {
            if (var == nesne) {
                secilimi = 1;
                break;
            }  
        }

        return secilimi;   
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        
        radiolist = new JRadioButton[]{nesne1Ad,nesne2Ad,nesne3Ad,nesne4Ad,nesne5Ad};
        
        //Nesne Seç Butonu için yapılacak işlemler...
        if(e.getSource() == nesneSec)
        {
            
            if (secilimi() == 0)
            {
                 JOptionPane.showMessageDialog(null, "NESNE SEÇMEDİNİZ!!!");  
                 return;
            }

            secilenler = new JRadioButton[5];
            if (indis < 4)
            {
                for (int i = 0; i < radiolist.length; i++)
                {
                    if (radiolist[i].isSelected())
                    {
                        n1 = kullanici.nesneListesi[i];
                        secilenler[indis] = radiolist[i];
                        radiolist[i].setEnabled(false);
                        bg.clearSelection();
                        indis++;
                        break;
                    }
                }
                
            }
            else 
            {
                for (JRadioButton radiolist1 : radiolist) {
                    radiolist1.setEnabled(true);
                }

                for (int i = 0; i < radiolist.length; i++)
                {
                    if (radiolist[i].isSelected())
                    {
                        n1 = kullanici.nesneListesi[i];
                        bg.clearSelection();
                        break;
                    }
                }
                
            }

            secilen1.setText(n1.getClass().getName().toUpperCase() + "_" + n1.id);
            etki1.setText("******");

            if (secilen_sayisi_2 < 5)
            {
                while (true)
                {
                    n2 = bilgisayar.nesneSec(bilgisayar.nesneListesi);
                    if (secildimi(secilenler_2, n2) == 0)
                    {
                        secilenler_2[secilen_sayisi_2] = n2;
                        secilen_sayisi_2++;
                        break;
                    }      
                }   
            }
            else
            {
               n2 = bilgisayar.nesneSec(bilgisayar.nesneListesi); 
            }
            
            

            secilen2.setText("******");
            etki2.setText("*****");
            
            musabaka.setEnabled(true);
            nesneSec.setEnabled(false);
            roundText.setText(""+round_sayac + "/" + round);
        }
        
        //Müsabaka Butonu için yapılacak işlemler...
        else if (e.getSource() == musabaka)
        {
            
            etki1.setText(String.format("%,.3f", n1.etkiHesapla(n2))); 
            secilen2.setText(n2.getClass().getName().toUpperCase() + "_" + n2.id);
            etki2.setText(String.format("%,.3f", n2.etkiHesapla(n1)));
            musabaka.setEnabled(false);
            nesneSec.setEnabled(true);
            
            if (n1.etkiHesapla(n2) > n2.etkiHesapla(n1))
            {
                sonuctext1.setIcon(winner);
                sonuctext2.setIcon(loser);
            }
            else if (n1.etkiHesapla(n2) < n2.etkiHesapla(n1))
            {
                sonuctext1.setIcon(loser);
                sonuctext2.setIcon(winner);
            }
            else
            {
                sonuctext1.setIcon(draw);
                sonuctext2.setIcon(draw); 
            }
                
            n1.durumGuncelle(n2);
            n2.durumGuncelle(n1);
            ArayuzGuncelle();
            n1 = null;
            n2 = null;
            
            int kullanici_null_karakter = null_karakter_say(kullanici.nesneListesi);
            int bilgisayar_null_karakter = null_karakter_say(bilgisayar.nesneListesi);
            
            if (round == round_sayac || kullanici_null_karakter == 1 || bilgisayar_null_karakter == 1)
            {
                musabaka.setEnabled(false);
                nesneSec.setEnabled(false);
                etkiPuani1.setText("SKOR");
                etkiPuani2.setText("SKOR");
                etki1.setText(String.format("%,.3f", kullanici.skorGoster()));
                etki2.setText(String.format("%,.3f", bilgisayar.skorGoster()));
                
                if (kullanici.skorGoster() > bilgisayar.skorGoster())
                {
                    secilen1.setText("KAZANDI!");
                    secilen2.setText("KAYBETTİ!");
                    sonuctext1.setIcon(winner);
                    sonuctext2.setIcon(loser);
                }
                    
                else if(kullanici.skorGoster() < bilgisayar.skorGoster())
                {
                    secilen1.setText("KAYBETTİ!");
                    secilen2.setText("KAZANDI!");
                    sonuctext1.setIcon(loser);
                    sonuctext2.setIcon(winner); 
                }
                else
                {
                    secilen1.setText("BERABERE!");
                    secilen2.setText("BERABERE!");
                    sonuctext1.setIcon(draw);
                    sonuctext2.setIcon(draw);  
                }
                
                
                // Oyun bittikten sonra bilgisayarın taşlarını göster
                //----------------------------------------------------
                if (bilgisayar.nesneListesi[0] == null)
                {
                    nesne12Ad.setEnabled(false);
                    nesne12Ad.setText("ELENDİ");   
                }
                else
                    nesne12Ad.setText(bilgisayar.nesneListesi[0].getClass().getName() + "_" + bilgisayar.nesneListesi[0].id);

                if (bilgisayar.nesneListesi[1] == null)
                {
                    nesne22Ad.setEnabled(false);
                    nesne22Ad.setText("ELENDİ");   
                }
                else
                    nesne22Ad.setText(bilgisayar.nesneListesi[1].getClass().getName() + "_" + bilgisayar.nesneListesi[1].id);

                if (bilgisayar.nesneListesi[2] == null)
                {
                    nesne32Ad.setEnabled(false);
                    nesne32Ad.setText("ELENDİ");   
                }
                else
                    nesne32Ad.setText(bilgisayar.nesneListesi[2].getClass().getName() + "_" + bilgisayar.nesneListesi[2].id);

                if (bilgisayar.nesneListesi[3] == null)
                {
                    nesne42Ad.setEnabled(false);
                    nesne42Ad.setText("ELENDİ");   
                }
                else
                    nesne42Ad.setText(bilgisayar.nesneListesi[3].getClass().getName() + "_" + bilgisayar.nesneListesi[3].id);

                if (bilgisayar.nesneListesi[4] == null)
                {
                    nesne52Ad.setEnabled(false);
                    nesne52Ad.setText("ELENDİ");   
                }
                else
                    nesne52Ad.setText(bilgisayar.nesneListesi[4].getClass().getName() + "_" + bilgisayar.nesneListesi[4].id);


                if (bilgisayar.nesneListesi[0] == null)
                    nesne12Dayaniklilik.setText("-");
                else
                    nesne12Dayaniklilik.setText(String.format("%,.3f",bilgisayar.nesneListesi[0].dayaniklilik));

                if (bilgisayar.nesneListesi[1] == null)
                    nesne22Dayaniklilik.setText("-");
                else
                    nesne22Dayaniklilik.setText(String.format("%,.3f",bilgisayar.nesneListesi[1].dayaniklilik));

                if (bilgisayar.nesneListesi[2] == null)
                    nesne32Dayaniklilik.setText("-");
                else
                    nesne32Dayaniklilik.setText(String.format("%,.3f",bilgisayar.nesneListesi[2].dayaniklilik));

                if (bilgisayar.nesneListesi[3] == null)
                    nesne42Dayaniklilik.setText("-");
                else
                    nesne42Dayaniklilik.setText(String.format("%,.3f",bilgisayar.nesneListesi[3].dayaniklilik));

                if (bilgisayar.nesneListesi[4] == null)
                    nesne52Dayaniklilik.setText("-");
                else
                    nesne52Dayaniklilik.setText(String.format("%,.3f",bilgisayar.nesneListesi[4].dayaniklilik));


                if (bilgisayar.nesneListesi[0] == null)
                    nesne12SeviyePuani.setText("-");
                else
                    nesne12SeviyePuani.setText(String.format("%,.1f",bilgisayar.nesneListesi[0].seviyePuani));

                if (bilgisayar.nesneListesi[1] == null)
                    nesne22SeviyePuani.setText("-");
                else
                    nesne22SeviyePuani.setText(String.format("%,.1f",bilgisayar.nesneListesi[1].seviyePuani));

                if (bilgisayar.nesneListesi[2] == null)
                    nesne32SeviyePuani.setText("-");
                else
                    nesne32SeviyePuani.setText(String.format("%,.1f",bilgisayar.nesneListesi[2].seviyePuani));

                if (bilgisayar.nesneListesi[3] == null)
                    nesne42SeviyePuani.setText("-");
                else
                    nesne42SeviyePuani.setText(String.format("%,.1f",bilgisayar.nesneListesi[3].seviyePuani));

                if (bilgisayar.nesneListesi[4] == null)
                    nesne52SeviyePuani.setText("-");
                else
                    nesne52SeviyePuani.setText(String.format("%,.1f",bilgisayar.nesneListesi[4].seviyePuani));

                // Sonuç ekranını aç.
                Arayuz3Sonuc sonuc = new Arayuz3Sonuc(kullanici, bilgisayar);     
            }
                     
            round_sayac++;    
        }
    }
    
}
