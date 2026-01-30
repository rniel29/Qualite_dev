import java.util.Arrays;

public class Mediane {

    public static void main(String[] args) {
        // Exemple de tableau de nombres
        int[] tableau = {12, 7, 9, 5, 14, 8, 10};

        // Appel de la méthode pour calculer la médiane
        double mediane = calculerMediane(tableau);

        // Affichage de la médiane
        System.out.println("La médiane est : " + mediane);
    }

    public static double calculerMediane(Long[] tableau) {
        // Trier le tableau en ordre croissant
        Arrays.sort(tableau);

        int taille = tableau.length;

        // Si la taille du tableau est impaire
        if (taille % 2 != 0) {
            // Retourner l'élément du milieu
            return tableau[taille / 2];
        } else {
            // Si la taille est paire, la médiane est la moyenne des deux éléments centraux
            int index1 = taille / 2 - 1;
            int index2 = taille / 2;
            return (tableau[index1] + tableau[index2]) / 2.0;
        }
    }
}
