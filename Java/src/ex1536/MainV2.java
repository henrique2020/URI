package ex1536;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MainV2 {

	public static void main(String[] args) throws IOException {
		
		//InputStreamReader ir = new InputStreamReader(System.in);
		FileReader ir = new FileReader("Entrada/1536");
		BufferedReader in = new BufferedReader(ir);
		String linha = in.readLine();
		int jogos = Integer.parseInt(linha);
		for (int i = 0; i < jogos; i++) {
			linha = in.readLine();
			String[] j1 = linha.split(" x ");
			int m1 = Integer.parseInt(j1[0]);	//Time 1
			int v2 = Integer.parseInt(j1[1]);	//Time 2
			
			linha = in.readLine();
			String[] j2 = linha.split(" x ");
			int m2 = Integer.parseInt(j2[0]);	//Time 2
			int v1 = Integer.parseInt(j2[1]);	//Time 1
			
			int t1 = m1+v1;
			int t2 = m2+v2;
			
			if (t1>t2 || (t1==t2 && v1>v2)) {
				System.out.println("Time 1");
			}
			else if (t1<t2 || (t1==t2 && v1<v2)) {
				System.out.println("Time 2");
			}
			else {
				System.out.println("Penaltis");
			}
		}
		
		in.close();
		ir.close();
	}

}
