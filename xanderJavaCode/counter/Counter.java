public class Counter{
	private int value = 0;
	
	public int getValue(){
		return value;
	}
	
	public void incr(){
		value++;
	}
	
	public void reset(){
		value = 0;
	}
}