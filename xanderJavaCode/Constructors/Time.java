public class Time{
	//...
	
	public String toString(){
		return this.getHours() + ":" + this.getMinutes() + ":" + this.getMinutes();
	}
}

//somewhere in main

Time t = new Time(1,2,3);
System.out.println(t.toString());

 //1:2:3