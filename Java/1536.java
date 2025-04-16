import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		
		String linha = in.readLine();
		int jogos = Integer.parseInt(linha);
		if (jogos >= 1 && jogos <= 100) {
			for (int i = 0; i < jogos; i++) {
				int t1 = 0, t2 = 0;
				linha = in.readLine();
				String[] placar = linha.split(" ");
				int M1 = Integer.parseInt(placar[0]);	//Time 1
				int V2 = Integer.parseInt(placar[2]);	//Time 2
				linha = in.readLine();
				String[] placar2 = linha.split(" ");
				int M2 = Integer.parseInt(placar2[0]);	//Time 2
				int V1 = Integer.parseInt(placar2[2]);	//Time 1
				if (M1>V2) {
					t1+=3;
				}
				if (M1<V2) {
					t2+=3;
				}else {
					t1++;
					t2++;
				}
				if (M2>V1) {
					t2+=3;
				}
				if (M2<V1) {
					t1+=3;
				}else {
					t1++;
					t2++;
				}
				
				if (t1>t2) {
					System.out.println("Time 1");
				}
				if (t1<t2) {
					System.out.println("Time 2");
				}if (t1==t2)  {
					int somat1 = M1+V1;
					int somat2 = M2+V2;
					if (somat1>somat2) {
						System.out.println("Time 1");
					}
					if (somat1<somat2) {
						System.out.println("Time 2");
					}if (somat1==somat2) {
						if (V1>V2) {
							System.out.println("Time 1");
						}
						if (V1<V2) {
							System.out.println("Time 2");
						}if (V1==V2) {
							System.out.println("Penaltis");
						}
					}
				}
			}			
		}
		
		in.close();
		ir.close();
	}
}
