#!/usr/bin/env python3
"""
Script de conversion CV Markdown vers PDF avec formatage professionnel
"""

import markdown
from pathlib import Path
import sys

# HTML template avec style professionnel
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - Fares CHEHIDI</title>
    <style>
        @page {{{{
            size: A4;
            margin: 1.5cm;
        }}}}
        
        * {{{{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}}}
        
        body {{{{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            background: white;
            padding: 20px;
        }}}}
        
        h1 {{{{
            color: #2c3e50;
            font-size: 32px;
            margin-bottom: 5px;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}}}
        
        h2 {{{{
            color: #3498db;
            font-size: 20px;
            margin-top: 25px;
            margin-bottom: 15px;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }}}}
        
        h3 {{{{
            color: #2c3e50;
            font-size: 16px;
            margin-top: 15px;
            margin-bottom: 8px;
            font-weight: 600;
        }}}}
        
        h4 {{{{
            color: #555;
            font-size: 14px;
            margin-top: 10px;
            margin-bottom: 5px;
            font-style: italic;
        }}}}
        
        p {{{{
            margin-bottom: 10px;
            text-align: justify;
        }}}}
        
        ul {{{{
            margin-left: 20px;
            margin-bottom: 15px;
        }}}}
        
        li {{{{
            margin-bottom: 8px;
            line-height: 1.5;
        }}}}
        
        strong {{{{
            color: #2c3e50;
            font-weight: 600;
        }}}}
        
        a {{{{
            color: #3498db;
            text-decoration: none;
        }}}}
        
        a:hover {{{{
            text-decoration: underline;
        }}}}
        
        hr {{{{
            border: none;
            border-top: 1px solid #ddd;
            margin: 20px 0;
        }}}}
        
        code {{{{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}}}
        
        blockquote {{{{
            border-left: 3px solid #3498db;
            padding-left: 15px;
            margin: 15px 0;
            color: #555;
            font-style: italic;
        }}}}
        
        /* Style pour les sections spécifiques */
        .contact-info {{{{
            font-size: 14px;
            color: #555;
            margin-bottom: 20px;
        }}}}
        
        .section-title {{{{
            background: #f8f9fa;
            padding: 8px 12px;
            border-radius: 4px;
            margin-top: 20px;
        }}}}
        
        /* Style pour les listes de compétences */
        ul li::marker {{{{
            color: #3498db;
        }}}}
        
        /* Espacement des sections */
        h2 + h3 {{{{
            margin-top: 10px;
        }}}}
        
        /* Style pour les emojis (garder la taille normale) */
        .emoji {{{{
            font-size: 1em;
        }}}}
        
        /* Impression */
        @media print {{{{
            body {{{{
                padding: 0;
            }}}}
            
            a {{{{
                color: #333;
            }}}}
            
            h2 {{{{
                page-break-after: avoid;
            }}}}
            
            h3 {{{{
                page-break-after: avoid;
            }}}}
        }}}}
        
        /* Style pour les badges/tags */
        .tech-stack {{{{
            display: inline-block;
            background: #e8f4f8;
            color: #2c3e50;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.9em;
            margin: 2px;
        }}}}
    </style>
</head>
<body>
{{content}}
</body>
</html>
"""

def convert_md_to_html(md_file: Path, output_file: Path):
    """Convertit un fichier Markdown en HTML formaté"""
    
    # Lire le contenu Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convertir Markdown en HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'tables', 'toc']
    )
    
    # Insérer dans le template
    full_html = HTML_TEMPLATE.format(content=html_content)
    
    # Écrire le fichier HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✅ Fichier HTML créé : {output_file}")
    return output_file

def main():
    # Chemins
    script_dir = Path(__file__).parent
    md_file = script_dir / "Fares_Chehidi_CV_Backend_Developer.md"
    html_file = script_dir / "Fares_Chehidi_CV_Backend_Developer.html"
    
    if not md_file.exists():
        print(f"❌ Erreur : Le fichier {md_file} n'existe pas")
        sys.exit(1)
    
    # Convertir en HTML
    convert_md_to_html(md_file, html_file)
    
    print("\n📄 Pour générer le PDF :")
    print("1. Ouvrez le fichier HTML dans votre navigateur")
    print("2. Utilisez Ctrl+P (Imprimer)")
    print("3. Sélectionnez 'Enregistrer au format PDF'")
    print("4. Ajustez les marges si nécessaire")
    print(f"\n🌐 Fichier HTML : {html_file.absolute()}")

if __name__ == "__main__":
    main()
