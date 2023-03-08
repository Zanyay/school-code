public abstract class Shape{
	
	protected double x;
	protected double y;
	
	public Shape(){
		this.x = 0;
		this.y = 0;
	}
	
	public Shape(double x, double y){
		this.x = x;
		this.y = y;
	}
	
	final double getX(){
		return this.x;
	}
	
	final double getY(){
		return this.y;
	}
	
	final void moveTo(double x, double y){
		this.x = x;
		this.y = y;
	}
	
	public void overrideMePlease(){
		
	}
	
	public String toString(){
		return "located at: ("+this.x+","+this.y+")";
	}
	
	public boolean isLeftOf(Shape s){
		return this.getX() < s.getX();
	}
	
	public abstract double area();
	
	public int compareTo(Shape other){
		if (area() < other.area()){
			return -1;
		}
		else if (area() == other.area()){
			return 0;
		}
		else{
			return 1;
		}
	}
	
	// public static void main(String[] args){
		// Shape s = new Shape(1.0,2.0);
		// System.out.print("the overrideMePlease method of the superclass Shape prints... ");
		// s.overrideMePlease();
		// Circle c = new Circle();
		// System.out.print("the overrideMePlease method of the subclass Shape prints... ");
		// c.overrideMePlease();
	// }
}