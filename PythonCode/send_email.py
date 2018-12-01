import smtplib
import time


def send_mail(username, password, froma, to, subject, body):

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (froma, ", ".join(to), subject, body)

    try:

        start_time = time.time()
        # print 'Connecting...'
        print('Please Wait for a while...')

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("--- %s seconds ---" % (time.time() - start_time))
        print('connected')
        server.ehlo()
        print('Signing ...')
        server.login(username, password)
        print('logged in')
        print('Sending...')

        server.sendmail(froma, to, email_text)

        server.close()

        print('Email sent!')

    except:
        print('Something went wrong...')
        print('Please Check your Internet Connection and try again.')


def credential_setup(flag):
    gmail_user = 'nwoccam2018@gmail.com'
    gmail_password = 'winterofcode'

    froma = gmail_user
    to = ['farhan.tuba@gmail.com']
    subject = 'Alert Message!'

    body = "Motion alert"

    if flag:
        send_mail(gmail_user, gmail_password, froma, to, subject, body)
    else:
        pass


flag = True
credential_setup(flag)
