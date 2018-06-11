
import glob
import os
from jinja2 import Template
import markdown
import json

pages = []
all_html_pages = []
all_html_pages = glob.glob("content/*.md")
#
#
def generate_docs():
    for page in all_html_pages:
        content = open(page).read()
        md = markdown.Markdown(extensions=["markdown.extensions.meta"])
        html = md.convert(content)
        title = md.Meta[" title"][0]
        page_name = os.path.basename(page)
        name_only, extension = os.path.splitext(page_name)
        full_page = str('docs/'+ name_only + '.html')
        full_pagefile = str(name_only + '.html')
        pages.append(full_pagefile)
    return html, title
#

def main():

    template_html = open('templates/base.html').read()
    template = Template(template_html)

    # pages_all = json.load(open('pages.json'))
    generate_docs()

    for page in all_html_pages: 
        html_results = template.render(
            content = html,
            title = title,
            pages = pages,
            file_name = full_page,
        )

        open(str('docs/'+ name_only + '.html'), 'w+').write(html_results)


        print(pages)
        # print(full_page)
        # print(full_pagefile)
        # print(all_html_pages)


    # print(pages)

        # print(title, "by", author)
        # print(html)

    # index_html = open("content/index.html").read()
    # template_html = open("templates/base.html").read()



# #
#
if __name__ == '__main__':
    main()
    # createjson()
