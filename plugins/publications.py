import os
import os.path
import shutil
import json

from os.path import exists, join

class publication:
    pass

PUBLIST_TPL = 'publist.html'
PUB_TPL = 'publication.html'

def execute(jimd):
    PUB_DIR = join(jimd.PROJ_DIR, 'publications')
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

            pdf_file = os.path.join(PUB_DIR, pub, pub + '.pdf')
            if exists(pdf_file):
                shutil.copy(pdf_file, pdf_file.replace(PUB_DIR, output_dir))
                p.pdf = pdf_file.replace(jimd.PROJ_DIR, '')

            bib_file = os.path.join(PUB_DIR, pub, pub + '.bib')
            if exists(bib_file):
                shutil.copy(bib_file, bib_file.replace(PUB_DIR, output_dir))
                p.bibfile = bib_file.replace(jimd.PROJ_DIR, '')

                #Read the file
                with open(bib_file) as f:
                    p.bibtex = f.read()

            content = jimd.env.get_template(PUB_TPL).render(pub=p, title=p.title)

            dst_file = join(p_dir, 'index.html')

            with open(dst_file, 'w') as f:
                f.write(content)

            publications.append(p)

    publications = sorted(publications, key = lambda p: p.date, reverse = True)

    content = jimd.env.get_template(PUBLIST_TPL).render(publications=publications, title='Publications')

    dst_file = join(output_dir, 'index.html')

    with open(dst_file, 'w') as f:
        f.write(content)
