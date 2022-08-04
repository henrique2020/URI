package ex1066;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
    	BufferedReader in = new BufferedReader(ir);
        String linha = null;
        
        int par = 0, impar = 0, positivo = 0, negativo = 0;
        
        for (int i = 0; i < 5; i++) {
			linha = in.readLine();
			int valor = Integer.parseInt(linha);
			if (valor>0) {
				positivo++;
			}
			if (valor<0) {
				negativo++;
			}
			if (valor%2 == 0) {
				par++;
			}else {
				impar++;
			}
		}
        
        System.out.printf("%d valor(es) par(es)\n", par);
        System.out.printf("%d valor(es) impar(es)\n", impar);
        System.out.printf("%d valor(es) positivo(s)\n", positivo);
        System.out.printf("%d valor(es) negativo(s)\n", negativo);
        
        in.close();
        ir.close();
	}
}