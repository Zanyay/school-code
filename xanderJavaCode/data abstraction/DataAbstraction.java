public class DataAbstraction{
	
	public static void main(String[] args){
		Point point;
		point = new Point();
		
		point.x = 1;
		point.y = 1;
		
		System.out.println(point.sumCoordinates());
	}
}