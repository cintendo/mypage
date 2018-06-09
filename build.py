
import glob
import os
from jinja2 import Template
import markdown
import json


pages = []

all_html_pages = []
all_html_pages = glob.glob("content/*.md")

def createjson():
    data = json.dumps(pages)
    open('pages.json', "w+").write(data)

def main():

    template_html = open('templates/base.html').read()
    template = Template(template_html)
    pages_all = json.load(open('pages.json'))
    for page in all_html_pages:

        #create dictionary for each page with key 'filename'
        page_defined = {}

        pages.append(page_defined)
        # page_defined.update({'filename': str(page)})

        #update dictionary with 'title' using markdown
        content = open(page).read()
        md = markdown.Markdown(extensions=["markdown.extensions.meta"])
        html = md.convert(content)
        title = md.Meta["title"][0]
        page_defined.update({'title': str(title)})


    #all_html_pages[page].append(str(title))

        page_name = os.path.basename(page)
        name_only, extension = os.path.splitext(page_name)
        full_page = str('docs/'+ name_only + '.html')
        full_pagefile = str(name_only + '.html')
        page_defined.update({'filename': full_pagefile})

        html_results = template.render(
            content = html,
            pages = pages_all,
        )


        open(full_page, 'w+').write(html_results)

    # print(pages)

        # print(title, "by", author)
        # print(html)

    # index_html = open("content/index.html").read()
    # template_html = open("templates/base.html").read()



# #
#
if __name__ == '__main__':
    main()
    createjson()
