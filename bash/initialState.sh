BASEDIR=$(dirname "$0")

sudo systemctl enable pioneer-bricks-wlan
python3 $BASEDIR/../src/default_webmenu.py