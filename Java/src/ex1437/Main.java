package ex1437;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		String linha;
		while(true){
			linha = in.readLine();
			int mover = Integer.parseInt(linha);
			if (mover == 0) {
				break;
			}else {
				linha = in.readLine();
				char[] direcao = linha.toCharArray();
				int D = 0, E = 0;
				for (int i = 0; i < mover; i++) {
					if (direcao[i] == 'D') {
						D++;
					}else {
						E++;
					}
				}
				boolean sair = false;
				if (D > E) {
					char[] pon_car = {'N', 'L', 'S', 'O'};
					mover = D - E;
					while(sair == false) {
						if (mover > 3) {
							mover -= 4;
						}else {
							System.out.printf("%s\n", pon_car[mover]);
							sair = true;
						}
					}
				}else {
					char[] pon_car = {'N', 'O', 'S', 'L'};
					mover = E - D;
					while(sair == false) {
						if (mover > 3) {
							mover -= 4;
						}else {
							System.out.printf("%s\n", pon_car[mover]);
							sair = true;
						}
					}
				}
			}
		}
		
		in.close();
		ir.close();
	}
}