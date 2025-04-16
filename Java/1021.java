import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        String linha = in.readLine();
        double valor = Double.parseDouble(linha);

        // Multiplica por 100 e converte para int para lidar com valores monetários em centavos
        int total = (int) Math.round(valor * 100);

        // Notas
        int n100 = total / 10000;
        total %= 10000;
        int n50 = total / 5000;
        total %= 5000;
        int n20 = total / 2000;
        total %= 2000;
        int n10 = total / 1000;
        total %= 1000;
        int n5 = total / 500;
        total %= 500;
        int n2 = total / 200;
        total %= 200;

        // Moedas
        int m1 = total / 100;
        total %= 100;
        int m05 = total / 50;
        total %= 50;
        int m025 = total / 25;
        total %= 25;
        int m010 = total / 10;
        total %= 10;
        int m005 = total / 5;
        total %= 5;
        int m001 = total;

        System.out.println("NOTAS:");
        System.out.printf("%d nota(s) de R$ 100.00\n", n100);
        System.out.printf("%d nota(s) de R$ 50.00\n", n50);
        System.out.printf("%d nota(s) de R$ 20.00\n", n20);
        System.out.printf("%d nota(s) de R$ 10.00\n", n10);
        System.out.printf("%d nota(s) de R$ 5.00\n", n5);
        System.out.printf("%d nota(s) de R$ 2.00\n", n2);

        System.out.println("MOEDAS:");
        System.out.printf("%d moeda(s) de R$ 1.00\n", m1);
        System.out.printf("%d moeda(s) de R$ 0.50\n", m05);
        System.out.printf("%d moeda(s) de R$ 0.25\n", m025);
        System.out.printf("%d moeda(s) de R$ 0.10\n", m010);
        System.out.printf("%d moeda(s) de R$ 0.05\n", m005);
        System.out.printf("%d moeda(s) de R$ 0.01\n", m001);

        in.close();
        ir.close();
    }
}

