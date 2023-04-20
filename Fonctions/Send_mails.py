import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('blabla@gmail.com', '')

smtpObj.sendmail('blabla@gmail.com', 'password','Subject: Plan de travail \n Au boulot')

smtpObj.quit()