public class Members {
	private String username;
	private String password;
	
	public Members(String user, String pass) {
		username = user;
		password = pass;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
}
