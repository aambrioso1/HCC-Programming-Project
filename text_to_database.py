"""
Retrieves a data base of text and creates a list of words.
"""

import re
from collections import Counter
import requests
def words(text): return re.findall(r'\w+', text.lower())



r = requests.get('https://norvig.com/big.txt')
txt = r.text

WORDS = Counter(words(txt))

print(f'most common words {WORDS.most_common(100)}')

