from smtplib import SMTP
with SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('feshchenko.vitalii@gmail.com','***')
    smtp.sendmail(from_addr="feshchenko.vitalii@gmail.com",to_addrs="el.piankova@gmail.com",msg="I did it!")
    smtp.quit()

    