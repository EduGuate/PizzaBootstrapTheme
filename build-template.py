"""Build a portable static template download, with a finite nested download."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from io import BytesIO
root = Path(__file__).resolve().parent
names = ['index.html', 'styles.css', 'app.js', 'config.js', 'LICENSE', 'README.md', 'IMAGE-PROMPTS.md', 'build-template.py']
files = [root / name for name in names] + sorted((root / 'assets').glob('*.webp'))
buffer = BytesIO()
with ZipFile(buffer, 'w', ZIP_DEFLATED) as z:
    for path in files:
        z.write(path, path.relative_to(root))
with ZipFile(root / 'pizza-viva-template.zip', 'w', ZIP_DEFLATED) as z:
    for path in files:
        z.write(path, path.relative_to(root))
    z.writestr('pizza-viva-template.zip', buffer.getvalue())
print('Template ZIP built.')
