import win32com.client
import pythoncom
import os, sys
import inspect
import sqlite3
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class XASessionEvents:
    status = False
    
    def OnLogin(self,code,msg):
        print("OnLogin : ", code, msg)
        XASessionEvents.status = True
    
    def OnLogout(self):
        print('OnLogout')

    def OnDisconnect(self):
        print('OnDisconnect')

class XAQueryEvents:
    status = False
    
    def OnReceiveData(self,szTrCode):
        print("OnReceiveData : %s" % szTrCode)
        XAQueryEvents.status = True
    
    def OnReceiveMessage(self,systemError,messageCode,message):
        print("OnReceiveMessage : ", systemError, messageCode, message)
        XAQueryEvents.status = True

class XARealEvents:
    pass


def login(id,pwd,cert='',url='demo.ebestsec.co.kr',svrtype=0,port=200001):
    '''
    return result, error_code, message, account_list, session
    '''
    session = win32com.client.DispatchWithEvents("XA_Session.XASession",XASessionEvents)
    result = session.ConnectServer(url,port)

    if not result:
        nErrCode = session.GetLastError()
        strErrMsg = session.GetErrorMessage(nErrCode)
        return (False,nErrCode,strErrMsg,None,session)
    
    # send a message
    session.Login(id,pwd,cert,svrtype,0)
    # wait the message of Login
    while XASessionEvents.status == False:
        pythoncom.PumpWaitingMessages()

    account_list = []
    num_of_account = session.GetAccountListCount()

    for i in range(num_of_account):
        account_list.append(session.GetAccountList(i))
    
    return (True,'','', account_list, session)


def t8424(gubun1=''):
    '''
    업종전체조회
    '''
    query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",XAQueryEvents)
    
    MYNAME = inspect.currentframe().f_code.co_name
    INBLOCK = "%sInBlock" % MYNAME
    OUTBLOCK = "%sOutBlock" % MYNAME
    OUTBLOCK1 = "%sOutBlock1" %MYNAME
    RESFILE = r"C:\eBEST\xingAPI\Res\%s.res"%MYNAME

    query.LoadFromResFile(RESFILE)
    query.SetFieldData(INBLOCK,"gubun1",0,gubun1)
    query.Request(0)
    
    while XAQueryEvents.status == False:
        pythoncom.PumpWaitingMessages()
    XAQueryEvents.status = False
    
    data = []
    block_count = query.GetBlockCount(OUTBLOCK)

    for i in range(block_count):
        hname = query.GetFieldData(OUTBLOCK,"hname",i).strip()
        upcode = query.GetFieldData(OUTBLOCK,"upcode",i).strip()
        lst = [hname,upcode]
        data.append(lst)

    df = pd.DataFrame(data=data,columns=['hname','upcode'])
    return df


def t1101(shcode):
    '''
    주식 현재가 호가 조회
    '''
    query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",XAQueryEvents)
    
    MYNAME = inspect.currentframe().f_code.co_name
    INBLOCK = "%sInBlock" % MYNAME
    OUTBLOCK = "%sOutBlock" % MYNAME
    OUTBLOCK1 = "%sOutBlock1" %MYNAME
    RESFILE = r"C:\eBEST\xingAPI\Res\%s.res"%MYNAME

    query.LoadFromResFile(RESFILE)
    query.SetFieldData(INBLOCK,"shcode",0,shcode)
    query.Request(0)
    
    while XAQueryEvents.status == False:
        pythoncom.PumpWaitingMessages()
    XAQueryEvents.status = False
    
    data = []
    block_count = query.GetBlockCount(OUTBLOCK)

    name_lst = ['hname','price','sign','change','diff','volume','jnilclose',
        'offerho1','bidho1','offerrem1','bidrem1','preoffercha1','prebidcha1',
        'offerho2','bidho2','offerrem2','bidrem2','preoffercha2','prebidcha2',
        'offerho3','bidho3','offerrem3','bidrem3','preoffercha3','prebidcha3',
        'offerho4','bidho4','offerrem4','bidrem4','preoffercha4','prebidcha4',
        'offerho5','bidho5','offerrem5','bidrem5','preoffercha5','prebidcha5',
        'offerho6','bidho6','offerrem6','bidrem6','preoffercha6','prebidcha6',
        'offerho7','bidho7','offerrem7','bidrem7','preoffercha7','prebidcha7',
        'offerho8','bidho8','offerrem8','bidrem8','preoffercha8','prebidcha8',
        'offerho9','bidho9','offerrem9','bidrem9','preoffercha9','prebidcha9',
        'offerho10','bidho10','offerrem10','bidrem10','preoffercha10','prebidcha10',
        'offer','bid','preoffercha','prebidcha','hotime','yeprice','yevolme',
        'yesign','yechange','yediff','tmoffer','tmbid','ho_status','shcode',
        'uplmtprice','dnlmtprice','open','high','low',
        ]

    for i in range(block_count):
        lst = []
        for name in name_lst:
            lst.append(query.GetFieldData(OUTBLOCK,name,i).strip())
        data.append(lst)

    df = pd.DataFrame(data=data,columns=name_lst)
    return df




if __name__ == '__main__':
    login(id='riew710',pwd='00aa')
    df = t8424()
    print(df)