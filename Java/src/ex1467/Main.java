package ex1467;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		String linha;
		while((linha = in.readLine()) != null){
			String[] jogou = linha.split(" ");
			int A = Integer.parseInt(jogou[0]);	//Alice
			int B = Integer.parseInt(jogou[1]);	//Beto
			int C = Integer.parseInt(jogou[2]);	//Clara
			
			if (A == B && B == C) {
				System.out.printf("*\n");
			}else {
				if (A == B) {
					System.out.printf("C\n");
				}else {
					if (A == C) {
						System.out.printf("B\n");
					}else {
						System.out.printf("A\n");
					}
				}
			}
		}
		
		in.close();
		ir.close();
	}
}
