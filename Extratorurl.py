from urllib.parse import urlparse

def extraire_domaine_sans_www(url):
    """Extrait le domaine principal d'une URL sans le 'www'"""
    try:
        # Ajoute https:// si pas de protocole
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        parsed = urlparse(url)
        domaine = parsed.netloc
        
        # Supprimer le www si présent
        if domaine.startswith('www.'):
            domaine = domaine[4:]
            
        return domaine
    except:
        return None

# Demander le format de sortie
print("=== EXTRACTEUR DE DOMAINES ===\n")
print("Choix du format de sortie :")
print("1 - Sans http:// (ex: google.com)")
print("2 - Avec http:// (ex: http://google.com)")
print("3 - Avec https:// (ex: https://google.com)")

choix = input("\nTon choix (1, 2 ou 3) : ").strip()

# Lire les URLs depuis urls.txt
with open('urls.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()

# Extraire les domaines
domaines = []
for url in urls:
    url = url.strip()
    if url:  # Ignorer les lignes vides
        domaine = extraire_domaine_sans_www(url)
        if domaine:
            domaines.append(domaine)

# Supprimer les doublons et trier
domaines_uniques = sorted(set(domaines))

# Ajouter le préfixe selon le choix
prefixe = ""
if choix == "2":
    prefixe = "http://"
elif choix == "3":
    prefixe = "https://"

# Afficher les résultats
print("\n" + "="*40)
print("Domaines extraits :")
print("-" * 30)
for domaine in domaines_uniques:
    print(f"• {prefixe}{domaine}")

print(f"\n✅ {len(domaines_uniques)} domaines trouvés")

# Sauvegarder dans resultat.txt
with open("resultat.txt", "w") as f:
    for domaine in domaines_uniques:
        f.write(f"{prefixe}{domaine}\n")

print(f"📁 Résultats sauvegardés dans 'resultat.txt' (format: {prefixe or 'sans http'})")