#!/usr/bin/env python3

print("Content-type: text/html")
print(" ")

print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Menu Generationм</title>
        </head>
        <body>""")

print("<h1>Menu Generation for all OS presnt</h1>")
print("<label for = 'docker'>Choose a docker application</label>")
print("<select>")
import os
f= os.popen("docker registry ls").read()
for i in f:
     print("<option>{}</option>".format(i))
print("</select>")
print("""</body>
        </html>""")