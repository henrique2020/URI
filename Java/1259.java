import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		InputStreamReader in = new InputStreamReader(System.in);
		BufferedReader ir = new BufferedReader(in);
		String linha;
		while((linha = ir.readLine()) != null) {
			int tamanho = Integer.parseInt(linha);
			int[] numeros = new int[tamanho];
			for (int i = 0; i < tamanho; i++) {
				linha = ir.readLine();
				int valor = Integer.parseInt(linha);
				numeros[i] = valor;
			}
			ArrayList<Integer> pares = new ArrayList<Integer>();
			ArrayList<Integer> impares = new ArrayList<Integer>();
			for (int i = 0; i < tamanho; i++) {
				if (numeros[i]%2 == 0) {
					pares.add(numeros[i]);
				}
				else {
					impares.add(numeros[i]);
				}
			}
			pares.sort(null);
			impares.sort(null);
			for (int i = 0; i < pares.size(); i++) {
				System.out.printf("%d\n", pares.get(i));
			}
			
			for (int i = impares.size()-1; i >= 0; i--) {
				System.out.printf("%d\n", impares.get(i));
			}
			
		}
		ir.close();
		in.close();
	}

}