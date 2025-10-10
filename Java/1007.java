// Problema: 1007 - Diferença | Resposta: Accepted
// Linguagem: Java 19 [+2s]   | Tempo: 0.085s

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int pegaInt(BufferedReader in) throws IOException {
		return Integer.parseInt(in.readLine());
	}

    public static void main(String[] args) throws IOException {
    	InputStreamReader ir = new InputStreamReader(System.in);
	    BufferedReader in = new BufferedReader(ir);

        System.out.printf("DIFERENCA = %d\n", (pegaInt(in) * pegaInt(in)) - (pegaInt(in) * pegaInt(in)));
        
        in.close();
        ir.close();
    }
}