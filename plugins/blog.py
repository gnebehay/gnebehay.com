import os
import os.path

from os.path import join

class article:
    pass

def execute(jimd):
    BLOG_DIR = join(jimd.CNT_DIR, 'blog')
    articles = os.listdir(BLOG_DIR)

    output_dir = join(jimd.OUT_DIR, 'blog')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    article_list = []

    for art in articles:
        a = article()

        article_md = join(BLOG_DIR, art, 'index.md')

        html, meta = jimd.read_markdown(article_md)

        a.title = meta['title']
        a.date = meta['date']
        a.url = join('/blog/' + art)
        a.intro = html[:html.find('</p>') + 4]

        article_list.append(a)

    article_list = sorted(article_list, key = lambda p: p.date, reverse = True)

    content = jimd.env.get_template('blog.html').render(articles = article_list)

    dst_file = join(output_dir, 'index.html')

    with open(dst_file, 'w') as f:
        f.write(content)
