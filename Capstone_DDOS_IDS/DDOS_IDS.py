from scapy.all import sniff
from os import rename, listdir
from scapy.utils import PcapWriter
from datetime import datetime
from subprocess import call
# this file is main
# models
from ae import *
import sendjson
# global

packetcont = 0
buf = scapy.plist.PacketList()
filename = "./packet/pcap/packet.pcap"
# name : date
# question : to decrese packet loss, is it the best solution to use index or just empty buf?
# scapy.plist.PacketList() as packetList

def ext_feature():
    # subprocess
    global filename
    subprocess.call(['./CICFlowMeter-4.0/bin/cfm', filename , './packet/csv/exfeature'])

# last solution async
def save():
    global buf
    global filename
    #filename = "/home/seleuchel/libcap/packet/"+"packet_" + str(filenum) + ".pcap"

    pktdump = PcapWriter(filename, append=True, sync=True)
    pktdump.write(buf)
    buf = []
    filenum += 1

def showPacket(packet):
# method 1 : save pcap and convert csv
# method 2 : input data into csv
# find csv output module
# first all wirte
# second time save
    global packetcont
    global model


    # traffic info
    timestamp = datetime.fromtimestamp(packet[0][1].time)
    print(packet[0][1])
    print('timestamp:',timestamp)
    print('Now packetcont:',packetcont)
    print('------------------------------------------------------')

    # seleuchel edit - save packet in real time
    filename = "./packet/pcap/packet.pcap"
    pktdump = PcapWriter(filename, append=True, sync=True)
    pktdump.write(packet)
    packetcont += 1

    if packetcont >= 1000:
        # extract pcap -> csv
        ext_feature()
        #model test
        model = AutoEncoder('./packet/csv/exfeature/packet.pcap_Flow.csv')
        result_csv = model.get_result()
        print(result_csv)

        #send to server
        sendjson.send(result_csv)
        packetcont = 0

def main():
    sniff(prn = showPacket, count = 0)

if __name__ == '__main__':
    main()
