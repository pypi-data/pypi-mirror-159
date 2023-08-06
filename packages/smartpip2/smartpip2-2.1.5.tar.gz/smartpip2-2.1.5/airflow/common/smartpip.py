import os #line:2
import requests #line:3
import time #line:4
import json #line:5
import re #line:6
import subprocess #line:7
import logging #line:8
try :#line:9
    from kafka import KafkaConsumer ,TopicPartition #line:10
except :#line:11
    logging .warning ('you need pip install kafka-python')#line:12
os .environ ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'#line:14
requests .packages .urllib3 .disable_warnings ()#line:15
from airflow .settings import ETL_FILE_PATH ,KETTLE_HOME ,HIVE_HOME ,P_URL ,DATASET_TOKEN ,REFRESH_TOKEN #line:17
from airflow .utils .email import fun_email ,list_email #line:18
from airflow .common .datax import datax_cmdStr #line:19
_OO0O00O000O0OO0O0 =f'{P_URL}/echart/dataset_api/?token={DATASET_TOKEN}&visitor=Airflow&type='#line:22
_O0O00O0OO0OO0OOOO =f'{P_URL}/echart/refresh_ds/?token={REFRESH_TOKEN}&type='#line:23
class SmartPipError (Exception ):#line:25
    def __init__ (OO000000OOO0O0OO0 ,err ='SmartPip Error'):#line:26
        Exception .__init__ (OO000000OOO0O0OO0 ,err )#line:27
def smart_upload (OOO000OO0O00O0000 ):#line:30
    OO00O0O0O0O00O000 ,OOO00O0OO0000OO0O =os .path .split (OOO000OO0O00O0000 )#line:31
    OOO00O0OO0000OO0O =OOO00O0OO0000OO0O .split ('.')[0 ]#line:32
    O0O00OO0OO00OOOO0 ={"title":OOO00O0OO0000OO0O ,"token":DATASET_TOKEN ,"visitor":"Airflow"}#line:37
    O0OO00000OO000O00 ={'file':open (OOO000OO0O00O0000 ,'rb')}#line:38
    O0O0000O0OO0O000O =f'''{P_URL}/echart/dataset_api/?type=506&visitor=Airflow&token={DATASET_TOKEN}&param={{"uptime":"{time.time()}","filename":"{OOO00O0OO0000OO0O}"}}'''#line:39
    OOOOOO0OOOOO000OO =60 #line:40
    OO00O0O00O00OO00O =requests .post (f'{P_URL}/etl/api/upload_file_api/',files =O0OO00000OO000O00 ,data =O0O00OO0OO00OOOO0 )#line:42
    print (OO00O0O00O00OO00O .status_code )#line:43
    if OO00O0O00O00OO00O .status_code ==200 :#line:44
        OO00O0O00O00OO00O =OO00O0O00O00OO00O .json ()#line:45
    elif OO00O0O00O00OO00O .status_code ==504 :#line:46
        print ('timeout, try waiting...')#line:47
        OO00O0O00O00OO00O ={"result":"error","data":"time out"}#line:48
        for O0O00OO00000OO000 in range (20 ):#line:49
            O00O0000OO0000O0O =requests .get (O0O0000O0OO0O000O ).json ()#line:50
            print (O00O0000OO0000O0O )#line:51
            O0O00OO0OO00OOOO0 =O00O0000OO0000O0O ['data']#line:52
            if len (O0O00OO0OO00OOOO0 )>1 :#line:53
                OO00O0O00O00OO00O ={"result":"success","data":"uploaded"}#line:54
                break #line:55
            time .sleep (OOOOOO0OOOOO000OO )#line:56
    else :#line:57
        OO00O0O00O00OO00O ={"result":"error","data":"some thing wrong"}#line:58
    print (OO00O0O00O00OO00O )#line:59
    if OO00O0O00O00OO00O ['result']=='error':#line:60
        raise SmartPipError ('Upload Error')#line:61
def get_dataset (OOOOO0OOOO000000O ):#line:62
    ""#line:67
    OOOOOOOOOO00O00O0 =requests .get (_OO0O00O000O0OO0O0 +str (OOOOO0OOOO000000O ),verify =False )#line:68
    OOOOOOOOOO00O00O0 =OOOOOOOOOO00O00O0 .json ()#line:69
    return OOOOOOOOOO00O00O0 #line:70
def dataset (OOO00O0000OOO0000 ,O000OO00000O000OO ,OOO00OOO0OOOO00O0 ,tolist =None ):#line:71
    ""#line:78
    OOO000OOOO00000OO =60 *15 #line:79
    OO0O00O00O000000O =3600 *2 #line:80
    OOO000O0OO0O0O0OO =''#line:81
    try :#line:82
        while True :#line:83
            O0OOOO0OOOOOOOOOO =requests .get (_OO0O00O000O0OO0O0 +O000OO00000O000OO ,verify =False )#line:84
            O0OOOO0OOOOOOOOOO =O0OOOO0OOOOOOOOOO .json ()#line:85
            OO0O00O0000O0OOOO =O0OOOO0OOOOOOOOOO ['result']#line:86
            O0OOOO0OOOOOOOOOO =O0OOOO0OOOOOOOOOO ['data']#line:87
            if OO0O00O0000O0OOOO =='error':#line:88
                raise Exception (f'{O0OOOO0OOOOOOOOOO}')#line:89
            OOO000O0OO0O0O0OO =',\n'.join ([str (O0O0OOO0O0O0OO00O )for O0O0OOO0O0O0OO00O in O0OOOO0OOOOOOOOOO ])#line:90
            print (f'Dataset: {OOO000O0OO0O0O0OO} ')#line:91
            if OOO00OOO0OOOO00O0 =='e3':#line:92
                if len (O0OOOO0OOOOOOOOOO )<2 :#line:93
                    if OO0O00O00O000000O <=0 :#line:94
                        raise Exception ('超时且数据为空')#line:95
                    else :#line:96
                        time .sleep (OOO000OOOO00000OO )#line:97
                        OO0O00O00O000000O =OO0O00O00O000000O -OOO000OOOO00000OO #line:98
                else :#line:99
                    break #line:100
            else :#line:101
                if len (O0OOOO0OOOOOOOOOO )>1 :#line:102
                    if OOO00OOO0OOOO00O0 =='e1':#line:103
                        raise Exception ('有异常数据')#line:104
                    elif OOO00OOO0OOOO00O0 =='e2':#line:105
                        list_email (f'Info_{OOO00O0000OOO0000}',f'{OOO00O0000OOO0000}-Dataset Status',O0OOOO0OOOOOOOOOO ,to_list =tolist )#line:106
                else :#line:107
                    if OOO00OOO0OOOO00O0 not in ['info','e1']:#line:108
                        OOO000O0OO0O0O0OO ='数据为空'#line:109
                        raise Exception (OOO000O0OO0O0O0OO )#line:110
                break #line:111
    except Exception as O00O00OOO000OOO00 :#line:112
        fun_email (f'{OOO00O0000OOO0000}-执行Dataset校验出错',OOO000O0OO0O0O0OO ,to_list =tolist )#line:113
        raise SmartPipError (str (O00O00OOO000OOO00 .args ))#line:114
def refresh_dash (OO0OOO0O00000000O ,O0O0O000OOO0O000O ):#line:115
    ""#line:118
    try :#line:119
        O0OO00OO00OOOOOO0 =requests .get (f'{_O0O00O0OO0OO0OOOO}{O0O0O000OOO0O000O}',verify =False )#line:120
        O0OO00OO00OOOOOO0 =O0OO00OO00OOOOOO0 .json ()#line:121
        print (O0OO00OO00OOOOOO0 )#line:122
        OO00OO0OOO0O0OOO0 =O0OO00OO00OOOOOO0 ['status']#line:123
        if OO00OO0OOO0O0OOO0 !=200 :#line:124
            raise SmartPipError ('refresh_dash')#line:125
    except Exception as O0OO000OOO0O00OO0 :#line:126
        fun_email (f'{OO0OOO0O00000000O}-执行re出错',str (O0OO000OOO0O00OO0 .args ))#line:127
        raise SmartPipError (str (O0OO000OOO0O00OO0 .args ))#line:128
def run_bash (O00OO0O0OOOOO00OO ):#line:131
    O0OO0OO0OO0OO00O0 =''#line:132
    OO0O00OOOO00O0O00 =subprocess .Popen (O00OO0O0OOOOO00OO ,stdout =subprocess .PIPE ,stderr =subprocess .STDOUT ,shell =True ,cwd =ETL_FILE_PATH )#line:133
    print ('PID:',OO0O00OOOO00O0O00 .pid )#line:134
    for OO0O00O00O000OOO0 in iter (OO0O00OOOO00O0O00 .stdout .readline ,b''):#line:135
        if OO0O00OOOO00O0O00 .poll ()and OO0O00O00O000OOO0 ==b'':#line:136
            break #line:137
        OO0O00O00O000OOO0 =OO0O00O00O000OOO0 .decode (encoding ='utf8')#line:138
        print (OO0O00O00O000OOO0 .rstrip ())#line:139
        O0OO0OO0OO0OO00O0 =O0OO0OO0OO0OO00O0 +OO0O00O00O000OOO0 #line:140
    OO0O00OOOO00O0O00 .stdout .close ()#line:141
    O0OOO0O0OO000OOO0 =OO0O00OOOO00O0O00 .wait ()#line:142
    print ('result code: ',O0OOO0O0OO000OOO0 )#line:143
    return O0OO0OO0OO0OO00O0 ,O0OOO0O0OO000OOO0 #line:144
def run_python (O0O0O0OO000O00OOO ,O00OOOO00000OOOO0 ,dev =''):#line:145
    O00O0O0000O00OO00 =O0O0O0OO000O00OOO .split ('/')#line:146
    _O0OOOOOO0OOOO0OOO ,O0OOO0OO00000O000 =run_bash ('python %s %s'%(O0O0O0OO000O00OOO ,O00OOOO00000OOOO0 ))#line:147
    if O0OOO0OO00000O000 !=0 :#line:148
        fun_email (f'{O00O0O0000O00OO00[-2]}/{O00O0O0000O00OO00[-1]}出错','python error')#line:149
        raise Exception ('error')#line:150
def run_dataxx (O000O0OOOO0OO000O ,O0OO0OOO00OOO0OOO ,dev =''):#line:154
    O00O000000OOOO00O =O000O0OOOO0OO000O .split ('/')#line:155
    if O0OO0OOO00OOO0OOO :#line:156
        O0OOO0O000O00OOOO =[f'-D{O0OO0OOOO0O000OOO}:{O0O00OOO0O00O0OO0}'for O0OO0OOOO0O000OOO ,O0O00OOO0O00O0OO0 in O0OO0OOO00OOO0OOO .items ()]#line:157
        OOO000O0O000O00O0 =' '.join (O0OOO0O000O00OOOO )#line:158
        O0000OOO00OOOO0O0 =[f'-p"{OOO000O0O000O00O0}"',O000O0OOOO0OO000O ]#line:159
    else :#line:160
        O0000OOO00OOOO0O0 =[O000O0OOOO0OO000O ]#line:161
    OO00OO0OO0O00OO00 =datax_cmdStr (O0000OOO00OOOO0O0 )#line:162
    _O0000OOOO00O0OO0O ,O000OO00OOO0000OO =run_bash (OO00OO0OO0O00OO00 )#line:163
    if O000OO00OOO0000OO !=0 :#line:164
        fun_email (f'{O00O000000OOOO00O[-2]}/{O00O000000OOOO00O[-1]}出错','datax error')#line:165
        raise Exception ('error')#line:166
def run_datax (O0OO000O00OO00OO0 ,OOOOOOO0O00O0OOO0 ,OOO0O000OOOOO0OO0 ,O000O0OOOO0OO00O0 ,dev =''):#line:167
    with open (O0OO000O00OO00OO0 ,'r',encoding ='utf8')as O00OOO00O0OO00OO0 :#line:168
        O0OOOOOOO00O0O000 =readSqlstr (O00OOO00O0OO00OO0 .read ().strip (),para_dict =O000O0OOOO0OO00O0 )#line:169
    O0OOOOOOO00O0O000 =O0OOOOOOO00O0O000 .split ('##')#line:170
    OO00OO000OO000000 ={}#line:171
    for O0OO00OOOO0OOO0OO in O0OOOOOOO00O0O000 :#line:172
        O0OO000OO0000OO0O =O0OO00OOOO0OOO0OO .find ('=')#line:173
        if O0OO000OO0000OO0O >0 :#line:174
            OO00OO000OO000000 [O0OO00OOOO0OOO0OO [:O0OO000OO0000OO0O ].strip ()]=O0OO00OOOO0OOO0OO [O0OO000OO0000OO0O +1 :].replace ('\n',' ').strip ()#line:175
    O0O0OOOO0OO0OOOOO =OO00OO000OO000000 .keys ()#line:176
    OOOO0OO0O00OO00O0 =OO00OO000OO000000 .pop ('template')if 'template'in O0O0OOOO0OO0OOOOO else 'default'#line:177
    O0O00O0OOO0OOO0O0 =OO00OO000OO000000 .get ('targetColumn')#line:178
    OO00OOOO0O0OOO000 =None #line:179
    if OOOO0OO0O00OO00O0 .endswith ('hdfs'):#line:180
        OO00OOOO0O0OOO000 =OO00OO000OO000000 .pop ('hiveSql')if 'hiveSql'in O0O0OOOO0OO0OOOOO else None #line:182
        if not OO00OOOO0O0OOO000 :#line:183
            OO00OOOO0O0OOO000 =OO00OO000OO000000 .pop ('postSql')if 'postSql'in O0O0OOOO0OO0OOOOO else None #line:184
        if O0O00O0OOO0OOO0O0 :#line:186
            O0O00O0OOO0OOO0O0 =O0O00O0OOO0OOO0O0 .split (',')#line:187
            OOOO00O00OO00O00O =[]#line:188
            for O0OO00OOOO0OOO0OO in O0O00O0OOO0OOO0O0 :#line:189
                if ':'in O0OO00OOOO0OOO0OO :#line:190
                    O0OO00OOOO0OOO0OO =O0OO00OOOO0OOO0OO .split (':')#line:191
                    OOOO00O00OO00O00O .append ({"name":O0OO00OOOO0OOO0OO [0 ].strip (),"type":O0OO00OOOO0OOO0OO [1 ].strip ()})#line:192
                else :#line:193
                    OOOO00O00OO00O00O .append ({"name":O0OO00OOOO0OOO0OO .strip (),"type":"STRING"})#line:194
            OO00OO000OO000000 ['targetColumn']=json .dumps (OOOO00O00OO00O00O )#line:195
    else :#line:196
        if O0O00O0OOO0OOO0O0 :#line:197
            O0O00O0OOO0OOO0O0 =[O0000O0000OOOO00O .strip ()for O0000O0000OOOO00O in O0O00O0OOO0OOO0O0 .split (',')]#line:198
            OO00OO000OO000000 ['targetColumn']=json .dumps (O0O00O0OOO0OOO0O0 )#line:199
        else :#line:200
            OO00OO000OO000000 ['targetColumn']='["*"]'#line:201
        if OOOO0OO0O00OO00O0 .endswith ('starrocks'):#line:203
            if '.'in OO00OO000OO000000 ['targetTable']:#line:204
                OO00OO000OO000000 ['targetDB'],OO00OO000OO000000 ['targetTable']=OO00OO000OO000000 ['targetTable'].split ('.')#line:205
            else :#line:206
                OO00OO000OO000000 ['targetDB']='Test'#line:207
    if 'preSql'in O0O0OOOO0OO0OOOOO :#line:209
        OO00OO000OO000000 ['preSql']=json .dumps (OO00OO000OO000000 ['preSql'].strip ().split (';'))#line:210
    else :#line:211
        OO00OO000OO000000 ['preSql']=''#line:212
    if 'postSql'in O0O0OOOO0OO0OOOOO :#line:213
        OO00OO000OO000000 ['postSql']=json .dumps (OO00OO000OO000000 ['postSql'].strip ().split (';'))#line:214
    else :#line:215
        OO00OO000OO000000 ['postSql']=''#line:216
    O000OO0OO00OO0O0O =O0OO000O00OO00OO0 .split ('/')#line:217
    O00OO0OO00000O00O =O000OO0OO00OO0O0O [-1 ].split ('.')[0 ]#line:218
    with open (os .path .join (OOO0O000OOOOO0OO0 ,'datax','templates',OOOO0OO0O00OO00O0 ),'r')as O00OOO00O0OO00OO0 :#line:219
        O0OO00OOOO000O000 =O00OOO00O0OO00OO0 .read ()#line:220
    O0OO000O00OO00OO0 =os .path .join (OOO0O000OOOOO0OO0 ,'datax',O00OO0OO00000O00O +'.json')#line:221
    with open (O0OO000O00OO00OO0 ,'w',encoding ='utf8')as O00OOO00O0OO00OO0 :#line:222
        O00OOO00O0OO00OO0 .write (readSqlstr (O0OO00OOOO000O000 ,OO00OO000OO000000 ))#line:223
    OOOO0O0O0000O0O0O =datax_cmdStr ([O0OO000O00OO00OO0 ])#line:224
    _O0000000OO00O00OO ,OO00O00O0OO0OO0OO =run_bash (OOOO0O0O0000O0O0O )#line:225
    if OO00O00O0OO0OO0OO !=0 :#line:226
        fun_email (f'{O000OO0OO00OO0O0O[-2]}/{O000OO0OO00OO0O0O[-1]}出错','datax error')#line:227
        raise Exception ('error')#line:228
    if OO00OOOO0O0OOO000 :#line:229
        print (_O0O00000OO000OOO0 (OO00OOOO0O0OOO000 .split (';'),OOOOOOO0O00O0OOO0 ,db_connect ='hive',dev =dev ))#line:230
def readSqlFile (OO0OOOOOOO0O0OO0O ,para_dict =None ):#line:234
    if OO0OOOOOOO0O0OO0O .find ('.sql')<0 :#line:235
        return 'file type error'#line:236
    with open (OO0OOOOOOO0O0OO0O ,'r',encoding ='utf-8')as O00O000OO0000OO0O :#line:237
        OO00O000OO0O000O0 =O00O000OO0000OO0O .read ()#line:238
    O0OOOO000OOOOO0OO =readSqlstr (OO00O000OO0O000O0 ,para_dict )#line:239
    return O0OOOO000OOOOO0OO #line:240
def readSqoopFile (O0OO00O000O00O00O ,para_dict =None ):#line:241
    if not O0OO00O000O00O00O .endswith ('.sql'):#line:242
        return 'file type error'#line:243
    with open (O0OO00O000O00O00O ,'r',encoding ='utf8')as OO0O000OO0000OOOO :#line:244
        OOOOOO00O0OO0O0O0 =OO0O000OO0000OOOO .read ().strip ()#line:245
    OOO00O0O0OOO00000 =re .match (r"/\*(.*?)\*/(.+)",OOOOOO00O0OO0O0O0 ,re .M |re .S )#line:246
    O0O0OOOO0000OOO0O =readSqlstr (OOO00O0O0OOO00000 .group (1 ).strip (),para_dict )#line:247
    O00O00O0OO0OOOOOO =OOO00O0O0OOO00000 .group (2 ).strip ()#line:248
    return O0O0OOOO0000OOO0O ,O00O00O0OO0OOOOOO #line:249
def readSqlstr (O00O0O00O00O00000 ,para_dict =None ):#line:250
    O000OOOO00000OO00 =re .sub (r"(\/\*(.|\n)*?\*\/)|--.*",'',O00O0O00O00O00000 .strip ())#line:251
    if para_dict :#line:252
        for OOO00O0O0O0OOOOOO ,OO0O00OOO0OO00OOO in para_dict .items ():#line:253
            O000OOOO00000OO00 =O000OOOO00000OO00 .replace ('$'+OOO00O0O0O0OOOOOO ,str (OO0O00OOO0OO00OOO ))#line:254
    return O000OOOO00000OO00 #line:255
def run_sql_file (OOO0OO000O00O000O ,OO000O00O00O00000 ,db_connect ='starrocks',para_dict =None ,dev =''):#line:256
    OO0O000O000O00000 =OOO0OO000O00O000O .split ('/')#line:257
    try :#line:258
        OO0O0000O0OOOOO0O =readSqlFile (OOO0OO000O00O000O ,para_dict ).split (';')#line:259
        O000O000O0OO0OOO0 =OO000O00O00O00000 .get (db_connect )#line:260
        if dev :#line:261
            if f'{db_connect}{dev}'in OO000O00O00O00000 .keys ():#line:262
                O000O000O0OO0OOO0 =OO000O00O00O00000 .get (f'{db_connect}{dev}')#line:263
        O000000O0O000O000 =connect_db_execute ().execute_sql_list (OO0O0000O0OOOOO0O ,db_connect ,connect_dict =O000O000O0OO0OOO0 )#line:264
        return O000000O0O000O000 #line:265
    except Exception as O00OOOO000O0OO0O0 :#line:266
        fun_email ('{}/{}执行出错'.format (OO0O000O000O00000 [-2 ],OO0O000O000O00000 [-1 ]),str (O00OOOO000O0OO0O0 .args ))#line:267
        print (O00OOOO000O0OO0O0 .args )#line:268
        raise SmartPipError ('Run SQL Error')#line:269
def _O0O00000OO000OOO0 (OOO0OO000O000O000 ,OOO0O00000OOOOOOO ,db_connect ='starrocks',para_dict =None ,dev =''):#line:270
    try :#line:271
        if isinstance (OOO0OO000O000O000 ,str ):#line:272
            OOO0OO000O000O000 =readSqlstr (OOO0OO000O000O000 ,para_dict ).split (';')#line:273
        OOOOOOOOOO0O00OO0 =OOO0O00000OOOOOOO .get (db_connect )#line:274
        if dev :#line:275
            if f'{db_connect}{dev}'in OOO0O00000OOOOOOO .keys ():#line:276
                OOOOOOOOOO0O00OO0 =OOO0O00000OOOOOOO .get (f'{db_connect}{dev}')#line:277
        OOO00OO0OOOOOOOOO =connect_db_execute ().execute_sql_list (OOO0OO000O000O000 ,db_connect ,connect_dict =OOOOOOOOOO0O00OO0 )#line:278
        return OOO00OO0OOOOOOOOO #line:279
    except Exception as OOOOOO00O0OOOO0O0 :#line:280
        fun_email ('SQL执行出错',f'{OOO0OO000O000O000}{OOOOOO00O0OOOO0O0.args}')#line:281
        print (OOOOOO00O0OOOO0O0 .args )#line:282
        raise SmartPipError ('Run SQL Error')#line:283
def run_kettle (O0O00OOOOO00000O0 ,para_str ='',dev =False ):#line:286
    ""#line:293
    OOO0O00OO0OO0O0OO =O0O00OOOOO00000O0 .split ('/')#line:294
    print ('kettle job start')#line:295
    if '.ktr'in O0O00OOOOO00000O0 :#line:297
        O0O0000OO000O0OOO =f'{KETTLE_HOME}/pan.sh -level=Basic -file={O0O00OOOOO00000O0}{para_str}'#line:298
    else :#line:299
        O0O0000OO000O0OOO =f'{KETTLE_HOME}/kitchen.sh -level=Basic -file={O0O00OOOOO00000O0}{para_str}'#line:300
    print (O0O0000OO000O0OOO )#line:301
    OO00OOOOOOOO0OOOO ,OOO0OOO0000OOOO00 =run_bash (O0O0000OO000O0OOO )#line:305
    if OOO0OOO0000OOOO00 ==0 :#line:306
        print ('{} 完成数据抽取'.format (str (O0O00OOOOO00000O0 )))#line:307
    else :#line:308
        print ('{} 执行错误'.format (O0O00OOOOO00000O0 ))#line:309
        fun_email ('{}/{}出错'.format (OOO0O00OO0OO0O0OO [-2 ],OOO0O00OO0OO0O0OO [-1 ]),str (OO00OOOOOOOO0OOOO ))#line:310
        raise SmartPipError ('Run Kettle Error')#line:311
def hdfsStarrocks (OOO00000O0O0OOO00 ,O000OO000OO00O000 ,para_dict =None ):#line:315
    ""#line:319
    OO0O0O0O0OOOO0OOO =OOO00000O0O0OOO00 .split ('/')#line:320
    print ('strocks load job start')#line:321
    O0O0OO0O00000OOO0 ,O0O00OOOO0O00OO0O =readSqoopFile (OOO00000O0O0OOO00 ,para_dict =para_dict )#line:322
    O0O0OO0O00000OOO0 =O0O0OO0O00000OOO0 .split ('\n')#line:323
    O0OO000000O000OOO ={}#line:324
    O0OO000000O000OOO ['LABEL']=f'{OO0O0O0O0OOOO0OOO[-2]}{OO0O0O0O0OOOO0OOO[-1][:-4]}{int(time.time())}'#line:325
    O0OO000000O000OOO ['HDFS']=HIVE_HOME #line:326
    for O00O0OOO0OO0OOO0O in O0O0OO0O00000OOO0 :#line:327
        OO0OO00O0OO0OOO00 =O00O0OOO0OO0OOO0O .find ('=')#line:328
        if OO0OO00O0OO0OOO00 >0 :#line:329
            O0OO000000O000OOO [O00O0OOO0OO0OOO0O [:OO0OO00O0OO0OOO00 ].strip ()]=O00O0OOO0OO0OOO0O [OO0OO00O0OO0OOO00 +1 :].strip ()#line:330
    O00OO00OO0OO0OO0O =O0OO000000O000OOO .get ('sleepTime')#line:332
    if O00OO00OO0OO0OO0O :#line:333
        O00OO00OO0OO0OO0O =int (O00OO00OO0OO0OO0O )#line:334
        if O00OO00OO0OO0OO0O <30 :#line:335
            O00OO00OO0OO0OO0O =30 #line:336
    else :#line:337
        O00OO00OO0OO0OO0O =30 #line:338
    O000O00OOO000O00O =O0OO000000O000OOO .get ('maxTime')#line:340
    if O000O00OOO000O00O :#line:341
        O000O00OOO000O00O =int (O000O00OOO000O00O )#line:342
        if O000O00OOO000O00O >3600 :#line:343
            O000O00OOO000O00O =3600 #line:344
    else :#line:345
        O000O00OOO000O00O =600 #line:346
    _O0O00000OO000OOO0 (O0O00OOOO0O00OO0O ,db_connect ='mysql',dev ='starrocks',para_dict =O0OO000000O000OOO )#line:348
    time .sleep (O00OO00OO0OO0OO0O )#line:349
    OO0O0O000OO0O0O0O =f'''show load from {O0OO000000O000OOO.get('targetDB')} where label = '{O0OO000000O000OOO['LABEL']}' order by CreateTime desc limit 1 '''#line:350
    OO0O0O0O0000O0000 ='start to check label'#line:351
    try :#line:352
        while True :#line:353
            OO0O0O0O0000O0000 =_O0O00000OO000OOO0 ([OO0O0O000OO0O0O0O ],O000OO000OO00O000 ,db_connect ='mysql',dev ='starrocks')#line:354
            print (OO0O0O0O0000O0000 )#line:355
            O000000OO00OO0OO0 =OO0O0O0O0000O0000 [1 ][2 ]#line:356
            if O000000OO00OO0OO0 =='CANCELLED':#line:357
                raise Exception (f'Starrocks:{O000000OO00OO0OO0}')#line:358
            elif O000000OO00OO0OO0 =='FINISHED':#line:359
                print ('Load completed')#line:360
                break #line:361
            if O000O00OOO000O00O <=0 :#line:362
                raise Exception ('超时未完成')#line:363
            else :#line:364
                time .sleep (O00OO00OO0OO0OO0O )#line:365
                O000O00OOO000O00O =O000O00OOO000O00O -O00OO00OO0OO0OO0O #line:366
    except Exception as OO0000OOO00O0O0OO :#line:367
        print ('{} 执行错误'.format (OOO00000O0O0OOO00 ))#line:368
        fun_email ('{}/{}执行出错'.format (OO0O0O0O0OOOO0OOO [-2 ],OO0O0O0O0OOOO0OOO [-1 ]),str (OO0O0O0O0000O0000 ))#line:369
        raise SmartPipError (str (OO0000OOO00O0O0OO .args ))#line:370
def kafkaStarrocks (OO00OOOOOOO000000 ,O00O00O00OO0OO0O0 ,OOO000OOOOO0000O0 ,OOO00O0O00O0OOO0O ,O00OOO0OO00OOO00O ,dev =''):#line:372
    with open (OO00OOOOOOO000000 ,'r',encoding ='utf8')as O0OO0O000OOO000OO :#line:373
        OOO0O000OOOO0000O =readSqlstr (O0OO0O000OOO000OO .read ().strip (),para_dict =O00OOO0OO00OOO00O )#line:374
    OOO0O000OOOO0000O =OOO0O000OOOO0000O .split ('##')#line:375
    O0O00OOO0OOOO0O00 ={}#line:376
    for OO0OOOO0O00000000 in OOO0O000OOOO0000O :#line:377
        O0000OO00O00OOOO0 =OO0OOOO0O00000000 .find ('=')#line:378
        if O0000OO00O00OOOO0 >0 :#line:379
            O0O00OOO0OO000OOO =OO0OOOO0O00000000 [O0000OO00O00OOOO0 +1 :].replace ('\n',' ').strip ()#line:380
            if O0O00OOO0OO000OOO :#line:381
                O0O00OOO0OOOO0O00 [OO0OOOO0O00000000 [:O0000OO00O00OOOO0 ].strip ()]=O0O00OOO0OO000OOO #line:382
    O0O0OO0000O000000 =O0O00OOO0OOOO0O00 .pop ('topic')#line:383
    O000O0O000OO0OOO0 =O0O00OOO0OOOO0O00 .pop ('table')#line:384
    OOO0OOOOOOOO00O00 =O0O00OOO0OOOO0O00 .keys ()#line:385
    if 'skipError'in OOO0OOOOOOOO00O00 :#line:386
        skipError =O0O00OOO0OOOO0O00 .pop ('skipError')#line:387
    else :#line:388
        skipError =None #line:389
    if 'kafkaConn'in OOO0OOOOOOOO00O00 :#line:390
        OO0OO0O0OO0000OO0 =O0O00OOO0OOOO0O00 .pop ('kafkaConn')#line:391
    else :#line:392
        OO0OO0O0OO0000OO0 ='default'#line:393
    if 'json_root'in OOO0OOOOOOOO00O00 :#line:394
        O0O0O0O0O00O000O0 =O0O00OOO0OOOO0O00 .pop ('json_root')#line:395
    else :#line:396
        O0O0O0O0O00O000O0 =None #line:397
    if 'jsonpaths'in OOO0OOOOOOOO00O00 :#line:398
        O0O0OO0O0000O0O0O =O0O00OOO0OOOO0O00 .get ('jsonpaths')#line:399
        if not O0O0OO0O0000O0O0O .startswith ('['):#line:400
            O0O0OO0O0000O0O0O =O0O0OO0O0000O0O0O .split (',')#line:401
            O0O0OO0O0000O0O0O =json .dumps (['$.'+O0OO0OO0000O0000O .strip ()for O0OO0OO0000O0000O in O0O0OO0O0000O0O0O ])#line:402
            O0O00OOO0OOOO0O00 ['jsonpaths']=O0O0OO0O0000O0O0O #line:403
    OO0000O00OO0OO000 =_OO0OOOO0OO0O0O000 (O0O0OO0000O000000 ,O00O00O00OO0OO0O0 [OO0OO0O0OO0000OO0 ],OOO00O0O00O0OOO0O )#line:404
    def O00OO0000O0O00000 (O0O0OOOOOOO0OO0O0 ):#line:405
        O0O0O00OO000000OO =b''#line:406
        OOOO00O0O0O0000O0 =None #line:407
        if 'format'in OOO0OOOOOOOO00O00 :#line:408
            for OOOO00O0O0O0000O0 in O0O0OOOOOOO0OO0O0 :#line:409
                OOO00O0O000O0O0OO =OOOO00O0O0O0000O0 .value #line:410
                if O0O0O0O0O00O000O0 :#line:411
                    OOO00O0O000O0O0OO =json .loads (OOO00O0O000O0O0OO .decode ('utf8'))#line:412
                    OOO00O0O000O0O0OO =json .dumps (OOO00O0O000O0O0OO [O0O0O0O0O00O000O0 ]).encode ('utf8')#line:413
                if OOO00O0O000O0O0OO .startswith (b'['):#line:414
                    O0O0O00OO000000OO =O0O0O00OO000000OO +b','+OOO00O0O000O0O0OO [1 :-1 ]#line:415
                else :#line:416
                    O0O0O00OO000000OO =O0O0O00OO000000OO +b','+OOO00O0O000O0O0OO #line:417
                if len (O0O0O00OO000000OO )>94857600 :#line:418
                    streamStarrocks (O000O0O000OO0OOO0 ,OOO000OOOOO0000O0 ,O0O00OOO0OOOO0O00 ,O0O0O00OO000000OO ,skipError )#line:419
                    OO0000O00OO0OO000 .write_offset (OOOO00O0O0O0000O0 .partition ,OOOO00O0O0O0000O0 .offset +1 )#line:420
                    O0O0O00OO000000OO =b''#line:421
        else :#line:422
            for OOOO00O0O0O0000O0 in O0O0OOOOOOO0OO0O0 :#line:423
                OOO00O0O000O0O0OO =OOOO00O0O0O0000O0 .value #line:424
                if O0O0O0O0O00O000O0 :#line:425
                    OOO00O0O000O0O0OO =json .loads (OOO00O0O000O0O0OO .decode ('utf8'))#line:426
                    OOO00O0O000O0O0OO =json .dumps (OOO00O0O000O0O0OO [O0O0O0O0O00O000O0 ]).encode ('utf8')#line:427
                O0O0O00OO000000OO =O0O0O00OO000000OO +b'\n'+OOO00O0O000O0O0OO #line:428
                if len (O0O0O00OO000000OO )>94857600 :#line:429
                    streamStarrocks (O000O0O000OO0OOO0 ,OOO000OOOOO0000O0 ,O0O00OOO0OOOO0O00 ,O0O0O00OO000000OO ,skipError )#line:430
                    OO0000O00OO0OO000 .write_offset (OOOO00O0O0O0000O0 .partition ,OOOO00O0O0O0000O0 .offset +1 )#line:431
                    O0O0O00OO000000OO =b''#line:432
        print (O0O0O00OO000000OO [1 :1000 ])#line:433
        if O0O0O00OO000000OO :#line:434
            streamStarrocks (O000O0O000OO0OOO0 ,OOO000OOOOO0000O0 ,O0O00OOO0OOOO0O00 ,O0O0O00OO000000OO ,skipError )#line:435
        return OOOO00O0O0O0000O0 #line:436
    OO0000O00OO0OO000 .consumer_topic (O00OO0000O0O00000 )#line:438
def streamStarrocks (O0O00OOO0O00O0OOO ,OO0OO000OOO0OO0O0 ,OOOO00O000OO0O000 ,OOO0OO0O00OOO0000 ,skipError =False ):#line:440
    import base64 ,uuid #line:441
    OO00000OO0000O00O ,O0O00OOO0O00O0OOO =O0O00OOO0O00O0OOO .split ('.')#line:442
    OO00OO0OO0OO000OO =str (base64 .b64encode (f'{OO0OO000OOO0OO0O0["user"]}:{OO0OO000OOO0OO0O0["password"]}'.encode ('utf-8')),'utf-8')#line:443
    OOO0OO0O00OOO0000 =OOO0OO0O00OOO0000 .strip ()#line:444
    if OOO0OO0O00OOO0000 .startswith (b','):#line:445
        OOOO00O000OO0O000 ['strip_outer_array']='true'#line:446
        OOO0OO0O00OOO0000 =b'['+OOO0OO0O00OOO0000 [1 :]+b']'#line:447
    OOO00O0O00OOO00O0 ={'Content-Type':'application/json','Authorization':f'Basic {OO00OO0OO0OO000OO}','label':f'{O0O00OOO0O00O0OOO}{uuid.uuid4()}',**OOOO00O000OO0O000 }#line:453
    OOO00OO00OOO00O0O =f"{OO0OO000OOO0OO0O0['url']}/api/{OO00000OO0000O00O}/{O0O00OOO0O00O0OOO}/_stream_load"#line:454
    print ('start loading to starrocks....')#line:455
    O0O000000OOOO00OO =requests .put (OOO00OO00OOO00O0O ,headers =OOO00O0O00OOO00O0 ,data =OOO0OO0O00OOO0000 ).json ()#line:456
    print (O0O000000OOOO00OO )#line:457
    if O0O000000OOOO00OO ['Status']=='Fail':#line:458
        if skipError :#line:459
            print (f'Starrocks Load Error, Skip this offset')#line:460
        else :#line:461
            raise Exception ('Starrocks Load Error')#line:462
def point_test (OO0OO0O00000O00O0 ,O00OO0OO0O0OO00O0 ,sleeptime ='',maxtime =''):#line:468
    ""#line:475
    import pymysql #line:476
    if sleeptime :#line:477
        sleeptime =int (sleeptime )#line:478
        sleeptime =sleeptime if sleeptime >60 else 60 #line:479
    if maxtime :#line:480
        maxtime =int (maxtime )#line:481
        maxtime =maxtime if maxtime <60 *60 *2 else 60 *60 *2 #line:482
    else :#line:483
        maxtime =0 #line:484
    O0OO0OO0O000O0OO0 =O00OO0OO0O0OO00O0 ['airflow']#line:485
    OO0OOOOO0OO000OOO =pymysql .connect (user =O0OO0OO0O000O0OO0 ['user'],password =O0OO0OO0O000O0OO0 ['password'],host =O0OO0OO0O000O0OO0 ['host'],port =O0OO0OO0O000O0OO0 ['port'],database =O0OO0OO0O000O0OO0 ['db'],autocommit =True )#line:493
    try :#line:494
        OOO00O000OO0O0000 =OO0OOOOO0OO000OOO .cursor ()#line:495
        OO0OOOOOO00000000 =f"select start_date,state from dag_run where dag_id ='{OO0OO0O00000O00O0}' ORDER BY id desc LIMIT 1"#line:496
        while True :#line:497
            OOO00O000OO0O0000 .execute (OO0OOOOOO00000000 )#line:498
            OOO00O000OOO0O000 =OOO00O000OO0O0000 .fetchall ()#line:499
            if OOO00O000OOO0O000 [0 ][1 ]!='success':#line:500
                if maxtime >0 and OOO00O000OOO0O000 [0 ][1 ]!='failed':#line:501
                    print ('waiting...'+OOO00O000OOO0O000 [0 ][1 ])#line:502
                    time .sleep (sleeptime )#line:503
                    maxtime =maxtime -sleeptime #line:504
                else :#line:505
                    OO0O00O0OO0OO00OO =OOO00O000OOO0O000 [0 ][0 ].strftime ("%Y-%m-%d %H:%M:%S")#line:506
                    O000OO00OOO0O00OO ='所依赖的dag:'+OO0OO0O00000O00O0 +',状态为'+OOO00O000OOO0O000 [0 ][1 ]+'.其最新的执行时间为'+OO0O00O0OO0OO00OO #line:507
                    fun_email (O000OO00OOO0O00OO ,'前置DAG任务未成功')#line:508
                    print (O000OO00OOO0O00OO )#line:509
                    raise SmartPipError ('Run DAG validate Error')#line:510
            else :#line:511
                print ('success...')#line:512
                break #line:513
    except Exception as OOOO000OO0OO0O0OO :#line:514
        print (OOOO000OO0OO0O0OO .args )#line:515
        raise SmartPipError ('DAG validate Error')#line:516
    finally :#line:517
        OO0OOOOO0OO000OOO .close ()#line:518
class connect_db_execute ():#line:523
    def __init__ (O0O0OO000000000OO ,dev =False ,db =''):#line:524
        O0O0OO000000000OO .dev =dev #line:525
    def insert_contents (O00O00OOO000O00O0 ,O0OOO0000OO0OO0O0 ,O0OOOO0O0O000O00O ,per_in =1000 ,connect_dict =None ):#line:527
        OO0O00OO0O0OO00O0 =time .time ()#line:528
        logging .info ('starting to execute insert contents...')#line:529
        if isinstance (connect_dict ,dict ):#line:530
            OO00O00O000OOO0OO =connect_dict ['dbtype']#line:531
        else :#line:532
            if connect_dict =='':#line:533
                OO00O00O000OOO0OO ='oracle'#line:534
            else :#line:535
                OO00O00O000OOO0OO =connect_dict #line:536
            connect_dict =None #line:537
        OO0O00O00O0O0OO00 =getattr (O00O00OOO000O00O0 ,'insert_contents_'+OO00O00O000OOO0OO )#line:538
        OO00OO0OOO00O000O =OO0O00O00O0O0OO00 (O0OOO0000OO0OO0O0 ,O0OOOO0O0O000O00O ,per_in ,connect_dict )#line:539
        logging .info ('execute insert contents time : {}ms'.format (time .time ()-OO0O00OO0O0OO00O0 ))#line:540
        return OO00OO0OOO00O000O #line:541
    def impala (OOOOO0O0O0O0OO0O0 ,OOO0O0O000O0OO000 ,connect_dict =None ):#line:543
        ""#line:544
        from impala .dbapi import connect as impala #line:545
        O0O0O0OOO00O00O00 =impala (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),auth_mechanism ='PLAIN')#line:552
        OO000000OOOO0O0OO =O0O0O0OOO00O00O00 .cursor ()#line:553
        OOO00O00OOOOO00O0 =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s|^refresh\s|^upsert\s'#line:554
        OOOOO00000O000OOO =None #line:555
        for O000OOOOOOOOO0OOO in OOO0O0O000O0OO000 :#line:556
            print (O000OOOOOOOOO0OOO )#line:557
            O000OOOOOOOOO0OOO =O000OOOOOOOOO0OOO .strip ()#line:558
            if not O000OOOOOOOOO0OOO :#line:559
                continue #line:560
            if re .search (OOO00O00OOOOO00O0 ,O000OOOOOOOOO0OOO ,re .I |re .IGNORECASE ):#line:561
                OO000000OOOO0O0OO .execute (O000OOOOOOOOO0OOO )#line:562
            else :#line:563
                OO000000OOOO0O0OO .execute (O000OOOOOOOOO0OOO )#line:564
                try :#line:565
                    OOOOO00000O000OOO =OO000000OOOO0O0OO .fetchall ()#line:566
                except Exception as O0O000OOOOOO0O0O0 :#line:567
                    print (O0O000OOOOOO0O0O0 .args )#line:568
        O0O0O0OOO00O00O00 .close ()#line:569
        return OOOOO00000O000OOO #line:570
    def hive (OOOOO0OO00O0OOOO0 ,OOOOOOO0O00OO0O00 ,connect_dict =None ):#line:572
        ""#line:573
        from impala .dbapi import connect as impala #line:574
        OO0OO0O0OO0O0000O =impala (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =int (connect_dict ['port']),auth_mechanism ='PLAIN')#line:581
        OO000O0OO000O00O0 =OO0OO0O0OO0O0000O .cursor ()#line:582
        O0OO000OOOOOOOOOO =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s'#line:583
        O0OOOO0O0O0OO0OOO =None #line:584
        for OO00OO0O00O00O00O in OOOOOOO0O00OO0O00 :#line:585
            OO00OO0O00O00O00O =OO00OO0O00O00O00O .strip ()#line:586
            if not OO00OO0O00O00O00O :#line:587
                continue #line:588
            print (OO00OO0O00O00O00O )#line:589
            if OO00OO0O00O00O00O .startswith ('refresh'):#line:590
                connect_dict ['port']=21050 #line:591
                OOOOO0OO00O0OOOO0 .impala ([OO00OO0O00O00O00O ],connect_dict =connect_dict )#line:592
            else :#line:593
                if re .search (O0OO000OOOOOOOOOO ,OO00OO0O00O00O00O ,re .I |re .IGNORECASE ):#line:594
                    OO000O0OO000O00O0 .execute (OO00OO0O00O00O00O )#line:595
                else :#line:596
                    OO000O0OO000O00O0 .execute (OO00OO0O00O00O00O )#line:597
                    try :#line:598
                        O0OOOO0O0O0OO0OOO =OO000O0OO000O00O0 .fetchall ()#line:599
                    except Exception as OOO0OO0O0O0000O00 :#line:600
                        print (OOO0OO0O0O0000O00 .args )#line:601
        OO0OO0O0OO0O0000O .close ()#line:602
        return O0OOOO0O0O0OO0OOO #line:603
    def mysql (OOOO0OO00OO0OOOO0 ,OO0O0OO0OOOO00OO0 ,connect_dict =None ):#line:605
        import pymysql #line:606
        OOOO00OO0O0O00OO0 =pymysql .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =connect_dict ['port'],database =connect_dict ['db'])#line:613
        try :#line:614
            OO0O000OO000OOOOO =OOOO00OO0O0O00OO0 .cursor ()#line:615
            OO000O0O00OO00000 =r'^insert\s|^update\s|^truncate\s|^delete\s|^load\s'#line:616
            for O00O00O00O0OOO000 in OO0O0OO0OOOO00OO0 :#line:617
                O00O00O00O0OOO000 =O00O00O00O0OOO000 .strip ()#line:618
                if not O00O00O00O0OOO000 :#line:619
                    continue #line:620
                print (O00O00O00O0OOO000 )#line:621
                if re .search (OO000O0O00OO00000 ,O00O00O00O0OOO000 ,re .I |re .IGNORECASE ):#line:622
                    try :#line:623
                        OO0O000OO000OOOOO .execute (O00O00O00O0OOO000 )#line:624
                        OOOO00OO0O0O00OO0 .commit ()#line:625
                    except Exception as O0OO00O0O0OOOOOO0 :#line:626
                        OOOO00OO0O0O00OO0 .rollback ()#line:627
                        raise O0OO00O0O0OOOOOO0 #line:628
                else :#line:629
                    OO0O000OO000OOOOO .execute (O00O00O00O0OOO000 )#line:630
                    OOO0O0O00O00000O0 =OO0O000OO000OOOOO .fetchall ()#line:631
                    OOO0O0O00O00000O0 =[[O00O00000O0OO000O [0 ]for O00O00000O0OO000O in OO0O000OO000OOOOO .description ]]+list (OOO0O0O00O00000O0 )#line:632
                    return OOO0O0O00O00000O0 #line:633
        except Exception as OO000OO0000OO0OOO :#line:634
            raise OO000OO0000OO0OOO #line:635
        finally :#line:636
            OOOO00OO0O0O00OO0 .close ()#line:637
    def starrocks (OOOO00O0OO0OO0000 ,OO0O0000O000000OO ,connect_dict =None ):#line:639
        return OOOO00O0OO0OO0000 .mysql (OO0O0000O000000OO ,connect_dict )#line:640
    def oracle (O0OOOO0O00OOOO0O0 ,O0O0O00O0O00O0OO0 ,connect_dict =None ):#line:642
        import cx_Oracle #line:643
        OO0OO0O00O00000OO ='{}/{}@{}/{}'.format (connect_dict ['user'],connect_dict ['password'],connect_dict ['host'],connect_dict ['db'])#line:648
        O00000O00OO00OO0O =cx_Oracle .connect (OO0OO0O00O00000OO )#line:649
        try :#line:650
            OO0OOO0OO0O0OOOO0 =O00000O00OO00OO0O .cursor ()#line:651
            OO0OOO00O00O00000 =r'^insert\s|^update\s|^truncate\s|^delete\s|^comment\s'#line:652
            for O0O0OO0O00O000OOO in O0O0O00O0O00O0OO0 :#line:653
                O0O0OO0O00O000OOO =O0O0OO0O00O000OOO .strip ()#line:654
                if not O0O0OO0O00O000OOO :#line:655
                    continue #line:656
                if re .search (OO0OOO00O00O00000 ,O0O0OO0O00O000OOO ,re .I ):#line:657
                    try :#line:658
                        OO0OOO0OO0O0OOOO0 .execute (O0O0OO0O00O000OOO )#line:659
                        O00000O00OO00OO0O .commit ()#line:660
                    except Exception as OOOO0O00OO0OO0OOO :#line:661
                        if O0O0OO0O00O000OOO .startswith ('comment'):#line:662
                            print ('err:',O0O0OO0O00O000OOO )#line:663
                            continue #line:664
                        O00000O00OO00OO0O .rollback ()#line:665
                        raise OOOO0O00OO0OO0OOO #line:666
                else :#line:667
                    OO0OOO0OO0O0OOOO0 .execute (O0O0OO0O00O000OOO )#line:668
                    OO000O000000O0000 =OO0OOO0OO0O0OOOO0 .fetchall ()#line:669
                    OO000O000000O0000 =[[O0O0OO0O00OOOO0OO [0 ]for O0O0OO0O00OOOO0OO in OO0OOO0OO0O0OOOO0 .description ]]+list (OO000O000000O0000 )#line:670
                    return OO000O000000O0000 #line:671
        except Exception as O0OOOOO00O0OO0OOO :#line:672
            raise O0OOOOO00O0OO0OOO #line:673
        finally :#line:674
            O00000O00OO00OO0O .close ()#line:675
    def gp (OOO00OO000OOO0000 ,O0O000OO0OO00OO00 ,connect_dict =None ):#line:677
        import psycopg2 #line:678
        OO0OO00000OOO000O =psycopg2 .connect (user =connect_dict ['user'],password =connect_dict ['password'],host =connect_dict ['host'],port =connect_dict ['port'],database =connect_dict ['db'])#line:685
        try :#line:686
            O00O00O000000OOOO =OO0OO00000OOO000O .cursor ()#line:687
            O000OO000O0O000O0 =r'^insert\s|^update\s|^truncate\s|^delete\s'#line:688
            for O00000OO00OOOOOOO in O0O000OO0OO00OO00 :#line:689
                O00000OO00OOOOOOO =O00000OO00OOOOOOO .strip ()#line:690
                if not O00000OO00OOOOOOO :#line:691
                    continue #line:692
                if re .search (O000OO000O0O000O0 ,O00000OO00OOOOOOO ,re .I |re .IGNORECASE ):#line:693
                    try :#line:694
                        O00O00O000000OOOO .execute (O00000OO00OOOOOOO )#line:695
                        OO0OO00000OOO000O .commit ()#line:696
                    except Exception as OO00000OO0OOOOO00 :#line:697
                        OO0OO00000OOO000O .rollback ()#line:698
                        raise OO00000OO0OOOOO00 #line:699
                else :#line:700
                    O00O00O000000OOOO .execute (O00000OO00OOOOOOO )#line:701
                    O0OO0OOOOOOO00O0O =O00O00O000000OOOO .fetchall ()#line:702
                    O0OO0OOOOOOO00O0O =[[O00OOO0OO0000OO00 [0 ]for O00OOO0OO0000OO00 in O00O00O000000OOOO .description ]]+list (O0OO0OOOOOOO00O0O )#line:703
                    return O0OO0OOOOOOO00O0O #line:704
        except Exception as OO0O00OOO0OOOO0OO :#line:705
            raise OO0O00OOO0OOOO0OO #line:706
        finally :#line:707
            OO0OO00000OOO000O .close ()#line:708
    def execute_sql_list (O0000OO0OOO0OOO00 ,OO0O0OO000OO00OO0 ,db_connect ='',connect_dict =None ):#line:710
        if db_connect =='':db_connect ='oracle'#line:711
        O00OOO00OOO00O000 =getattr (O0000OO0OOO0OOO00 ,db_connect )#line:712
        return O00OOO00OOO00O000 (OO0O0OO000OO00OO0 ,connect_dict =connect_dict )#line:713
    def excute_proc (O0OOOO000O0O0OO0O ,OOO00O0OO00000OOO ,OOOOOO00OO000OOOO ,proc_para =None ):#line:715
        import cx_Oracle #line:716
        OO000O0OOO0OO0OO0 ='{}/{}@{}/{}'.format (OOOOOO00OO000OOOO ['user'],OOOOOO00OO000OOOO ['password'],OOOOOO00OO000OOOO ['host'],OOOOOO00OO000OOOO ['db'])#line:722
        OOOO0O0O0O0OO0OO0 =cx_Oracle .connect (OO000O0OOO0OO0OO0 )#line:723
        try :#line:725
            OOOOO0OO0OOO0OO0O =OOOO0O0O0O0OO0OO0 .cursor ()#line:726
            print ("开始执行过程:{}  参数: {}".format (OOO00O0OO00000OOO ,proc_para ))#line:727
            if proc_para is None :#line:728
                O0O00O0OOO0OOOO0O =OOOOO0OO0OOO0OO0O .callproc (OOO00O0OO00000OOO )#line:729
                OOOO0O0O0O0OO0OO0 .commit ()#line:730
            else :#line:731
                O0O00O0OOO0OOOO0O =OOOOO0OO0OOO0OO0O .callproc (OOO00O0OO00000OOO ,proc_para )#line:733
                OOOO0O0O0O0OO0OO0 .commit ()#line:734
            OOOOO0OO0OOO0OO0O .close ()#line:735
            OOOO0O0O0O0OO0OO0 .close ()#line:736
            print (O0O00O0OOO0OOOO0O )#line:737
        except Exception as O0O0000OOO0OO0O0O :#line:738
            OOOO0O0O0O0OO0OO0 .rollback ()#line:739
            OOOO0O0O0O0OO0OO0 .close ()#line:740
            raise O0O0000OOO0OO0O0O #line:742
        return True #line:743
    def insert_contents_oracle (OO0O00O00OOOOO0O0 ,O000O0O00O000OO0O ,O00OO0O0OO0O0OO00 ,per_in =100 ,connect_dict =None ):#line:745
        import cx_Oracle #line:746
        OOO0OOO000OO0OOOO ='{}/{}@{}:{}/{}'.format (connect_dict ['user'],connect_dict ['password'],connect_dict ['host'],connect_dict ['port'],connect_dict ['db'])#line:752
        OO000O00OO00OOOO0 =cx_Oracle .connect (OOO0OOO000OO0OOOO )#line:753
        O0O0O00O0OOO00O00 =OO000O00OO00OOOO0 .cursor ()#line:754
        OO00OO00OOOO00O00 =' into {} values {}'#line:755
        O000000O000OO0000 =''#line:756
        O0OOOO00OO0O00O0O =len (O000O0O00O000OO0O )#line:757
        logging .info ("total {} records need to insert table {}: ".format (O0OOOO00OO0O00O0O ,O00OO0O0OO0O0OO00 ))#line:758
        try :#line:759
            for O0O000000OOOO0O0O in range (O0OOOO00OO0O00O0O ):#line:760
                O000000O000OO0000 =O000000O000OO0000 +OO00OO00OOOO00O00 .format (O00OO0O0OO0O0OO00 ,tuple (O000O0O00O000OO0O [O0O000000OOOO0O0O ]))+'\n'#line:761
                if (O0O000000OOOO0O0O +1 )%per_in ==0 or O0O000000OOOO0O0O ==O0OOOO00OO0O00O0O -1 :#line:762
                    OO0OOOOO0O0O0O0OO ='insert all '+O000000O000OO0000 +'select 1 from dual'#line:763
                    logging .debug (OO0OOOOO0O0O0O0OO )#line:764
                    O0O0O00O0OOO00O00 .execute (OO0OOOOO0O0O0O0OO )#line:765
                    OO000O00OO00OOOO0 .commit ()#line:766
                    O000000O000OO0000 =''#line:767
            return str (O0OOOO00OO0O00O0O )#line:768
        except Exception as OOOOOO0OOO0OOO00O :#line:769
            try :#line:770
                OO000O00OO00OOOO0 .rollback ()#line:771
                O0O0O00O0OOO00O00 .execute ("delete from {} where UPLOADTIME = '{}'".format (O00OO0O0OO0O0OO00 ,O000O0O00O000OO0O [0 ][-1 ]))#line:772
                OO000O00OO00OOOO0 .commit ()#line:773
            except Exception :#line:774
                logging .error ('can not delete by uploadtime')#line:775
            finally :#line:776
                raise OOOOOO0OOO0OOO00O #line:777
        finally :#line:778
            OO000O00OO00OOOO0 .close ()#line:779
class _OO0OOOO0OO0O0O000 (object ):#line:782
    connect =None #line:783
    def __init__ (O0O0O0000O0O0OOOO ,O00O000000O00O00O ,OOOOOOOO00O00O0OO ,OO00OO0O0000OO0OO ):#line:784
        O0O0O0000O0O0OOOO .offset =None #line:785
        O0O0O0000O0O0OOOO .db_err_count =0 #line:786
        O0O0O0000O0O0OOOO .topic =O00O000000O00O00O #line:787
        O0O0O0000O0O0OOOO .kafkaconfig =OOOOOOOO00O00O0OO #line:788
        O0O0O0000O0O0OOOO .offsetDict ={}#line:789
        O0O0O0000O0O0OOOO .current_dir =OO00OO0O0000OO0OO #line:790
        try :#line:791
            O0O0O0000O0O0OOOO .consumer =O0O0O0000O0O0OOOO .connect_kafka_customer ()#line:792
        except Exception as O0OOOO00OO0OOOO0O :#line:793
            O0OOOO00OO0OOOO0O ='kafka无法连接','ErrLocation：{}\n'.format (O00O000000O00O00O )+str (O0OOOO00OO0OOOO0O )+',kafka消费者无法创建'#line:794
            raise O0OOOO00OO0OOOO0O #line:795
    def get_toggle_or_offset (OO0OO0OOOOOO000OO ,O0O00O0O0OOOO000O ,OOO0000O0O00O00O0 ):#line:798
        ""#line:799
        O0OO0OO0OOOOO0000 =0 #line:800
        try :#line:801
            O000O00OO00O000O0 =f"{OO0OO0OOOOOO000OO.current_dir}/kafka/{O0O00O0O0OOOO000O}_offset_{OOO0000O0O00O00O0}.txt"#line:802
            if os .path .exists (O000O00OO00O000O0 ):#line:803
                OO0OOO00000OOO00O =open (O000O00OO00O000O0 ).read ()#line:804
                if OO0OOO00000OOO00O :#line:805
                    O0OO0OO0OOOOO0000 =int (OO0OOO00000OOO00O )#line:806
            else :#line:807
                with open (O000O00OO00O000O0 ,encoding ='utf-8',mode ='a')as OO0000OO0O000OO00 :#line:808
                    OO0000OO0O000OO00 .close ()#line:809
        except Exception as OO00OOO0O0OOOOOO0 :#line:810
            print (f"读取失败：{OO00OOO0O0OOOOOO0}")#line:811
            raise OO00OOO0O0OOOOOO0 #line:812
        return O0OO0OO0OOOOO0000 #line:813
    def write_offset (O0O0O0O00OOOOOOO0 ,O0O0O0OO0OOOOOO00 ,offset =None ):#line:815
        ""#line:818
        if O0O0O0O00OOOOOOO0 .topic and offset :#line:819
            OO0O00OOOOOO0OOO0 =f"{O0O0O0O00OOOOOOO0.current_dir}/kafka/{O0O0O0O00OOOOOOO0.topic}_offset_{O0O0O0OO0OOOOOO00}.txt"#line:821
            try :#line:822
                with open (OO0O00OOOOOO0OOO0 ,'w')as O0000OOO0OOOOOOOO :#line:823
                    O0000OOO0OOOOOOOO .write (str (offset ))#line:824
                    O0000OOO0OOOOOOOO .close ()#line:825
            except Exception as OOO0O0OO00OOO0O00 :#line:826
                print (f"写入offset出错：{OOO0O0OO00OOO0O00}")#line:827
                raise OOO0O0OO00OOO0O00 #line:828
    def connect_kafka_customer (O0O0OOO00O0O0O000 ):#line:830
        ""#line:831
        OOOOOO0OO000000O0 =KafkaConsumer (**O0O0OOO00O0O0O000 .kafkaconfig )#line:832
        return OOOOOO0OO000000O0 #line:833
    def parse_data (O000000000O0O0OOO ,O00OOOOO0OOOO0000 ):#line:835
        ""#line:840
        return dict ()#line:841
    def gen_sql (OO000O0OO00OO000O ,OOOOO0OOOOO00O0O0 ):#line:843
        ""#line:848
        O0O0O000OOOO000OO =[]#line:849
        for O00O0OO0OOO00O0O0 in OOOOO0OOOOO00O0O0 :#line:850
            O0O0O000OOOO000OO .append (str (tuple (O00O0OO0OOO00O0O0 )))#line:852
        return ','.join (O0O0O000OOOO000OO )#line:853
    def dispose_kafka_data (O0OO0O0000OO00OOO ,OOO0O00O00OO00O00 ):#line:855
        ""#line:860
        pass #line:861
    def get_now_time (OO0O00000OO0O00OO ):#line:863
        ""#line:867
        O0OO0OOO0OO0O0000 =int (time .time ())#line:868
        return time .strftime ('%Y-%m-%d %H:%M:%S',time .localtime (O0OO0OOO0OO0O0000 ))#line:869
    def tran_data (O000OO00OOO000000 ,O00O00000OOO0O0O0 ,OO00O0O000O0000OO ):#line:871
        ""#line:877
        O000O0OOO0O0O0000 =O00O00000OOO0O0O0 .get (OO00O0O000O0000OO ,"")#line:878
        O000O0OOO0O0O0000 =""if O000O0OOO0O0O0000 is None else O000O0OOO0O0O0000 #line:879
        return str (O000O0OOO0O0O0000 )#line:880
    def consumer_data (O0O0OO000O0OO00OO ,O0000OOO0OOO00OOO ,O000O00O0OO0OO000 ,OO0O0O000000OO000 ):#line:882
        ""#line:889
        if O0O0OO000O0OO00OO .consumer :#line:890
            O0O0OO000O0OO00OO .consumer .assign ([TopicPartition (topic =O0O0OO000O0OO00OO .topic ,partition =O0000OOO0OOO00OOO )])#line:891
            OO00O0OOOO00O0000 =TopicPartition (topic =O0O0OO000O0OO00OO .topic ,partition =O0000OOO0OOO00OOO )#line:893
            OOOOOOOO0O00OO0OO =O0O0OO000O0OO00OO .consumer .beginning_offsets ([OO00O0OOOO00O0000 ])#line:894
            O0OOO000O00OOOO0O =OOOOOOOO0O00OO0OO .get (OO00O0OOOO00O0000 )#line:895
            OOOOO0O00O0O0OOOO =O0O0OO000O0OO00OO .consumer .end_offsets ([OO00O0OOOO00O0000 ])#line:896
            O0000O000O0OO0O0O =OOOOO0O00O0O0OOOO .get (OO00O0OOOO00O0000 )#line:897
            print (f'建立消费者, {O0000OOO0OOO00OOO}分区, 最小offset:{O0OOO000O00OOOO0O}, 最大offset:{O0000O000O0OO0O0O}')#line:898
            if O000O00O0OO0OO000 >=O0000O000O0OO0O0O :#line:899
                print (f'消费offset：{O000O00O0OO0OO000} 大于最大offset:{O0000O000O0OO0O0O}, 本次不消费')#line:900
                return #line:901
            if O000O00O0OO0OO000 <O0OOO000O00OOOO0O :#line:902
                print (f'Warning: 消费offset：{O000O00O0OO0OO000} 小于最小offset:{O0OOO000O00OOOO0O}')#line:903
                O000O00O0OO0OO000 =O0OOO000O00OOOO0O #line:904
            O0O0OO000O0OO00OO .consumer .seek (TopicPartition (topic =O0O0OO000O0OO00OO .topic ,partition =O0000OOO0OOO00OOO ),offset =O000O00O0OO0OO000 )#line:905
            print (f'消费{O0000OOO0OOO00OOO}分区, 开始消费offset：{O000O00O0OO0OO000}')#line:906
            OO0O0O000O00OO0OO =OO0O0O000000OO000 (O0O0OO000O0OO00OO .consumer )#line:907
            O000O00O0OO0OO000 =OO0O0O000O00OO0OO.offset +1 #line:908
            O0O0OO000O0OO00OO .offsetDict [O0000OOO0OOO00OOO ]=O000O00O0OO0OO000 #line:911
            O0O0OO000O0OO00OO .write_offset (O0000OOO0OOO00OOO ,O000O00O0OO0OO000 )#line:912
    def consumer_topic (OO00O0O000OOOO00O ,OO0OO0O00OO00O000 ):#line:914
        print (f"topic: {OO00O0O000OOOO00O.topic}")#line:915
        print ('开始解析。')#line:916
        O0O0O0O000OOO000O =OO00O0O000OOOO00O .consumer .partitions_for_topic (topic =OO00O0O000OOOO00O .topic )#line:918
        for O0O0OOOOO00OO0O00 in O0O0O0O000OOO000O :#line:919
            O0OOO0O0O0OO0O000 =OO00O0O000OOOO00O .get_toggle_or_offset (OO00O0O000OOOO00O .topic ,O0O0OOOOO00OO0O00 )#line:920
            O00O0O00O0OOOOOO0 =None if O0OOO0O0O0OO0O000 <0 else O0OOO0O0O0OO0O000 #line:922
            OO00O0O000OOOO00O .consumer_data (O0O0OOOOO00OO0O00 ,O00O0O00O0OOOOOO0 ,OO0OO0O00OO00O000 )#line:923
    def save_all_offset (OO00O000O00OO0O00 ):#line:925
        for OO000O00000OO00OO ,O0O000OO0OOOO0OO0 in OO00O000O00OO0O00 .offsetDict :#line:926
            OO00O000O00OO0O00 .write_offset (OO000O00000OO00OO ,O0O000OO0OOOO0OO0 )#line:927
