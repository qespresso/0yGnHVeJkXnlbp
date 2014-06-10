sudo apt-get install git gcc make libpcap-dev

sudo apt-get install python-pip

sudo apt-get install python-paramiko

sudo pip install ecdsa

git clone https://github.com/robertdavidgraham/masscan

cd masscan

make

sudo make install


============
grep -oP  "([0-9]{1,3}\.){3}[0-9]{1,3}"  open.txt > openip.txt 
