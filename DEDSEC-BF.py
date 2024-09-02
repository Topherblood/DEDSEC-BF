import random
from pyfiglet import Figlet

# Définition des caractères
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()_-:?!*#"

# Liste de mots significatifs pour le mode "lettres seulement"
significant_words = [
    # Marques de voitures
    "Tesla", "Ferrari", "Lamborghini", "Toyota", "Ford", "Chevrolet", "Mercedes", "BMW", "Audi", "Porsche",
    
    # Noms d'animaux
    "Lion", "Tiger", "Eagle", "Shark", "Wolf", "Dolphin", "Elephant", "Giraffe", "Panther", "Falcon",
    "Bear", "Fox", "Rabbit", "Deer", "Kangaroo", "Panda", "Cheetah", "Leopard", "Owl", "Hawk",
    "Crocodile", "Alligator", "Snake", "Turtle", "Whale", "Penguin", "Seal", "Otter", "Raccoon", "Bison",
    "Buffalo", "Moose", "Beaver", "Antelope", "Hedgehog", "Porcupine", "Sloth", "Armadillo", "Meerkat", "Zebra",
    "Hippo", "Rhino", "Chimpanzee", "Orangutan", "Gorilla", "Lemur", "Koala", "Wallaby", "Dingo", "Bat",
    "Parrot", "Sparrow", "Peacock", "Swan", "Flamingo", "Pelican", "Albatross", "Stork", "Heron", "Crane",
    "Coyote", "Jackal", "Hyena", "Vulture", "Condor", "Buzzard", "Raven", "Crow", "Magpie", "Jay",
    "Lynx", "Bobcat", "Cougar", "Puma", "Jaguar", "Caracal", "Serval", "Ocelot", "Fossa", "Ibex",
    
    # Termes technologiques
    "Python", "Java", "Laptop", "Server", "Router", "Firewall", "Crypto", "AI", "Cloud", "Quantum",
    
    # Prénoms
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", 
    "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", 
    "Christopher", "Nancy", "Daniel", "Margaret", "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Dorothy", 
    "Donald", "Sandra", "Steven", "Ashley", "Paul", "Kimberly", "Andrew", "Donna", "Joshua", "Emily", 
    "Kenneth", "Michelle", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa", "Edward", "Deborah", 
    "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Laura", "Jeffrey", "Sharon", "Ryan", "Cynthia", 
    "Judah", "Scarlett", "Beckett",

    # Noms de villes ou pays
    "Paris", "Berlin", "Tokyo", "NewYork", "London", "Sydney", "Cairo", "Moscow", "Rome", "Dublin",
    "LosAngeles", "Chicago", "Houston", "Miami", "Toronto", "Vancouver", "Montreal", "Rio", "SaoPaulo", "BuenosAires",
    "Lima", "Bogota", "Santiago", "Madrid", "Barcelona", "Lisbon", "Amsterdam", "Brussels", "Zurich", "Geneva",
    "Vienna", "Prague", "Budapest", "Warsaw", "Athens", "Istanbul", "Dubai", "Doha", "Beijing", "Shanghai",
    "HongKong", "Seoul", "Bangkok", "Singapore", "KualaLumpur", "Jakarta", "Manila", "Hanoi", "HoChiMinh", "Mumbai",
    "Delhi", "Bangalore", "Chennai", "CapeTown", "Johannesburg", "Nairobi", "Lagos", "Casablanca", "Rabat", "Algiers",

    # Autres termes significatifs
    "Secure", "Password", "Hacker", "Enigma", "Cipher", "Matrix", "Wizard", "Galaxy", "Phantom", "Jupiter"
]

# Le vrai mot de passe du compte
true_password = "Secure*29"  # Remplacez par le vrai mot de passe à trouver

def randomize_string(s):
    # Transforme certains caractères en symboles ou chiffres aléatoirement, mais seulement parfois
    result = []
    for char in s:
        if random.random() < 0.3:  # 30% de chance de modifier le caractère
            if char.isalpha() and random.random() < 0.5:  # 50% de chance d'ajouter un symbole
                result.append(random.choice(symbols))
            elif char.isalpha() and random.random() >= 0.5:  # 50% de chance d'ajouter un chiffre
                result.append(random.choice(number))
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)

def add_number_to_name(s):
    # Ajoute un nombre aléatoire à la fin du nom
    return f"{s}{random.randint(10, 99)}"

# Utiliser pyfiglet pour afficher le texte en ASCII art avec une police plus petite
custom_fig = Figlet(font='small')
ascii_art_text = custom_fig.renderText('DEDSEC BF V2.0')

# Définir les informations à afficher dans le cadre
info = [
    "BY: 2806",
    "Telegram: t.me/Mr_2806",
    "Tiktok: dedsec_x.0",
    "Youtube: Dedsec assistant"
]

# Calculer la largeur du texte le plus large
max_width = max(len(line) for line in info)

# Création du cadre avec du texte bleu
border = "+" + "-" * (max_width + 2) + "+"
blue_text = "\033[91m"  # Couleur bleue du texte
reset = "\033[0m"  # Réinitialiser la couleur

# Afficher le texte ASCII art
print(f"\033[91m{ascii_art_text}\033[0m")


# Trouver la largeur de la console pour centrer le cadre
import shutil
terminal_width = shutil.get_terminal_size().columns
centered_padding = (terminal_width - (max_width + 4)) // 2

# Afficher le cadre centré avec texte blue
print("\n" * 2)  # Espacement avant le cadre
print(f"{' ' * centered_padding}{blue_text}{border}{reset}")
for line in info:
    print(f"{' ' * centered_padding}{blue_text}| {line.ljust(max_width)} |{reset}")
print(f"{' ' * centered_padding}{blue_text}{border}{reset}")

# Demander le nom de l'utilisateur
print("\033[92mEntrez votre nom :\033[0m", end="")
nom = input("\033[92m")

try:
    counter = 0  # Initialiser le compteur
    while True:
        # Choisir un type de mot de passe aléatoirement
        password_type = random.choice(["numbers_only", "numbers_with_letter", "letters_only"])

        if password_type == "numbers_only":
            # Mot de passe composé uniquement de chiffres
            password = ''.join(random.choices(number, k=8))

        elif password_type == "numbers_with_letter":
            # Mot de passe composé de 7 chiffres et une lettre
            digits = ''.join(random.choices(number, k=7))
            letter = random.choice(lower_case + upper_case)
            password = digits + letter
            password = ''.join(random.sample(password, len(password)))  # Mélanger les caractères

        elif password_type == "letters_only":
            # Mot de passe composé uniquement de lettres formant un mot significatif
            word = random.choice(significant_words)
            if counter % 5 == 0:  # Ajouter des chiffres tous les 5 mots de passe
                word = add_number_to_name(word)
            password = word

        # Incrémenter le compteur
        counter += 1

        # Modifier le mot de passe aléatoirement tous les 5 mots de passe
        if counter % 5 == 0:
            password = randomize_string(password)

        # Afficher le mot de passe généré en vert
        print(f"\033[92mVotre mot de passe est : {password}\033[0m")
        
        # Arrêter lorsque le mot de passe généré correspond au vrai mot de passe
        if password == true_password:
            print(f"\033[92mMot de passe correct trouvé : {password}\033[0m")
            break

except KeyboardInterrupt:
    # Code à exécuter lorsque Ctrl+C est pressé
    print("\nGénération de mots de passe interrompue.")