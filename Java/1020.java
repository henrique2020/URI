import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		
		String linha = null;
		while((linha = in.readLine()) != null) {
			int total_dias = Integer.parseInt(linha);
			
			int ano = total_dias/365;
			int mes = (total_dias%365)/30;
			int dias = ((total_dias%365)%30);
			
			System.out.printf("%d ano(s)\n", ano);
			System.out.printf("%d mes(es)\n", mes);
			System.out.printf("%d dia(s)\n", dias);
		}
		
		in.close();
		ir.close();
	}
}