import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class LoginScreen extends JFrame implements ActionListener{
	
	private static final long serialVersionUID = -2839718921768169525L; //we have to generate this in eclipse from what I can see
	
	private JLabel UsernameLabel, PassLabel;
	private JTextField UserInput;
	private JPasswordField PassInput;
	private JButton Submit,Close;
	private JPanel Panel;
	private ArrayList<Members> allMembers;
	private ArrayList<Furniture> allFurniture;
	LoginScreen(ArrayList<Members> all,ArrayList<Furniture> allFurniture){
		allMembers = all;
		this.allFurniture = allFurniture;
		UsernameLabel = new JLabel();
		UsernameLabel.setText("Username: "); //creating a text that says "Username: " so user knows where to put username
		PassLabel = new JLabel();
		PassLabel.setText("Password: "); //creating a text that says "Password: " so user knows where to put Password
		UserInput = new JTextField(30); //setting max username length to 30
		PassInput = new JPasswordField(30); //setting max password length to 30
		Submit = new JButton("Submit"); //creating button to submit the informaton and validate
		Close = new JButton("Close"); //You can close by pressing "x" but this looks cleaner
		Panel = new JPanel(new GridLayout(3,2)); //create a panel with 3 rows and 2 column
		Panel.add(UsernameLabel);
		Panel.add(UserInput);
		Panel.add(PassLabel);
		Panel.add(PassInput);
		Panel.add(Close);
		Panel.add(Submit);
		setTitle("Furnex Sign-In");
		add(Panel,BorderLayout.CENTER);
		Submit.addActionListener(this);
		Close.addActionListener(this);
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == Close) {
			setVisible(false);
			dispose();
		}
		else if(e.getSource() == Submit) {
			String UsernameInputted = UserInput.getText();
			String PasswordInputted = String.valueOf(PassInput.getPassword());
			for (int i =0; i<allMembers.size();i++) {
				if(allMembers.get(i).getUsername().toLowerCase().equals(UsernameInputted.toLowerCase())) {
					if(!(allMembers.get(i).getPassword().equals(PasswordInputted))) {
						JOptionPane.showMessageDialog(Panel,"The Password is Incorrect!");//The username was found but the password was incorrect
						return;
					} 
					else {
						setVisible(false);
						dispose();
						FurnexScreen Furnex = new FurnexScreen(allFurniture);
						Furnex.setSize(710,700);
						Furnex.setLocationRelativeTo(null);
						Furnex.setVisible(true);
						return;
					}
				}
			}
			JOptionPane.showMessageDialog(Panel,"Username Does Not Exist!"); //if we loop through the whole array and dont find the username then its not in our database
		}
		
	}
}
