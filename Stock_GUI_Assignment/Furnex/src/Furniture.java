public class Furniture {
	private String title;
	private int stock;
	private String imageSource;
	private double price;
	Furniture(String title, int stock, double price, String imageSource){
		this.title = title;
		this.stock = stock;
		this.price = price;
		this.imageSource = imageSource;
		
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public int getStock() {
		return stock;
	}
	public void setStock(int stock) {
		this.stock = stock;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public String getImageSource() {
		return imageSource;
	}
	public void setImageSource(String imageSource) {
		this.imageSource = imageSource;
	}
	
}
