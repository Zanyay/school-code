public class TestConstructor{
	public static void main(String[] args){
		Time t1;
		t1= new Time(16,37,25);
		t1.hours == 16;
		t1.minutes == 37;
		t1.seconds == 25;
		
		Time t2;
		t2= new Time(16,37,25);
		t2.hours == 16;
		t2.minutes == 37;
		t2.seconds == 25;
	}
}