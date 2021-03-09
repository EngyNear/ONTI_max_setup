# ! /bin/bash
BASEDIR=$(dirname "$0")

sudo systemctl disable pioneer-bricks-wlan
sudo systemctl enable wlan-butterfly
sudo systemctl enable code-server-wlan
sudo systemctl enable web-wlan-menu

# sudo systemctl enable code-server-eth
# sudo systemctl enable eth-butterfly
# sudo systemctl enable web-eth-menu
python3 $BASEDIR/../src/edit_webmenu.py