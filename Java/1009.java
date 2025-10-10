// Problema: 1009 - Salário com Bônus | Resposta: Accepted
// Linguagem: Java 19 [+2s]           | Tempo: 0.065s

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        in.readLine();
        float salario = Float.parseFloat(in.readLine());
        float vendas = Float.parseFloat(in.readLine());
         
        System.out.printf("TOTAL = R$ %.2f\n", salario + vendas*0.15);
        
        in.close();
        ir.close();
    }
}