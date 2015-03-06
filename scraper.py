from bs4 import BeautifulSoup
import urllib.request

FILE = open('RoyalNavyShipNames.txt','w')
root_url = 'http://wikipedia.org/wiki/List_of_ship_names_of_the_Royal_Navy_'
ship_urls = ['(A)','(B)','(C)','(D-F)','(G-H)','(I-L)','(M-N)','(O-Q)','(R-T)','(U-Z)']

for url in ship_urls:
    wiki_html = urllib.request.urlopen(root_url+url).read().decode('utf-8')
    soup = BeautifulSoup(wiki_html)
    links = soup.find_all('a')
    for link in links:
        title = str(link.get('title'))
        try:
            if title.startswith('HMS'):
                if '(page does not exist)' in title:
                    title = title[:title.index('(page does not exist)')]
                FILE.write(title)
                FILE.write('\n')
        except UnicodeEncodeError:
            continue
