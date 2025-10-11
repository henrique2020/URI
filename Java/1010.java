// Problema: 1010 - Cálculo Simples | Resposta: Accepted
// Linguagem: Java 19 [+2s]         | Tempo: 0.085s

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static String[] pegaArray(BufferedReader in) throws IOException {
		return in.readLine().split(" ");
	}
	
	static float converteFloat(String valor) throws IOException {
		return Float.parseFloat(valor);
	}

    public static void main(String[] args) throws IOException {
    	InputStreamReader ir = new InputStreamReader(System.in);
	    BufferedReader in = new BufferedReader(ir);
	    
	    String[] linha;
	    float valor = 0;
	    
	    linha = pegaArray(in);
	    valor += converteFloat(linha[1]) * converteFloat(linha[2]);
	    linha = pegaArray(in);
	    valor += converteFloat(linha[1]) * converteFloat(linha[2]);

        System.out.printf("VALOR A PAGAR: R$ %.2f\n", valor);
        
        in.close();
        ir.close();
    }
}