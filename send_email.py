import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Create phishing email
def send_phishing_email(to_email):
    #Email credentials
    sender_email = "csforeveryone.nu@gmail.com"
    sender_password = "gmsy okjk pcqr taay" #app password
    #gmsy okjk pcqr taay - csforeveryone.nu@gmail.com
    #otxi fiwq kyat cxmm - vuhuygiahan@gmail.com
    subject = "Your Khoury account has been deactivated"
    #tracking_link = f"https://mykhoury-neu.github.io/my.Khoury?email={to_email}"
    tracking_link = f"https://my-khoury-northeastern.onrender.com?email={to_email}"
    #Email content
    body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Aptos, sans-serif;
                color: #333;
                line-height: 1.2;
                font-size: 16px;
            }}
            h1 {{
                font-size: 23px;
                font-weight: bold;
            }}
            strong {{
                font-weight: bold;
            }}
            p {{
                margin: 12px 0;
            }}
        </style>
    </head>
    <body>
        <br>
        <h1>Your Khoury account has been deactivated</h1>
  
        <p>This email is being sent to inform you that your Khoury account has been deactivated.</p>

        <p>If you are taking a class next semester, please note that accounts are automatically reactivated when a new semester starts and the registrar data updates to reflect your enrollment status.</p>

        <p>This is an automated process triggered by the NUID you provided falling out of our registrar data feed. The most likely causes of this are that you have graduated or are no longer taking a class at Khoury. Per university and college policy, services must end within 30 days of such an affiliation change.</p>

        <p>If you are an active student that is a Khoury major or graduate student with a concentration at Khoury, 
        please <a href="{tracking_link}">log in</a> your Khoury account and it will be reactivated automatically.</p>

        <p>For Khoury minors, we only receive information from the Registrar for majors, grads, and students enrolled in classes. Your account will be reactivated once you are back in a Khoury class. However, if you require access to your account when not currently taking a class with us, please reply to this email with a copy of your enrollment information showing that you are a minor and we will reactivate your account.</p>

        <p>Please note that outside of these affiliations, we can only keep accounts open while you are taking a class with us.</p>

        <p>If you believe this deactivation to be in error, reply to this email with proof of your current enrollment.</p>

        <p>Thanks,<br>
        <strong>The Khoury Systems Team</strong></p>
    </body>
    </html>
    """

    #Create the email to send
    msg = MIMEMultipart()
    msg['From'] = f'"systems@ccs.neu.edu" <khoury.neu@gmail.com>'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    try:
        #Connect to SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Phishing email sent to {to_email}")
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

#read email from email list
def read_email_list(filename):
    try:
        with open(filename, "r") as file:
            email_list = [line.strip() for line in file.readlines() if line.strip()]
        return email_list
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

if __name__ == "__main__":
    recipient_list = read_email_list("emails.txt")
    for recipient in recipient_list:
        send_phishing_email(recipient)

