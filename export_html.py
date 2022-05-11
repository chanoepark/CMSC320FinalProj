import glob
import os
import sys
from pathlib import PurePath

notebooks = glob.glob('./*.ipynb')

if len(notebooks) != 1:
    sys.exit('More than one ipynb file')

p = PurePath(notebooks[0])

if os.path.exists('index.html'):
    os.remove('index.html')

os.system(f'jupyter nbconvert --execute --to html {p.name}')
p = p.with_suffix('.html')
os.rename(p.name, 'index.html')