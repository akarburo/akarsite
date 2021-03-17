import smtplib
content = "Bu bir maildir"
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("metastaban@gmail.com","Qaz1907qaz.")
mail.sendmail("metastaban@gmail.com","mehmetemin@tastaban.net",content)
