import os
import os.path
import shutil
import json
import urllib

from urllib.request import urlopen

from os.path import exists, join

class publication:
    pass

PUBLIST_TPL = 'publist.html'
PUB_TPL = 'publication.html'

def configure(jimd, config):

    pub_config = config['publications']

    if 'PDF_DIR' in pub_config:
        jimd.PDF_DIR = pub_config['PDF_DIR']

        if not os.path.exists(jimd.PDF_DIR):
            print('WARNING: PDF_DIR {} does not exist')

    else:
        print('WARNING: PDF_DIR not set, unable to retrieve publications')

def export_article(article_id, outfile):

    delete = ['abstract', 'citeulike-article-id', 'posted-at', 'priority', 'citeulike-linkout-0',
              'citeulike-linkout-1']

    site = 'http://www.citeulike.org/bibtex/user/gnebehay/article/' + str(article_id)

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) ' +
           'Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = urllib.request.Request(site, headers=hdr)
    response = urlopen(req)
    html = response.read().decode()

    # Remove unneccessary fields
    print('Remove unneccessary fields')

    # My favourite python line so far.
    bibtex = '\n'.join([line for line in html.split('\n') if all([(entry + ' = ' not in line)
                        for entry in delete])])

    # Remove whitespace
    bibtex = bibtex.strip()

    with open(outfile, 'w') as f:
        f.write(bibtex)

def fetch(jimd):
    pub_dir = os.path.join(jimd.PRJ_DIR, 'publications')
    publications = os.listdir(pub_dir)
    for publication in publications:
        with open(os.path.join(pub_dir, publication, 'index.json'), 'r') as f:
            data = json.load(f)
            if 'citeulike_id' in data.keys():
                article_id = data['citeulike_id']
                outfile = os.path.join(pub_dir, publication, publication + '.bib')
                export_article(article_id, outfile)


def build(jimd):
    PUB_DIR = join(jimd.PRJ_DIR, 'publications')
    pubs = os.listdir(PUB_DIR)

    output_dir = join(jimd.OUT_DIR, 'publications')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    publications = []

    for pub in pubs:
        pub_file = os.path.join(PUB_DIR, pub, 'index.json')
        with open(pub_file) as f:
            p = publication()
            j = json.load(f)

            p.title = j['title']
            p.authors = j['authors']
            p.published = j['published']
            p.abstract = j['abstract']
            p.date = j['date']
            if 'code' in j:
                p.code = j['code']
            if 'url' in j:
                p.project = j['url']
            if 'note' in j:
                p.note = j['note']

            p.url = '/publications/' + pub

            p_dir = join(output_dir, pub)

            if not exists(p_dir):
                os.mkdir(p_dir)

            pdf_file = os.path.join(jimd.PDF_DIR, pub + '.pdf')
            if exists(pdf_file):
                shutil.copy(pdf_file, p_dir)
                p.pdf = os.path.join(pub, pub + '.pdf')

            bib_file = os.path.join(PUB_DIR, pub, pub + '.bib')
            if exists(bib_file):
                shutil.copy(bib_file, bib_file.replace(PUB_DIR, output_dir))
                p.bibfile = bib_file.replace(jimd.PRJ_DIR, '')

                # Read the file
                with open(bib_file) as f:
                    p.bibtex = f.read()

            content = jimd.env.get_template(PUB_TPL).render(pub=p, title=p.title)

            dst_file = join(p_dir, 'index.html')

            with open(dst_file, 'w') as f:
                f.write(content)

            publications.append(p)

    publications = sorted(publications, key=lambda p: p.date, reverse=True)

    content = jimd.env.get_template(PUBLIST_TPL).render(publications=publications, title='Publications')

    dst_file = join(output_dir, 'index.html')

    with open(dst_file, 'w') as f:
        f.write(content)
