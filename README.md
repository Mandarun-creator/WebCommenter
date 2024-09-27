
# WebCommenter

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**WebCommenter** est un outil en ligne de commande qui permet d'analyser les commentaires présents dans le code source HTML d'un site web. Il peut extraire, rechercher et afficher les commentaires HTML ainsi que leurs contextes associés dans le code source.

## Fonctionnalités

- **Extraction du code source** : Afficher le code source complet d'une page web.
- **Extraction des commentaires HTML** : Extraire uniquement les commentaires HTML présents dans une page web.
- **Recherche dans les commentaires** : Rechercher un mot ou une phrase spécifique dans les commentaires et afficher leur contexte dans le code.
- **Enregistrement des résultats** : Enregistrer les résultats dans un fichier texte pour une consultation ultérieure.

## Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre machine **Kali Linux** :

- **Python 3.x** : [Télécharger Python ici](https://www.python.org/downloads/)
- **Connexion Internet** : Le script récupère le code source des pages web en ligne.
- **pip** : Outil de gestion des dépendances Python (généralement inclus avec Python).

## Étapes d'installation

### 1. Cloner le projet

Commencez par cloner le dépôt GitHub sur votre machine locale en utilisant la commande suivante :

```bash
git clone https://github.com/Mandarun-creator/WebCommenter.git
cd WebCommenter
```

### 2. Installer les dépendances

Le projet utilise la bibliothèque **requests**, qui est une dépendance externe. Vous pouvez l'installer avec `pip` en exécutant la commande suivante :

```bash
pip install requests
```

Cette étape est essentielle pour que le script fonctionne correctement.

## Utilisation du script

Une fois le projet cloné et les dépendances installées, vous pouvez exécuter le script depuis n'importe quel répertoire de votre système Kali Linux. Il vous suffit de naviguer vers le répertoire où vous souhaitez l'utiliser ou de le lancer directement à partir du répertoire cloné.

### Exemple d'exécution

Vous pouvez exécuter le script depuis **n'importe quel répertoire** en indiquant simplement le chemin du script, ou en vous rendant dans le répertoire `WebCommenter`. Voici quelques exemples d'exécution :

1. **Afficher tout le code source d'une page web** depuis le répertoire `Documents` :

   ```bash
   cd ~/Documents
   python3 ~/WebCommenter/webcommenter.py -c https://example.com
   ```

2. **Afficher uniquement les commentaires HTML d'une page web** depuis le répertoire `Téléchargements` :

   ```bash
   cd ~/Téléchargements
   python3 ~/WebCommenter/webcommenter.py -C https://example.com
   ```

3. **Rechercher le mot "TODO" dans les commentaires et afficher le contexte du code** à partir de n'importe quel emplacement :

   ```bash
   python3 ~/WebCommenter/webcommenter.py -S "TODO" https://example.com
   ```

4. **Enregistrer les résultats des commentaires dans un fichier `resultat.txt`** depuis le répertoire `Desktop` (Bureau) :

   ```bash
   cd ~/Desktop
   python3 ~/WebCommenter/webcommenter.py -C -o resultat.txt https://example.com
   ```

## Utilisation en tant que Module Python

Vous pouvez également utiliser les fonctions du script dans d'autres projets Python en important les fonctions depuis `webcommenter.py`.

### Exemple d'importation et d'utilisation

```python
from webcommenter import get_source, get_comments_with_lines, search_comments_in_lines, get_code_context

# Exemple d'utilisation des fonctions importées

url = "https://example.com"
source_code = get_source(url)
comments = get_comments_with_lines(source_code)
filtered_comments = search_comments_in_lines(comments, "TODO")
if filtered_comments:
    context = get_code_context(source_code, filtered_comments[0][0])
    print(context)
```

## Tests

Vous pouvez exécuter les tests unitaires pour valider le bon fonctionnement du script en utilisant l'option `--test`.

```bash
python3 ~/WebCommenter/webcommenter.py --test
```

Cela exécutera les tests unitaires qui valideront plusieurs fonctionnalités, comme l'extraction des commentaires et la recherche dans ceux-ci.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet ou corriger des bugs, suivez ces étapes :

1. Forker le dépôt.
2. Créer une branche pour vos modifications.
3. Pousser vos modifications dans la branche.
4. Ouvrir une Pull Request.

Assurez-vous d'inclure des tests unitaires pour tout nouveau code ou toute nouvelle fonctionnalité.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.
