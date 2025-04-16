import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		
		int valores = Integer.parseInt(in.readLine());
		for (int i = 0; i < valores; i++) {
			int n = Integer.parseInt(in.readLine());
			if(n%2 == 0){
				System.out.printf("0\n");
			}else {
				System.out.printf("1\n");
			}
		}
		
		in.close();
		ir.close();
	}

}
