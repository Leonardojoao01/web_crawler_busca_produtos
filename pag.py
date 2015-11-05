import urllib

f = urllib.urlopen("http://codare.net")
contents = f.read()
f.close()
print contents