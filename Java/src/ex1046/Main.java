package ex1046;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
    	BufferedReader in = new BufferedReader(ir);
        String linha = null;
        
        while((linha = in.readLine()) != null) {
        	String[] horas = linha.split(" ");
        	int hi = Integer.parseInt(horas[0]);
        	int hf = Integer.parseInt(horas[1]);
        	if (hi>hf) {
        		int jogo = 24-(hi-hf);
				System.out.printf("O JOGO DUROU %d HORA(S)\n", jogo);
			}else if(hi<hf) {
				int jogo = hf-hi;
				System.out.printf("O JOGO DUROU %d HORA(S)\n", jogo);
			}else {
				System.out.printf("O JOGO DUROU 24 HORA(S)\n");
			}
        }
        
        in.close();
        ir.close();
	}

}
