import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
     
    public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        
		double r = Double.parseDouble(in.readLine());
        double x = r * r * 3.14159;
                
        System.out.printf("A=%.4f\n", x);
        
        in.close();
        ir.close();
    }	
}
