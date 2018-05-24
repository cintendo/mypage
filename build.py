# First, get the template files
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# Read in index HTML code
content = open('content/index.html').read()

# Combine template HTML code with index HTML code
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)

# Rinse and repeat, but with resume HTML code
content = open('content/resume.html').read()
resume_html = top_template + content + bottom_template
open('resume.html', 'w+').write(resume_html)

# And again, this time with contact HTML code
content = open('content/contact.html').read()
contact_html = top_template + content + bottom_template
open('contact.html', 'w+').write(contact_html)
