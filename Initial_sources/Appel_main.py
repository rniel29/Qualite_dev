import subprocess

def run_java_program(totalcount, numWorkers, program_name):
    """
    Exécute un programme Java avec les paramètres spécifiés.
    """
    try:
        # Commande pour exécuter le programme Java
        command = [
            "java",
            program_name,
            str(totalcount),
            str(numWorkers)
        ]
        print(f"Exécution : {command}")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {program_name} avec totalcount={totalcount} et numWorkers={numWorkers}")
        print(e)

def main():
    # Paramètres à tester
    totalcount_values = [120000000, 240000000, 360000000]  # Différentes valeurs de totalcount
    numWorkers_values = [1, 2, 4, 8, 12]  # Différents nombres de processus

    # Nom du programme Java à exécuter
    program_name = "main_scalabilte_PIforte"  # Ou "main_scalabilte_PIfaible"

    # Boucler sur les combinaisons de paramètres
    for totalcount in totalcount_values:
        for numWorkers in numWorkers_values:
            print(f"Lancement avec totalcount={totalcount}, numWorkers={numWorkers}")
            run_java_program(totalcount/numWorkers, numWorkers, program_name)

if __name__ == "__main__":
    main()