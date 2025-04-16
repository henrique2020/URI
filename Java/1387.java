import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		String linha;
		while((linha = in.readLine()) != null){
			String[] filhos = linha.split(" ");
			int n_filhos = Integer.parseInt(filhos[0]);
			int n_filhas = Integer.parseInt(filhos[1]);
			if ((n_filhos == 0 && n_filhas == 0) || n_filhos < 1 || n_filhas > 5) {
				break;
			}else {
				int t_filhos = n_filhos + n_filhas;
				System.out.printf("%d\n",t_filhos);
			}
		}
		
		in.close();
		ir.close();
	}

}