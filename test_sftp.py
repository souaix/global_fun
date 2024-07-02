import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def sftp_upload(sHostName,PATHS,FILES,PPK=""):
    
PATHS = PATHS.split("/")
    
if(sHostName == 'ltg1database.theil.com'):
    sUserName = 'cim'
    sPassWord = '23aU6eyW'

elif(sHostName == '10.21.150.42'):
    sUserName = 'sftpuser'
    sPassWord = 'sftpuser'

elif(sHostName == 'mft-ap.st.com'):
    sUserName = 'tonghsing_996Z'
    sPassWord = 'xxx'
    PPK = "/home/cim/global_fun/PublicKeyForST/STSFTP_DSAKEY"
        

if PPK =="":

    srv = pysftp.Connection(sHostName, username=sUserName, password=sPassWord, cnopts=cnopts) 

else:

    srv = pysftp.Connection(sHostName, username=sUserName, private_key=PPK, cnopts=cnopts) 

        
if(sUserName):
    with srv as sftp:

        for p in PATHS :
            #print(p)
            path_exist  = True if p in sftp.listdir() else False
                
            if not path_exist  and p!= '':
                try:
                    sftp.mkdir(p)

                except Exception as E:
                    print("mkdir fail : " +p+"--"+str(E))

            sftp.cwd(p)

        # 上傳檔案
        if(type(FILES) == list):

            for i in FILES:
                sftp.put(i)

        elif(type(FILES) == str):
            try:
                sftp.put(FILES)

            except Exception as E:
                print(str(E))
