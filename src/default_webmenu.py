path = "/home/ubuntu/web-menu/templates/index.html"
original = open("../src/original.html")
with open(path, 'w', encoding="utf-8") as file:
    data = file.writelines(original.readlines())
original.close()