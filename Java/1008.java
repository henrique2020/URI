// Problema: 1008 - Salário | Resposta: Accepted
// Linguagem: Java 19 [+2s] | Tempo: 0.089s

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int pegaInt(BufferedReader in) throws IOException {
		return Integer.parseInt(in.readLine());
	}
	
	static float pegaFloat(BufferedReader in) throws IOException {
		return Float.parseFloat(in.readLine());
	}

    public static void main(String[] args) throws IOException {
    	InputStreamReader ir = new InputStreamReader(System.in);
	    BufferedReader in = new BufferedReader(ir);
	    
	    int id = pegaInt(in);
	    int horas = pegaInt(in);
	    float valor_hora = pegaFloat(in);

        System.out.printf("NUMBER = %d\n", id);
        System.out.printf("SALARY = U$ %.2f\n", horas*valor_hora);
        
        in.close();
        ir.close();
    }
}