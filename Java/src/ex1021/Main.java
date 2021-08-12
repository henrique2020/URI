package ex1021;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		//InputStreamReader ir = new InputStreamReader(System.in);
		FileReader ir = new FileReader("Entrada/1021");
		BufferedReader in = new BufferedReader(ir);
		
		String linha = null;
		while((linha = in.readLine()) != null) {
			float total_dinheiro = Float.parseFloat(linha);
			
			float n_100 = total_dinheiro/100;
			float n_50 = (total_dinheiro%100)/50;
			float n_20 = ((total_dinheiro%100)%50)/20;
			float n_10 = (((total_dinheiro%100)%50)%20)/10;
			float n_5 = ((((total_dinheiro%100)%50)%20)%10)/5;
			float n_2 = (((((total_dinheiro%100)%50)%20)%10)%5)/2;
			
			System.out.printf("NOTAS:\n");
			System.out.printf("%d nota(s) de R$ 100.00\n", (int) n_100);
			System.out.printf("%d nota(s) de R$ 50.00\n", (int) n_50);
			System.out.printf("%d nota(s) de R$ 20.00\n", (int) n_20);
			System.out.printf("%d nota(s) de R$ 10.00\n", (int) n_10);
			System.out.printf("%d nota(s) de R$ 5.00\n", (int) n_5);
			System.out.printf("%d nota(s) de R$ 2.00\n", (int) n_2);
			
			float m_1 = (n_5%2);
			float m_05 = (float) (((m_1)%1)/0.5);
			float m_025 = (float) ((((m_1)%1)%0.5)/0.25);
			float m_010 = (float) (((((m_1)%1)%0.5)%0.25)/0.01);
			float m_005 = (float) ((((((m_1)%1)%0.5)%0.25)%0.01)/0.005);
			float m_001 = (float) ((((((m_1)%1)%0.5)%0.25)%0.01)%0.005);
			
			System.out.printf("MOEDAS:\n");
			System.out.printf("%d moeda(s) de R$ 1.00\n", (int) m_1);
			System.out.printf("%d moeda(s) de R$ 0.50\n", (int) m_05);
			System.out.printf("%d moeda(s) de R$ 0.25\n", (int) m_025);
			System.out.printf("%d moeda(s) de R$ 0.10\n", (int) m_010);
			System.out.printf("%d moeda(s) de R$ 0.05\n", (int) m_005);
			System.out.printf("%d moeda(s) de R$ 0.01\n", (int) m_001);
		}
		
		in.close();
		ir.close();
	}
}
