
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;


public class Arayuz2NesneSec implements ActionListener {

    JFrame frame;
    JCheckBox[] cblist = new JCheckBox[]{new JCheckBox(), new JCheckBox(),new JCheckBox(),new JCheckBox(),new JCheckBox(),
                                         new JCheckBox(),new JCheckBox(),new JCheckBox(),new JCheckBox(),new JCheckBox(),
                                         new JCheckBox(),new JCheckBox(),new JCheckBox(),new JCheckBox(),new JCheckBox()};
    
    JLabel label1, textuyari;
    JButton tasdik;
    JButton kontrol;
    
    
    Oyuncu kullanici;
    Oyuncu bilgisayar;
    int round;
    int barajPuani;
    
    JFrame anaekran;
    
    
    public Arayuz2NesneSec(Oyuncu kullanici, Oyuncu bilgisayar, int round, JFrame anaekran, int barajPuani){
        
    this.kullanici = kullanici;
    this.bilgisayar = bilgisayar;
    this.anaekran = anaekran;
    this.round = round;
    this.barajPuani = barajPuani;
        
    frame = new JFrame();
    
    label1 = new JLabel("Lütfen 5 adet nesne seçiniz ve Kontrol Et butonuna tıklayınız!");
    label1.setFont(new Font("SansSerif", Font.BOLD | Font.ITALIC, 18));
    label1.setBounds(50, 10, 550,30);
    frame.add(label1);
    
    textuyari = new JLabel();
    textuyari.setFont(new Font("SansSerif", Font.BOLD | Font.ITALIC, 15));
    textuyari.setBounds(210, 360, 400,30);
    frame.add(textuyari);

    tasdik = new JButton("TAMAM");
    tasdik.setBounds(475, 150, 125, 155);
    tasdik.setFont(new Font("SansSerif", Font.BOLD | Font.ITALIC, 20));
    tasdik.addActionListener(this);
    tasdik.setEnabled(false);
    frame.add(tasdik);
    
    kontrol = new JButton("Kontrol Et");
    kontrol.setBounds(50, 350, 150, 50);
    kontrol.setFont(new Font("SansSerif", Font.BOLD | Font.ITALIC, 15));
    kontrol.addActionListener(this);
    frame.add(kontrol);


    int x = 50;
    int y = 60;
    
    for (int i = 0; i < 15; i++)
    {
        if ((i != 0) & (i %5 == 0))
        {
            x +=150;
            y = 60;
        }
        
        cblist[i].setText(kullanici.nesneler[i].getClass().getName() + "_" + kullanici.nesneler[i].id);
        cblist[i].setBounds(x, y, 100, 45);
        cblist[i].setFont(new Font("SansSerif", Font.BOLD, 16));

        y+=50;
        frame.add(cblist[i]);   
    }

    frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
    frame.setSize(650, 450);
    frame.getContentPane().setBackground(new Color(100, 150, 200));
    frame.setLayout(null);
    frame.setVisible(true);
    frame.setResizable(false);
    frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                anaekran.setVisible(true);
            }
        });

    }

    @Override
    public void actionPerformed(ActionEvent e) {
   
    if (e.getSource() == kontrol)   
    {
    
        int toplam = 0;    
        for (int i = 0; i < 15; i++)
            {
                if (cblist[i].isSelected())
                    toplam++;
            }

        if (toplam == 5)
            {
                textuyari.setText("NESNE SEÇİMİ ONAYLANDI!!");
                tasdik.setEnabled(true); 
            }

        else if(toplam < 5)
                textuyari.setText("İLAVE " + (5-toplam) + " ADET NESNE SEÇİNİZ!!");
        else if (toplam > 5)
                textuyari.setText("SEÇİMLERDEN " + (toplam - 5) + " ADET NESNE ÇIKARINIZ!!");
   
    }
    else if (e.getSource() == tasdik)
    {
        int indis = 0;
        for (int i = 0; i < 15; i++)
            {
                if (cblist[i].isSelected())
                    kullanici.nesneListesi[indis++] = kullanici.nesneler[Integer.parseInt(cblist[i].getText().replaceAll("[^0-9]", ""))];     
            }

        Arayuz2K2B A = new Arayuz2K2B(kullanici, bilgisayar, round, anaekran, barajPuani);
        frame.dispose();

    }

    }
     
}
