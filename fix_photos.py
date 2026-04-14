import re

IMG_STYLE = 'width:100%;height:100%;object-fit:cover;object-position:top;display:block;'

DOCS = [
    ('1b3a6b', 'img/doc-artan.jpg', 'Dr. Artan Hoxha',  'Artan+Hoxha',  '1b3a6b'),
    ('4a1942', 'img/doc-besa.jpg',  'Dr. Besa Malaj',   'Besa+Malaj',   '4a1942'),
    ('0f3d2b', 'img/doc-erion.jpg', 'Dr. Erion Cela',   'Erion+Cela',   '0f3d2b'),
    ('4a3000', 'img/doc-lira.jpg',  'Dr. Lira Gjoka',   'Lira+Gjoka',   '4a3000'),
]

def replace_silhouettes(content):
    for color, src, alt, name_param, bg in DOCS:
        fallback = f'https://ui-avatars.com/api/?name={name_param}&size=400&background={bg}&color=fff&font-size=0.35'
        img_tag = f'<img src="{src}" alt="{alt}" onerror="this.src=\'{fallback}\'" style="{IMG_STYLE}">'
        pattern = rf'<div class="doc-silhouette"[^>]*{color}[^>]*>.*?</div>\s*<div class="doc-initial">[^<]*</div>\s*</div>'
        content = re.sub(pattern, img_tag, content, flags=re.DOTALL)
    return content

for fname in ['index.html', 'stafi.html']:
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    new_c = replace_silhouettes(c)
    if new_c != c:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f'SUCCESS: {fname}')
    else:
        print(f'NO MATCH: {fname}')
