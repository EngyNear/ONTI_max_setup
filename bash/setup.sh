#! /bin/bash
sudo systemctl disable pioneer-bricks-wlan
sudo systemctl stop pioneer-bricks-wlan
sh ./enableNetworkManager.sh
python3 ../src/edit_webmenu.py