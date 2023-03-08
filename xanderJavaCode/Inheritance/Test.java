public class Test{
	public static void main(String[] args){
		// Shape shape1 = new Shape();
		// Shape shape2 = new Shape(3,5);
		// Circle circle1 = new Circle();
		// Circle circle2 = new Circle(5,6,7);
		
		// System.out.println(shape1.toString());
		// System.out.println(shape2);
		// System.out.println(circle1+" and "+circle2);
		
		// shape1.moveTo(10,11);
		// System.out.println(shape1);
		
		// circle2.moveTo(20,21);
		// System.out.println(circle2);
		
		// Rectangle myRectangle = new Rectangle(0,0,2,3);
		// System.out.println(myRectangle);
		
		// Circle c = new Circle(10,20,5);
		// Rectangle r = new Rectangle(0,0,1,1);
		// System.out.println(r.isLeftOf(c));
		
		// Shape s;
		// Rectangle r2;
		// r2 = new Rectangle(0,0,1,1);
		// s = new Rectangle(0,0,2,2);
		// System.out.println(r2+" and "+s);
		
		Rectangle r3 = new Rectangle(0,0,5,10);
		Circle c2 = new Circle(0,0,1);
		System.out.println(r3.compareTo(c2));
	}
}