BASEDIR=$(dirname "$0")

sh $BASEDIR/enableNetworkManager.sh
python3 $BASEDIR/../src/usb2s.py
python3 $BASEDIR/../src/camera2wlan.py

sudo nmcli device wifi connect "OlyNTI" password "mospolytech1" name "ONTI"
sudo nmcli con up "OlyNTI"

sh $BASEDIR/start_wlan_services.sh
python3 $BASEDIR/../src/restart_s.py