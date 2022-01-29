import imaplib
from win10toast_click import ToastNotifier
import datetime
import webbrowser as w
chrome_path=chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"# Incase you are useing firefox or edge as default browser comment out this line and the preceding line
w.register('chrome',None,w.BackgroundBrowser(chrome_path))
def gmail():#server code
    global y,count,data1,From,f
    imap_host='imap.gmail.com'
    imap_port=993
    username=""#Enter your username
    password=""#enter your password
    server=imaplib.IMAP4_SSL(imap_host,imap_port)
    server.login(username,password)
    status,count=server.select('inbox')
    #print(status,count)
    p=datetime.datetime.ctime(datetime.datetime.now())[-4:]
    dt=(datetime.date.today()-datetime.timedelta(1)).strftime("%d-%b-%y")
    k=dt.split("-")
    a=''
    k.pop()
    k.append(p)
    for i  in range(0,3):
        if i!=2:
            a+=k[i]
            a+="-"
        else:
            a+=k[i]
    stat,data1=server.search(None,'(UNSEEN SINCE {})'.format(a))
    #print((data1))
    subject=server.fetch\
                 (count[0],\
                  ("(UID BODY[HEADER.FIELDS (SUBJECT)])"))[-1]
    f=subject[0][1].decode('utf8')
    f=f.lstrip('Subject:').strip()
    #print(f)
    data=server.fetch(count[0],\
                      ("(UID BODY[HEADER.FIELDS (FROM)])"))[-1]

    From=data[0][1].decode('utf8')
    From=From[:From.find('<')].strip()
    #print(From)
    y=server.fetch(count[0],\
                      ("(UID BODY[HEADER.FIELDS (DATE)])"))[-1]
    y=y[0][1].decode('utf8')
def ok():
    w.get('chrome').open("https://mail.google.com/mail/u/0/#inbox",new=0)    #incase you are using other browser enter the other browser name in the get() field
def main():
    tstamp=0
    tstamp1=int((datetime.datetime.now()-datetime.timedelta(1)).strftime("%M"))
    while(True): 
        if(int((datetime.datetime.now()-datetime.timedelta(1)).strftime("%M"))==tstamp1+1):
            gmail()
            if int(str(data1[0])[-2])==int(str(count[0])[-2]):
                #print("New Mail")
                tstamp1=int((datetime.datetime.now()-datetime.timedelta(1)).strftime("%M"))
                notification_window=ToastNotifier()
                notification_window.show_toast(From,f,callback_on_click=ok)
                
            else:
                #print("No New Mails")
                tstamp1=int((datetime.datetime.now()-datetime.timedelta(1)).strftime("%M"))

main()

