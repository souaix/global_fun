import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def sftp_upload(sHostName,PATHS,FILES):
    
    PATHS = PATHS.split("/")
    
    if(sHostName == 'ltg1database.theil.com'):
        sUserName = 'cim'
        sPassWord = '23aU6eyW'

    elif(sHostName == '10.21.150.42'):
        sUserName = 'sftpuser'
        sPassWord = 'sftpuser'

        
    if(sUserName):
        with pysftp.Connection(sHostName, username=sUserName, password=sPassWord, cnopts=cnopts) as sftp:

            for p in PATHS :
                #print(p)
                path_exist  = True if p in sftp.listdir() else False
                
                if not path_exist  and p!= '':
                    sftp.mkdir(p)

                sftp.cwd(p)

            # 上傳檔案
            if(type(FILES) == list):

                for i in FILES:
                    sftp.put(i)

            elif(type(FILES) == str):

                sftp.put(FILES)
