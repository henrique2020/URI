import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);

		String linha;
		while((linha = in.readLine()) != null) {
			
			int hobbit = 0;
			int humano = 0;
			int elfo = 0;
			int anao = 0;
			int mago = 0;
			
			int X = Integer.parseInt(linha);
			for (int i = 0; i < X; i++) {
				linha = in.readLine();
				String[] personagem = linha.split(" ");
				if (personagem[1].equals("X")) {
					hobbit++;
				}
				else if (personagem[1].equals("H")) {
					humano++;
				}
				else if (personagem[1].equals("E")) {
					elfo++;
				}
				else if (personagem[1].equals("A")) {
					anao++;
				}
				else if (personagem[1].equals("M")) {
					mago++;
				}
			}
			
			System.out.printf("%d Hobbit(s)\n", hobbit);
			System.out.printf("%d Humano(s)\n", humano);
			System.out.printf("%d Elfo(s)\n", elfo);
			System.out.printf("%d Anao(s)\n", anao);
			System.out.printf("%d Mago(s)\n", mago);		
		}
		in.close();
		ir.close();
	}
}
