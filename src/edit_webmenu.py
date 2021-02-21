# -*- coding: utf-8 -*-
path = "/home/ubuntu/web-menu/templates/index.html"
ddns = "pioneermax.ddns.net"
edit_tag = "<!--edited for ONTI-->"
with open(path, 'r', encoding="utf-8") as file:
    data = file.readlines()

if data[-1]!=edit_tag:
    util_names = ["CodeOss", "Butterfly"]

    href_line_nums = [87, 102]
    href_p1 = '                <a class="btn btn-outline-success" href="http://' 
    href_p2 = '" style="left: 50%; position: sticky;">Открыть</a>'

    i = 0
    for num in href_line_nums:
        data[num-1] = href_p1 + ddns + ":" + input(util_names[i]+ " WAN port: ") + href_p2
        i+=1

    remove_lines = [33, 34, 35]
    for j in range(108, 129):
        remove_lines.append(j)

    for line in remove_lines:
        data[line-1] = ""

    data.append("\n"+edit_tag)

    with open(path, 'w', encoding="utf-8") as file:
        data = file.writelines(data)
else:
    answer = input("HTML is already edited for ONTI\nWant to return the original version? (y/n)")
    if answer == 'y' or answer == 'yes':
        original = open("../src/original.html")
        with open(path, 'w', encoding="utf-8") as file:
            data = file.writelines(original.readlines())
        original.close()
    elif answer == 'n' or answer == 'no':
        pass
    else:
        pass