import sys
# sys.path.append(r'C:\Users\User\Desktop\python')
sys.path.append('/home/cim')
# connector
import connect.connect as cc
eng_cim = cc.connect('CIM_ubuntu', 'email')

import pandas as pd

from email import encoders  # 用於附檔編碼
from email.mime.base import MIMEBase  # 用於承載附檔
from email.mime.text import MIMEText  # 用於製作文字內文
from email.mime.multipart import MIMEMultipart  # email內容載體
import ssl
import datetime
import smtplib

def thmail(program,contents,attachments,subject):
    #寄件人
    from_address = 'CIM.ROBOT@theil.com'
    #收件人
    sql = "SELECT address from rec_list WHERE program ='"+program+"'"
    df = pd.read_sql(sql,eng_cim)    
    to_address = df['address'].tolist()
    #附件
    attachments = attachments.split(",")
    

    # 開始組合信件內容
    mail = MIMEMultipart()
    mail['From'] = from_address
    mail['To'] = ', '.join(to_address)
    mail['Subject'] = subject    
    
    # 將信件內文加到email中
    mail.attach(MIMEText(contents))    
    
    if(attachments[0] !='' ):
        # 將附加檔案們加到email中
        for file in attachments:
            with open(file, 'rb') as fp:
                add_file = MIMEBase('application', "octet-stream")
                add_file.set_payload(fp.read())
            encoders.encode_base64(add_file)
            add_file.add_header('Content-Disposition',
                                'attachment', filename=file)
            mail.attach(add_file)

    # 設定smtp伺服器並寄發信件

    smtpserver = smtplib.SMTP("ltrelay.theil.com", 25)
    smtpserver.ehlo()
    # smtpserver.login(gmail_user, gmail_password)
    smtpserver.sendmail(from_address, to_address, mail.as_string())
    smtpserver.quit()    
