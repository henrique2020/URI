package ex2714;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		String linha;
		while((linha = in.readLine()) != null) {
			int tamanho = Integer.parseInt(linha);
			String[] resposta = new String[tamanho];
			for (int i = 0; i < tamanho; i++) {
				linha = in.readLine();
				String[] caracter = linha.split("");
				String inicio = caracter[0]+caracter[1];
				if (inicio.equals("RA")) {
					if ((caracter.length)-2 == 18) {
						int posicao = 0;
						for (int j = 2; j < caracter.length; j++) {
							if (!caracter[j].equals("0")) {
								posicao = j;
								break;
							}
						}
						String res = "";
						for (int j = posicao; j < caracter.length; j++) {
							res = res+caracter[j];
						}
						resposta[i] = res;
					}
					else{
						resposta[i] = "INVALID DATA";
					}
				}
				else{
					resposta[i] = "INVALID DATA";
				}
				System.out.println(resposta[i]);	
			}
		}
	}
}