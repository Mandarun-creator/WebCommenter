
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

Les dépendances nécessaires pour ce projet sont listées dans le fichier `requirements.txt`. Pour installer ces dépendances, exécutez la commande suivante :

```bash
pip install -r requirements.txt
```

Cette étape installera la bibliothèque `requests` et toutes les autres dépendances nécessaires.

## Utilisation du script

Une fois le projet cloné et les dépendances installées, vous pouvez rendre le script exécutable et l'utiliser directement depuis n'importe quel répertoire de votre système **Kali Linux**.

### Étapes pour rendre le script exécutable

1. **Ajouter la ligne shebang** dans le fichier `webcommenter.py` :
   
   Assurez-vous que la première ligne du fichier `webcommenter.py` est :

   ```bash
   #!/usr/bin/env python3
   ```

2. **Rendre le fichier exécutable** :

   Utilisez la commande suivante pour rendre le script exécutable :

   ```bash
   chmod +x webcommenter.py
   ```

3. **Créer un lien symbolique** (facultatif) :

   Si vous souhaitez exécuter `webcommenter` depuis n'importe quel répertoire en tant que commande, créez un lien symbolique vers `/usr/local/bin` :

   ```bash
   sudo ln -s ~/Documents/WebCommenter/webcommenter.py /usr/local/bin/webcommenter
   ```

### Exemple d'exécution

1. **Afficher tout le code source d'une page web** depuis n'importe où dans le système :

   ```bash
   webcommenter -c https://example.com
   ```

2. **Afficher uniquement les commentaires HTML d'une page web** :

   ```bash
   webcommenter -C https://example.com
   ```

3. **Rechercher le mot "TODO" dans les commentaires et afficher le contexte du code** :

   ```bash
   webcommenter -S "TODO" https://example.com
   ```

4. **Enregistrer les résultats des commentaires dans un fichier `resultat.txt`** :

   ```bash
   webcommenter -C -o resultat.txt https://example.com
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
webcommenter --test
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
