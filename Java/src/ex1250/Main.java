package ex1250;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader in = new InputStreamReader(System.in);
		BufferedReader ir = new BufferedReader(in);
		String linha;
		while((linha = ir.readLine()) != null) {
			int jogos = Integer.parseInt(linha);
			for (int i = 0; i < jogos; i++) {
				linha = ir.readLine();
				int tiros = Integer.parseInt(linha);
				
				linha = ir.readLine();
				String[] posicoes = linha.split(" ");
				int[] tiro_posicao = new int[posicoes.length];
				
				for (int j = 0; j < posicoes.length; j++) {
					tiro_posicao[j] = Integer.parseInt(posicoes[j]);
				}
				
				linha = ir.readLine();
				String[] movimento = linha.split("");
				
				int cont = 0;
				for (int j = 0; j < tiros; j++) {
					if (movimento[j].equals("J")) {
						if (tiro_posicao[j] >= 3) {
							cont++;
						}
					}
					else {
						if (tiro_posicao[j] <= 2) {
							cont++;
						}
					}
				}
				System.out.printf("%d\n", cont);
			}
		}
		ir.close();
		in.close();
	}
}