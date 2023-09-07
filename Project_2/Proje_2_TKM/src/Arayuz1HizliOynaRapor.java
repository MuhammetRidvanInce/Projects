import java.awt.FlowLayout;
import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class Arayuz1HizliOynaRapor extends JFrame{
    
    final private JFrame f; 
    final private JTextArea ta; 
    final private JScrollPane sbrText; 
    String txt;
    
    public Arayuz1HizliOynaRapor(String txt)
    { 
        
        f = new JFrame("HIZLI OYNAT RAPOR");
	f.getContentPane().setLayout(new FlowLayout());
        ta = new JTextArea(txt, 25, 20);
        ta.setFont(new Font("Serif", Font.BOLD, 15));
        
	ta.setLineWrap(true);
	sbrText = new JScrollPane(ta);
	sbrText.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

        f.getContentPane().add(sbrText);
        f.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        f.pack();
        f.setVisible(true);
    }
    
}
