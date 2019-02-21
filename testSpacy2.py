#sudo apt install python3-pip
#pip3 install -U spacy
#python3 -m spacy download es
#pip3 install beautifulsoup4
#pip3 install html5lib
#pip3 install IPython
#pip3 install metakernel
#python3 -m pip install --upgrade pip
#python3 -m pip install jupyter
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
# pprint([(X.text, X.label_) for X in doc.ents])
# pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

from bs4 import BeautifulSoup
import requests
import re

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
len(article.ents)
labels = [x.label_ for x in article.ents]
Counter(labels)
items = [x.text for x in article.ents]
pprint(Counter(items).most_common(3))
sentences = [x for x in article.sents]
print(sentences[20])
displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')