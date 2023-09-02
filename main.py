import sys
import markdown

html =  markdown.markdown(sys.argv[1])
with open(sys.argv[1], 'r') as md:
    mdtext = md.read()
    html = markdown.markdown(mdtext)
    with open(sys.argv[2], 'w') as output:
        output.write(html)
