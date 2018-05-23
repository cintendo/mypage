# First, get the template files
top_template = open('top.html').read()
bottom_template = open('bottom.html').read()

# Read in index HTML code
content = open('index.html').read()

# Combine template HTML code with index HTML code
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)

# Rinse and repeat, but with resume HTML code
content = open('resume.html').read()
resume_html = top_template + content + bottom_template
open('resume.html', 'w+').write(resume_html)

# And again, this time with contact HTML code
content = open('contact.html').read()
contact_html = top_template + content + bottom_template
open('contact.html', 'w+').write(contact_html)

