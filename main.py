import sys
import markdown
import os

mdpath = sys.argv[1]
if not os.path.exists(mdpath):
    raise sys.stdout.buffer.write(b'Input file does not exist')
htmlpath = sys.argv[2]

with open(mdpath, 'r') as mdinput:
    html = markdown.markdown(mdinput.read())

    with open(htmlpath, 'w') as htmloutput:
        htmloutput.write(html)
