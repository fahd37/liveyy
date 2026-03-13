import os
from datetime import datetime

# --- CONFIGURATION ---
# Replace with your actual project URL (e.g., https://yourusername.github.io/your-repo)
BASE_URL = "https://fahd37.github.io/liveyy"
# The folder containing your files
CONTENT_DIR = "assets" 

def generate_matrix():
    print(f"🔍 Scanning '{CONTENT_DIR}' directory...")
    
    # Ensure the directory exists
    if not os.path.exists(CONTENT_DIR):
        print(f"⚠️ Directory '{CONTENT_DIR}' not found. Exiting.")
        return

    # Grab all files in the directory
    files = [f for f in os.listdir(CONTENT_DIR) if os.path.isfile(os.path.join(CONTENT_DIR, f))]
    
    if not files:
        print("⚠️ No files found to index.")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    # 1. BUILD THE HTML HUB
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Official Content Directory</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; max-width: 800px; }}
        a {{ color: #0366d6; text-decoration: none; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
        ul {{ list-style-type: square; }}
    </style>
</head>
<body>
    <h1>📂 Document Archive</h1>
    <p>Last updated: {today}</p>
    <ul>
"""
    for f in files:
        html_content += f'        <li><a href="{CONTENT_DIR}/{f}">{f}</a></li>\n'
    html_content += """    </ul>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ Successfully built index.html")

    # 2. BUILD THE XML SITEMAP
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Add the Hub page itself (Highest Priority)
    xml_content += f"""    <url>
        <loc>{BASE_URL}/index.html</loc>
        <lastmod>{today}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>\n"""

    # Add all the individual files
    for f in files:
        xml_content += f"""    <url>
        <loc>{BASE_URL}/{CONTENT_DIR}/{f}</loc>
        <lastmod>{today}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>\n"""
    
    xml_content += '</urlset>'

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("✅ Successfully built sitemap.xml")

if __name__ == "__main__":
    generate_matrix()