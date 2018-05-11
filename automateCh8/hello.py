import os

helloFile = open("/Users/josh.dematteo/Documents/notes.txt")

hello = helloFile.read()

print(os.path.exists('/Users/josh.dematteo/Documents'))

print(hello)
helloFile.close()