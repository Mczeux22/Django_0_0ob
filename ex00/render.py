import sys
import re


def render(template_filename):
    # Vérification de l'extension
    if not template_filename.endswith(".template"):
        print("Error: template file must have a .template extension")
        sys.exit(1)

    # Import des variables depuis settings.py
    try:
        import settings
        variables = vars(settings)
    except Exception as e:
        print("Error: could not import settings.py")
        sys.exit(1)

    # Lecture du fichier template
    try:
        with open(template_filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: template file not found")
        sys.exit(1)

    # Fonction de remplacement des variables
    def var_swap(match):
        key = match.group(1)
        return str(variables.get(key, match.group(0)))

    # Remplacement dans le contenu
    content = re.sub(r"\{(\w+)\}", var_swap, content)

    # Création du fichier de sortie
    output_filename = template_filename.replace(".template", ".html")
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fichier généré : {output_filename}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py fichier.template")
        sys.exit(1)

    template_filename = sys.argv[1]
    render(template_filename)


if __name__ == "__main__":
    main()
