pages = [
    {
        'filename': 'content/index.html',
        'title': 'index',
    },
    {
        'filename': 'content/resume.html',
        'title': 'resume',
    },
    {
        'filename': 'content/contact.html',
        'title': 'contact',
    },
]

def main():
    template = open('templates/base.html').read()


    for page in pages:
        content = open(page['filename']).read()
        full_page_contents = template.replace('{{content}}', content)
        full_page = str('docs/'+ page['title'] + '.html')
        open(full_page, 'w+').write(full_page_contents)



main()

#
#
# # Read in index HTML code
# content = open('content/index.html').read()
#
# # Combine template HTML code with index HTML code
# index_html = top_template + content + bottom_template
# open('index.html', 'w+').write(index_html)
#
# # Rinse and repeat, but with resume HTML code
# content = open('content/resume.html').read()
# resume_html = top_template + content + bottom_template
# open('resume.html', 'w+').write(resume_html)
#
# # And again, this time with contact HTML code
# content = open('content/contact.html').read()
# contact_html = top_template + content + bottom_template
# open('contact.html', 'w+').write(contact_html)
#
#
if __name__ == '__main__':
    main()
