import openpyxl
import smtplib

workbook = openpyxl.load_workbook('Book1.xlsx') # specify your file name
sheet = workbook.active
emails = [cell.value for cell in sheet['A']] # type: ignore # assuming emails are in column A

# your email credentials (make sure to turn on "less secure app access" in your Google account)
EMAIL_ADDRESS = 'ssarantos@extreme-impact.com'
EMAIL_PASSWORD = '2411Valley'


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # Gmail's SMTP server
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Follow Up Email'
    body = 'This is the content of the follow-up email.'
    msg = f'Subject: {subject}\n\n{body}'

    # Sending the email to all addresses
    for email in emails:
        smtp.sendmail(EMAIL_ADDRESS, email, msg)