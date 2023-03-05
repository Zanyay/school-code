public class Test{
	public static void main(String[] args){
		Counter counter = new Counter();
		System.out.println("value = " + counter.getValue());
		
		for(int i=0; i<5; i++){
			counter.incr();
			System.out.println("value after increment = " + counter.getValue());
		}
	}
}