#generate password which is tough to breakk for hacker 2806

import random
from pyfiglet import Figlet

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#€_&-+()/*':;!?,.~`|•√π÷×§∆£¥$¢^°={}\%©®™✓[]<>"

use_for = lower_case + upper_case + number + symbols
length_for_pass = 8

# Utiliser pyfiglet pour afficher le texte en ASCII art avec une police plus petite
custom_fig = Figlet(font='small')
ascii_art_text = custom_fig.renderText('DEDSEC BF V1.0')

# Afficher le texte en rouge et ajouter "BY: 2806"
print(f"\033[91m{ascii_art_text}BY: 2806\033[0m")

# Demander le nom de l'utilisateur
print("\033[92mEntrez votre nom :\033[0m", end="")
nom = input("\033[92m")

try:
    while True:
        # Assurer qu'il y a exactement un symbole
        password = [
            random.choice(symbols)  # Ajouter un symbole
        ]

        # Compléter avec des caractères aléatoires mais exclure les symboles
        remaining_length = length_for_pass - len(password)
        password += random.choices(lower_case + upper_case + number, k=remaining_length)

        # Mélanger les caractères pour assurer une distribution aléatoire
        random.shuffle(password)

        # Convertir la liste en chaîne
        password = "".join(password)

        # Afficher le mot de passe en vert
        print(f"\033[92mVotre mot de passe est : {password}\033[0m")
except KeyboardInterrupt:
    # Code à exécuter lorsque Ctrl+C est pressé
    print("\nGénération de mots de passe arrêtée.")
