package ex1005;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
     
    public static void main(String[] args) throws IOException {
		
    	File arquivo = new File("Entrada/1005");
    	//InputStreamReader ir = new InputStreamReader(System.in);
    	FileReader ir = new FileReader(arquivo);
    	BufferedReader in = new BufferedReader(ir);
    	
    	double A = Double.parseDouble(in.readLine());
    	double B = Double.parseDouble(in.readLine());
    	
    	double media = (A*3.5)/10+(B*7.5)/10;	//Representa a média, mas com nota máxima = 11
    	double media10 = ((media*10)/11);	//Corrige a nota máxima para 10
    	System.out.printf("MEDIA = %.5f\n", media10);
    	
    	in.close();
    	ir.close();
    }
}
