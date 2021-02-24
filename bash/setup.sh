# ! /bin/bash
BASEDIR=$(dirname "$0")

sudo systemctl disable pioneer-bricks-wlan
sudo systemctl stop pioneer-bricks-wlan
python3 $BASEDIR/../src/edit_webmenu.py