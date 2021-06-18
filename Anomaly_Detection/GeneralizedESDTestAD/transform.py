import pandas as pd #데이터가 많아질 수록 속도가 느려지는데, 효율적으로 빠르게 저장하기 위해 pandas 사용
import pymysql
from datetime import datetime

def savecsv():
    start = datetime.now()
    print('start-time :', str(datetime.now())[:19])
    conn = pymysql.connect(host="",port=, user="",passwd="",db="raspi_db")
    query = "SELECT timestamp,temp FROM collect_data_dht11 WHERE uscd = 1;"

    df = pd.read_sql_query(query,conn)
    df.to_csv(r'temp_data.csv', index=False) #
    print('end-time : ',str(datetime.now())[:19])
    end = datetime.now()
    print('elapsed-time : ',end-start)

