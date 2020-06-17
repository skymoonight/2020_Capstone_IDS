# to create data, i use post
import requests
import json
# method1 : send all json and precess in restapi
    # it is more simple
    # django model set muse change

# method2 : send index json
    # ids sending time is longer # maybe check delay time

# want 2 extract
def send(result_csv):
    want_feature = ['Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol', 'Flow Duration', 'Flow Packets/s', 'Label']
    rename_want_feature = ['Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol', 'Flow Duration', 'Flow Packets/s', 'Label']

    # dataframe 2 json (str)
    df = result_csv
    to_json = df.to_json(orient='index') #str

    # str to dictionary
    dic_obj = json.loads(to_json)

    # bring all kinds key
    all_feature = dic_obj.keys()


    # rename columns in row for fit sqlite column name & delete white space, capital letter
    for i in range(len(rename_want_feature)):
        rename_want_feature[i] = rename_want_feature[i].replace(' ','')
        rename_want_feature[i] = rename_want_feature[i].replace('/','_')
        rename_want_feature[i] = rename_want_feature[i].lower()

    # row in rows
    for i in range(len(df)): #len(df)
        send_data = {}

        # extract row value by id
        row = dic_obj[str(i)]


        # make new senddata
        for k in range(len(want_feature)):
            send_data[rename_want_feature[k]] = row[want_feature[k]]

        # send one row
        r = requests.post('http://127.0.0.1:8000/admin/api/DjangoBoard/',data=send_data)

    print('[SUCCESS!]===============================')
