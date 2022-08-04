package ex2950;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);

		String linha;
		while((linha = in.readLine()) != null) {
			String[] info = linha.split(" ");
			float dis = Float.parseFloat(info[0]);
			float tA = Float.parseFloat(info[1]);
			float tB = Float.parseFloat(info[2]);
			
			//float resultado = (dis/(tA+tB));
			System.out.printf("%.2f\n", (dis/(tA+tB)));
		}
		in.close();
		ir.close();
	}
}