package ex1828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		InputStreamReader ir = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(ir);
		String linha;
		
		int tamanho = Integer.parseInt(in.readLine());
		
		for (int i = 0; i < tamanho; i++) {
			linha = in.readLine();
			String[] movimento = linha.split(" ");
			String sheldon = movimento[0];
			String raj =  movimento[1];
			
			System.out.printf("Caso #%d: ", (i+1));
			
			if(sheldon.equals("tesoura")){
				if (raj.equals("tesoura")){
					System.out.println("De novo!");
				}if(raj.equals("papel")){
					System.out.println("Bazinga!");
				}if (raj.equals("pedra")){
					System.out.println("Raj trapaceou!");
				}if (raj.equals("lagarto")){
					System.out.println("Bazinga!");
				}if (raj.equals("Spock")){
					System.out.println("Raj trapaceou!");
				}
			}
			if(sheldon.equals("pedra")){
				if (raj.equals("tesoura")){
					System.out.println("Bazinga!");
				}if(raj.equals("papel")){
					System.out.println("Raj trapaceou!");
				}if (raj.equals("pedra")){
					System.out.println("De novo!");
				}if (raj.equals("lagarto")){
					System.out.println("Bazinga!");
				}if (raj.equals("Spock")){
					System.out.println("Raj trapaceou!");
				}
			}
			if(sheldon.equals("papel")){
				if (raj.equals("tesoura")){
					System.out.println("Raj trapaceou!");
				}if(raj.equals("papel")){
					System.out.println("De novo!");
				}if (raj.equals("pedra")){
					System.out.println("Bazinga!");
				}if (raj.equals("lagarto")){
					System.out.println("Raj trapaceou!");
				}if (raj.equals("Spock")){
					System.out.println("Bazinga!");
				}
			}
			if(sheldon.equals("lagarto")){
				if (raj.equals("tesoura")){
					System.out.println("Raj trapaceou!");
				}if(raj.equals("papel")){
					System.out.println("Bazinga!");
				}if (raj.equals("pedra")){
					System.out.println("Raj trapaceou!");
				}if (raj.equals("lagarto")){
					System.out.println("De novo!");
				}if (raj.equals("Spock")){
					System.out.println("Bazinga!");
				}
			}
			
			if(sheldon.equals("Spock")){
				if (raj.equals("tesoura")){
					System.out.println("Bazinga!");
				}if(raj.equals("papel")){
					System.out.println("Raj trapaceou!");
				}if (raj.equals("pedra")){
					System.out.println("Bazinga!");
				}if (raj.equals("lagarto")){
					System.out.println("Raj trapaceou!");
				}if (raj.equals("Spock")){
					System.out.println("De novo!");
				}
			}	
		}
		in.close();
		ir.close();
	}
}
