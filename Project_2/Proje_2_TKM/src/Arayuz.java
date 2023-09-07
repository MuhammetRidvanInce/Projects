
import java.awt.Color;
import java.awt.Font;
import static java.awt.PageAttributes.ColorType.COLOR;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.Border;

public class Arayuz implements ActionListener {
    
    JTextField dayanikliliktxt, katiliktxt, nufuztxt, keskinliktxt, sicakliktxt, kalinliktxt, direnctxt,
            beta1txt, beta2txt, alphatxt, roundtxt, seviyePuanitxt;
    
    JTextArea message;
    
    JButton B2B, K2B;
    
    JFrame frame;
    Oyuncu oyuncu1;
    Oyuncu oyuncu2;
    
    Oyuncu kullanici;
    Oyuncu bilgisayar;
 
    
    Arayuz(){

        
        frame = new JFrame();

        
        Border border1 = BorderFactory.createLineBorder(Color.black);
        JPanel panel1 = new JPanel(); 
        panel1.setBounds(25,50,240,470); 
        panel1.setBackground(Color.gray);
        panel1.setBorder(border1);
        panel1.setLayout(null);
        frame.add(panel1);
        
        JLabel baslik = new JLabel("OYUN PARAMETRELERİ");
        baslik.setBounds(10, 15, 300, 25);
        baslik.setFont(new Font("DialogInput", Font.BOLD, 25));
        frame.add(baslik); 
        
        JLabel dayaniklilik = new JLabel("Dayaniklilik");
        dayaniklilik.setBounds(5, 5, 135, 25);
        dayaniklilik.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(dayaniklilik); 
        
        JLabel seviyePuani = new JLabel("Seviye Puanı");
        seviyePuani.setBounds(5, 35, 135, 25);
        seviyePuani.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(seviyePuani); 

        
        JLabel katilik = new JLabel("Katılık");
        katilik.setBounds(5, 100, 135, 25);
        katilik.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(katilik); 
 
        JLabel nufuz = new JLabel("Nüfuz");
        nufuz.setBounds(5, 130, 135, 25);
        nufuz.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(nufuz); 

        JLabel keskinlik = new JLabel("Keskinlik");
        keskinlik.setBounds(5, 160, 135, 25);
        keskinlik.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(keskinlik); 

        JLabel sicaklik = new JLabel("Sıcaklık");
        sicaklik.setBounds(5, 210, 135, 25);
        sicaklik.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(sicaklik); 
        
        JLabel kalinlik = new JLabel("Kalınlık");
        kalinlik.setBounds(5, 240, 135, 25);
        kalinlik.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(kalinlik); 

        JLabel direnc = new JLabel("Direnç");
        direnc.setBounds(5, 270, 135, 25);
        direnc.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(direnc);

        JLabel alpha = new JLabel("alpha");
        alpha.setBounds(5, 320, 135, 25);
        alpha.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(alpha); 
        
        JLabel beta1 = new JLabel("Beta1");
        beta1.setBounds(5, 350, 135, 25);
        beta1.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(beta1); 

        JLabel beta2 = new JLabel("Beta2");
        beta2.setBounds(5, 380, 135, 25);
        beta2.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(beta2);
        
        JLabel roundlabel = new JLabel("ROUND SAYISI");
        roundlabel.setBounds(5, 420, 135, 25);
        roundlabel.setFont(new Font("DialogInput", Font.BOLD, 18));
        panel1.add(roundlabel);
        

        dayanikliliktxt = new JTextField("20");
        dayanikliliktxt.setBounds(150,5,50,25);
        dayanikliliktxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        dayanikliliktxt.setHorizontalAlignment(0);
        dayanikliliktxt.setBackground(Color.white);
        dayanikliliktxt.setBorder(border1);
        dayanikliliktxt.setVisible(true);       
        panel1.add(dayanikliliktxt);
        
        
        seviyePuanitxt = new JTextField("30");
        seviyePuanitxt.setBounds(150,35,50,25);
        seviyePuanitxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        seviyePuanitxt.setHorizontalAlignment(0);
        seviyePuanitxt.setBackground(Color.white);
        seviyePuanitxt.setBorder(border1);
        seviyePuanitxt.setVisible(true);
        panel1.add(seviyePuanitxt);
        
        katiliktxt = new JTextField("2");
        katiliktxt.setBounds(150,100,50,25);
        katiliktxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        katiliktxt.setHorizontalAlignment(0);
        katiliktxt.setBackground(Color.white);
        katiliktxt.setBorder(border1);
        katiliktxt.setVisible(true);
        panel1.add(katiliktxt);
        
        
        nufuztxt = new JTextField("2");
        nufuztxt.setBounds(150,130,50,25);
        nufuztxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        nufuztxt.setHorizontalAlignment(0);
        nufuztxt.setBackground(Color.white);
        nufuztxt.setBorder(border1);
        nufuztxt.setVisible(true);
        panel1.add(nufuztxt);
        
        keskinliktxt = new JTextField("2");
        keskinliktxt.setBounds(150,160,50,25);
        keskinliktxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        keskinliktxt.setHorizontalAlignment(0);
        keskinliktxt.setBackground(Color.white);
        keskinliktxt.setBorder(border1);
        keskinliktxt.setVisible(true);
        panel1.add(keskinliktxt);
        
        
        sicakliktxt = new JTextField("2");
        sicakliktxt.setBounds(150,210,50,25);
        sicakliktxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        sicakliktxt.setHorizontalAlignment(0);
        sicakliktxt.setBackground(Color.white);
        sicakliktxt.setBorder(border1);
        sicakliktxt.setVisible(true);
        panel1.add(sicakliktxt);
        
        kalinliktxt = new JTextField("2");
        kalinliktxt.setBounds(150,240,50,25);
        kalinliktxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        kalinliktxt.setHorizontalAlignment(0);
        kalinliktxt.setBackground(Color.white);
        kalinliktxt.setBorder(border1);
        kalinliktxt.setVisible(true);
        panel1.add(kalinliktxt);
        
        
        direnctxt = new JTextField("2");
        direnctxt.setBounds(150,270,50,25);
        direnctxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        direnctxt.setHorizontalAlignment(0);
        direnctxt.setBackground(Color.white);
        direnctxt.setBorder(border1);
        direnctxt.setVisible(true);
        panel1.add(direnctxt);
        
        
        alphatxt = new JTextField("0.2");
        alphatxt.setBounds(150,320,50,25);
        alphatxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        alphatxt.setHorizontalAlignment(0);
        alphatxt.setBackground(Color.white);
        alphatxt.setBorder(border1);
        alphatxt.setVisible(true);
        panel1.add(alphatxt);
        
        
        beta1txt = new JTextField("3.125");
        beta1txt.setBounds(150,350,50,25);
        beta1txt.setFont(new Font("SansSerif", Font.BOLD, 18));
        beta1txt.setHorizontalAlignment(0);
        beta1txt.setBackground(Color.white);
        beta1txt.setBorder(border1);
        beta1txt.setVisible(true);
        panel1.add(beta1txt);
        
        beta2txt = new JTextField("5");
        beta2txt.setBounds(150,380,50,25);
        beta2txt.setFont(new Font("SansSerif", Font.BOLD, 18));
        beta2txt.setHorizontalAlignment(0);
        beta2txt.setBackground(Color.white);
        beta2txt.setBorder(border1);
        beta2txt.setVisible(true);
        panel1.add(beta2txt);
        
        roundtxt = new JTextField("10");
        roundtxt.setBounds(150,420,50,25);
        roundtxt.setFont(new Font("SansSerif", Font.BOLD, 20));
        roundtxt.setHorizontalAlignment(0);
        roundtxt.setBackground(Color.white);
        roundtxt.setBorder(border1);
        roundtxt.setVisible(true);
        panel1.add(roundtxt);
        
        B2B = new JButton("B2B Oyun Başlat");
        B2B.setBounds(285, 50, 175, 45);
        B2B.addActionListener(this);
        B2B.setFont(new Font("SansSerif", Font.BOLD, 16));
        frame.add(B2B);

        
        K2B = new JButton("K2B Oyun Başlat");
        K2B.setBounds(285, 100, 175, 45);
        K2B.addActionListener(this);
        K2B.setFont(new Font("SansSerif", Font.BOLD, 16));
        frame.add(K2B);
        
        
        message = new JTextArea();
        
        message.setBounds(285, 160, 175,360);
        message.setFont(new Font("Serif", Font.BOLD, 15));
        message.setBackground(Color.black);
        message.setText("Oyun parametreleri\nsol panelden\ndeğiştirilebilir.\n"+
                "\nSeviye Puanı: Bir\nnesnenin terfi edeceği\npuan barajını\ngöstermektedir\n"+
                "\nBeta1: İki aynı nesne\nkarşılaşırsa karşılıklı\ndüşecek puan.\n"+
                "\nBeta2: Biri terfi\netmis diğeri etmemis\niki aynı nesne karşılaşırsa\nterfi etmeyenden\ndüşecek puan.");
        message.setEnabled(false);
        frame.add(message);


        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 570);
        frame.setLayout(null);
        frame.setVisible(true); 
        frame.setResizable(false);

      
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        
        if(e.getSource()==B2B)
        {

            oyuncu1 = new Bilgisayar(1, "Bilgisayar",0);
            parametreGuncelle(oyuncu1.nesneler);
            oyuncu1.nesneListesiOlustur();

            oyuncu2 = new Bilgisayar(2, "Bilgisayar",0);
            parametreGuncelle(oyuncu2.nesneler);
            oyuncu2.nesneListesiOlustur();
            int round = Integer.parseInt(roundtxt.getText()); 
            int barajPuan = Integer.parseInt(seviyePuanitxt.getText());


            Arayuz1B2B b2b = new Arayuz1B2B(oyuncu1, oyuncu2, round, frame, barajPuan);
            frame.setVisible(false);
        }
        
        else if(e.getSource()==K2B)
            
        {
            
            kullanici = new Kullanici(1, "Kullanıcı", 0);
            parametreGuncelle(kullanici.nesneler);
            // Kullanıcı nesne listesi manuel oluşturuluyor...

            bilgisayar = new Bilgisayar(1, "Bilgisayar", 0);
            parametreGuncelle(bilgisayar.nesneler);
            bilgisayar.nesneListesiOlustur();
            
            int round = Integer.parseInt(roundtxt.getText());
            int barajPuan = Integer.parseInt(seviyePuanitxt.getText());
            Arayuz2NesneSec nesnesec = new Arayuz2NesneSec(kullanici, bilgisayar, round, frame, barajPuan);
            frame.setVisible(false);
  
        }

    }

    public void parametreGuncelle(Nesne[] tumNesneler)
    {
        
        for (Nesne nesne : tumNesneler) {
            
            nesne.dayaniklilik = Double.parseDouble(dayanikliliktxt.getText());
            nesne.alpha = Double.parseDouble(alphatxt.getText());
            nesne.beta1 = Double.parseDouble(beta1txt.getText());
            nesne.beta2 = Double.parseDouble(beta2txt.getText());
            
            String name = nesne.getClass().getName();
            
            if (("Tas".equals(name)) || ("AgirTas".equals(name)) )
                nesne.setKatilik(Double.parseDouble(katiliktxt.getText()));
            else if (("Kagit".equals(name)) || ("OzelKagit".equals(name)))
                nesne.nufuz = Double.parseDouble(nufuztxt.getText());
            else if (("Makas".equals(name)) || ("UstaMakas".equals(name)))
                nesne.keskinlik = Double.parseDouble(keskinliktxt.getText());
            
            if ("AgirTas".equals(name))
                nesne.sicaklik = Double.parseDouble(sicakliktxt.getText());
            else if ("OzelKagit".equals(name))
                nesne.kalinlik = Double.parseDouble(kalinliktxt.getText());            
            else if ("UstaMakas".equals(name))
                nesne.direnc = Double.parseDouble(direnctxt.getText());  

        }
  
    }
   
}
