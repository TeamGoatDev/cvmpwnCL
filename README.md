# CVM Pwner for command line

"CVM Pwner for command line" (cvmpwnerCL.py) est un brute-forcer visant le serveur ftp du Cégep du Vieux Montréal. Il s'agît d'une adaptation moins messy et utilisant seulement la command line interface de l'ancienne version qui utilisait PyQt. Cette version est plus portable car elle ne nécessite aucune librairie externe (pis en plus t'as l'air fucking 1337 quand tu écris dans le terminal)

### Fonctionnement
Par defaut, le mot de passe d'un compte FTP étudiant au CVM est la date de naissance de l'étudiant en question sous le format AAMMJJ. Ce mot de passe est rarement changé. Comme il est possible d'obtenir la liste des comptes (disponible dans ce repo), nous pouvons itérer les dates de naissances d'une année afin de brute-forcer notre entrée. Le serveur bloque une connexion lorsqu'il détecte trop de mauvaises tentatives en peu de temps pour un même compte. Pour palier à ce problème, nous n'essayons pas tous les mots de passes pour un utilisateur, mais plutôt tous les utilisateurs pour un mot de passe, la boucle étant assez longue pour que le serveur ait remis son compteur de tentatives a 0 lorsque nous réessayerons cet utilisateur.

### Utilisation
`$python cvmpwnerCL.py (-y <year> (-r <results>)) (-l) (-h)`

`-y` 	Le paramètre `-y` permet de choisir l'année que l'application va utiliser
	comme référence, sachant que le mot de passe est constitué d'une date.

`-r` 	Le paramètre `-r` est le chemin vers le fichier de résultats où sera
	stocké les paires username/password découverts

`-l` 	Le paramètre `-l` utilise le dictionnaire de noms d'utilisateurs **Ressources/lists/CVM_dir.txt** pour
	restaurer la liste de cibles **users.txt**

`-h`    Le paramètre `-h` fait apparaitre l'aide


Lors du lancement, l'application génèrera toutes les dates de naisance possibles de l'année contenue dans le paramètre `-y` pour les stocker dans la liste de mots de passes possibles (lists/pass.txt).

Il prendra alors chaque mot de passe l'un apres l'autre et tentera de se connecter avec les noms d'utilisateurs fournis (c'est à dire ceux du fichier "lists/users.txt". Utilisez d'abord `-l` pour remplir le fichier users.txt avec tous les utillisateurs connus du dictionnaire CVM_dir.txt et retirez manuellement ceux qui ne vous intéresse pas. Vous pouvez ainsi garder le dictionnaire intact pour le futur).

Finalement, chaque fois qu'une connexion ne retourne pas d'erreurs, il stockera la paire dans le fichier de résultat. Si le paramètre `-r` n'est pas rempli, le fichier par défaut se nomme **workin_login.txt**

## Mass Downloader

MassDownload est un script post-exploitation. Il "craft" et exécute des commandes wget récursives pour télécharger la totalité des dossiers possédés par les utilisateurs pwnés précédemment. Il faut bien-sûr avoir wget installé sur sa machine.

#### Utilisation:

`$python MassDownload.py`


## Legal Disclaimer

Bien sûr, tout ceci est une satire et le code, une oeuvre théorique visant à montrer la faiblesse de la politique de création de mots de passe, ne dois pas être utilisé sans la permission d'un technicien de l'établissement.

~ Mixbo
www.wakowakowako.com

~ Team Goat
https://github.com/TeamGoatDev
