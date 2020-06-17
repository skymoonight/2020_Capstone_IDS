#!/bin/bash

#git clone 
# please, ture to public before 

#install pip
sudo apt-get install python3-pip -y

#pip version up
pip3 install --upgrade pip


#IDS : MODULE
sudo apt install default-jre -y
sudo apt install libpcap-dev -y

#IDS : pip3
pip3 install tensorflow==1.15
pip3 install sklearn
pip3 install pandas
pip3 install scapy

#DJANGO 
pip3 install django
pip3 install django-rest-framework

# start
# 1. startdjango server 
# sudo python3 manage.py runserver
# 2. start IDS
# cd Capstone_DDOS_IDS
# sudo python3 DDOS_IDS.py

cd mysite
sudo python3 manage.py runserver &
cd ..
cd Capstone_DDOS_IDS
sudo python3 DDOS_IDS.py


