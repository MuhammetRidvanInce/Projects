
import java.awt.Color;
import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JTextArea;


public class Arayuz3Sonuc {

    Oyuncu oyuncu1, oyuncu2;
    
    public Arayuz3Sonuc(Oyuncu oyuncu1, Oyuncu oyuncu2) {
        this.oyuncu1 = oyuncu1;
        this.oyuncu2 = oyuncu2;

        JFrame frame = new JFrame();
        JTextArea text = new JTextArea();
        
        
        text.setBounds(0, 0, 350,250);
        frame.add(text);
        
        if (oyuncu1.skorGoster() > oyuncu2.skorGoster())
            text.setText("OYUN BİTTİ!\nKazanan: " + oyuncu1.OyuncuAdi + " " + oyuncu1.oyuncuID + "\nSkor: " + String.format("%,.3f", oyuncu1.skorGoster()));
        else if(oyuncu1.skorGoster() < oyuncu2.skorGoster())
            text.setText("OYUN BİTTİ!\nKazanan: " + oyuncu2.OyuncuAdi + " " + oyuncu2.oyuncuID + "\nSkor: " + String.format("%,.3f", oyuncu2.skorGoster()));
        else
            text.setText("OYUN BERABERE BİTTİ!\nSkorlar: " + String.format("%,.3f", oyuncu1.skorGoster()) + " / " + String.format("%,.3f", oyuncu2.skorGoster()));
        
        text.setFont(new Font("SansSerif", Font.BOLD, 16));
        
        

        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(350, 250);
        frame.getContentPane().setBackground(new Color(100, 150, 200));
        frame.setLayout(null);
        frame.setVisible(true); 
  
    }
  
}
