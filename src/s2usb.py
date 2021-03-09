# -*- coding: utf-8 -*-
path = "/home/ubuntu/geoscan_ws/src/gs_core/launch/pioneer.launch"
change = '        <param name="port" value="/dev/ttyUSB0"/>\n'

with open(path, 'r', encoding="utf-8") as file:
    lines = file.readlines()
lines[3] = change

with open(path, 'w', encoding="utf-8") as file:
    file.writelines(lines)
