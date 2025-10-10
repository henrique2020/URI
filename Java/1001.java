// Problema: 1001 - Extremamente Básico | Resposta: Accepted
// Linguagem: Java 8 [+2s]              | Tempo: 0.088s

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
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
