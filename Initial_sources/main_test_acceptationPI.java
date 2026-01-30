import java.util.ArrayList;
import java.util.List;

public class main_test_acceptationPI {
    public static void main(String[] args) throws Exception 
    {
	List<Long> results = new ArrayList<Long>();
	//lancer l'experience 10fois et renvoyer chaque temps et faire la medianne des 10 resultats
	for(int i=0;i<10;i++) {
		long total=0;
		// 10 workers, 50000 iterations each
		total = new Master().doRun(12000000,1 );
        //on ne veut que le temps de calcul
        
		results.add(total);
		System.out.println( i+" total from Master = " + total);
    }
	System.out.println(calculerMediane(results));
	}
	
}
