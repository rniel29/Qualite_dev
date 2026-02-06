import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class main_scalabilte_PIfaible {
    public static void main(String[] args) throws Exception 
    {
	// Créer le dossier resultat s'il n'existe pas
	File resultatDir = new File("resultat");
	if (!resultatDir.exists()) {
	    resultatDir.mkdir();
	}
	
	// Créer le fichier CSV
	File csvFile = new File(resultatDir, "resultats.csv");
	boolean fileExists = csvFile.exists();
	
	try (PrintWriter writer = new PrintWriter(new FileWriter(csvFile, true))) {
	    // Écrire l'en-tête si le fichier est nouveau
	    if (!fileExists) {
		writer.println("Ntot,NumWorkers,Temps(ns),Pi,Erreur");
	    }
	    
	    // NTOT constant pour scalabilité forte
	    int totalcount = 120000000;
	    int numWorkers = 12; // À changer manuellement pour chaque test
	
	    // Lancer l'expérience
		//forte
	    //Master.Result result = new Master().doRun(NTOT/numWorkers, numWorkers);
	    //faible
		Master.Result result = new Master().doRun(totalcount, numWorkers);
	    // Écrire les résultats dans le CSV
	    writer.println(result.ntot + "," + 
	                   result.numWorkers + "," + 
	                   result.timeNanos + "," + 
	                   result.pi + "," + 
	                   result.error);
	    
	    System.out.println("Résultats enregistrés dans resultat/resultats.csv");
	}
    }
}
	

