# -*- coding: utf-8 -*-
path = "/home/ubuntu/geoscan_ws/src/gs_camera/launch/camera.launch"
change = '        <param name="interface" value="eth0"/>'

with open(path, 'r', encoding="utf-8") as file:
    lines = file.readlines()
lines[6] = change

with open(path, 'w', encoding="utf-8") as file:
    file.writelines(lines)
