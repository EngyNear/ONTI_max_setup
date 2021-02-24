# -*- coding: utf-8 -*-
import os
cwd = os.path.dirname(os.path.realpath(__file__))
path = "/home/ubuntu/web-menu/templates/index.html"
ddns = "pioneermax.ddns.net"
edit_tag = "<!--edited for ONTI-->"

with open(path, 'r', encoding="utf-8") as file:
    check = file.readlines()

if check[-1]!=edit_tag:
    with open(cwd+"/original.html", 'w', encoding="utf-8") as file:
        file.writelines(check)

    with open(cwd+"/edit.html", 'r', encoding="utf-8") as file:
        data = file.readlines()
    
    if(input("Want to edit DNS? (y/n)")=='y'):
        ddns = input("Enter new dns: ")
    
    util_names = ["CodeOss", "Butterfly"]

    href1 = '                <a class="btn btn-outline-success" href="http://'
    href2 = '" style="left: 50%; position: sticky;">Открыть</a>'

    for name in util_names:
        port = input(name+" WAN port: ")
        if(name=="CodeOss"):
            data[75] = href1 + ddns + ":" + port + href2
        elif(name=="Butterfly"):
            data[90] = href1 + ddns + ":" + port + href2

    data.append("\n"+edit_tag)

    with open(path, 'w', encoding="utf-8") as file:
        data = file.writelines(data)
else:
    answer = input("HTML is already edited for ONTI\nWant to return the original version? (y/n)")
    if answer == 'y' or answer == 'yes':
        original = open(cwd+"/original.html")
        with open(path, 'w', encoding="utf-8") as file:
            file.writelines(original.readlines())
        original.close()
    elif answer == 'n' or answer == 'no':
        pass
    else:
        pass
