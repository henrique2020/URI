package ex1001;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
        
		File arquivo = new File("Entrada/1001");
		//InputStreamReader ir = new InputStreamReader(System.in);
    	FileReader ir = new FileReader(arquivo);
        BufferedReader in = new BufferedReader(ir);
    	        
        int A = 0, B = 0, X = 0;
         
        A = Integer.parseInt(in.readLine());
        B = Integer.parseInt(in.readLine());
        
        X = A + B;
         
        System.out.printf("X = %d", X);
        
        in.close();
        ir.close();
    }
	     
}
