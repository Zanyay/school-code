import java.lang.Math.*;

public class Circle extends Shape{
	
	private double radius;
	
	public Circle(){
		super();
		radius = 0;
	}
	public Circle(double x, double y, double radius){
		super(x,y);
		this.radius = radius;
	}
	
	public void overrideMePlease(){
		System.out.println("i am overriding you dawg!");
	}
	
	public double getRadius(){
		return this.radius;
	}
	
	public String toString(){
		return "located at: ("+x+","+y+"), with radius: "+radius;
	}
	
	public double area(){
		return Math.PI * this.radius * this.radius;
	}
}