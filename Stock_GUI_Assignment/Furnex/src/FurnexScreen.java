import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class FurnexScreen extends JFrame implements ActionListener {
	
	private JButton Buy,Close;
	private JPanel mainPanel;
	private ArrayList<Furniture> allFurniture;
	private JTextField First  = new JTextField("0"),Second = new JTextField("0"),Third = new JTextField("0"),Fourth = new JTextField("0");
	private JLabel StockOne = new JLabel(), StockTwo = new JLabel(), StockThree = new JLabel() ,StockFour = new JLabel();
	
	private static final long serialVersionUID = 4271666945216738362L; //required in eclipse for jframe classes
	FurnexScreen(ArrayList<Furniture> allFurniture ){
		this.allFurniture = allFurniture;
		mainPanel = new JPanel();
		mainPanel.setLayout(new BoxLayout(mainPanel,BoxLayout.Y_AXIS));
		Buy = new JButton("Buy");
		Close = new JButton("Close");
		JPanel Welcome = new JPanel();
		Welcome.setMaximumSize( new Dimension(700, 100) );
		Welcome.setAlignmentX(Component.LEFT_ALIGNMENT);
		JLabel topLabel = new JLabel("STOCK");
		topLabel.setPreferredSize(new Dimension(200,50));
		topLabel.setFont(topLabel.getFont().deriveFont(30.0f));
		topLabel.setForeground(Color.CYAN);
		JLabel Empty = new JLabel();
		Empty.setPreferredSize(new Dimension(110,50));
		Welcome.add(Empty);
		Welcome.add(topLabel);
		Welcome.setBackground(Color.black);
		mainPanel.add(Welcome);
		//we loop over the furniture and put them into an organized grid but with resized demensions which is why we use gridlayoutbag
		for(int i =0; i<allFurniture.size();i++) {
			JPanel currPanel = new JPanel(new FlowLayout());
			JLabel imageLabel= new JLabel();
			imageLabel.setIcon(new ImageIcon(allFurniture.get(i).getImageSource()));
			imageLabel.setPreferredSize(new Dimension(200, 128));
			currPanel.add(imageLabel);
			JLabel Title = new JLabel(allFurniture.get(i).getTitle());
			Title.setPreferredSize(new Dimension(100, 128));
			currPanel.add(Title);
			JLabel Price = new JLabel("$" + allFurniture.get(i).getPrice());
			Price.setPreferredSize(new Dimension(100, 128));
			currPanel.add(Price);
			switch(i) {
			case 0:
				StockOne.setText("Current Stock: " + Integer.toString(allFurniture.get(i).getStock()));
				StockOne.setPreferredSize(new Dimension(200, 128));
				currPanel.add(StockOne);
				First.setPreferredSize(new Dimension(70, 30));
				currPanel.add(First);
				break;
			case 1:
				StockTwo.setText("Current Stock: " + Integer.toString(allFurniture.get(i).getStock()));
				StockTwo.setPreferredSize(new Dimension(200, 128));
				currPanel.add(StockTwo);
				Second.setPreferredSize(new Dimension(70, 30));
				currPanel.add(Second);
				break;
			case 2:
				StockThree.setText("Current Stock: " + Integer.toString(allFurniture.get(i).getStock()));
				StockThree.setPreferredSize(new Dimension(200, 128));
				currPanel.add(StockThree);
				Third.setPreferredSize(new Dimension(70, 30));
				currPanel.add(Third);
				break;
			case 3:
				StockFour.setText("Current Stock: " + Integer.toString(allFurniture.get(i).getStock()));
				StockFour.setPreferredSize(new Dimension(200, 128));
				currPanel.add(StockFour);
				Fourth.setPreferredSize(new Dimension(70, 30));
				currPanel.add(Fourth);
				break;
			}
			currPanel.setMaximumSize( new Dimension(700, 200) );
			currPanel.setAlignmentX(Component.LEFT_ALIGNMENT);
			currPanel.setBackground(Color.gray);
			mainPanel.add(currPanel);
		}
		Buy.addActionListener(this);
		Close.addActionListener(this);
		JPanel bigEmpty = new JPanel(new FlowLayout());
		bigEmpty.setMaximumSize( new Dimension(700, 200) );
		bigEmpty.setAlignmentX(Component.LEFT_ALIGNMENT);
		JLabel empty = new JLabel();
		empty.setPreferredSize(new Dimension(610, 0));
		Buy.setPreferredSize(new Dimension(70, 30));
		bigEmpty.add(empty);
		bigEmpty.add(Buy);
		mainPanel.add(bigEmpty);
		mainPanel.setBackground(Color.gray);
		add(mainPanel);
		//Down here we're also going to make sure that the stock is written to file even if the user closes the window rather than pressing "Close" button
		addWindowListener(new WindowAdapter() {
			  public void windowClosing(WindowEvent e) {
			    try {
					reWriteStock();
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
			  }
			});
		
	}
	
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == Buy) {
			int count =0; //counts how many blank values the user inputted
			JPanel cartFrame = new JPanel(new GridLayout(0,3)); //set to 3 columns and rows will incriment depending on how many the user inputed
			cartFrame.add(new JLabel("Item"));
			cartFrame.add(new JLabel("Amount"));
			cartFrame.add(new JLabel("Total Price"));
			for(int i =0; i<allFurniture.size();i++) {
				String current = "";
				switch(i) {
				//decide which text box the user effected
				case 0:
					current = First.getText();
					break;
				case 1:
					current = Second.getText();
					break;
				case 2:
					current = Third.getText();
					break;
				case 3:
					current = Fourth.getText();
					break;
				}
				if (!current.equals("") && !current.equals("0")) {//first we check if its blank if its not we check the number
					if(Double.parseDouble(current) > allFurniture.get(i).getStock()) {
						JOptionPane.showMessageDialog(null, "You Tried to Buy More Stock than we currently have!");
						Reset(); //make all labels blank
						return; //return so we dont display the cart
					}
					if(Double.parseDouble(current) < 0) {
						JOptionPane.showMessageDialog(null, "We Don't Take in Items, We Only Sell Them!");
						Reset(); //make all labels blank
						return; //return so we dont display the cart
					}
					cartFrame.add(new JLabel(allFurniture.get(i).getTitle()));
					cartFrame.add(new JLabel(current));
					try{
						double price = Double.parseDouble(current)* allFurniture.get(i).getPrice();
						cartFrame.add(new JLabel(String.valueOf(price)));
					}
					catch(Exception ex){
						JOptionPane.showMessageDialog(null, "Please Enter valid numbers!");
						Reset(); //make all labels blank
						return; //return so we dont display the cart
					}
				}
				else {
					count++;
				}
				
			}
			
			if(count == allFurniture.size()) { //if the count = the size then we know the user didnt enter anything
				JOptionPane.showMessageDialog(null, "You didn't Purchase Anything!");
				return;
			}
			int choice = JOptionPane.showConfirmDialog(null,cartFrame,"Are you sure you want to purchase" ,JOptionPane.OK_CANCEL_OPTION); //if choice = 0 then yes was pressed if choice = 1 then cancel was pressed
			if(choice ==0) {
				for(int i =0; i<allFurniture.size();i++) {
					String current = "";
					switch(i) {
					case 0:
						current = First.getText();
						if(!current.equals("")) {
							StockOne.setText("Current Stock: " + String.valueOf(allFurniture.get(i).getStock()- Integer.parseInt(current)));
						}
						break;
					case 1:
						current = Second.getText();
						if(!current.equals("")) {
							StockTwo.setText("Current Stock: " + String.valueOf(allFurniture.get(i).getStock()- Integer.parseInt(current)));
						}
						break;
					case 2:
						current = Third.getText();
						if(!current.equals("")) {
							StockThree.setText("Current Stock: " + String.valueOf(allFurniture.get(i).getStock()- Integer.parseInt(current)));
						}
						break;
					case 3:
						current = Fourth.getText();
						if(!current.equals("")) {
							StockFour.setText("Current Stock: " + String.valueOf(allFurniture.get(i).getStock()- Integer.parseInt(current)));
						}
						break;
					}
					if(!current.equals("")) {
						allFurniture.get(i).setStock(allFurniture.get(i).getStock()- Integer.parseInt(current)); //set furniture stock to previous - user input
					}
					
				}
				
			}
			Reset(); //make all labels blank
		}
		
		if(e.getSource() == Close) {
			setVisible(false);
			this.dispose();
			try {
				reWriteStock();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
	}
	private void Reset() {
		First.setText("0");
		Second.setText("0");
		Third.setText("0");
		Fourth.setText("0");
	}
	//we will reWrite to the csv file after the user closes whether that be by pressing x or clicking close
	private void reWriteStock() throws IOException{
		BufferedWriter wr = new BufferedWriter(new FileWriter("Stock.csv"));
		for(int i =0; i<allFurniture.size();i++){
			wr.write(allFurniture.get(i).getTitle() + "," + String.valueOf(allFurniture.get(i).getStock())+ "," + String.valueOf(allFurniture.get(i).getPrice())+ ","+ allFurniture.get(i).getImageSource()+"\n");
		}
		wr.close();
	}
	

}
