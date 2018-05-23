# Get Template Files
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# readin index.html
content = open('content/index.html').read()

#for index html
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)

# for resume html
content = open('content/resume.html').read()
resume_html = top_template + content + bottom_template
open('resume.html', 'w+').write(resume_html)

# for contact html
content = open('content/contact.html').read()
contact_html = top_template + content + bottom_template
open('contact.html', 'w+').write(contact_html)
