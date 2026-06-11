import os
import re

portfolio_dir = r"g:\Deta\HYSTORIA\Assets\portfolio"
html_path = r"g:\Deta\HYSTORIA\index.html"

files = [f for f in os.listdir(portfolio_dir) if f.endswith(('.jpg', '.webp', '.png'))]

html_fragments = []
for idx, f in enumerate(files):
    if idx < 6:
        delay = (idx % 3) + 1
        html_fragments.append(f'''                <div class="portfolio-item reveal delay-{delay}">
                    <img src="Assets/portfolio/{f}" alt="Portfolio {idx+1}" class="gallery-img">
                </div>''')
    else:
        if idx == 6:
            html_fragments.append('                <!-- Extra Hidden Items -->')
        html_fragments.append(f'''                <div class="portfolio-item hidden-item">
                    <img src="Assets/portfolio/{f}" alt="Portfolio {idx+1}" class="gallery-img">
                </div>''')

new_gallery_html = '<div class="portfolio-gallery">\n' + '\n'.join(html_fragments) + '\n            </div>'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace between <div class="portfolio-gallery"> and the next </div> that matches its indentation
# We know it ends before '<div class="text-center reveal"'
pattern = re.compile(r'<div class="portfolio-gallery">.*?</div>\s*<div class="text-center reveal"', re.DOTALL)
new_content = pattern.sub(new_gallery_html + '\n            \n            <div class="text-center reveal"', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated HTML with", len(files), "portfolio images.")
