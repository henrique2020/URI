package ex1036;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
     
    public static void main(String[] args) throws IOException {
		
    	File arquivo = new File("Entrada/1036");
    	//InputStreamReader ir = new InputStreamReader(System.in);
    	FileReader ir = new FileReader(arquivo);
    	BufferedReader in = new BufferedReader(ir);
    	
    	String[] valores = in.readLine().split(" ");
    	double A = Double.parseDouble(valores[0]);
    	double B = Double.parseDouble(valores[1]);
    	double C = Double.parseDouble(valores[2]);
    	if (A != 0 && B != 0 && C != 0) {
    		double raiz = Math.sqrt((B*B)-4*C*A);
        	if (raiz >= 0) {
        		double R1 = ((-B)+raiz)/(A*2);
            	double R2 = ((-B)-raiz)/(A*2);
            	System.out.printf("R1 = %.5f\n", R1);
            	System.out.printf("R2 = %.5f\n", R2);
    		}else {
    			System.out.printf("Impossivel calcular\n");
    		}
		}else {
			System.out.printf("Impossivel calcular\n");
		}
    	
    	in.close();
		ir.close();
    }
}
