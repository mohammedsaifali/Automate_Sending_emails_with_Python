import smtplib
# insert the emails you want to send email to
emaillist = ['one@gmail.com, two@gmail.com, three@gmail.com']
# looping the email to all list by following for loop
for e in emaillist :
    con = smtplib.STMP(stmp.gmail.com,'587')
    con.startls()
    con.login('youremail@gmail.com', 'yourpassword')
    msg = "your message"
    con.sendmail('youremail@gmail.com, 'receivermail@gmail.com, msg)
    con.quit()
print("Emails Send")