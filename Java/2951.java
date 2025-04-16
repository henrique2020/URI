import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);

		String linha;
		while((linha = in.readLine()) != null) {
			String[] jogo = linha.split(" ");
			
			int n_runas = Integer.parseInt(jogo[0]);
			int amizade = 0;
			
			String[] runa = new String[n_runas];
			int[] runa_A = new int[n_runas];
			for (int i = 0; i < n_runas; i++) {
				linha = in.readLine();
				String[] r_u = linha.split(" ");
				runa[i] = r_u[0];
				runa_A[i] = Integer.parseInt(r_u[1]);
			}
			linha = in.readLine();
			linha = in.readLine();
			String[] runas_usadas = linha.split(" ");
			for (int i = 0; i < runas_usadas.length; i++) {
				for (int j = 0; j < runa.length; j++) {
					if (runas_usadas[i].equals(runa[j])) {
						amizade += runa_A[j];
					}
				}
			}
			
			int vida = Integer.parseInt(jogo[1]);
			System.out.printf("%d\n",amizade);
			if (vida <= amizade) {
				System.out.println("You shall pass!");
			} else {
				System.out.println("My precioooous");
			}		
		}
		in.close();
		ir.close();
	}
}