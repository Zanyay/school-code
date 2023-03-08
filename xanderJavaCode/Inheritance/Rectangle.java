public class Rectangle extends Shape{
	private double width;
	private double height;
	
	public Rectangle(){
		super();
		this.width = 0;
		this.height = 0;
	}
	
	public Rectangle(double x, double y, double width, double height){
		super(x,y);
		this.width = width;
		this.height = height;
	}
	
	public double getWidth(){
		return this.width;
	}
	
	public double getHeight(){
		return this.height;
	}
	
	public void flip(){
		double tmp = width;
		this.width = this.height;
		this.height = tmp;
	}
	
	public String toString(){
		return "Located at: ("+x+","+y+"), width "+this.width+" and length "+this.height;
	}
	
	public double area(){
		return this.width * this.height;
	}
}