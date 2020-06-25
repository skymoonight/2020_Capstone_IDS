import serial
import pymysql

ser = serial.Serial('/dev/ttyACM0',9600)
DB = pymysql.connect(
    host='localhost',
    port = 3306,
    user='user',
    password='1234',
    db='capston'
)

db_curs = DB.cursor()
i = 0
while True:
    try:
        RMSCurrent = 0.0
        RMSPower = 0.0
        kilos = 0.0
        peakPower = 0.0
        ele = 0
        while True:
            # get data
            dataline = ser.readline()
            print(dataline.decode('ascii'))
            dataline = dataline.decode('ascii')

            if ('RMSCurrent' in dataline) and (ele == 0):
                RMSCurrent = dataline.split(":")[-1]
                RMSCurrent = float(RMSCurrent)
                ele += 1
            elif ('RMSPower' in dataline) and (ele == 1):
                RMSPower = dataline.split(":")[-1]
                RMSPower = float(RMSPower)
                ele +=1
            elif ('kilos' in dataline) and (ele == 2):
                kilos = dataline.split(":")[-1]
                kilos = float(kilos)
                ele += 1
            elif ('peakPower' in dataline) and (ele == 3):
                peakPower = dataline.split(":")[-1]
                peakPower = float(peakPower)
                ele += 1
            elif ('========' in dataline) and ( ele > 3):
                # save DB
                sql = """insert into info (RMSCurrent, RMSPower, kilos, peakPower) values (%f,%f,%f,%f)""" % (RMSCurrent, RMSPower, kilos, peakPower)
                print(type(RMSCurrent))
                print(type(RMSPower))
                print(type(kilos))
                print("%f"%(RMSCurrent))
                print(type(peakPower))
                db_curs.execute(sql)
                print("OK : ", RMSCurrent, RMSPower, kilos, peakPower)
                DB.commit()
                break;
            else:
                print("something wrong : ", ele) # remove all []
                break;

    except KeyboardInterrupt:
        print("U close program by key interrupt (Ctrl + C)")
        exit(1)
print("Program ended")
