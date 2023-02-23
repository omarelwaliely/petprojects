import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException{
		ArrayList<Members> Team = new ArrayList<Members>();
		ArrayList<Furniture> allFurniture = new ArrayList<Furniture>();
		createMembers(Team);
		createStock(allFurniture);
		LoginScreen Start = new LoginScreen(Team,allFurniture); 
		Start.setSize(800,100);
		Start.setLocationRelativeTo(null);
		Start.setVisible(true);
		
	}
	public static void createMembers(ArrayList <Members> allMembers) throws IOException{
		BufferedReader br = new BufferedReader(new FileReader("Members.csv"));
		String line = "";
		while((line = br.readLine())!= null) {
			String [] sentence = line.split(",");
			Members curr = new Members(sentence[0].toLowerCase(),sentence[1]);
			allMembers.add(curr);
		}
		br.close();
	}
	public static void createStock(ArrayList<Furniture> Items)throws IOException{
		BufferedReader br = new BufferedReader(new FileReader("Stock.csv"));
		String line = "";
		while((line = br.readLine())!= null) {
			String [] currSentence = line.split(",");
			try {
				Furniture currItem = new Furniture(currSentence[0], Integer.parseInt(currSentence[1]), Double.parseDouble(currSentence[2]),currSentence[3]);
				Items.add(currItem);
			}
			catch(Exception e) {
				System.out.printf("%s has an error please fix this line in your database and run the program again!",line);
				System.exit(0);
			}
		}
		br.close();
	}

}
