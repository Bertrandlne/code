import os

def get_largest_files(root_dir, num_files=10):
    """
    Parcourt les répertoires à partir de root_dir et retourne les fichiers les plus volumineux.

    :param root_dir: Le répertoire de départ pour la recherche.
    :param num_files: Le nombre de fichiers les plus volumineux à retourner.
    :return: Une liste de tuples (chemin du fichier, taille du fichier).
    """
    file_sizes = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_sizes.append((file_path, file_size))
            except OSError as e:
                print(f"Erreur lors de l'accès au fichier {file_path}: {e}")

    # Trier les fichiers par taille décroissante
    file_sizes.sort(key=lambda x: x[1], reverse=True)

    # Retourner les fichiers les plus volumineux
    return file_sizes[:num_files]

def main():
    root_directory = "C:\\"  # Vous pouvez changer ce chemin selon vos besoins
    num_largest_files = 10  # Nombre de fichiers les plus volumineux à afficher

    largest_files = get_largest_files(root_directory, num_largest_files)

    print(f"Les {num_largest_files} fichiers les plus volumineux sont :")
    for file_path, file_size in largest_files:
        print(f"{file_path} : {file_size} octets")

if __name__ == "__main__":
    main()
