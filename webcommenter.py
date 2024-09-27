import argparse
import requests
import re
import sys
import unittest

# Fonction pour récupérer le code source d'une URL
def get_source(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[!] Erreur lors de la récupération de l'URL : {e}")
        return None

# Fonction pour extraire les lignes de code contenant des commentaires HTML
def get_comments_with_lines(source_code):
    lines = source_code.splitlines()
    comment_lines = []
    comment_regex = re.compile(r'<!--(.*?)-->', re.DOTALL)

    for i, line in enumerate(lines, start=1):
        match = comment_regex.search(line)
        if match:
            comment = match.group(1).strip()
            comment_lines.append((i, comment, line.strip()))  # (numéro de ligne, commentaire, ligne complète)
    
    return comment_lines

# Fonction pour rechercher des mots/phrases spécifiques dans les commentaires
def search_comments_in_lines(comments_with_lines, search_term):
    return [(line_num, comment, full_line) for line_num, comment, full_line in comments_with_lines if search_term in comment]

# Fonction pour afficher les lignes de contexte autour d'un commentaire
def get_code_context(source_code, line_num, context_lines=2):
    lines = source_code.splitlines()
    start = max(0, line_num - context_lines - 1)
    end = min(len(lines), line_num + context_lines)
    return "\n".join(lines[start:end])

# Fonction pour enregistrer les données dans un fichier
def save_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(data)
        print(f"[+] Les données ont été enregistrées avec succès dans le fichier : {filename}")
    except IOError as e:
        print(f"[!] Erreur lors de l'écriture dans le fichier : {e}")

# Tests unitaires utilisant unittest
class TestWebCommenter(unittest.TestCase):

    html_content = """
    <html>
    <head>
    <!-- This is a test comment -->
    <title>Test Page</title>
    </head>
    <body>
    <!-- TODO: Add more features -->
    <p>This is a test paragraph.</p>
    </body>
    </html>
    """

    def test_get_comments_with_lines(self):
        comments = get_comments_with_lines(self.html_content)
        self.assertEqual(len(comments), 2)
        self.assertIn("This is a test comment", comments[0][1])
        self.assertIn("TODO", comments[1][1])

    def test_search_comments_in_lines(self):
        comments = get_comments_with_lines(self.html_content)
        search_results = search_comments_in_lines(comments, "TODO")
        self.assertEqual(len(search_results), 1)
        self.assertIn("TODO", search_results[0][1])

    def test_get_code_context(self):
        # Ajuster pour obtenir un bon contexte (plus de lignes)
        context = get_code_context(self.html_content, 7, context_lines=4)
        self.assertIn("TODO: Add more features", context)
        self.assertIn("<p>This is a test paragraph.</p>", context)

# Fonction principale
def main():
    parser = argparse.ArgumentParser(
        description="WebCommenter - Un outil pour analyser les commentaires dans le code source d'un site web."
    )

    parser.add_argument(
        "-c", "--code", action="store_true", 
        help="Afficher tout le code source du site web."
    )
    parser.add_argument(
        "-C", "--comment", action="store_true", 
        help="Afficher uniquement les commentaires HTML présents dans le code source."
    )
    parser.add_argument(
        "-S", "--search", metavar="TERM", 
        help="Rechercher un commentaire contenant une phrase ou un mot spécifique."
    )
    parser.add_argument(
        "-o", "--output", metavar="FILENAME", 
        help="Spécifier un fichier pour enregistrer les résultats."
    )
    parser.add_argument(
        "--test", action="store_true", 
        help="Exécuter les tests unitaires."
    )

    parser.add_argument("url", nargs="?", help="L'URL du site web à analyser.")
    
    args = parser.parse_args()

    if args.test:
        print("[+] Exécution des tests unitaires...")
        unittest.main(argv=[''], exit=False)
        return

    # Si l'utilisateur n'utilise pas l'option --test, exécuter le script normalement
    if not args.url:
        parser.print_help()
        sys.exit("\n[!] Erreur : L'URL du site web est obligatoire.\n")

    if not (args.code or args.comment or args.search):
        parser.print_help()
        sys.exit("\n[!] Erreur : Vous devez spécifier au moins une option (-c, -C ou -S).\n")

    # Récupère le code source de l'URL donnée
    source_code = get_source(args.url)
    if source_code is None:
        sys.exit("[!] Impossible de récupérer le code source. Vérifiez l'URL.")

    result = ""

    # Afficher tout le code source
    if args.code:
        result += (
            "+-----------------------------+\n"
            "|      Code Source Complet     |\n"
            "+-----------------------------+\n"
        )
        result += source_code + "\n"

    # Afficher uniquement les lignes contenant des commentaires
    if args.comment:
        comments_with_lines = get_comments_with_lines(source_code)
        result += (
            "\n+------------------------------+\n"
            "|   Commentaires HTML Trouvés   |\n"
            "+------------------------------+\n"
        )
        if comments_with_lines:
            for line_num, comment, _ in comments_with_lines:
                result += f"[+] Ligne {line_num}: {comment}\n"
        else:
            result += "[-] Aucun commentaire trouvé.\n"

    # Rechercher un terme spécifique dans les commentaires et afficher le contexte du code
    if args.search:
        comments_with_lines = get_comments_with_lines(source_code)
        matching_comments = search_comments_in_lines(comments_with_lines, args.search)
        result += (
            "\n+------------------------------+\n"
            f"|   Résultats de la Recherche : '{args.search}'   |\n"
            "+------------------------------+\n"
        )
        if matching_comments:
            for line_num, comment, full_line in matching_comments:
                result += f"[+] Ligne {line_num}: {comment}\n"
                result += "+----------------------------+\n"
                result += get_code_context(source_code, line_num) + "\n"
                result += "+----------------------------+\n"
        else:
            result += f"[-] Aucun commentaire contenant '{args.search}' trouvé.\n"

    # Affichage des résultats ou enregistrement dans un fichier
    if args.output:
        save_to_file(result, args.output)
    else:
        print(result)

if __name__ == "__main__":
    main()
