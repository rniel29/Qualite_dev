import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class main_scalabilte_PIforte {
    public static void main(String[] args) throws Exception {
        // Vérifier les arguments
        if (args.length < 2) {
            System.out.println("Usage: java main_scalabilte_PIforte <totalcount> <numWorkers>");
            return;
        }

        // Lire les arguments
        int totalcount = Integer.parseInt(args[0]);
        int numWorkers = Integer.parseInt(args[1]);

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

            // Lancer l'expérience
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
	

