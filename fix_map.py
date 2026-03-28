import re

filepath = r'd:\Envato\vera virhov\klinika-premium.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<a href="https://maps\.google\.com" target="_blank" class="map-embed">.*?</a>'
replacement = '<div class="map-embed">\n          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2996.257219437874!2d19.809797011166342!3d41.325019799742456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x135031faa495061b%3A0x97cae56ace55ccdc!2sM1-%20KLINIKA%20VERA-VIRHOV!5e0!3m2!1sen!2s!4v1774650998275!5m2!1sen!2s" width="100%" height="260" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n        </div>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: Map embed replaced with iframe')
else:
    print('ERROR: Pattern not found')
