BASEDIR=$(dirname "$0")

python3 $BASEDIR/../src/s2usb.py
python3 $BASEDIR/../src/camera2eth.py

# sudo nmcli device wifi connect "OlyNTI" password "mospolytech1" name "ONTI"
sudo nmcli con down "OlyNTI"

sh $BASEDIR/start_eth_services.sh
python3 $BASEDIR/../src/restart_usb.py