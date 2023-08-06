import sys #line:10
import time #line:11
import copy #line:12
from time import strftime #line:14
from time import gmtime #line:15
import pandas as pd #line:17
import numpy #line:18
class cleverminer :#line:20
    version_string ="1.0.0"#line:22
    def __init__ (OOOO000OOO0OOO000 ,**O00O00O0OO00OOO00 ):#line:24
        OOOO000OOO0OOO000 ._print_disclaimer ()#line:25
        OOOO000OOO0OOO000 .stats ={'total_cnt':0 ,'total_ver':0 ,'total_valid':0 ,'control_number':0 ,'start_prep_time':time .time (),'end_prep_time':time .time (),'start_proc_time':time .time (),'end_proc_time':time .time ()}#line:34
        OOOO000OOO0OOO000 .options ={'max_categories':100 ,'max_rules':None ,'optimizations':True }#line:38
        OOOO000OOO0OOO000 .kwargs =None #line:39
        if len (O00O00O0OO00OOO00 )>0 :#line:40
            OOOO000OOO0OOO000 .kwargs =O00O00O0OO00OOO00 #line:41
        OOOO000OOO0OOO000 .verbosity ={}#line:42
        OOOO000OOO0OOO000 .verbosity ['debug']=False #line:43
        OOOO000OOO0OOO000 .verbosity ['print_rules']=False #line:44
        OOOO000OOO0OOO000 .verbosity ['print_hashes']=True #line:45
        OOOO000OOO0OOO000 .verbosity ['last_hash_time']=0 #line:46
        OOOO000OOO0OOO000 .verbosity ['hint']=False #line:47
        if "opts"in O00O00O0OO00OOO00 :#line:48
            OOOO000OOO0OOO000 ._set_opts (O00O00O0OO00OOO00 .get ("opts"))#line:49
        if "opts"in O00O00O0OO00OOO00 :#line:50
            if "verbose"in O00O00O0OO00OOO00 .get ('opts'):#line:51
                if O00O00O0OO00OOO00 ['verbose'].upper ()=='FULL':#line:52
                    OOOO000OOO0OOO000 .verbosity ['debug']=True #line:53
                    OOOO000OOO0OOO000 .verbosity ['print_rules']=True #line:54
                    OOOO000OOO0OOO000 .verbosity ['print_hashes']=False #line:55
                    OOOO000OOO0OOO000 .verbosity ['hint']=True #line:56
                elif O00O00O0OO00OOO00 ['verbose'].upper ()=='RULES':#line:57
                    OOOO000OOO0OOO000 .verbosity ['debug']=False #line:58
                    OOOO000OOO0OOO000 .verbosity ['print_rules']=True #line:59
                    OOOO000OOO0OOO000 .verbosity ['print_hashes']=True #line:60
                    OOOO000OOO0OOO000 .verbosity ['hint']=True #line:61
                elif O00O00O0OO00OOO00 ['verbose'].upper ()=='HINT':#line:62
                    OOOO000OOO0OOO000 .verbosity ['debug']=False #line:63
                    OOOO000OOO0OOO000 .verbosity ['print_rules']=False #line:64
                    OOOO000OOO0OOO000 .verbosity ['print_hashes']=True #line:65
                    OOOO000OOO0OOO000 .verbosity ['last_hash_time']=0 #line:66
                    OOOO000OOO0OOO000 .verbosity ['hint']=True #line:67
        OOOO000OOO0OOO000 ._is_py310 =sys .version_info [0 ]>=4 or (sys .version_info [0 ]>=3 and sys .version_info [1 ]>=10 )#line:68
        if not (OOOO000OOO0OOO000 ._is_py310 ):#line:69
            print ("Warning: Python 3.10+ NOT detected. You should upgrade to Python 3.10 or greater to get better performance")#line:70
        else :#line:71
            if (OOOO000OOO0OOO000 .verbosity ['debug']):#line:72
                print ("Python 3.10+ detected.")#line:73
        OOOO000OOO0OOO000 ._initialized =False #line:74
        OOOO000OOO0OOO000 ._init_data ()#line:75
        OOOO000OOO0OOO000 ._init_task ()#line:76
        if len (O00O00O0OO00OOO00 )>0 :#line:77
            if "df"in O00O00O0OO00OOO00 :#line:78
                OOOO000OOO0OOO000 ._prep_data (O00O00O0OO00OOO00 .get ("df"))#line:79
            else :#line:80
                print ("Missing dataframe. Cannot initialize.")#line:81
                OOOO000OOO0OOO000 ._initialized =False #line:82
                return #line:83
            O000O000O0O00000O =O00O00O0OO00OOO00 .get ("proc",None )#line:84
            if not (O000O000O0O00000O ==None ):#line:85
                OOOO000OOO0OOO000 ._calculate (**O00O00O0OO00OOO00 )#line:86
            else :#line:88
                if OOOO000OOO0OOO000 .verbosity ['debug']:#line:89
                    print ("INFO: just initialized")#line:90
        OOOO000OOO0OOO000 ._initialized =True #line:91
    def _set_opts (OOO0OOOOOOO0000OO ,O0O00OOO0OO00O00O ):#line:93
        if "no_optimizations"in O0O00OOO0OO00O00O :#line:94
            OOO0OOOOOOO0000OO .options ['optimizations']=not (O0O00OOO0OO00O00O ['no_optimizations'])#line:95
            print ("No optimization will be made.")#line:96
        if "max_rules"in O0O00OOO0OO00O00O :#line:97
            OOO0OOOOOOO0000OO .options ['max_rules']=O0O00OOO0OO00O00O ['max_rules']#line:98
        if "max_categories"in O0O00OOO0OO00O00O :#line:99
            OOO0OOOOOOO0000OO .options ['max_categories']=O0O00OOO0OO00O00O ['max_categories']#line:100
            if OOO0OOOOOOO0000OO .verbosity ['debug']==True :#line:101
                print (f"Maximum number of categories set to {OOO0OOOOOOO0000OO.options['max_categories']}")#line:102
    def _init_data (O0O0000OOOOO0OOOO ):#line:105
        O0O0000OOOOO0OOOO .data ={}#line:107
        O0O0000OOOOO0OOOO .data ["varname"]=[]#line:108
        O0O0000OOOOO0OOOO .data ["catnames"]=[]#line:109
        O0O0000OOOOO0OOOO .data ["vtypes"]=[]#line:110
        O0O0000OOOOO0OOOO .data ["dm"]=[]#line:111
        O0O0000OOOOO0OOOO .data ["rows_count"]=int (0 )#line:112
        O0O0000OOOOO0OOOO .data ["data_prepared"]=0 #line:113
    def _init_task (OOOOO00O0000O00O0 ):#line:115
        if "opts"in OOOOO00O0000O00O0 .kwargs :#line:117
            OOOOO00O0000O00O0 ._set_opts (OOOOO00O0000O00O0 .kwargs .get ("opts"))#line:118
        OOOOO00O0000O00O0 .cedent ={'cedent_type':'none','defi':{},'num_cedent':0 ,'trace_cedent':[],'trace_cedent_asindata':[],'traces':[],'generated_string':'','rule':{},'filter_value':int (0 )}#line:128
        OOOOO00O0000O00O0 .task_actinfo ={'proc':'','cedents_to_do':[],'cedents':[]}#line:132
        OOOOO00O0000O00O0 .rulelist =[]#line:133
        OOOOO00O0000O00O0 .stats ['total_cnt']=0 #line:135
        OOOOO00O0000O00O0 .stats ['total_valid']=0 #line:136
        OOOOO00O0000O00O0 .stats ['control_number']=0 #line:137
        OOOOO00O0000O00O0 .result ={}#line:138
        OOOOO00O0000O00O0 ._opt_base =None #line:139
        OOOOO00O0000O00O0 ._opt_relbase =None #line:140
        OOOOO00O0000O00O0 ._opt_base1 =None #line:141
        OOOOO00O0000O00O0 ._opt_relbase1 =None #line:142
        OOOOO00O0000O00O0 ._opt_base2 =None #line:143
        OOOOO00O0000O00O0 ._opt_relbase2 =None #line:144
        OO0000OOOOO0O0O0O =None #line:145
        if not (OOOOO00O0000O00O0 .kwargs ==None ):#line:146
            OO0000OOOOO0O0O0O =OOOOO00O0000O00O0 .kwargs .get ("quantifiers",None )#line:147
            if not (OO0000OOOOO0O0O0O ==None ):#line:148
                for O000O00O0OO0OO0OO in OO0000OOOOO0O0O0O .keys ():#line:149
                    if O000O00O0OO0OO0OO .upper ()=='BASE':#line:150
                        OOOOO00O0000O00O0 ._opt_base =OO0000OOOOO0O0O0O .get (O000O00O0OO0OO0OO )#line:151
                    if O000O00O0OO0OO0OO .upper ()=='RELBASE':#line:152
                        OOOOO00O0000O00O0 ._opt_relbase =OO0000OOOOO0O0O0O .get (O000O00O0OO0OO0OO )#line:153
                    if (O000O00O0OO0OO0OO .upper ()=='FRSTBASE')|(O000O00O0OO0OO0OO .upper ()=='BASE1'):#line:154
                        OOOOO00O0000O00O0 ._opt_base1 =OO0000OOOOO0O0O0O .get (O000O00O0OO0OO0OO )#line:155
                    if (O000O00O0OO0OO0OO .upper ()=='SCNDBASE')|(O000O00O0OO0OO0OO .upper ()=='BASE2'):#line:156
                        OOOOO00O0000O00O0 ._opt_base2 =OO0000OOOOO0O0O0O .get (O000O00O0OO0OO0OO )#line:157
                    if (O000O00O0OO0OO0OO .upper ()=='FRSTRELBASE')|(O000O00O0OO0OO0OO .upper ()=='RELBASE1'):#line:158
                        OOOOO00O0000O00O0 ._opt_relbase1 =OO0000OOOOO0O0O0O .get (O000O00O0OO0OO0OO )#line:159
                    if (O000O00O0OO0OO0OO .upper ()=='SCNDRELBASE')|(O000O00O0OO0OO0OO .upper ()=='RELBASE2'):#line:160
                        OOOOO00O0000O00O0 ._opt_relbase2 =OO0000OOOOO0O0O0O .get (O000O00O0OO0OO0OO )#line:161
            else :#line:162
                print ("Warning: no quantifiers found. Optimization will not take place (1)")#line:163
        else :#line:164
            print ("Warning: no quantifiers found. Optimization will not take place (2)")#line:165
    def mine (O00OOOOO000000000 ,**O0OOOOOOO0O0OOOOO ):#line:168
        if not (O00OOOOO000000000 ._initialized ):#line:169
            print ("Class NOT INITIALIZED. Please call constructor with dataframe first")#line:170
            return #line:171
        O00OOOOO000000000 .kwargs =None #line:172
        if len (O0OOOOOOO0O0OOOOO )>0 :#line:173
            O00OOOOO000000000 .kwargs =O0OOOOOOO0O0OOOOO #line:174
        O00OOOOO000000000 ._init_task ()#line:175
        if len (O0OOOOOOO0O0OOOOO )>0 :#line:176
            O0O0OO0OO000OOOO0 =O0OOOOOOO0O0OOOOO .get ("proc",None )#line:177
            if not (O0O0OO0OO000OOOO0 ==None ):#line:178
                O00OOOOO000000000 ._calc_all (**O0OOOOOOO0O0OOOOO )#line:179
            else :#line:180
                print ("Rule mining procedure missing")#line:181
    def _get_ver (O0O0OOO00000O0OO0 ):#line:184
        return O0O0OOO00000O0OO0 .version_string #line:185
    def _print_disclaimer (O0OOOO0O0O0OO0OO0 ):#line:187
        print (f"Cleverminer version {O0OOOO0O0O0OO0OO0._get_ver()}. Note: This version is for personal and educational use only. If you need PRO version (support, fixing structures for compactibility in future versions for production deployment, additional development, licensing of commercial use of subroutines used), feel free to ask authors. Most of these functionalities are maintained in best-effort, as soon as this project is at given conditions for free use and rapid development is needed, they cannot be guaranteed.")#line:189
    def _prep_data (O000OOO0OO0OOO0O0 ,OOO0OO0OO0O0OO0O0 ):#line:195
        print ("Starting data preparation ...")#line:196
        O000OOO0OO0OOO0O0 ._init_data ()#line:197
        O000OOO0OO0OOO0O0 .stats ['start_prep_time']=time .time ()#line:198
        O000OOO0OO0OOO0O0 .data ["rows_count"]=OOO0OO0OO0O0OO0O0 .shape [0 ]#line:199
        for OOOO0OOO0OOOOOO0O in OOO0OO0OO0O0OO0O0 .select_dtypes (exclude =['category']).columns :#line:200
            OOO0OO0OO0O0OO0O0 [OOOO0OOO0OOOOOO0O ]=OOO0OO0OO0O0OO0O0 [OOOO0OOO0OOOOOO0O ].apply (str )#line:201
        OOOOOOO00OOOO0OOO =pd .DataFrame .from_records ([(OO000OO0OO00O000O ,OOO0OO0OO0O0OO0O0 [OO000OO0OO00O000O ].nunique ())for OO000OO0OO00O000O in OOO0OO0OO0O0OO0O0 .columns ],columns =['Column_Name','Num_Unique']).sort_values (by =['Num_Unique'])#line:203
        if O000OOO0OO0OOO0O0 .verbosity ['hint']:#line:204
            print ("Quick profile of input data: unique value counts are:")#line:205
            print (OOOOOOO00OOOO0OOO )#line:206
            for OOOO0OOO0OOOOOO0O in OOO0OO0OO0O0OO0O0 .columns :#line:207
                if OOO0OO0OO0O0OO0O0 [OOOO0OOO0OOOOOO0O ].nunique ()<O000OOO0OO0OOO0O0 .options ['max_categories']:#line:208
                    OOO0OO0OO0O0OO0O0 [OOOO0OOO0OOOOOO0O ]=OOO0OO0OO0O0OO0O0 [OOOO0OOO0OOOOOO0O ].astype ('category')#line:209
                else :#line:210
                    print (f"WARNING: attribute {OOOO0OOO0OOOOOO0O} has more than {O000OOO0OO0OOO0O0.options['max_categories']} values, will be ignored.\r\n If you haven't set maximum number of categories and you really need more categories and you know what you are doing, please use max_categories option to increase allowed number of categories.")#line:211
                    del OOO0OO0OO0O0OO0O0 [OOOO0OOO0OOOOOO0O ]#line:212
        print ("Encoding columns into bit-form...")#line:213
        O000OOOOO000OOO00 =0 #line:214
        O000O0000O00OO00O =0 #line:215
        for OOOOO0000000OO0O0 in OOO0OO0OO0O0OO0O0 :#line:216
            if O000OOO0OO0OOO0O0 .verbosity ['debug']:#line:218
                print ('Column: '+OOOOO0000000OO0O0 )#line:219
            O000OOO0OO0OOO0O0 .data ["varname"].append (OOOOO0000000OO0O0 )#line:220
            OO00OOOO0O0OO0OOO =pd .get_dummies (OOO0OO0OO0O0OO0O0 [OOOOO0000000OO0O0 ])#line:221
            OOOOOOO0000O00O00 =0 #line:222
            if (OOO0OO0OO0O0OO0O0 .dtypes [OOOOO0000000OO0O0 ].name =='category'):#line:223
                OOOOOOO0000O00O00 =1 #line:224
            O000OOO0OO0OOO0O0 .data ["vtypes"].append (OOOOOOO0000O00O00 )#line:225
            O0O0OO0000OOO00O0 =0 #line:228
            OOO0OO0OOOOOO0OO0 =[]#line:229
            O0O00OO0OOO0OO0O0 =[]#line:230
            for OOOO0000000OO0000 in OO00OOOO0O0OO0OOO :#line:232
                if O000OOO0OO0OOO0O0 .verbosity ['debug']:#line:234
                    print ('....category : '+str (OOOO0000000OO0000 )+" @ "+str (time .time ()))#line:235
                OOO0OO0OOOOOO0OO0 .append (OOOO0000000OO0000 )#line:236
                O00O00OOOOO0O000O =int (0 )#line:237
                OO0O0OO000OO00O0O =OO00OOOO0O0OO0OOO [OOOO0000000OO0000 ].values #line:238
                O0000O0O0OOOOOOOO =numpy .packbits (OO0O0OO000OO00O0O ,bitorder ='little')#line:240
                O00O00OOOOO0O000O =int .from_bytes (O0000O0O0OOOOOOOO ,byteorder ='little')#line:241
                O0O00OO0OOO0OO0O0 .append (O00O00OOOOO0O000O )#line:242
                O0O0OO0000OOO00O0 +=1 #line:260
                O000O0000O00OO00O +=1 #line:261
            O000OOO0OO0OOO0O0 .data ["catnames"].append (OOO0OO0OOOOOO0OO0 )#line:263
            O000OOO0OO0OOO0O0 .data ["dm"].append (O0O00OO0OOO0OO0O0 )#line:264
        print ("Encoding columns into bit-form...done")#line:266
        if O000OOO0OO0OOO0O0 .verbosity ['hint']:#line:267
            print (f"List of attributes for analysis is: {O000OOO0OO0OOO0O0.data['varname']}")#line:268
            print (f"List of category names for individual attributes is : {O000OOO0OO0OOO0O0.data['catnames']}")#line:269
        if O000OOO0OO0OOO0O0 .verbosity ['debug']:#line:270
            print (f"List of vtypes is (all should be 1) : {O000OOO0OO0OOO0O0.data['vtypes']}")#line:271
        O000OOO0OO0OOO0O0 .data ["data_prepared"]=1 #line:273
        print ("Data preparation finished.")#line:274
        if O000OOO0OO0OOO0O0 .verbosity ['debug']:#line:275
            print ('Number of variables : '+str (len (O000OOO0OO0OOO0O0 .data ["dm"])))#line:276
            print ('Total number of categories in all variables : '+str (O000O0000O00OO00O ))#line:277
        O000OOO0OO0OOO0O0 .stats ['end_prep_time']=time .time ()#line:278
        if O000OOO0OO0OOO0O0 .verbosity ['debug']:#line:279
            print ('Time needed for data preparation : ',str (O000OOO0OO0OOO0O0 .stats ['end_prep_time']-O000OOO0OO0OOO0O0 .stats ['start_prep_time']))#line:280
    def _bitcount (OOO000OO0O0O0O0OO ,OOOOOOOO0OO00O000 ):#line:282
        O0O000O0000OOO00O =None #line:283
        if (OOO000OO0O0O0O0OO ._is_py310 ):#line:284
            O0O000O0000OOO00O =OOOOOOOO0OO00O000 .bit_count ()#line:285
        else :#line:286
            O0O000O0000OOO00O =bin (OOOOOOOO0OO00O000 ).count ("1")#line:287
        return O0O000O0000OOO00O #line:288
    def _verifyCF (O0O00O0OO0O0O000O ,_OOOO00OOOOOOOO000 ):#line:291
        OO000000O0O0O0000 =O0O00O0OO0O0O000O ._bitcount (_OOOO00OOOOOOOO000 )#line:292
        OO0OO0000OO0O0O0O =[]#line:293
        O0O0O0OO0O0OO00O0 =[]#line:294
        O000OOOO00OO00OO0 =0 #line:295
        OOO0OOO00O0O00O0O =0 #line:296
        OO0OO0O0OOOO0O0O0 =0 #line:297
        OO000O00O000000O0 =0 #line:298
        OOO0OO00O00OOO00O =0 #line:299
        OO0O00O0OO0OO0O0O =0 #line:300
        O0000000OO00O0OO0 =0 #line:301
        O00OOOO000000O0OO =0 #line:302
        O0O00000O00000000 =0 #line:303
        OOOOOO000OO0O0000 =O0O00O0OO0O0O000O .data ["dm"][O0O00O0OO0O0O000O .data ["varname"].index (O0O00O0OO0O0O000O .kwargs .get ('target'))]#line:304
        for O0000O000OO0000O0 in range (len (OOOOOO000OO0O0000 )):#line:305
            OOO0OOO00O0O00O0O =O000OOOO00OO00OO0 #line:306
            O000OOOO00OO00OO0 =O0O00O0OO0O0O000O ._bitcount (_OOOO00OOOOOOOO000 &OOOOOO000OO0O0000 [O0000O000OO0000O0 ])#line:307
            OO0OO0000OO0O0O0O .append (O000OOOO00OO00OO0 )#line:308
            if O0000O000OO0000O0 >0 :#line:309
                if (O000OOOO00OO00OO0 >OOO0OOO00O0O00O0O ):#line:310
                    if (OO0OO0O0OOOO0O0O0 ==1 ):#line:311
                        O00OOOO000000O0OO +=1 #line:312
                    else :#line:313
                        O00OOOO000000O0OO =1 #line:314
                    if O00OOOO000000O0OO >OO000O00O000000O0 :#line:315
                        OO000O00O000000O0 =O00OOOO000000O0OO #line:316
                    OO0OO0O0OOOO0O0O0 =1 #line:317
                    OO0O00O0OO0OO0O0O +=1 #line:318
                if (O000OOOO00OO00OO0 <OOO0OOO00O0O00O0O ):#line:319
                    if (OO0OO0O0OOOO0O0O0 ==-1 ):#line:320
                        O0O00000O00000000 +=1 #line:321
                    else :#line:322
                        O0O00000O00000000 =1 #line:323
                    if O0O00000O00000000 >OOO0OO00O00OOO00O :#line:324
                        OOO0OO00O00OOO00O =O0O00000O00000000 #line:325
                    OO0OO0O0OOOO0O0O0 =-1 #line:326
                    O0000000OO00O0OO0 +=1 #line:327
                if (O000OOOO00OO00OO0 ==OOO0OOO00O0O00O0O ):#line:328
                    OO0OO0O0OOOO0O0O0 =0 #line:329
                    O0O00000O00000000 =0 #line:330
                    O00OOOO000000O0OO =0 #line:331
        OO0O0O0O0O00OO000 =True #line:334
        for O000O0O0000OO0OOO in O0O00O0OO0O0O000O .quantifiers .keys ():#line:335
            if O000O0O0000OO0OOO .upper ()=='BASE':#line:336
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=OO000000O0O0O0000 )#line:337
            if O000O0O0000OO0OOO .upper ()=='RELBASE':#line:338
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=OO000000O0O0O0000 *1.0 /O0O00O0OO0O0O000O .data ["rows_count"])#line:339
            if O000O0O0000OO0OOO .upper ()=='S_UP':#line:340
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=OO000O00O000000O0 )#line:341
            if O000O0O0000OO0OOO .upper ()=='S_DOWN':#line:342
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=OOO0OO00O00OOO00O )#line:343
            if O000O0O0000OO0OOO .upper ()=='S_ANY_UP':#line:344
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=OO000O00O000000O0 )#line:345
            if O000O0O0000OO0OOO .upper ()=='S_ANY_DOWN':#line:346
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=OOO0OO00O00OOO00O )#line:347
            if O000O0O0000OO0OOO .upper ()=='MAX':#line:348
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=max (OO0OO0000OO0O0O0O ))#line:349
            if O000O0O0000OO0OOO .upper ()=='MIN':#line:350
                OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=min (OO0OO0000OO0O0O0O ))#line:351
            if O000O0O0000OO0OOO .upper ()=='RELMAX':#line:352
                if sum (OO0OO0000OO0O0O0O )>0 :#line:353
                    OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=max (OO0OO0000OO0O0O0O )*1.0 /sum (OO0OO0000OO0O0O0O ))#line:354
                else :#line:355
                    OO0O0O0O0O00OO000 =False #line:356
            if O000O0O0000OO0OOO .upper ()=='RELMAX_LEQ':#line:357
                if sum (OO0OO0000OO0O0O0O )>0 :#line:358
                    OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )>=max (OO0OO0000OO0O0O0O )*1.0 /sum (OO0OO0000OO0O0O0O ))#line:359
                else :#line:360
                    OO0O0O0O0O00OO000 =False #line:361
            if O000O0O0000OO0OOO .upper ()=='RELMIN':#line:362
                if sum (OO0OO0000OO0O0O0O )>0 :#line:363
                    OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )<=min (OO0OO0000OO0O0O0O )*1.0 /sum (OO0OO0000OO0O0O0O ))#line:364
                else :#line:365
                    OO0O0O0O0O00OO000 =False #line:366
            if O000O0O0000OO0OOO .upper ()=='RELMIN_LEQ':#line:367
                if sum (OO0OO0000OO0O0O0O )>0 :#line:368
                    OO0O0O0O0O00OO000 =OO0O0O0O0O00OO000 and (O0O00O0OO0O0O000O .quantifiers .get (O000O0O0000OO0OOO )>=min (OO0OO0000OO0O0O0O )*1.0 /sum (OO0OO0000OO0O0O0O ))#line:369
                else :#line:370
                    OO0O0O0O0O00OO000 =False #line:371
        O0OOOO0O000O00O0O ={}#line:372
        if OO0O0O0O0O00OO000 ==True :#line:373
            O0O00O0OO0O0O000O .stats ['total_valid']+=1 #line:375
            O0OOOO0O000O00O0O ["base"]=OO000000O0O0O0000 #line:376
            O0OOOO0O000O00O0O ["rel_base"]=OO000000O0O0O0000 *1.0 /O0O00O0OO0O0O000O .data ["rows_count"]#line:377
            O0OOOO0O000O00O0O ["s_up"]=OO000O00O000000O0 #line:378
            O0OOOO0O000O00O0O ["s_down"]=OOO0OO00O00OOO00O #line:379
            O0OOOO0O000O00O0O ["s_any_up"]=OO0O00O0OO0OO0O0O #line:380
            O0OOOO0O000O00O0O ["s_any_down"]=O0000000OO00O0OO0 #line:381
            O0OOOO0O000O00O0O ["max"]=max (OO0OO0000OO0O0O0O )#line:382
            O0OOOO0O000O00O0O ["min"]=min (OO0OO0000OO0O0O0O )#line:383
            if sum (OO0OO0000OO0O0O0O )>0 :#line:386
                O0OOOO0O000O00O0O ["rel_max"]=max (OO0OO0000OO0O0O0O )*1.0 /sum (OO0OO0000OO0O0O0O )#line:387
                O0OOOO0O000O00O0O ["rel_min"]=min (OO0OO0000OO0O0O0O )*1.0 /sum (OO0OO0000OO0O0O0O )#line:388
            else :#line:389
                O0OOOO0O000O00O0O ["rel_max"]=0 #line:390
                O0OOOO0O000O00O0O ["rel_min"]=0 #line:391
            O0OOOO0O000O00O0O ["hist"]=OO0OO0000OO0O0O0O #line:392
        return OO0O0O0O0O00OO000 ,O0OOOO0O000O00O0O #line:394
    def _verify4ft (O0OOO0O0000O0OOO0 ,_O0O00000O0OO0OO0O ):#line:396
        O000OO0OO0O000OO0 ={}#line:397
        OOO0O0OOOO000O0OO =0 #line:398
        for O0OO0O00O0OOOOO0O in O0OOO0O0000O0OOO0 .task_actinfo ['cedents']:#line:399
            O000OO0OO0O000OO0 [O0OO0O00O0OOOOO0O ['cedent_type']]=O0OO0O00O0OOOOO0O ['filter_value']#line:401
            OOO0O0OOOO000O0OO =OOO0O0OOOO000O0OO +1 #line:402
        O0OO0O0O000OOO0OO =O0OOO0O0000O0OOO0 ._bitcount (O000OO0OO0O000OO0 ['ante']&O000OO0OO0O000OO0 ['succ']&O000OO0OO0O000OO0 ['cond'])#line:404
        O0O0OOOOO0O0O00OO =None #line:405
        O0O0OOOOO0O0O00OO =0 #line:406
        if O0OO0O0O000OOO0OO >0 :#line:415
            O0O0OOOOO0O0O00OO =O0OOO0O0000O0OOO0 ._bitcount (O000OO0OO0O000OO0 ['ante']&O000OO0OO0O000OO0 ['succ']&O000OO0OO0O000OO0 ['cond'])*1.0 /O0OOO0O0000O0OOO0 ._bitcount (O000OO0OO0O000OO0 ['ante']&O000OO0OO0O000OO0 ['cond'])#line:416
        O0OOOO0OO0OO0O0O0 =1 <<O0OOO0O0000O0OOO0 .data ["rows_count"]#line:418
        OO000OOO000OO0000 =O0OOO0O0000O0OOO0 ._bitcount (O000OO0OO0O000OO0 ['ante']&O000OO0OO0O000OO0 ['succ']&O000OO0OO0O000OO0 ['cond'])#line:419
        OOOO0O00000OOO00O =O0OOO0O0000O0OOO0 ._bitcount (O000OO0OO0O000OO0 ['ante']&~(O0OOOO0OO0OO0O0O0 |O000OO0OO0O000OO0 ['succ'])&O000OO0OO0O000OO0 ['cond'])#line:420
        O0OO0O00O0OOOOO0O =O0OOO0O0000O0OOO0 ._bitcount (~(O0OOOO0OO0OO0O0O0 |O000OO0OO0O000OO0 ['ante'])&O000OO0OO0O000OO0 ['succ']&O000OO0OO0O000OO0 ['cond'])#line:421
        OOOOO0O0O00OOOOOO =O0OOO0O0000O0OOO0 ._bitcount (~(O0OOOO0OO0OO0O0O0 |O000OO0OO0O000OO0 ['ante'])&~(O0OOOO0OO0OO0O0O0 |O000OO0OO0O000OO0 ['succ'])&O000OO0OO0O000OO0 ['cond'])#line:422
        OO0O00OO000OOO00O =0 #line:423
        if (OO000OOO000OO0000 +OOOO0O00000OOO00O )*(OO000OOO000OO0000 +O0OO0O00O0OOOOO0O )>0 :#line:424
            OO0O00OO000OOO00O =OO000OOO000OO0000 *(OO000OOO000OO0000 +OOOO0O00000OOO00O +O0OO0O00O0OOOOO0O +OOOOO0O0O00OOOOOO )/(OO000OOO000OO0000 +OOOO0O00000OOO00O )/(OO000OOO000OO0000 +O0OO0O00O0OOOOO0O )-1 #line:425
        else :#line:426
            OO0O00OO000OOO00O =None #line:427
        OO0000OO000O00OO0 =0 #line:428
        if (OO000OOO000OO0000 +OOOO0O00000OOO00O )*(OO000OOO000OO0000 +O0OO0O00O0OOOOO0O )>0 :#line:429
            OO0000OO000O00OO0 =1 -OO000OOO000OO0000 *(OO000OOO000OO0000 +OOOO0O00000OOO00O +O0OO0O00O0OOOOO0O +OOOOO0O0O00OOOOOO )/(OO000OOO000OO0000 +OOOO0O00000OOO00O )/(OO000OOO000OO0000 +O0OO0O00O0OOOOO0O )#line:430
        else :#line:431
            OO0000OO000O00OO0 =None #line:432
        OOOOOO00OOO0000OO =True #line:433
        for OOOO00OO00OOO0OOO in O0OOO0O0000O0OOO0 .quantifiers .keys ():#line:434
            if OOOO00OO00OOO0OOO .upper ()=='BASE':#line:435
                OOOOOO00OOO0000OO =OOOOOO00OOO0000OO and (O0OOO0O0000O0OOO0 .quantifiers .get (OOOO00OO00OOO0OOO )<=O0OO0O0O000OOO0OO )#line:436
            if OOOO00OO00OOO0OOO .upper ()=='RELBASE':#line:437
                OOOOOO00OOO0000OO =OOOOOO00OOO0000OO and (O0OOO0O0000O0OOO0 .quantifiers .get (OOOO00OO00OOO0OOO )<=O0OO0O0O000OOO0OO *1.0 /O0OOO0O0000O0OOO0 .data ["rows_count"])#line:438
            if (OOOO00OO00OOO0OOO .upper ()=='PIM')or (OOOO00OO00OOO0OOO .upper ()=='CONF'):#line:439
                OOOOOO00OOO0000OO =OOOOOO00OOO0000OO and (O0OOO0O0000O0OOO0 .quantifiers .get (OOOO00OO00OOO0OOO )<=O0O0OOOOO0O0O00OO )#line:440
            if OOOO00OO00OOO0OOO .upper ()=='AAD':#line:441
                if OO0O00OO000OOO00O !=None :#line:442
                    OOOOOO00OOO0000OO =OOOOOO00OOO0000OO and (O0OOO0O0000O0OOO0 .quantifiers .get (OOOO00OO00OOO0OOO )<=OO0O00OO000OOO00O )#line:443
                else :#line:444
                    OOOOOO00OOO0000OO =False #line:445
            if OOOO00OO00OOO0OOO .upper ()=='BAD':#line:446
                if OO0000OO000O00OO0 !=None :#line:447
                    OOOOOO00OOO0000OO =OOOOOO00OOO0000OO and (O0OOO0O0000O0OOO0 .quantifiers .get (OOOO00OO00OOO0OOO )<=OO0000OO000O00OO0 )#line:448
                else :#line:449
                    OOOOOO00OOO0000OO =False #line:450
            OO0OO000O0O000O00 ={}#line:451
        if OOOOOO00OOO0000OO ==True :#line:452
            O0OOO0O0000O0OOO0 .stats ['total_valid']+=1 #line:454
            OO0OO000O0O000O00 ["base"]=O0OO0O0O000OOO0OO #line:455
            OO0OO000O0O000O00 ["rel_base"]=O0OO0O0O000OOO0OO *1.0 /O0OOO0O0000O0OOO0 .data ["rows_count"]#line:456
            OO0OO000O0O000O00 ["conf"]=O0O0OOOOO0O0O00OO #line:457
            OO0OO000O0O000O00 ["aad"]=OO0O00OO000OOO00O #line:458
            OO0OO000O0O000O00 ["bad"]=OO0000OO000O00OO0 #line:459
            OO0OO000O0O000O00 ["fourfold"]=[OO000OOO000OO0000 ,OOOO0O00000OOO00O ,O0OO0O00O0OOOOO0O ,OOOOO0O0O00OOOOOO ]#line:460
        return OOOOOO00OOO0000OO ,OO0OO000O0O000O00 #line:464
    def _verifysd4ft (O0OOO000OOO00000O ,_OOOO00OOOOOOOOO0O ):#line:466
        OOOOOO0OO0OO0O0OO ={}#line:467
        O0O00OO000000OO00 =0 #line:468
        for O00O0000O0O0O0OO0 in O0OOO000OOO00000O .task_actinfo ['cedents']:#line:469
            OOOOOO0OO0OO0O0OO [O00O0000O0O0O0OO0 ['cedent_type']]=O00O0000O0O0O0OO0 ['filter_value']#line:471
            O0O00OO000000OO00 =O0O00OO000000OO00 +1 #line:472
        OO00O0OOO0000OOOO =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])#line:474
        O00OOO0OO0O0OOOOO =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])#line:475
        O0O0OOO0O00O0OO0O =None #line:476
        O00OOO00OO00OO0O0 =0 #line:477
        OOOOO0O000OO000O0 =0 #line:478
        if OO00O0OOO0000OOOO >0 :#line:487
            O00OOO00OO00OO0O0 =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])*1.0 /O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])#line:488
        if O00OOO0OO0O0OOOOO >0 :#line:489
            OOOOO0O000OO000O0 =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])*1.0 /O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])#line:490
        O0OOO0O000O000OO0 =1 <<O0OOO000OOO00000O .data ["rows_count"]#line:492
        O000O000O00O0OO0O =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])#line:493
        O000O00OOOO0OOO00 =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['succ'])&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])#line:494
        OOO0OOOO00O0O0OOO =O0OOO000OOO00000O ._bitcount (~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['ante'])&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])#line:495
        O0000OO0O0OO0OOO0 =O0OOO000OOO00000O ._bitcount (~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['ante'])&~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['succ'])&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['frst'])#line:496
        O0OOO0O0OOO000000 =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])#line:497
        O0OOO00O000OO0OO0 =O0OOO000OOO00000O ._bitcount (OOOOOO0OO0OO0O0OO ['ante']&~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['succ'])&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])#line:498
        OOOOO000O00O0OOOO =O0OOO000OOO00000O ._bitcount (~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['ante'])&OOOOOO0OO0OO0O0OO ['succ']&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])#line:499
        O000OO00OO0O000OO =O0OOO000OOO00000O ._bitcount (~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['ante'])&~(O0OOO0O000O000OO0 |OOOOOO0OO0OO0O0OO ['succ'])&OOOOOO0OO0OO0O0OO ['cond']&OOOOOO0OO0OO0O0OO ['scnd'])#line:500
        O0000OOO0O00O0O00 =True #line:501
        for OOOO0OOO0O0OO0OO0 in O0OOO000OOO00000O .quantifiers .keys ():#line:502
            if (OOOO0OOO0O0OO0OO0 .upper ()=='FRSTBASE')|(OOOO0OOO0O0OO0OO0 .upper ()=='BASE1'):#line:503
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=OO00O0OOO0000OOOO )#line:504
            if (OOOO0OOO0O0OO0OO0 .upper ()=='SCNDBASE')|(OOOO0OOO0O0OO0OO0 .upper ()=='BASE2'):#line:505
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=O00OOO0OO0O0OOOOO )#line:506
            if (OOOO0OOO0O0OO0OO0 .upper ()=='FRSTRELBASE')|(OOOO0OOO0O0OO0OO0 .upper ()=='RELBASE1'):#line:507
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=OO00O0OOO0000OOOO *1.0 /O0OOO000OOO00000O .data ["rows_count"])#line:508
            if (OOOO0OOO0O0OO0OO0 .upper ()=='SCNDRELBASE')|(OOOO0OOO0O0OO0OO0 .upper ()=='RELBASE2'):#line:509
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=O00OOO0OO0O0OOOOO *1.0 /O0OOO000OOO00000O .data ["rows_count"])#line:510
            if (OOOO0OOO0O0OO0OO0 .upper ()=='FRSTPIM')|(OOOO0OOO0O0OO0OO0 .upper ()=='PIM1')|(OOOO0OOO0O0OO0OO0 .upper ()=='FRSTCONF')|(OOOO0OOO0O0OO0OO0 .upper ()=='CONF1'):#line:511
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=O00OOO00OO00OO0O0 )#line:512
            if (OOOO0OOO0O0OO0OO0 .upper ()=='SCNDPIM')|(OOOO0OOO0O0OO0OO0 .upper ()=='PIM2')|(OOOO0OOO0O0OO0OO0 .upper ()=='SCNDCONF')|(OOOO0OOO0O0OO0OO0 .upper ()=='CONF2'):#line:513
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=OOOOO0O000OO000O0 )#line:514
            if (OOOO0OOO0O0OO0OO0 .upper ()=='DELTAPIM')|(OOOO0OOO0O0OO0OO0 .upper ()=='DELTACONF'):#line:515
                O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=O00OOO00OO00OO0O0 -OOOOO0O000OO000O0 )#line:516
            if (OOOO0OOO0O0OO0OO0 .upper ()=='RATIOPIM')|(OOOO0OOO0O0OO0OO0 .upper ()=='RATIOCONF'):#line:519
                if (OOOOO0O000OO000O0 >0 ):#line:520
                    O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )<=O00OOO00OO00OO0O0 *1.0 /OOOOO0O000OO000O0 )#line:521
                else :#line:522
                    O0000OOO0O00O0O00 =False #line:523
            if (OOOO0OOO0O0OO0OO0 .upper ()=='RATIOPIM_LEQ')|(OOOO0OOO0O0OO0OO0 .upper ()=='RATIOCONF_LEQ'):#line:524
                if (OOOOO0O000OO000O0 >0 ):#line:525
                    O0000OOO0O00O0O00 =O0000OOO0O00O0O00 and (O0OOO000OOO00000O .quantifiers .get (OOOO0OOO0O0OO0OO0 )>=O00OOO00OO00OO0O0 *1.0 /OOOOO0O000OO000O0 )#line:526
                else :#line:527
                    O0000OOO0O00O0O00 =False #line:528
        O00000OOOO00O0O0O ={}#line:529
        if O0000OOO0O00O0O00 ==True :#line:530
            O0OOO000OOO00000O .stats ['total_valid']+=1 #line:532
            O00000OOOO00O0O0O ["base1"]=OO00O0OOO0000OOOO #line:533
            O00000OOOO00O0O0O ["base2"]=O00OOO0OO0O0OOOOO #line:534
            O00000OOOO00O0O0O ["rel_base1"]=OO00O0OOO0000OOOO *1.0 /O0OOO000OOO00000O .data ["rows_count"]#line:535
            O00000OOOO00O0O0O ["rel_base2"]=O00OOO0OO0O0OOOOO *1.0 /O0OOO000OOO00000O .data ["rows_count"]#line:536
            O00000OOOO00O0O0O ["conf1"]=O00OOO00OO00OO0O0 #line:537
            O00000OOOO00O0O0O ["conf2"]=OOOOO0O000OO000O0 #line:538
            O00000OOOO00O0O0O ["deltaconf"]=O00OOO00OO00OO0O0 -OOOOO0O000OO000O0 #line:539
            if (OOOOO0O000OO000O0 >0 ):#line:540
                O00000OOOO00O0O0O ["ratioconf"]=O00OOO00OO00OO0O0 *1.0 /OOOOO0O000OO000O0 #line:541
            else :#line:542
                O00000OOOO00O0O0O ["ratioconf"]=None #line:543
            O00000OOOO00O0O0O ["fourfold1"]=[O000O000O00O0OO0O ,O000O00OOOO0OOO00 ,OOO0OOOO00O0O0OOO ,O0000OO0O0OO0OOO0 ]#line:544
            O00000OOOO00O0O0O ["fourfold2"]=[O0OOO0O0OOO000000 ,O0OOO00O000OO0OO0 ,OOOOO000O00O0OOOO ,O000OO00OO0O000OO ]#line:545
        return O0000OOO0O00O0O00 ,O00000OOOO00O0O0O #line:549
    def _verifynewact4ft (O0O000OO0O0O000O0 ,_O0OOOOO0O00O00OOO ):#line:551
        O00OO0OOOO0000O0O ={}#line:552
        for O000OO0000O0OO000 in O0O000OO0O0O000O0 .task_actinfo ['cedents']:#line:553
            O00OO0OOOO0000O0O [O000OO0000O0OO000 ['cedent_type']]=O000OO0000O0OO000 ['filter_value']#line:555
        O0O0O0O0O0OOO0OOO =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond'])#line:557
        O0OO000OO0O0OOO00 =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond']&O00OO0OOOO0000O0O ['antv']&O00OO0OOOO0000O0O ['sucv'])#line:558
        OOOO00OO000O00O00 =None #line:559
        OOOO0O00OO000O00O =0 #line:560
        OOOO0O000OO000O0O =0 #line:561
        if O0O0O0O0O0OOO0OOO >0 :#line:570
            OOOO0O00OO000O00O =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond'])*1.0 /O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['cond'])#line:571
        if O0OO000OO0O0OOO00 >0 :#line:572
            OOOO0O000OO000O0O =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond']&O00OO0OOOO0000O0O ['antv']&O00OO0OOOO0000O0O ['sucv'])*1.0 /O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['cond']&O00OO0OOOO0000O0O ['antv'])#line:574
        O00OOOO0OOOOO00OO =1 <<O0O000OO0O0O000O0 .rows_count #line:576
        OOOO0OO0O000O0O00 =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond'])#line:577
        OO0O0OOOOO0O00OO0 =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&~(O00OOOO0OOOOO00OO |O00OO0OOOO0000O0O ['succ'])&O00OO0OOOO0000O0O ['cond'])#line:578
        O000OOOOOO0OO0O0O =O0O000OO0O0O000O0 ._bitcount (~(O00OOOO0OOOOO00OO |O00OO0OOOO0000O0O ['ante'])&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond'])#line:579
        O0OO00O000O0O00OO =O0O000OO0O0O000O0 ._bitcount (~(O00OOOO0OOOOO00OO |O00OO0OOOO0000O0O ['ante'])&~(O00OOOO0OOOOO00OO |O00OO0OOOO0000O0O ['succ'])&O00OO0OOOO0000O0O ['cond'])#line:580
        OOOO0O00O0O0O0OOO =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond']&O00OO0OOOO0000O0O ['antv']&O00OO0OOOO0000O0O ['sucv'])#line:581
        O00OO0O00OOO00O0O =O0O000OO0O0O000O0 ._bitcount (O00OO0OOOO0000O0O ['ante']&~(O00OOOO0OOOOO00OO |(O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['sucv']))&O00OO0OOOO0000O0O ['cond'])#line:582
        OOO00O00O00000O0O =O0O000OO0O0O000O0 ._bitcount (~(O00OOOO0OOOOO00OO |(O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['antv']))&O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['cond']&O00OO0OOOO0000O0O ['sucv'])#line:583
        O00O0O00OOOOO0O00 =O0O000OO0O0O000O0 ._bitcount (~(O00OOOO0OOOOO00OO |(O00OO0OOOO0000O0O ['ante']&O00OO0OOOO0000O0O ['antv']))&~(O00OOOO0OOOOO00OO |(O00OO0OOOO0000O0O ['succ']&O00OO0OOOO0000O0O ['sucv']))&O00OO0OOOO0000O0O ['cond'])#line:584
        OOOO0O00OO0000OO0 =True #line:585
        for O000O0OO0000OOOO0 in O0O000OO0O0O000O0 .quantifiers .keys ():#line:586
            if (O000O0OO0000OOOO0 =='PreBase')|(O000O0OO0000OOOO0 =='Base1'):#line:587
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=O0O0O0O0O0OOO0OOO )#line:588
            if (O000O0OO0000OOOO0 =='PostBase')|(O000O0OO0000OOOO0 =='Base2'):#line:589
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=O0OO000OO0O0OOO00 )#line:590
            if (O000O0OO0000OOOO0 =='PreRelBase')|(O000O0OO0000OOOO0 =='RelBase1'):#line:591
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=O0O0O0O0O0OOO0OOO *1.0 /O0O000OO0O0O000O0 .data ["rows_count"])#line:592
            if (O000O0OO0000OOOO0 =='PostRelBase')|(O000O0OO0000OOOO0 =='RelBase2'):#line:593
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=O0OO000OO0O0OOO00 *1.0 /O0O000OO0O0O000O0 .data ["rows_count"])#line:594
            if (O000O0OO0000OOOO0 =='Prepim')|(O000O0OO0000OOOO0 =='pim1')|(O000O0OO0000OOOO0 =='PreConf')|(O000O0OO0000OOOO0 =='conf1'):#line:595
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=OOOO0O00OO000O00O )#line:596
            if (O000O0OO0000OOOO0 =='Postpim')|(O000O0OO0000OOOO0 =='pim2')|(O000O0OO0000OOOO0 =='PostConf')|(O000O0OO0000OOOO0 =='conf2'):#line:597
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=OOOO0O000OO000O0O )#line:598
            if (O000O0OO0000OOOO0 =='Deltapim')|(O000O0OO0000OOOO0 =='DeltaConf'):#line:599
                OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=OOOO0O00OO000O00O -OOOO0O000OO000O0O )#line:600
            if (O000O0OO0000OOOO0 =='Ratiopim')|(O000O0OO0000OOOO0 =='RatioConf'):#line:603
                if (OOOO0O000OO000O0O >0 ):#line:604
                    OOOO0O00OO0000OO0 =OOOO0O00OO0000OO0 and (O0O000OO0O0O000O0 .quantifiers .get (O000O0OO0000OOOO0 )<=OOOO0O00OO000O00O *1.0 /OOOO0O000OO000O0O )#line:605
                else :#line:606
                    OOOO0O00OO0000OO0 =False #line:607
        OO0O000OO0OO0O0O0 ={}#line:608
        if OOOO0O00OO0000OO0 ==True :#line:609
            O0O000OO0O0O000O0 .stats ['total_valid']+=1 #line:611
            OO0O000OO0OO0O0O0 ["base1"]=O0O0O0O0O0OOO0OOO #line:612
            OO0O000OO0OO0O0O0 ["base2"]=O0OO000OO0O0OOO00 #line:613
            OO0O000OO0OO0O0O0 ["rel_base1"]=O0O0O0O0O0OOO0OOO *1.0 /O0O000OO0O0O000O0 .data ["rows_count"]#line:614
            OO0O000OO0OO0O0O0 ["rel_base2"]=O0OO000OO0O0OOO00 *1.0 /O0O000OO0O0O000O0 .data ["rows_count"]#line:615
            OO0O000OO0OO0O0O0 ["conf1"]=OOOO0O00OO000O00O #line:616
            OO0O000OO0OO0O0O0 ["conf2"]=OOOO0O000OO000O0O #line:617
            OO0O000OO0OO0O0O0 ["deltaconf"]=OOOO0O00OO000O00O -OOOO0O000OO000O0O #line:618
            if (OOOO0O000OO000O0O >0 ):#line:619
                OO0O000OO0OO0O0O0 ["ratioconf"]=OOOO0O00OO000O00O *1.0 /OOOO0O000OO000O0O #line:620
            else :#line:621
                OO0O000OO0OO0O0O0 ["ratioconf"]=None #line:622
            OO0O000OO0OO0O0O0 ["fourfoldpre"]=[OOOO0OO0O000O0O00 ,OO0O0OOOOO0O00OO0 ,O000OOOOOO0OO0O0O ,O0OO00O000O0O00OO ]#line:623
            OO0O000OO0OO0O0O0 ["fourfoldpost"]=[OOOO0O00O0O0O0OOO ,O00OO0O00OOO00O0O ,OOO00O00O00000O0O ,O00O0O00OOOOO0O00 ]#line:624
        return OOOO0O00OO0000OO0 ,OO0O000OO0OO0O0O0 #line:626
    def _verifyact4ft (OO00O00000000OO00 ,_O0OOO0000OOO000OO ):#line:628
        OOO00O0O0OOOOOO00 ={}#line:629
        for O0OOOO0O0OOO0O000 in OO00O00000000OO00 .task_actinfo ['cedents']:#line:630
            OOO00O0O0OOOOOO00 [O0OOOO0O0OOO0O000 ['cedent_type']]=O0OOOO0O0OOO0O000 ['filter_value']#line:632
        O000OOO0O00OO0OOO =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv-']&OOO00O0O0OOOOOO00 ['sucv-'])#line:634
        OO00OOOOOO0OO0000 =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv+']&OOO00O0O0OOOOOO00 ['sucv+'])#line:635
        O0OO00OOOO0OOOO00 =None #line:636
        OOOOOOOOO0OOO0O00 =0 #line:637
        O00O0OOO0OO0OOO00 =0 #line:638
        if O000OOO0O00OO0OOO >0 :#line:647
            OOOOOOOOO0OOO0O00 =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv-']&OOO00O0O0OOOOOO00 ['sucv-'])*1.0 /OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv-'])#line:649
        if OO00OOOOOO0OO0000 >0 :#line:650
            O00O0OOO0OO0OOO00 =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv+']&OOO00O0O0OOOOOO00 ['sucv+'])*1.0 /OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv+'])#line:652
        OO0OOO000000O0OOO =1 <<OO00O00000000OO00 .data ["rows_count"]#line:654
        OOOO00OOO0O0OO0O0 =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv-']&OOO00O0O0OOOOOO00 ['sucv-'])#line:655
        O0O0O00OOO0OO000O =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['antv-']&~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['sucv-']))&OOO00O0O0OOOOOO00 ['cond'])#line:656
        O0OOOOO00OO0OOOO0 =OO00O00000000OO00 ._bitcount (~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['antv-']))&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['sucv-'])#line:657
        OO0OO000OOO0O0000 =OO00O00000000OO00 ._bitcount (~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['antv-']))&~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['sucv-']))&OOO00O0O0OOOOOO00 ['cond'])#line:658
        OO000OO0OOOOO0OOO =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['antv+']&OOO00O0O0OOOOOO00 ['sucv+'])#line:659
        OOO00O00O00OOO0OO =OO00O00000000OO00 ._bitcount (OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['antv+']&~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['sucv+']))&OOO00O0O0OOOOOO00 ['cond'])#line:660
        OO0000000000O00O0 =OO00O00000000OO00 ._bitcount (~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['antv+']))&OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['cond']&OOO00O0O0OOOOOO00 ['sucv+'])#line:661
        O00O0O0OO00OO0OOO =OO00O00000000OO00 ._bitcount (~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['ante']&OOO00O0O0OOOOOO00 ['antv+']))&~(OO0OOO000000O0OOO |(OOO00O0O0OOOOOO00 ['succ']&OOO00O0O0OOOOOO00 ['sucv+']))&OOO00O0O0OOOOOO00 ['cond'])#line:662
        O0O000000O00OOO0O =True #line:663
        for OOO0O0000OOO0OOO0 in OO00O00000000OO00 .quantifiers .keys ():#line:664
            if (OOO0O0000OOO0OOO0 =='PreBase')|(OOO0O0000OOO0OOO0 =='Base1'):#line:665
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=O000OOO0O00OO0OOO )#line:666
            if (OOO0O0000OOO0OOO0 =='PostBase')|(OOO0O0000OOO0OOO0 =='Base2'):#line:667
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=OO00OOOOOO0OO0000 )#line:668
            if (OOO0O0000OOO0OOO0 =='PreRelBase')|(OOO0O0000OOO0OOO0 =='RelBase1'):#line:669
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=O000OOO0O00OO0OOO *1.0 /OO00O00000000OO00 .data ["rows_count"])#line:670
            if (OOO0O0000OOO0OOO0 =='PostRelBase')|(OOO0O0000OOO0OOO0 =='RelBase2'):#line:671
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=OO00OOOOOO0OO0000 *1.0 /OO00O00000000OO00 .data ["rows_count"])#line:672
            if (OOO0O0000OOO0OOO0 =='Prepim')|(OOO0O0000OOO0OOO0 =='pim1')|(OOO0O0000OOO0OOO0 =='PreConf')|(OOO0O0000OOO0OOO0 =='conf1'):#line:673
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=OOOOOOOOO0OOO0O00 )#line:674
            if (OOO0O0000OOO0OOO0 =='Postpim')|(OOO0O0000OOO0OOO0 =='pim2')|(OOO0O0000OOO0OOO0 =='PostConf')|(OOO0O0000OOO0OOO0 =='conf2'):#line:675
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=O00O0OOO0OO0OOO00 )#line:676
            if (OOO0O0000OOO0OOO0 =='Deltapim')|(OOO0O0000OOO0OOO0 =='DeltaConf'):#line:677
                O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=OOOOOOOOO0OOO0O00 -O00O0OOO0OO0OOO00 )#line:678
            if (OOO0O0000OOO0OOO0 =='Ratiopim')|(OOO0O0000OOO0OOO0 =='RatioConf'):#line:681
                if (OOOOOOOOO0OOO0O00 >0 ):#line:682
                    O0O000000O00OOO0O =O0O000000O00OOO0O and (OO00O00000000OO00 .quantifiers .get (OOO0O0000OOO0OOO0 )<=O00O0OOO0OO0OOO00 *1.0 /OOOOOOOOO0OOO0O00 )#line:683
                else :#line:684
                    O0O000000O00OOO0O =False #line:685
        O000O0O0O0O0OO0O0 ={}#line:686
        if O0O000000O00OOO0O ==True :#line:687
            OO00O00000000OO00 .stats ['total_valid']+=1 #line:689
            O000O0O0O0O0OO0O0 ["base1"]=O000OOO0O00OO0OOO #line:690
            O000O0O0O0O0OO0O0 ["base2"]=OO00OOOOOO0OO0000 #line:691
            O000O0O0O0O0OO0O0 ["rel_base1"]=O000OOO0O00OO0OOO *1.0 /OO00O00000000OO00 .data ["rows_count"]#line:692
            O000O0O0O0O0OO0O0 ["rel_base2"]=OO00OOOOOO0OO0000 *1.0 /OO00O00000000OO00 .data ["rows_count"]#line:693
            O000O0O0O0O0OO0O0 ["conf1"]=OOOOOOOOO0OOO0O00 #line:694
            O000O0O0O0O0OO0O0 ["conf2"]=O00O0OOO0OO0OOO00 #line:695
            O000O0O0O0O0OO0O0 ["deltaconf"]=OOOOOOOOO0OOO0O00 -O00O0OOO0OO0OOO00 #line:696
            if (OOOOOOOOO0OOO0O00 >0 ):#line:697
                O000O0O0O0O0OO0O0 ["ratioconf"]=O00O0OOO0OO0OOO00 *1.0 /OOOOOOOOO0OOO0O00 #line:698
            else :#line:699
                O000O0O0O0O0OO0O0 ["ratioconf"]=None #line:700
            O000O0O0O0O0OO0O0 ["fourfoldpre"]=[OOOO00OOO0O0OO0O0 ,O0O0O00OOO0OO000O ,O0OOOOO00OO0OOOO0 ,OO0OO000OOO0O0000 ]#line:701
            O000O0O0O0O0OO0O0 ["fourfoldpost"]=[OO000OO0OOOOO0OOO ,OOO00O00O00OOO0OO ,OO0000000000O00O0 ,O00O0O0OO00OO0OOO ]#line:702
        return O0O000000O00OOO0O ,O000O0O0O0O0OO0O0 #line:704
    def _verify_opt (OOOOO00O00O00OO00 ,OO0OO000O00OOOOOO ,O0OOOOO0OO0000O00 ):#line:706
        OOOOO00O00O00OO00 .stats ['total_ver']+=1 #line:707
        O0000O00OOO0OOO00 =False #line:708
        if not (OO0OO000O00OOOOOO ['optim'].get ('only_con')):#line:711
            return False #line:712
        if not (OOOOO00O00O00OO00 .options ['optimizations']):#line:715
            return False #line:717
        O000O0O0OO000OOO0 ={}#line:719
        for O00O0O0O00O0OOOOO in OOOOO00O00O00OO00 .task_actinfo ['cedents']:#line:720
            O000O0O0OO000OOO0 [O00O0O0O00O0OOOOO ['cedent_type']]=O00O0O0O00O0OOOOO ['filter_value']#line:722
        O0O00O0OOO00O0000 =1 <<OOOOO00O00O00OO00 .data ["rows_count"]#line:724
        O0OO0O0O000O000O0 =O0O00O0OOO00O0000 -1 #line:725
        O0OOO0OO00O0OOOOO =""#line:726
        OOO00OO000OO00OO0 =0 #line:727
        if (O000O0O0OO000OOO0 .get ('ante')!=None ):#line:728
            O0OO0O0O000O000O0 =O0OO0O0O000O000O0 &O000O0O0OO000OOO0 ['ante']#line:729
        if (O000O0O0OO000OOO0 .get ('succ')!=None ):#line:730
            O0OO0O0O000O000O0 =O0OO0O0O000O000O0 &O000O0O0OO000OOO0 ['succ']#line:731
        if (O000O0O0OO000OOO0 .get ('cond')!=None ):#line:732
            O0OO0O0O000O000O0 =O0OO0O0O000O000O0 &O000O0O0OO000OOO0 ['cond']#line:733
        OOO00O0OOOO0000OO =None #line:736
        if (OOOOO00O00O00OO00 .proc =='CFMiner')|(OOOOO00O00O00OO00 .proc =='4ftMiner'):#line:761
            O0O0OOOO0OO0O00OO =OOOOO00O00O00OO00 ._bitcount (O0OO0O0O000O000O0 )#line:762
            if not (OOOOO00O00O00OO00 ._opt_base ==None ):#line:763
                if not (OOOOO00O00O00OO00 ._opt_base <=O0O0OOOO0OO0O00OO ):#line:764
                    O0000O00OOO0OOO00 =True #line:765
            if not (OOOOO00O00O00OO00 ._opt_relbase ==None ):#line:767
                if not (OOOOO00O00O00OO00 ._opt_relbase <=O0O0OOOO0OO0O00OO *1.0 /OOOOO00O00O00OO00 .data ["rows_count"]):#line:768
                    O0000O00OOO0OOO00 =True #line:769
        if (OOOOO00O00O00OO00 .proc =='SD4ftMiner'):#line:771
            O0O0OOOO0OO0O00OO =OOOOO00O00O00OO00 ._bitcount (O0OO0O0O000O000O0 )#line:772
            if (not (OOOOO00O00O00OO00 ._opt_base1 ==None ))&(not (OOOOO00O00O00OO00 ._opt_base2 ==None )):#line:773
                if not (max (OOOOO00O00O00OO00 ._opt_base1 ,OOOOO00O00O00OO00 ._opt_base2 )<=O0O0OOOO0OO0O00OO ):#line:774
                    O0000O00OOO0OOO00 =True #line:776
            if (not (OOOOO00O00O00OO00 ._opt_relbase1 ==None ))&(not (OOOOO00O00O00OO00 ._opt_relbase2 ==None )):#line:777
                if not (max (OOOOO00O00O00OO00 ._opt_relbase1 ,OOOOO00O00O00OO00 ._opt_relbase2 )<=O0O0OOOO0OO0O00OO *1.0 /OOOOO00O00O00OO00 .data ["rows_count"]):#line:778
                    O0000O00OOO0OOO00 =True #line:779
        return O0000O00OOO0OOO00 #line:781
        if OOOOO00O00O00OO00 .proc =='CFMiner':#line:784
            if (O0OOOOO0OO0000O00 ['cedent_type']=='cond')&(O0OOOOO0OO0000O00 ['defi'].get ('type')=='con'):#line:785
                O0O0OOOO0OO0O00OO =bin (O000O0O0OO000OOO0 ['cond']).count ("1")#line:786
                O00O0O0OO0OO000O0 =True #line:787
                for O000OO0000O0O0O00 in OOOOO00O00O00OO00 .quantifiers .keys ():#line:788
                    if O000OO0000O0O0O00 =='Base':#line:789
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O0O0OOOO0OO0O00OO )#line:790
                        if not (O00O0O0OO0OO000O0 ):#line:791
                            print (f"...optimization : base is {O0O0OOOO0OO0O00OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:792
                    if O000OO0000O0O0O00 =='RelBase':#line:793
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O0O0OOOO0OO0O00OO *1.0 /OOOOO00O00O00OO00 .data ["rows_count"])#line:794
                        if not (O00O0O0OO0OO000O0 ):#line:795
                            print (f"...optimization : base is {O0O0OOOO0OO0O00OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:796
                O0000O00OOO0OOO00 =not (O00O0O0OO0OO000O0 )#line:797
        elif OOOOO00O00O00OO00 .proc =='4ftMiner':#line:798
            if (O0OOOOO0OO0000O00 ['cedent_type']=='cond')&(O0OOOOO0OO0000O00 ['defi'].get ('type')=='con'):#line:799
                O0O0OOOO0OO0O00OO =bin (O000O0O0OO000OOO0 ['cond']).count ("1")#line:800
                O00O0O0OO0OO000O0 =True #line:801
                for O000OO0000O0O0O00 in OOOOO00O00O00OO00 .quantifiers .keys ():#line:802
                    if O000OO0000O0O0O00 =='Base':#line:803
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O0O0OOOO0OO0O00OO )#line:804
                        if not (O00O0O0OO0OO000O0 ):#line:805
                            print (f"...optimization : base is {O0O0OOOO0OO0O00OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:806
                    if O000OO0000O0O0O00 =='RelBase':#line:807
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O0O0OOOO0OO0O00OO *1.0 /OOOOO00O00O00OO00 .data ["rows_count"])#line:808
                        if not (O00O0O0OO0OO000O0 ):#line:809
                            print (f"...optimization : base is {O0O0OOOO0OO0O00OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:810
                O0000O00OOO0OOO00 =not (O00O0O0OO0OO000O0 )#line:811
            if (O0OOOOO0OO0000O00 ['cedent_type']=='ante')&(O0OOOOO0OO0000O00 ['defi'].get ('type')=='con'):#line:812
                O0O0OOOO0OO0O00OO =bin (O000O0O0OO000OOO0 ['ante']&O000O0O0OO000OOO0 ['cond']).count ("1")#line:813
                O00O0O0OO0OO000O0 =True #line:814
                for O000OO0000O0O0O00 in OOOOO00O00O00OO00 .quantifiers .keys ():#line:815
                    if O000OO0000O0O0O00 =='Base':#line:816
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O0O0OOOO0OO0O00OO )#line:817
                        if not (O00O0O0OO0OO000O0 ):#line:818
                            print (f"...optimization : ANTE: base is {O0O0OOOO0OO0O00OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:819
                    if O000OO0000O0O0O00 =='RelBase':#line:820
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O0O0OOOO0OO0O00OO *1.0 /OOOOO00O00O00OO00 .data ["rows_count"])#line:821
                        if not (O00O0O0OO0OO000O0 ):#line:822
                            print (f"...optimization : ANTE:  base is {O0O0OOOO0OO0O00OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:823
                O0000O00OOO0OOO00 =not (O00O0O0OO0OO000O0 )#line:824
            if (O0OOOOO0OO0000O00 ['cedent_type']=='succ')&(O0OOOOO0OO0000O00 ['defi'].get ('type')=='con'):#line:825
                O0O0OOOO0OO0O00OO =bin (O000O0O0OO000OOO0 ['ante']&O000O0O0OO000OOO0 ['cond']&O000O0O0OO000OOO0 ['succ']).count ("1")#line:826
                OOO00O0OOOO0000OO =0 #line:827
                if O0O0OOOO0OO0O00OO >0 :#line:828
                    OOO00O0OOOO0000OO =bin (O000O0O0OO000OOO0 ['ante']&O000O0O0OO000OOO0 ['succ']&O000O0O0OO000OOO0 ['cond']).count ("1")*1.0 /bin (O000O0O0OO000OOO0 ['ante']&O000O0O0OO000OOO0 ['cond']).count ("1")#line:829
                O0O00O0OOO00O0000 =1 <<OOOOO00O00O00OO00 .data ["rows_count"]#line:830
                O000O0OOOO0OOOO00 =bin (O000O0O0OO000OOO0 ['ante']&O000O0O0OO000OOO0 ['succ']&O000O0O0OO000OOO0 ['cond']).count ("1")#line:831
                OOOOO0000000OOOO0 =bin (O000O0O0OO000OOO0 ['ante']&~(O0O00O0OOO00O0000 |O000O0O0OO000OOO0 ['succ'])&O000O0O0OO000OOO0 ['cond']).count ("1")#line:832
                O00O0O0O00O0OOOOO =bin (~(O0O00O0OOO00O0000 |O000O0O0OO000OOO0 ['ante'])&O000O0O0OO000OOO0 ['succ']&O000O0O0OO000OOO0 ['cond']).count ("1")#line:833
                OOO0O0000OOO000O0 =bin (~(O0O00O0OOO00O0000 |O000O0O0OO000OOO0 ['ante'])&~(O0O00O0OOO00O0000 |O000O0O0OO000OOO0 ['succ'])&O000O0O0OO000OOO0 ['cond']).count ("1")#line:834
                O00O0O0OO0OO000O0 =True #line:835
                for O000OO0000O0O0O00 in OOOOO00O00O00OO00 .quantifiers .keys ():#line:836
                    if O000OO0000O0O0O00 =='pim':#line:837
                        O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=OOO00O0OOOO0000OO )#line:838
                    if not (O00O0O0OO0OO000O0 ):#line:839
                        print (f"...optimization : SUCC:  pim is {OOO00O0OOOO0000OO} for {O0OOOOO0OO0000O00['generated_string']}")#line:840
                    if O000OO0000O0O0O00 =='aad':#line:842
                        if (O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 )*(O000O0OOOO0OOOO00 +O00O0O0O00O0OOOOO )>0 :#line:843
                            O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=O000O0OOOO0OOOO00 *(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 +O00O0O0O00O0OOOOO +OOO0O0000OOO000O0 )/(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 )/(O000O0OOOO0OOOO00 +O00O0O0O00O0OOOOO )-1 )#line:844
                        else :#line:845
                            O00O0O0OO0OO000O0 =False #line:846
                        if not (O00O0O0OO0OO000O0 ):#line:847
                            O0O000OOO0OO000O0 =O000O0OOOO0OOOO00 *(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 +O00O0O0O00O0OOOOO +OOO0O0000OOO000O0 )/(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 )/(O000O0OOOO0OOOO00 +O00O0O0O00O0OOOOO )-1 #line:848
                            print (f"...optimization : SUCC:  aad is {O0O000OOO0OO000O0} for {O0OOOOO0OO0000O00['generated_string']}")#line:849
                    if O000OO0000O0O0O00 =='bad':#line:850
                        if (O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 )*(O000O0OOOO0OOOO00 +O00O0O0O00O0OOOOO )>0 :#line:851
                            O00O0O0OO0OO000O0 =O00O0O0OO0OO000O0 and (OOOOO00O00O00OO00 .quantifiers .get (O000OO0000O0O0O00 )<=1 -O000O0OOOO0OOOO00 *(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 +O00O0O0O00O0OOOOO +OOO0O0000OOO000O0 )/(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 )/(O000O0OOOO0OOOO00 +O00O0O0O00O0OOOOO ))#line:852
                        else :#line:853
                            O00O0O0OO0OO000O0 =False #line:854
                        if not (O00O0O0OO0OO000O0 ):#line:855
                            OO00OO0O00OO00OOO =1 -O000O0OOOO0OOOO00 *(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 +O00O0O0O00O0OOOOO +OOO0O0000OOO000O0 )/(O000O0OOOO0OOOO00 +OOOOO0000000OOOO0 )/(O000O0OOOO0OOOO00 +O00O0O0O00O0OOOOO )#line:856
                            print (f"...optimization : SUCC:  bad is {OO00OO0O00OO00OOO} for {O0OOOOO0OO0000O00['generated_string']}")#line:857
                O0000O00OOO0OOO00 =not (O00O0O0OO0OO000O0 )#line:858
        if (O0000O00OOO0OOO00 ):#line:859
            print (f"... OPTIMALIZATION - SKIPPING BRANCH at cedent {O0OOOOO0OO0000O00['cedent_type']}")#line:860
        return O0000O00OOO0OOO00 #line:861
    def _print (OO00OOOOOOOO0OOO0 ,OOOO0OOO00OO0000O ,_OO0OOOO0000O0OOOO ,_OOOO0O0O0OO0O0O0O ):#line:864
        if (len (_OO0OOOO0000O0OOOO ))!=len (_OOOO0O0O0OO0O0O0O ):#line:865
            print ("DIFF IN LEN for following cedent : "+str (len (_OO0OOOO0000O0OOOO ))+" vs "+str (len (_OOOO0O0O0OO0O0O0O )))#line:866
            print ("trace cedent : "+str (_OO0OOOO0000O0OOOO )+", traces "+str (_OOOO0O0O0OO0O0O0O ))#line:867
        O0OO00OO000O0000O =''#line:868
        O0OO000000O00OOOO ={}#line:869
        OOOO00O000O0O000O =[]#line:870
        for OOO000OO0O0O0000O in range (len (_OO0OOOO0000O0OOOO )):#line:871
            OOO00O00OOOOO0O00 =OO00OOOOOOOO0OOO0 .data ["varname"].index (OOOO0OOO00OO0000O ['defi'].get ('attributes')[_OO0OOOO0000O0OOOO [OOO000OO0O0O0000O ]].get ('name'))#line:872
            O0OO00OO000O0000O =O0OO00OO000O0000O +OO00OOOOOOOO0OOO0 .data ["varname"][OOO00O00OOOOO0O00 ]+'('#line:874
            OOOO00O000O0O000O .append (OOO00O00OOOOO0O00 )#line:875
            OO00OOOO0OOO0O00O =[]#line:876
            for OO000O0O00000O000 in _OOOO0O0O0OO0O0O0O [OOO000OO0O0O0000O ]:#line:877
                O0OO00OO000O0000O =O0OO00OO000O0000O +str (OO00OOOOOOOO0OOO0 .data ["catnames"][OOO00O00OOOOO0O00 ][OO000O0O00000O000 ])+" "#line:878
                OO00OOOO0OOO0O00O .append (str (OO00OOOOOOOO0OOO0 .data ["catnames"][OOO00O00OOOOO0O00 ][OO000O0O00000O000 ]))#line:879
            O0OO00OO000O0000O =O0OO00OO000O0000O [:-1 ]+')'#line:880
            O0OO000000O00OOOO [OO00OOOOOOOO0OOO0 .data ["varname"][OOO00O00OOOOO0O00 ]]=OO00OOOO0OOO0O00O #line:881
            if OOO000OO0O0O0000O +1 <len (_OO0OOOO0000O0OOOO ):#line:882
                O0OO00OO000O0000O =O0OO00OO000O0000O +' & '#line:883
        return O0OO00OO000O0000O ,O0OO000000O00OOOO ,OOOO00O000O0O000O #line:887
    def _print_hypo (OOO00OO00000OO000 ,OOOOO0O0O000O0OO0 ):#line:889
        OOO00OO00000OO000 .print_rule (OOOOO0O0O000O0OO0 )#line:890
    def _print_rule (O0OO00OOOO000O000 ,OOOO0O00OO0OOO00O ):#line:892
        if O0OO00OOOO000O000 .verbosity ['print_rules']:#line:893
            print ('Rules info : '+str (OOOO0O00OO0OOO00O ['params']))#line:894
            for O0O0OOO0O0OOOOOOO in O0OO00OOOO000O000 .task_actinfo ['cedents']:#line:895
                print (O0O0OOO0O0OOOOOOO ['cedent_type']+' = '+O0O0OOO0O0OOOOOOO ['generated_string'])#line:896
    def _genvar (O00000O00OO0OOO00 ,OOOO0O00O00O0OOOO ,O00000O00OO0OOOOO ,_OOOO0OOO0000OO00O ,_OO000O00OOO0000OO ,_O0OOOOO0O0OOOO000 ,_OO0000OOO0OOOOO0O ,_O0O000OO0OOOO00OO ):#line:898
        for O000OOO0O0OO0O000 in range (O00000O00OO0OOOOO ['num_cedent']):#line:899
            if len (_OOOO0OOO0000OO00O )==0 or O000OOO0O0OO0O000 >_OOOO0OOO0000OO00O [-1 ]:#line:900
                _OOOO0OOO0000OO00O .append (O000OOO0O0OO0O000 )#line:901
                O0OOO0O0OOOOO0O0O =O00000O00OO0OOO00 .data ["varname"].index (O00000O00OO0OOOOO ['defi'].get ('attributes')[O000OOO0O0OO0O000 ].get ('name'))#line:902
                _O0O00OO0000OOOO0O =O00000O00OO0OOOOO ['defi'].get ('attributes')[O000OOO0O0OO0O000 ].get ('minlen')#line:903
                _O000OO0O0O000OO0O =O00000O00OO0OOOOO ['defi'].get ('attributes')[O000OOO0O0OO0O000 ].get ('maxlen')#line:904
                _O00000O00OO000O00 =O00000O00OO0OOOOO ['defi'].get ('attributes')[O000OOO0O0OO0O000 ].get ('type')#line:905
                OO0O000O00OO00OO0 =len (O00000O00OO0OOO00 .data ["dm"][O0OOO0O0OOOOO0O0O ])#line:906
                _OO0OOO00O00OOO0O0 =[]#line:907
                _OO000O00OOO0000OO .append (_OO0OOO00O00OOO0O0 )#line:908
                _OO000OO00O0OO00OO =int (0 )#line:909
                O00000O00OO0OOO00 ._gencomb (OOOO0O00O00O0OOOO ,O00000O00OO0OOOOO ,_OOOO0OOO0000OO00O ,_OO000O00OOO0000OO ,_OO0OOO00O00OOO0O0 ,_O0OOOOO0O0OOOO000 ,_OO000OO00O0OO00OO ,OO0O000O00OO00OO0 ,_O00000O00OO000O00 ,_OO0000OOO0OOOOO0O ,_O0O000OO0OOOO00OO ,_O0O00OO0000OOOO0O ,_O000OO0O0O000OO0O )#line:910
                _OO000O00OOO0000OO .pop ()#line:911
                _OOOO0OOO0000OO00O .pop ()#line:912
    def _gencomb (OOO0OO0000O00OOOO ,OO0OOOOO00O00OO00 ,OOOO0OOOOOOOOO0OO ,_OOO0OO0OOO00O00O0 ,_O0O000OO00OOO0OO0 ,_O0O000O0000OOO0O0 ,_O0OOO00O0OOO00OO0 ,_OO0OOOO0O00OO0000 ,OO00OO0O000O0O000 ,_OOO0OOO00O0OOO0O0 ,_O000O00O0O00OOOO0 ,_OOO0O0O00OOOO0O0O ,_OO0OO0O0OOO0O0OOO ,_O0OOOOOO0OO0O00OO ):#line:914
        _OOOOOOOO00000OO00 =[]#line:915
        if _OOO0OOO00O0OOO0O0 =="subset":#line:916
            if len (_O0O000O0000OOO0O0 )==0 :#line:917
                _OOOOOOOO00000OO00 =range (OO00OO0O000O0O000 )#line:918
            else :#line:919
                _OOOOOOOO00000OO00 =range (_O0O000O0000OOO0O0 [-1 ]+1 ,OO00OO0O000O0O000 )#line:920
        elif _OOO0OOO00O0OOO0O0 =="seq":#line:921
            if len (_O0O000O0000OOO0O0 )==0 :#line:922
                _OOOOOOOO00000OO00 =range (OO00OO0O000O0O000 -_OO0OO0O0OOO0O0OOO +1 )#line:923
            else :#line:924
                if _O0O000O0000OOO0O0 [-1 ]+1 ==OO00OO0O000O0O000 :#line:925
                    return #line:926
                O0OO0O0O00O0OO0O0 =_O0O000O0000OOO0O0 [-1 ]+1 #line:927
                _OOOOOOOO00000OO00 .append (O0OO0O0O00O0OO0O0 )#line:928
        elif _OOO0OOO00O0OOO0O0 =="lcut":#line:929
            if len (_O0O000O0000OOO0O0 )==0 :#line:930
                O0OO0O0O00O0OO0O0 =0 ;#line:931
            else :#line:932
                if _O0O000O0000OOO0O0 [-1 ]+1 ==OO00OO0O000O0O000 :#line:933
                    return #line:934
                O0OO0O0O00O0OO0O0 =_O0O000O0000OOO0O0 [-1 ]+1 #line:935
            _OOOOOOOO00000OO00 .append (O0OO0O0O00O0OO0O0 )#line:936
        elif _OOO0OOO00O0OOO0O0 =="rcut":#line:937
            if len (_O0O000O0000OOO0O0 )==0 :#line:938
                O0OO0O0O00O0OO0O0 =OO00OO0O000O0O000 -1 ;#line:939
            else :#line:940
                if _O0O000O0000OOO0O0 [-1 ]==0 :#line:941
                    return #line:942
                O0OO0O0O00O0OO0O0 =_O0O000O0000OOO0O0 [-1 ]-1 #line:943
            _OOOOOOOO00000OO00 .append (O0OO0O0O00O0OO0O0 )#line:945
        elif _OOO0OOO00O0OOO0O0 =="one":#line:946
            if len (_O0O000O0000OOO0O0 )==0 :#line:947
                OOO0O00O00OOO00O0 =OOO0OO0000O00OOOO .data ["varname"].index (OOOO0OOOOOOOOO0OO ['defi'].get ('attributes')[_OOO0OO0OOO00O00O0 [-1 ]].get ('name'))#line:948
                try :#line:949
                    O0OO0O0O00O0OO0O0 =OOO0OO0000O00OOOO .data ["catnames"][OOO0O00O00OOO00O0 ].index (OOOO0OOOOOOOOO0OO ['defi'].get ('attributes')[_OOO0OO0OOO00O00O0 [-1 ]].get ('value'))#line:950
                except :#line:951
                    print (f"ERROR: attribute '{OOOO0OOOOOOOOO0OO['defi'].get('attributes')[_OOO0OO0OOO00O00O0[-1]].get('name')}' has not value '{OOOO0OOOOOOOOO0OO['defi'].get('attributes')[_OOO0OO0OOO00O00O0[-1]].get('value')}'")#line:952
                    exit (1 )#line:953
                _OOOOOOOO00000OO00 .append (O0OO0O0O00O0OO0O0 )#line:954
                _OO0OO0O0OOO0O0OOO =1 #line:955
                _O0OOOOOO0OO0O00OO =1 #line:956
            else :#line:957
                print ("DEBUG: one category should not have more categories")#line:958
                return #line:959
        else :#line:960
            print ("Attribute type "+_OOO0OOO00O0OOO0O0 +" not supported.")#line:961
            return #line:962
        for OOOO0OO0O0O00000O in _OOOOOOOO00000OO00 :#line:965
                _O0O000O0000OOO0O0 .append (OOOO0OO0O0O00000O )#line:967
                _O0O000OO00OOO0OO0 .pop ()#line:968
                _O0O000OO00OOO0OO0 .append (_O0O000O0000OOO0O0 )#line:969
                _OO0OO0000O0OOOOO0 =_OO0OOOO0O00OO0000 |OOO0OO0000O00OOOO .data ["dm"][OOO0OO0000O00OOOO .data ["varname"].index (OOOO0OOOOOOOOO0OO ['defi'].get ('attributes')[_OOO0OO0OOO00O00O0 [-1 ]].get ('name'))][OOOO0OO0O0O00000O ]#line:973
                _O000OOOO00O000OO0 =1 #line:975
                if (len (_OOO0OO0OOO00O00O0 )<_O000O00O0O00OOOO0 ):#line:976
                    _O000OOOO00O000OO0 =-1 #line:977
                if (len (_O0O000OO00OOO0OO0 [-1 ])<_OO0OO0O0OOO0O0OOO ):#line:979
                    _O000OOOO00O000OO0 =0 #line:980
                _OO0O0O000O00OO00O =0 #line:982
                if OOOO0OOOOOOOOO0OO ['defi'].get ('type')=='con':#line:983
                    _OO0O0O000O00OO00O =_O0OOO00O0OOO00OO0 &_OO0OO0000O0OOOOO0 #line:984
                else :#line:985
                    _OO0O0O000O00OO00O =_O0OOO00O0OOO00OO0 |_OO0OO0000O0OOOOO0 #line:986
                OOOO0OOOOOOOOO0OO ['trace_cedent']=_OOO0OO0OOO00O00O0 #line:987
                OOOO0OOOOOOOOO0OO ['traces']=_O0O000OO00OOO0OO0 #line:988
                O0OOO00OOO0000O0O ,OO00000O0OO00O00O ,OO00000O0O00000OO =OOO0OO0000O00OOOO ._print (OOOO0OOOOOOOOO0OO ,_OOO0OO0OOO00O00O0 ,_O0O000OO00OOO0OO0 )#line:989
                OOOO0OOOOOOOOO0OO ['generated_string']=O0OOO00OOO0000O0O #line:990
                OOOO0OOOOOOOOO0OO ['rule']=OO00000O0OO00O00O #line:991
                OOOO0OOOOOOOOO0OO ['filter_value']=_OO0O0O000O00OO00O #line:992
                OOOO0OOOOOOOOO0OO ['traces']=copy .deepcopy (_O0O000OO00OOO0OO0 )#line:993
                OOOO0OOOOOOOOO0OO ['trace_cedent']=copy .deepcopy (_OOO0OO0OOO00O00O0 )#line:994
                OOOO0OOOOOOOOO0OO ['trace_cedent_asindata']=copy .deepcopy (OO00000O0O00000OO )#line:995
                OO0OOOOO00O00OO00 ['cedents'].append (OOOO0OOOOOOOOO0OO )#line:997
                OO0O00OO00OOO000O =OOO0OO0000O00OOOO ._verify_opt (OO0OOOOO00O00OO00 ,OOOO0OOOOOOOOO0OO )#line:998
                if not (OO0O00OO00OOO000O ):#line:1004
                    if _O000OOOO00O000OO0 ==1 :#line:1005
                        if len (OO0OOOOO00O00OO00 ['cedents_to_do'])==len (OO0OOOOO00O00OO00 ['cedents']):#line:1007
                            if OOO0OO0000O00OOOO .proc =='CFMiner':#line:1008
                                O00O00OOO0O00OO0O ,O000OOO0OOOOO0O00 =OOO0OO0000O00OOOO ._verifyCF (_OO0O0O000O00OO00O )#line:1009
                            elif OOO0OO0000O00OOOO .proc =='4ftMiner':#line:1010
                                O00O00OOO0O00OO0O ,O000OOO0OOOOO0O00 =OOO0OO0000O00OOOO ._verify4ft (_OO0OO0000O0OOOOO0 )#line:1011
                            elif OOO0OO0000O00OOOO .proc =='SD4ftMiner':#line:1012
                                O00O00OOO0O00OO0O ,O000OOO0OOOOO0O00 =OOO0OO0000O00OOOO ._verifysd4ft (_OO0OO0000O0OOOOO0 )#line:1013
                            elif OOO0OO0000O00OOOO .proc =='NewAct4ftMiner':#line:1014
                                O00O00OOO0O00OO0O ,O000OOO0OOOOO0O00 =OOO0OO0000O00OOOO ._verifynewact4ft (_OO0OO0000O0OOOOO0 )#line:1015
                            elif OOO0OO0000O00OOOO .proc =='Act4ftMiner':#line:1016
                                O00O00OOO0O00OO0O ,O000OOO0OOOOO0O00 =OOO0OO0000O00OOOO ._verifyact4ft (_OO0OO0000O0OOOOO0 )#line:1017
                            else :#line:1018
                                print ("Unsupported procedure : "+OOO0OO0000O00OOOO .proc )#line:1019
                                exit (0 )#line:1020
                            if O00O00OOO0O00OO0O ==True :#line:1021
                                OO0OO0O0O0OO0O000 ={}#line:1022
                                OO0OO0O0O0OO0O000 ["rule_id"]=OOO0OO0000O00OOOO .stats ['total_valid']#line:1023
                                OO0OO0O0O0OO0O000 ["cedents_str"]={}#line:1024
                                OO0OO0O0O0OO0O000 ["cedents_struct"]={}#line:1025
                                OO0OO0O0O0OO0O000 ['traces']={}#line:1026
                                OO0OO0O0O0OO0O000 ['trace_cedent_taskorder']={}#line:1027
                                OO0OO0O0O0OO0O000 ['trace_cedent_dataorder']={}#line:1028
                                for OOOO00OOO0OO00O0O in OO0OOOOO00O00OO00 ['cedents']:#line:1029
                                    OO0OO0O0O0OO0O000 ['cedents_str'][OOOO00OOO0OO00O0O ['cedent_type']]=OOOO00OOO0OO00O0O ['generated_string']#line:1031
                                    OO0OO0O0O0OO0O000 ['cedents_struct'][OOOO00OOO0OO00O0O ['cedent_type']]=OOOO00OOO0OO00O0O ['rule']#line:1032
                                    OO0OO0O0O0OO0O000 ['traces'][OOOO00OOO0OO00O0O ['cedent_type']]=OOOO00OOO0OO00O0O ['traces']#line:1033
                                    OO0OO0O0O0OO0O000 ['trace_cedent_taskorder'][OOOO00OOO0OO00O0O ['cedent_type']]=OOOO00OOO0OO00O0O ['trace_cedent']#line:1034
                                    OO0OO0O0O0OO0O000 ['trace_cedent_dataorder'][OOOO00OOO0OO00O0O ['cedent_type']]=OOOO00OOO0OO00O0O ['trace_cedent_asindata']#line:1035
                                OO0OO0O0O0OO0O000 ["params"]=O000OOO0OOOOO0O00 #line:1037
                                OOO0OO0000O00OOOO ._print_rule (OO0OO0O0O0OO0O000 )#line:1039
                                OOO0OO0000O00OOOO .rulelist .append (OO0OO0O0O0OO0O000 )#line:1045
                            OOO0OO0000O00OOOO .stats ['total_cnt']+=1 #line:1047
                            OOO0OO0000O00OOOO .stats ['total_ver']+=1 #line:1048
                    if _O000OOOO00O000OO0 >=0 :#line:1049
                        if len (OO0OOOOO00O00OO00 ['cedents_to_do'])>len (OO0OOOOO00O00OO00 ['cedents']):#line:1050
                            OOO0OO0000O00OOOO ._start_cedent (OO0OOOOO00O00OO00 )#line:1051
                    OO0OOOOO00O00OO00 ['cedents'].pop ()#line:1052
                    if (len (_OOO0OO0OOO00O00O0 )<_OOO0O0O00OOOO0O0O ):#line:1053
                        OOO0OO0000O00OOOO ._genvar (OO0OOOOO00O00OO00 ,OOOO0OOOOOOOOO0OO ,_OOO0OO0OOO00O00O0 ,_O0O000OO00OOO0OO0 ,_OO0O0O000O00OO00O ,_O000O00O0O00OOOO0 ,_OOO0O0O00OOOO0O0O )#line:1054
                else :#line:1055
                    OO0OOOOO00O00OO00 ['cedents'].pop ()#line:1056
                if len (_O0O000O0000OOO0O0 )<_O0OOOOOO0OO0O00OO :#line:1057
                    OOO0OO0000O00OOOO ._gencomb (OO0OOOOO00O00OO00 ,OOOO0OOOOOOOOO0OO ,_OOO0OO0OOO00O00O0 ,_O0O000OO00OOO0OO0 ,_O0O000O0000OOO0O0 ,_O0OOO00O0OOO00OO0 ,_OO0OO0000O0OOOOO0 ,OO00OO0O000O0O000 ,_OOO0OOO00O0OOO0O0 ,_O000O00O0O00OOOO0 ,_OOO0O0O00OOOO0O0O ,_OO0OO0O0OOO0O0OOO ,_O0OOOOOO0OO0O00OO )#line:1058
                _O0O000O0000OOO0O0 .pop ()#line:1059
    def _start_cedent (O0OO0O0O0O0OOOOO0 ,O000O0O00O00OO0O0 ):#line:1061
        if len (O000O0O00O00OO0O0 ['cedents_to_do'])>len (O000O0O00O00OO0O0 ['cedents']):#line:1062
            _O00O0OO0O0OOO000O =[]#line:1063
            _OO00OO0OOO0O0OOOO =[]#line:1064
            OO0OOO00O0O0OOO00 ={}#line:1065
            OO0OOO00O0O0OOO00 ['cedent_type']=O000O0O00O00OO0O0 ['cedents_to_do'][len (O000O0O00O00OO0O0 ['cedents'])]#line:1066
            O0000O0OOO0000O00 =OO0OOO00O0O0OOO00 ['cedent_type']#line:1067
            if ((O0000O0OOO0000O00 [-1 ]=='-')|(O0000O0OOO0000O00 [-1 ]=='+')):#line:1068
                O0000O0OOO0000O00 =O0000O0OOO0000O00 [:-1 ]#line:1069
            OO0OOO00O0O0OOO00 ['defi']=O0OO0O0O0O0OOOOO0 .kwargs .get (O0000O0OOO0000O00 )#line:1071
            if (OO0OOO00O0O0OOO00 ['defi']==None ):#line:1072
                print ("Error getting cedent ",OO0OOO00O0O0OOO00 ['cedent_type'])#line:1073
            _OOOO0OO00OOOO0OO0 =int (0 )#line:1074
            OO0OOO00O0O0OOO00 ['num_cedent']=len (OO0OOO00O0O0OOO00 ['defi'].get ('attributes'))#line:1079
            if (OO0OOO00O0O0OOO00 ['defi'].get ('type')=='con'):#line:1080
                _OOOO0OO00OOOO0OO0 =(1 <<O0OO0O0O0O0OOOOO0 .data ["rows_count"])-1 #line:1081
            O0OO0O0O0O0OOOOO0 ._genvar (O000O0O00O00OO0O0 ,OO0OOO00O0O0OOO00 ,_O00O0OO0O0OOO000O ,_OO00OO0OOO0O0OOOO ,_OOOO0OO00OOOO0OO0 ,OO0OOO00O0O0OOO00 ['defi'].get ('minlen'),OO0OOO00O0O0OOO00 ['defi'].get ('maxlen'))#line:1082
    def _calc_all (O00OOOO0000O0O000 ,**O0OO00OOO0OO00O00 ):#line:1085
        if "df"in O0OO00OOO0OO00O00 :#line:1086
            O00OOOO0000O0O000 ._prep_data (O00OOOO0000O0O000 .kwargs .get ("df"))#line:1087
        if not (O00OOOO0000O0O000 ._initialized ):#line:1088
            print ("ERROR: dataframe is missing and not initialized with dataframe")#line:1089
        else :#line:1090
            O00OOOO0000O0O000 ._calculate (**O0OO00OOO0OO00O00 )#line:1091
    def _check_cedents (OO0O0000OOO0O0OO0 ,O000O0000000OO000 ,**OO000O000000OOO0O ):#line:1093
        O00OOOO0OO00OOO0O =True #line:1094
        if (OO000O000000OOO0O .get ('quantifiers',None )==None ):#line:1095
            print (f"Error: missing quantifiers.")#line:1096
            O00OOOO0OO00OOO0O =False #line:1097
            return O00OOOO0OO00OOO0O #line:1098
        if (type (OO000O000000OOO0O .get ('quantifiers'))!=dict ):#line:1099
            print (f"Error: quantifiers are not dictionary type.")#line:1100
            O00OOOO0OO00OOO0O =False #line:1101
            return O00OOOO0OO00OOO0O #line:1102
        for OOO00O00OOOOOOO0O in O000O0000000OO000 :#line:1104
            if (OO000O000000OOO0O .get (OOO00O00OOOOOOO0O ,None )==None ):#line:1105
                print (f"Error: cedent {OOO00O00OOOOOOO0O} is missing in parameters.")#line:1106
                O00OOOO0OO00OOO0O =False #line:1107
                return O00OOOO0OO00OOO0O #line:1108
            OOO0O00000O0O0OOO =OO000O000000OOO0O .get (OOO00O00OOOOOOO0O )#line:1109
            if (OOO0O00000O0O0OOO .get ('minlen'),None )==None :#line:1110
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has no minimal length specified.")#line:1111
                O00OOOO0OO00OOO0O =False #line:1112
                return O00OOOO0OO00OOO0O #line:1113
            if not (type (OOO0O00000O0O0OOO .get ('minlen'))is int ):#line:1114
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has invalid type of minimal length ({type(OOO0O00000O0O0OOO.get('minlen'))}).")#line:1115
                O00OOOO0OO00OOO0O =False #line:1116
                return O00OOOO0OO00OOO0O #line:1117
            if (OOO0O00000O0O0OOO .get ('maxlen'),None )==None :#line:1118
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has no maximal length specified.")#line:1119
                O00OOOO0OO00OOO0O =False #line:1120
                return O00OOOO0OO00OOO0O #line:1121
            if not (type (OOO0O00000O0O0OOO .get ('maxlen'))is int ):#line:1122
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has invalid type of maximal length.")#line:1123
                O00OOOO0OO00OOO0O =False #line:1124
                return O00OOOO0OO00OOO0O #line:1125
            if (OOO0O00000O0O0OOO .get ('type'),None )==None :#line:1126
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has no type specified.")#line:1127
                O00OOOO0OO00OOO0O =False #line:1128
                return O00OOOO0OO00OOO0O #line:1129
            if not ((OOO0O00000O0O0OOO .get ('type'))in (['con','dis'])):#line:1130
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has invalid type. Allowed values are 'con' and 'dis'.")#line:1131
                O00OOOO0OO00OOO0O =False #line:1132
                return O00OOOO0OO00OOO0O #line:1133
            if (OOO0O00000O0O0OOO .get ('attributes'),None )==None :#line:1134
                print (f"Error: cedent {OOO00O00OOOOOOO0O} has no attributes specified.")#line:1135
                O00OOOO0OO00OOO0O =False #line:1136
                return O00OOOO0OO00OOO0O #line:1137
            for O0O00OOOO0O00O0OO in OOO0O00000O0O0OOO .get ('attributes'):#line:1138
                if (O0O00OOOO0O00O0OO .get ('name'),None )==None :#line:1139
                    print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO} has no 'name' attribute specified.")#line:1140
                    O00OOOO0OO00OOO0O =False #line:1141
                    return O00OOOO0OO00OOO0O #line:1142
                if not ((O0O00OOOO0O00O0OO .get ('name'))in OO0O0000OOO0O0OO0 .data ["varname"]):#line:1143
                    print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} not in variable list. Please check spelling.")#line:1144
                    O00OOOO0OO00OOO0O =False #line:1145
                    return O00OOOO0OO00OOO0O #line:1146
                if (O0O00OOOO0O00O0OO .get ('type'),None )==None :#line:1147
                    print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} has no 'type' attribute specified.")#line:1148
                    O00OOOO0OO00OOO0O =False #line:1149
                    return O00OOOO0OO00OOO0O #line:1150
                if not ((O0O00OOOO0O00O0OO .get ('type'))in (['rcut','lcut','seq','subset','one'])):#line:1151
                    print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} has unsupported type {O0O00OOOO0O00O0OO.get('type')}. Supported types are 'subset','seq','lcut','rcut','one'.")#line:1152
                    O00OOOO0OO00OOO0O =False #line:1153
                    return O00OOOO0OO00OOO0O #line:1154
                if (O0O00OOOO0O00O0OO .get ('minlen'),None )==None :#line:1155
                    print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} has no minimal length specified.")#line:1156
                    O00OOOO0OO00OOO0O =False #line:1157
                    return O00OOOO0OO00OOO0O #line:1158
                if not (type (O0O00OOOO0O00O0OO .get ('minlen'))is int ):#line:1159
                    if not (O0O00OOOO0O00O0OO .get ('type')=='one'):#line:1160
                        print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} has invalid type of minimal length.")#line:1161
                        O00OOOO0OO00OOO0O =False #line:1162
                        return O00OOOO0OO00OOO0O #line:1163
                if (O0O00OOOO0O00O0OO .get ('maxlen'),None )==None :#line:1164
                    print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} has no maximal length specified.")#line:1165
                    O00OOOO0OO00OOO0O =False #line:1166
                    return O00OOOO0OO00OOO0O #line:1167
                if not (type (O0O00OOOO0O00O0OO .get ('maxlen'))is int ):#line:1168
                    if not (O0O00OOOO0O00O0OO .get ('type')=='one'):#line:1169
                        print (f"Error: cedent {OOO00O00OOOOOOO0O} / attribute {O0O00OOOO0O00O0OO.get('name')} has invalid type of maximal length.")#line:1170
                        O00OOOO0OO00OOO0O =False #line:1171
                        return O00OOOO0OO00OOO0O #line:1172
        return O00OOOO0OO00OOO0O #line:1173
    def _calculate (O0OOOOO000O00O000 ,**OO00O00OOO000OO0O ):#line:1175
        if O0OOOOO000O00O000 .data ["data_prepared"]==0 :#line:1176
            print ("Error: data not prepared")#line:1177
            return #line:1178
        O0OOOOO000O00O000 .kwargs =OO00O00OOO000OO0O #line:1179
        O0OOOOO000O00O000 .proc =OO00O00OOO000OO0O .get ('proc')#line:1180
        O0OOOOO000O00O000 .quantifiers =OO00O00OOO000OO0O .get ('quantifiers')#line:1181
        O0OOOOO000O00O000 ._init_task ()#line:1183
        O0OOOOO000O00O000 .stats ['start_proc_time']=time .time ()#line:1184
        O0OOOOO000O00O000 .task_actinfo ['cedents_to_do']=[]#line:1185
        O0OOOOO000O00O000 .task_actinfo ['cedents']=[]#line:1186
        if OO00O00OOO000OO0O .get ("proc")=='CFMiner':#line:1189
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do']=['cond']#line:1190
            if OO00O00OOO000OO0O .get ('target',None )==None :#line:1191
                print ("ERROR: no target variable defined for CF Miner")#line:1192
                return #line:1193
            if not (O0OOOOO000O00O000 ._check_cedents (['cond'],**OO00O00OOO000OO0O )):#line:1194
                return #line:1195
            if not (OO00O00OOO000OO0O .get ('target')in O0OOOOO000O00O000 .data ["varname"]):#line:1196
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1197
                return #line:1198
        elif OO00O00OOO000OO0O .get ("proc")=='4ftMiner':#line:1200
            if not (O0OOOOO000O00O000 ._check_cedents (['ante','succ'],**OO00O00OOO000OO0O )):#line:1201
                return #line:1202
            _O00OOOO0O0OOO00OO =OO00O00OOO000OO0O .get ("cond")#line:1204
            if _O00OOOO0O0OOO00OO !=None :#line:1205
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1206
            else :#line:1207
                O000O0OOOO0O0000O =O0OOOOO000O00O000 .cedent #line:1208
                O000O0OOOO0O0000O ['cedent_type']='cond'#line:1209
                O000O0OOOO0O0000O ['filter_value']=(1 <<O0OOOOO000O00O000 .data ["rows_count"])-1 #line:1210
                O000O0OOOO0O0000O ['generated_string']='---'#line:1211
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1213
                O0OOOOO000O00O000 .task_actinfo ['cedents'].append (O000O0OOOO0O0000O )#line:1214
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('ante')#line:1218
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('succ')#line:1219
        elif OO00O00OOO000OO0O .get ("proc")=='NewAct4ftMiner':#line:1220
            _O00OOOO0O0OOO00OO =OO00O00OOO000OO0O .get ("cond")#line:1223
            if _O00OOOO0O0OOO00OO !=None :#line:1224
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1225
            else :#line:1226
                O000O0OOOO0O0000O =O0OOOOO000O00O000 .cedent #line:1227
                O000O0OOOO0O0000O ['cedent_type']='cond'#line:1228
                O000O0OOOO0O0000O ['filter_value']=(1 <<O0OOOOO000O00O000 .data ["rows_count"])-1 #line:1229
                O000O0OOOO0O0000O ['generated_string']='---'#line:1230
                print (O000O0OOOO0O0000O ['filter_value'])#line:1231
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1232
                O0OOOOO000O00O000 .task_actinfo ['cedents'].append (O000O0OOOO0O0000O )#line:1233
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('antv')#line:1234
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('sucv')#line:1235
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('ante')#line:1236
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('succ')#line:1237
        elif OO00O00OOO000OO0O .get ("proc")=='Act4ftMiner':#line:1238
            _O00OOOO0O0OOO00OO =OO00O00OOO000OO0O .get ("cond")#line:1241
            if _O00OOOO0O0OOO00OO !=None :#line:1242
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1243
            else :#line:1244
                O000O0OOOO0O0000O =O0OOOOO000O00O000 .cedent #line:1245
                O000O0OOOO0O0000O ['cedent_type']='cond'#line:1246
                O000O0OOOO0O0000O ['filter_value']=(1 <<O0OOOOO000O00O000 .data ["rows_count"])-1 #line:1247
                O000O0OOOO0O0000O ['generated_string']='---'#line:1248
                print (O000O0OOOO0O0000O ['filter_value'])#line:1249
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1250
                O0OOOOO000O00O000 .task_actinfo ['cedents'].append (O000O0OOOO0O0000O )#line:1251
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('antv-')#line:1252
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('antv+')#line:1253
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('sucv-')#line:1254
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('sucv+')#line:1255
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('ante')#line:1256
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('succ')#line:1257
        elif OO00O00OOO000OO0O .get ("proc")=='SD4ftMiner':#line:1258
            if not (O0OOOOO000O00O000 ._check_cedents (['ante','succ','frst','scnd'],**OO00O00OOO000OO0O )):#line:1261
                return #line:1262
            _O00OOOO0O0OOO00OO =OO00O00OOO000OO0O .get ("cond")#line:1263
            if _O00OOOO0O0OOO00OO !=None :#line:1264
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1265
            else :#line:1266
                O000O0OOOO0O0000O =O0OOOOO000O00O000 .cedent #line:1267
                O000O0OOOO0O0000O ['cedent_type']='cond'#line:1268
                O000O0OOOO0O0000O ['filter_value']=(1 <<O0OOOOO000O00O000 .data ["rows_count"])-1 #line:1269
                O000O0OOOO0O0000O ['generated_string']='---'#line:1270
                O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('cond')#line:1272
                O0OOOOO000O00O000 .task_actinfo ['cedents'].append (O000O0OOOO0O0000O )#line:1273
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('frst')#line:1274
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('scnd')#line:1275
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('ante')#line:1276
            O0OOOOO000O00O000 .task_actinfo ['cedents_to_do'].append ('succ')#line:1277
        else :#line:1278
            print ("Unsupported procedure")#line:1279
            return #line:1280
        print ("Will go for ",OO00O00OOO000OO0O .get ("proc"))#line:1281
        O0OOOOO000O00O000 .task_actinfo ['optim']={}#line:1284
        OOO000OO0O000OO0O =True #line:1285
        for O00OOO0000O0O00O0 in O0OOOOO000O00O000 .task_actinfo ['cedents_to_do']:#line:1286
            try :#line:1287
                O00O0O00000000O0O =O0OOOOO000O00O000 .kwargs .get (O00OOO0000O0O00O0 )#line:1288
                if O00O0O00000000O0O .get ('type')!='con':#line:1292
                    OOO000OO0O000OO0O =False #line:1293
            except :#line:1295
                OOOO0OOO0OO0OO000 =1 <2 #line:1296
        if O0OOOOO000O00O000 .options ['optimizations']==False :#line:1298
            OOO000OO0O000OO0O =False #line:1299
        OO00OO0O0000O0000 ={}#line:1300
        OO00OO0O0000O0000 ['only_con']=OOO000OO0O000OO0O #line:1301
        O0OOOOO000O00O000 .task_actinfo ['optim']=OO00OO0O0000O0000 #line:1302
        print ("Starting to mine rules.")#line:1310
        O0OOOOO000O00O000 ._start_cedent (O0OOOOO000O00O000 .task_actinfo )#line:1311
        O0OOOOO000O00O000 .stats ['end_proc_time']=time .time ()#line:1313
        print ("Done. Total verifications : "+str (O0OOOOO000O00O000 .stats ['total_cnt'])+", rules "+str (O0OOOOO000O00O000 .stats ['total_valid'])+",control number:"+str (O0OOOOO000O00O000 .stats ['control_number'])+", times: prep "+str (O0OOOOO000O00O000 .stats ['end_prep_time']-O0OOOOO000O00O000 .stats ['start_prep_time'])+", processing "+str (O0OOOOO000O00O000 .stats ['end_proc_time']-O0OOOOO000O00O000 .stats ['start_proc_time']))#line:1316
        OOO00O0OO00O0O0OO ={}#line:1317
        O0O0O00OO0O0OOO0O ={}#line:1318
        O0O0O00OO0O0OOO0O ["task_type"]=OO00O00OOO000OO0O .get ('proc')#line:1319
        O0O0O00OO0O0OOO0O ["target"]=OO00O00OOO000OO0O .get ('target')#line:1321
        O0O0O00OO0O0OOO0O ["self.quantifiers"]=O0OOOOO000O00O000 .quantifiers #line:1322
        if OO00O00OOO000OO0O .get ('cond')!=None :#line:1324
            O0O0O00OO0O0OOO0O ['cond']=OO00O00OOO000OO0O .get ('cond')#line:1325
        if OO00O00OOO000OO0O .get ('ante')!=None :#line:1326
            O0O0O00OO0O0OOO0O ['ante']=OO00O00OOO000OO0O .get ('ante')#line:1327
        if OO00O00OOO000OO0O .get ('succ')!=None :#line:1328
            O0O0O00OO0O0OOO0O ['succ']=OO00O00OOO000OO0O .get ('succ')#line:1329
        if OO00O00OOO000OO0O .get ('opts')!=None :#line:1330
            O0O0O00OO0O0OOO0O ['opts']=OO00O00OOO000OO0O .get ('opts')#line:1331
        OOO00O0OO00O0O0OO ["taskinfo"]=O0O0O00OO0O0OOO0O #line:1332
        O0OOOO0000O00OO0O ={}#line:1333
        O0OOOO0000O00OO0O ["total_verifications"]=O0OOOOO000O00O000 .stats ['total_cnt']#line:1334
        O0OOOO0000O00OO0O ["valid_rules"]=O0OOOOO000O00O000 .stats ['total_valid']#line:1335
        O0OOOO0000O00OO0O ["total_verifications_with_opt"]=O0OOOOO000O00O000 .stats ['total_ver']#line:1336
        O0OOOO0000O00OO0O ["time_prep"]=O0OOOOO000O00O000 .stats ['end_prep_time']-O0OOOOO000O00O000 .stats ['start_prep_time']#line:1337
        O0OOOO0000O00OO0O ["time_processing"]=O0OOOOO000O00O000 .stats ['end_proc_time']-O0OOOOO000O00O000 .stats ['start_proc_time']#line:1338
        O0OOOO0000O00OO0O ["time_total"]=O0OOOOO000O00O000 .stats ['end_prep_time']-O0OOOOO000O00O000 .stats ['start_prep_time']+O0OOOOO000O00O000 .stats ['end_proc_time']-O0OOOOO000O00O000 .stats ['start_proc_time']#line:1339
        OOO00O0OO00O0O0OO ["summary_statistics"]=O0OOOO0000O00OO0O #line:1340
        OOO00O0OO00O0O0OO ["rules"]=O0OOOOO000O00O000 .rulelist #line:1341
        OO00O0OO00OOO0OO0 ={}#line:1342
        OO00O0OO00OOO0OO0 ["varname"]=O0OOOOO000O00O000 .data ["varname"]#line:1343
        OO00O0OO00OOO0OO0 ["catnames"]=O0OOOOO000O00O000 .data ["catnames"]#line:1344
        OOO00O0OO00O0O0OO ["datalabels"]=OO00O0OO00OOO0OO0 #line:1345
        O0OOOOO000O00O000 .result =OOO00O0OO00O0O0OO #line:1348
    def print_summary (OOOO00O0O0O0OOO0O ):#line:1350
        print ("")#line:1351
        print ("CleverMiner task processing summary:")#line:1352
        print ("")#line:1353
        print (f"Task type : {OOOO00O0O0O0OOO0O.result['taskinfo']['task_type']}")#line:1354
        print (f"Number of verifications : {OOOO00O0O0O0OOO0O.result['summary_statistics']['total_verifications']}")#line:1355
        print (f"Number of rules : {OOOO00O0O0O0OOO0O.result['summary_statistics']['valid_rules']}")#line:1356
        print (f"Total time needed : {strftime('%Hh %Mm %Ss', gmtime(OOOO00O0O0O0OOO0O.result['summary_statistics']['time_total']))}")#line:1357
        print (f"Time of data preparation : {strftime('%Hh %Mm %Ss', gmtime(OOOO00O0O0O0OOO0O.result['summary_statistics']['time_prep']))}")#line:1359
        print (f"Time of rule mining : {strftime('%Hh %Mm %Ss', gmtime(OOOO00O0O0O0OOO0O.result['summary_statistics']['time_processing']))}")#line:1360
        print ("")#line:1361
    def print_hypolist (OOO0O0OOOOO0O0O0O ):#line:1363
        OOO0O0OOOOO0O0O0O .print_rulelist ();#line:1364
    def print_rulelist (O0O0O0O000OOO00O0 ):#line:1366
        print ("")#line:1368
        print ("List of rules:")#line:1369
        if O0O0O0O000OOO00O0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1370
            print ("RULEID BASE  CONF  AAD    Rule")#line:1371
        elif O0O0O0O000OOO00O0 .result ['taskinfo']['task_type']=="CFMiner":#line:1372
            print ("RULEID BASE  S_UP  S_DOWN Condition")#line:1373
        elif O0O0O0O000OOO00O0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1374
            print ("RULEID BASE1 BASE2 RatioConf DeltaConf Rule")#line:1375
        else :#line:1376
            print ("Unsupported task type for rulelist")#line:1377
            return #line:1378
        for O00O00OO000OO0000 in O0O0O0O000OOO00O0 .result ["rules"]:#line:1379
            OOOOO0OO0OO000OO0 ="{:6d}".format (O00O00OO000OO0000 ["rule_id"])#line:1380
            if O0O0O0O000OOO00O0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1381
                OOOOO0OO0OO000OO0 =OOOOO0OO0OO000OO0 +" "+"{:5d}".format (O00O00OO000OO0000 ["params"]["base"])+" "+"{:.3f}".format (O00O00OO000OO0000 ["params"]["conf"])+" "+"{:+.3f}".format (O00O00OO000OO0000 ["params"]["aad"])#line:1382
                OOOOO0OO0OO000OO0 =OOOOO0OO0OO000OO0 +" "+O00O00OO000OO0000 ["cedents_str"]["ante"]+" => "+O00O00OO000OO0000 ["cedents_str"]["succ"]+" | "+O00O00OO000OO0000 ["cedents_str"]["cond"]#line:1383
            elif O0O0O0O000OOO00O0 .result ['taskinfo']['task_type']=="CFMiner":#line:1384
                OOOOO0OO0OO000OO0 =OOOOO0OO0OO000OO0 +" "+"{:5d}".format (O00O00OO000OO0000 ["params"]["base"])+" "+"{:5d}".format (O00O00OO000OO0000 ["params"]["s_up"])+" "+"{:5d}".format (O00O00OO000OO0000 ["params"]["s_down"])#line:1385
                OOOOO0OO0OO000OO0 =OOOOO0OO0OO000OO0 +" "+O00O00OO000OO0000 ["cedents_str"]["cond"]#line:1386
            elif O0O0O0O000OOO00O0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1387
                OOOOO0OO0OO000OO0 =OOOOO0OO0OO000OO0 +" "+"{:5d}".format (O00O00OO000OO0000 ["params"]["base1"])+" "+"{:5d}".format (O00O00OO000OO0000 ["params"]["base2"])+"    "+"{:.3f}".format (O00O00OO000OO0000 ["params"]["ratioconf"])+"    "+"{:+.3f}".format (O00O00OO000OO0000 ["params"]["deltaconf"])#line:1388
                OOOOO0OO0OO000OO0 =OOOOO0OO0OO000OO0 +"  "+O00O00OO000OO0000 ["cedents_str"]["ante"]+" => "+O00O00OO000OO0000 ["cedents_str"]["succ"]+" | "+O00O00OO000OO0000 ["cedents_str"]["cond"]+" : "+O00O00OO000OO0000 ["cedents_str"]["frst"]+" x "+O00O00OO000OO0000 ["cedents_str"]["scnd"]#line:1389
            print (OOOOO0OO0OO000OO0 )#line:1391
        print ("")#line:1392
    def print_hypo (OO0OOOO0O0O0O0OO0 ,OO0000OOO0OOOO0OO ):#line:1394
        OO0OOOO0O0O0O0OO0 .print_rule (OO0000OOO0OOOO0OO )#line:1395
    def print_rule (OO0OOOOOO00OO0000 ,OOOOOOOOO0OO0O000 ):#line:1398
        print ("")#line:1399
        if (OOOOOOOOO0OO0O000 <=len (OO0OOOOOO00OO0000 .result ["rules"])):#line:1400
            if OO0OOOOOO00OO0000 .result ['taskinfo']['task_type']=="4ftMiner":#line:1401
                print ("")#line:1402
                O0O00O0OOOOO0OO00 =OO0OOOOOO00OO0000 .result ["rules"][OOOOOOOOO0OO0O000 -1 ]#line:1403
                print (f"Rule id : {O0O00O0OOOOO0OO00['rule_id']}")#line:1404
                print ("")#line:1405
                print (f"Base : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['base'])}  Relative base : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['rel_base'])}  CONF : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['conf'])}  AAD : {'{:+.3f}'.format(O0O00O0OOOOO0OO00['params']['aad'])}  BAD : {'{:+.3f}'.format(O0O00O0OOOOO0OO00['params']['bad'])}")#line:1406
                print ("")#line:1407
                print ("Cedents:")#line:1408
                print (f"  antecedent : {O0O00O0OOOOO0OO00['cedents_str']['ante']}")#line:1409
                print (f"  succcedent : {O0O00O0OOOOO0OO00['cedents_str']['succ']}")#line:1410
                print (f"  condition  : {O0O00O0OOOOO0OO00['cedents_str']['cond']}")#line:1411
                print ("")#line:1412
                print ("Fourfold table")#line:1413
                print (f"    |  S  |  ¬S |")#line:1414
                print (f"----|-----|-----|")#line:1415
                print (f" A  |{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold'][0])}|{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold'][1])}|")#line:1416
                print (f"----|-----|-----|")#line:1417
                print (f"¬A  |{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold'][2])}|{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold'][3])}|")#line:1418
                print (f"----|-----|-----|")#line:1419
            elif OO0OOOOOO00OO0000 .result ['taskinfo']['task_type']=="CFMiner":#line:1420
                print ("")#line:1421
                O0O00O0OOOOO0OO00 =OO0OOOOOO00OO0000 .result ["rules"][OOOOOOOOO0OO0O000 -1 ]#line:1422
                print (f"Rule id : {O0O00O0OOOOO0OO00['rule_id']}")#line:1423
                print ("")#line:1424
                print (f"Base : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['base'])}  Relative base : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['rel_base'])}  Steps UP (consecutive) : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['s_up'])}  Steps DOWN (consecutive) : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['s_down'])}  Steps UP (any) : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['s_any_up'])}  Steps DOWN (any) : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['s_any_down'])}  Histogram maximum : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['max'])}  Histogram minimum : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['min'])}  Histogram relative maximum : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['rel_max'])} Histogram relative minimum : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['rel_min'])}")#line:1426
                print ("")#line:1427
                print (f"Condition  : {O0O00O0OOOOO0OO00['cedents_str']['cond']}")#line:1428
                print ("")#line:1429
                print (f"Histogram {O0O00O0OOOOO0OO00['params']['hist']}")#line:1430
            elif OO0OOOOOO00OO0000 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1431
                print ("")#line:1432
                O0O00O0OOOOO0OO00 =OO0OOOOOO00OO0000 .result ["rules"][OOOOOOOOO0OO0O000 -1 ]#line:1433
                print (f"Rule id : {O0O00O0OOOOO0OO00['rule_id']}")#line:1434
                print ("")#line:1435
                print (f"Base1 : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['base1'])} Base2 : {'{:5d}'.format(O0O00O0OOOOO0OO00['params']['base2'])}  Relative base 1 : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['rel_base1'])} Relative base 2 : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['rel_base2'])} CONF1 : {'{:.3f}'.format(O0O00O0OOOOO0OO00['params']['conf1'])}  CONF2 : {'{:+.3f}'.format(O0O00O0OOOOO0OO00['params']['conf2'])}  Delta Conf : {'{:+.3f}'.format(O0O00O0OOOOO0OO00['params']['deltaconf'])} Ratio Conf : {'{:+.3f}'.format(O0O00O0OOOOO0OO00['params']['ratioconf'])}")#line:1436
                print ("")#line:1437
                print ("Cedents:")#line:1438
                print (f"  antecedent : {O0O00O0OOOOO0OO00['cedents_str']['ante']}")#line:1439
                print (f"  succcedent : {O0O00O0OOOOO0OO00['cedents_str']['succ']}")#line:1440
                print (f"  condition  : {O0O00O0OOOOO0OO00['cedents_str']['cond']}")#line:1441
                print (f"  first set  : {O0O00O0OOOOO0OO00['cedents_str']['frst']}")#line:1442
                print (f"  second set : {O0O00O0OOOOO0OO00['cedents_str']['scnd']}")#line:1443
                print ("")#line:1444
                print ("Fourfold tables:")#line:1445
                print (f"FRST|  S  |  ¬S |  SCND|  S  |  ¬S |");#line:1446
                print (f"----|-----|-----|  ----|-----|-----| ")#line:1447
                print (f" A  |{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold1'][0])}|{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold1'][1])}|   A  |{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold2'][0])}|{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold2'][1])}|")#line:1448
                print (f"----|-----|-----|  ----|-----|-----|")#line:1449
                print (f"¬A  |{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold1'][2])}|{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold1'][3])}|  ¬A  |{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold2'][2])}|{'{:5d}'.format(O0O00O0OOOOO0OO00['params']['fourfold2'][3])}|")#line:1450
                print (f"----|-----|-----|  ----|-----|-----|")#line:1451
            else :#line:1452
                print ("Unsupported task type for rule details")#line:1453
            print ("")#line:1457
        else :#line:1458
            print ("No such rule.")#line:1459
