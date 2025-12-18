#!/usr/bin/env python3
"""
Script de conversion CV Markdown vers PDF via navigateur
Génère un HTML optimisé ATS et ouvre le navigateur pour export PDF
"""

import markdown
from pathlib import Path
import sys
import webbrowser

# HTML template avec style professionnel
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - Fares CHEHIDI - Backend Developer Python | ML Engineer</title>
    <style>
        @page {{
            size: A4;
            margin: 1.5cm;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            background: white;
            padding: 20px;
        }}
        
        h1 {{
            color: #2c3e50;
            font-size: 32px;
            margin-bottom: 5px;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        
        h2 {{
            color: #3498db;
            font-size: 20px;
            margin-top: 25px;
            margin-bottom: 15px;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }}
        
        h3 {{
            color: #2c3e50;
            font-size: 16px;
            margin-top: 15px;
            margin-bottom: 8px;
            font-weight: 600;
        }}
        
        h4 {{
            color: #555;
            font-size: 14px;
            margin-top: 10px;
            margin-bottom: 5px;
            font-style: italic;
        }}
        
        p {{
            margin-bottom: 10px;
            text-align: justify;
        }}
        
        ul {{
            margin-left: 20px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
            line-height: 1.5;
        }}
        
        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}
        
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 20px 0;
        }}
        
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        
        blockquote {{
            border-left: 3px solid #3498db;
            padding-left: 15px;
            margin: 15px 0;
            color: #555;
            font-style: italic;
        }}
        
        .contact-info {{
            font-size: 14px;
            color: #555;
            margin-bottom: 20px;
        }}
        
        .section-title {{
            background: #f8f9fa;
            padding: 8px 12px;
            border-radius: 4px;
            margin-top: 20px;
        }}
        
        ul li::marker {{
            color: #3498db;
        }}
        
        h2 + h3 {{
            margin-top: 10px;
        }}
        
        .emoji {{
            font-size: 1em;
        }}
        
        @media print {{
            body {{
                padding: 0;
            }}
            
            a {{
                color: #333;
            }}
            
            h2 {{
                page-break-after: avoid;
            }}
            
            h3 {{
                page-break-after: avoid;
            }}
        }}
        
        .tech-stack {{
            display: inline-block;
            background: #e8f4f8;
            color: #2c3e50;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.9em;
            margin: 2px;
        }}
        
        /* Instructions pour l'export PDF */
        .pdf-instructions {{
            background: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 20px;
        }}
        
        .pdf-instructions h3 {{
            color: #856404;
            margin-top: 0;
        }}
        
        .pdf-instructions ol {{
            margin-left: 20px;
        }}
        
        .pdf-instructions li {{
            margin-bottom: 5px;
        }}
        
        @media print {{
            .pdf-instructions {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="pdf-instructions">
        <h3>📄 Instructions pour générer le PDF compatible ATS</h3>
        <ol>
            <li><strong>Appuyez sur Ctrl+P</strong> (ou Cmd+P sur Mac)</li>
            <li>Sélectionnez <strong>"Enregistrer au format PDF"</strong> comme destination</li>
            <li>Activez <strong>"Arrière-plans graphiques"</strong> dans les options</li>
            <li>Vérifiez que les marges sont réglées sur <strong>1.5 cm</strong></li>
            <li>Cliquez sur <strong>"Enregistrer"</strong></li>
        </ol>
        <p><strong>✓ Le PDF généré sera compatible ATS :</strong> texte sélectionnable, liens cliquables</p>
    </div>
{content}
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
    pdf_file = script_dir / "Fares_Chehidi_CV_Backend_Developer.pdf"
    
    if not md_file.exists():
        print(f"❌ Erreur : Le fichier {md_file} n'existe pas")
        sys.exit(1)
    
    # Convertir en HTML
    print("🔄 Génération du HTML optimisé ATS...")
    convert_md_to_html(md_file, html_file)
    
    # Ouvrir dans le navigateur
    print("\n📄 Ouverture dans le navigateur...")
    print("   ✓ Texte sélectionnable (compatible ATS)")
    print("   ✓ Liens cliquables")
    print("\n⚠️  Suivez les instructions affichées dans le navigateur pour générer le PDF")
    
    webbrowser.open(html_file.absolute().as_uri())
    
    print(f"\n✅ HTML généré : {html_file.absolute()}")
    print(f"📝 PDF à enregistrer : {pdf_file.name}")

if __name__ == "__main__":
    main()
