import pymysql
import pandas as pd


conn = pymysql.connect(host='127.0.0.1',user='root',password='root1234', db='uipathrpa',port=3306,charset='utf8',use_unicode= True)
currency_ = []
wiresending_ = []
usdexchange_ = []
try :
    cursor = conn.cursor()
    
    sql= """select * from exrate"""
    cursor.execute(sql)
    conn.commit()
    exchange = cursor.fetchall()
    for i in exchange: # 공백으로 분리한 데이터를 각 항목별로 모아서 저장
        currency_.append(i[0])
        wiresending_.append(i[1])
        usdexchange_.append(i[2])

    s_currency = pd.Series(currency_)
    s_wiresending = pd.Series(wiresending_)
    s_usdexchange = pd.Series(usdexchange_)
    df_exchange = pd.DataFrame(
        {
            'Currency':s_currency,
            'WireSending':s_wiresending,
            'USDExchange':usdexchange_
        }
    )
    print(df_exchange)

except Exception as e :
    print('db 연동 실패 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()