import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
     
    public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
    	BufferedReader in = new BufferedReader(ir);
    	
    	double A = Double.parseDouble(in.readLine());
    	double B = Double.parseDouble(in.readLine());
    	
    	double media = (A*3.5)/10+(B*7.5)/10;	//Representa a m�dia, mas com nota m�xima = 11
    	double media10 = ((media*10)/11);	//Corrige a nota m�xima para 10
    	System.out.printf("MEDIA = %.5f\n", media10);
    	
    	in.close();
    	ir.close();
    }
}
