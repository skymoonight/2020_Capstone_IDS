import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from sklearn import metrics
import pandas as pd
import numpy as np

def proto2str(result_data):
    proto = ['HOPOPT','ICMP','IGMP','GGP','IPv4','ST','TCP','CBT','EGP','IGP',\
    'BBN-RCC-MON','NVP-II','PUP','ARGUS (deprecated)','EMCON','XNET','CHAOS',\
    'UDP','MUX','DCN-MEAS','HMP', 'PRM','XNS-IDP','TRUNK-1','TRUNK-2','LEAF-1',\
    'LEAF-2','RDP','IRTP','ISO-TP4','NETBLT','MFE-NSP','MERIT-INP','DCCP','3PC',\
    'IDPR','XTP','DDP','IDPR-CMTP','TP++','IL','IPv6','SDRP','IPv6-Route','IPv6-Frag',\
    'IDRP','RSVP','GRE','DSR','BNA','ESP','AH','I-NLSP','SWIPE (deprecated)','NARP',\
    'MOBILE','TLSP','SKIP','IPv6-ICMP','IPv6-NoNxt','IPv6-Opts','UNKNOWN''CFTP','UNKNOWN',\
    'SAT-EXPAK','KRYPTOLAN','RVD','IPPC','UNKNOWN','SAT-MON','VISA','IPCV','CPNX','CPHB',\
    'WSN','PVP','BR-SAT-MON','SUN-ND','WB-MON','WB-EXPAK','ISO-IP','VMTP','SECURE-VMTP',\
    'VINES','TTP','IPTM','NSFNET-IGP','DGP','TCF','EIGRP','OSPFIGP','Sprite-RPC','LARP',\
    'MTP','AX.25','IPIP','MICP (deprecated)','SCC-SP','ETHERIP','ENCAP','UNKNOWN','GMTP',\
    'IFMP','PNNI','PIM','ARIS','SCPS','QNX','A/N','IPComp','SNP','Compaq-Peer','IPX-in-IP',\
    'VRRP','PGM','UNKNOWN','L2TP','DDX','IATP','STP','SRP','UTI','SMP','SM (deprecated)',\
    'PTP','ISIS over IPv4','FIRE','CRTP','CRUDP','SSCOPMCE','IPLT','SPS','PIPE','SCTP',\
    'RSVP-E2E-IGNORE','Mobility Header','UDPLite','MPLS-in-IP','manet','HIP','Shim6','WESP',\
    'ROHC','Ethernet']

        # 인덱스에 있으면 그걸로 변환, 없으면 UNKNOWN
    for i in range(len(result_data)):
            # out of index set.
        protonum = result_data['Protocol'][i]

        if protonum >= len(result_data):
            result_data['Protocol'][i] = 'UNKNOWN'
        else:
            result_data['Protocol'][i] = proto[protonum]

    return result_data

class AutoEncoder():
    #data = ""
    #temp = ""
    def __init__(self, test_data_path):
        #self.model_path = '/home/seleuchel/libcap/model/model.h5'
        self.data=pd.read_csv(test_data_path)
        self.temp=pd.read_csv(test_data_path)
        self.first = True

    def preprocess(self):
        data1=self.data[['Flow Duration', 'Total Length of Fwd Packet',
        'Fwd Packet Length Max', 'Fwd Packet Length Min',
        'Fwd Packet Length Mean','Fwd Packet Length Std',
        'Bwd Packet Length Max','Bwd Packet Length Mean',
        'Bwd Packet Length Std','Flow Packets/s','Flow IAT Mean',
        'Flow IAT Std','Flow IAT Max','Fwd IAT Total','Fwd IAT Mean',
        'Fwd IAT Std','Fwd IAT Max','Bwd IAT Total','Bwd IAT Mean',
        'Bwd IAT Std','Bwd IAT Max','Packet Length Max',
        'Packet Length Mean','Packet Length Std','Packet Length Variance',
        'Down/Up Ratio','Average Packet Size','Fwd Segment Size Avg',
        'Bwd Segment Size Avg','Subflow Fwd Bytes','Fwd Act Data Pkts',
        'Idle Mean','Idle Max','Idle Min']]
        data2 = self.temp
        data2 = data2.dropna(axis=0)
        data1 = data1.dropna(axis=0)

        a = data2['Flow Packets/s']=='Infinity'
        a2 = data2['Flow Bytes/s']=='Infinity'
        b = data1['Flow Packets/s']=='Infinity'
        #data1 = data1[~a]
        data1 = data1[~b]
        self.temp = data2[~a]
        self.temp = data2[~a2]

        #data_norm = (data1-data1.min())/(data1.max()-data1.min())
        return data1

    def load(self):
        input_data = self.preprocess()
        min_max_scaler = MinMaxScaler()
        norm_data = min_max_scaler.fit_transform(input_data)
        norm_data = pd.DataFrame(norm_data,columns=input_data.columns,index=list(input_data.index.values))

        threshold = 0.25#0.0002768409243105919
        model = load_model('./model/model.h5')
        predictions = model.predict(norm_data)
        mse = np.mean(np.power(norm_data-predictions,2),axis=1)
        error_df = pd.DataFrame({'Reconstruction_error':mse})
        pred_y = [1 if e>threshold else 0 for e in error_df['Reconstruction_error'].values]

        return pred_y


    def get_result(self):
        result = self.load()
        result_data = self.temp
        result_data['Label'] = result

        # preprocessing before sending
        result_data = proto2str(result_data)

        #save to csv - all feature
        if(self.first == True):
            result_data.to_csv('./packet/csv/predict/predict.csv',mode='a',header=True, index=False)
            self.first = False
        else:
            result_data.to_csv('./packet/csv/predict/predict.csv',mode='a',header=False, index=False)

        return result_data
