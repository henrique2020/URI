package ex1072;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {		
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		int tamanho = Integer.parseInt(in.readLine());
		if (tamanho < 10000) {
			int in_d = 0, out_f = 0;	//Dentro //Fora
			for (int i = 0; i < tamanho; i++) {
				int valor = Integer.parseInt(in.readLine());
				if (valor >= 10 && valor <= 20) {
					in_d++;
				}else {
					out_f++;
				}
			}
			System.out.printf("%d in\n", in_d);
			System.out.printf("%d out\n", out_f);
		}
		
		ir.close();
		in.close();
	}
}
