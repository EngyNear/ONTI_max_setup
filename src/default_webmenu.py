import os
cwd = os.path.dirname(os.path.realpath(__file__))
path = "/home/ubuntu/web-menu/templates/index.html"
original = open(cwd+"/original.html")
with open(path, 'w', encoding="utf-8") as file:
    data = file.writelines(original.readlines())
original.close()