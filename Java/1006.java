// Problema: 1006 - Média 2 | Resposta: Accepted
// Linguagem: Java 19 [+2s] | Tempo: 0.072s

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        float 
        	n1 = Float.parseFloat(in.readLine()),
        	n2 = Float.parseFloat(in.readLine()),
            n3 = Float.parseFloat(in.readLine());
        
        double media = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5);
        System.out.printf("MEDIA = %.1f\n", media);
        
        in.close();
        ir.close();
    }
}