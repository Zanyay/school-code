public class Ticket{
	private static int lastSerialNumber = 0;
	private int serialNumber;
	
	public Ticket(){
		serialNumber = lastSerialNumber;
		lastSerialNumber++;
	}
	public int getSerialNumber(){
		return serialNumber;
	}
}