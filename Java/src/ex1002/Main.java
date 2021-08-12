package ex1002;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
     
    public static void main(String[] args) throws IOException {
		
    	File arquivo = new File("Entrada/1002");
		//InputStreamReader ir = new InputStreamReader(System.in);
    	FileReader ir = new FileReader(arquivo);
        BufferedReader in = new BufferedReader(ir);
        
		double r = Double.parseDouble(in.readLine());
        double x = r * r * 3.14159;
                
        System.out.printf("A=%.4f\n", x);
        
        in.close();
        ir.close();
    }	
}
