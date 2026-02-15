import subprocess
import os
import glob

WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(WORKSPACE_ROOT, "Initial_sources")

def compile_java_sources():
    """
    Compile les sources Java dans Initial_sources.
    """
    java_files = glob.glob(os.path.join(SRC_DIR, "*.java"))
    if not java_files:
        raise FileNotFoundError("Aucun fichier .java trouvé dans Initial_sources")

    command = ["javac", *java_files]
    print(f"Compilation : {command}")
    subprocess.run(command, check=True, cwd=WORKSPACE_ROOT)

def run_java_program(totalcount, numWorkers, program_name):
    """
    Exécute un programme Java avec les paramètres spécifiés.
    """
    try:
        # Commande pour exécuter le programme Java
        command = [
            "java",
            "-cp",
            "Initial_sources",
            program_name,
            str(int(totalcount)),
            str(int(numWorkers))
        ]
        print(f"Exécution : {command}")
        subprocess.run(command, check=True, cwd=WORKSPACE_ROOT)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {program_name} avec totalcount={totalcount} et numWorkers={numWorkers}")
        print(e)

def main():
    # Compiler les sources Java avant exécution
    compile_java_sources()

    # Paramètres à tester
    totalcount_values = [120000, 240000000,120000000]  # Différentes valeurs de totalcount
    numWorkers_values = [1, 2, 4, 8, 12, 24]  # Différents nombres de processus

    # Nom du programme Java à exécuter
    program_name = "main_scalabilte_PIforte"  # Ou "main_scalabilte_PIfaible"

    # Boucler sur les combinaisons de paramètres (10 répétitions par cas)
    repetitions = 10
    for totalcount in totalcount_values:
        for numWorkers in numWorkers_values:
            for i in range(repetitions):
                print(
                    f"Lancement {i + 1}/{repetitions} avec totalcount={totalcount}, numWorkers={numWorkers}"
                )
                run_java_program(totalcount // numWorkers, numWorkers, program_name)

if __name__ == "__main__":
    main()