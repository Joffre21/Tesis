import imaplib
import email
import traceback

mail_direction = "joffregvz00@gmail.com"
password = "ljirhmuztysissru"

imap_server = "imap.gmail.com"
port = 993

try:
    mail = imaplib.IMAP4_SSL(imap_server, port)
    mail.login(mail_direction, password)
    mail.select("[Gmail]/Spam")
    #mail.select("INBOX")
    #select specific mails
    _, selected_mails = mail.search(None, 'SEEN')
    #total number of mails from specific user
    print("Total Messages: " , len(selected_mails[0].split()))
    for num in selected_mails[0].split():
        _, data = mail.fetch(num , '(RFC822)')
        _, bytes_data = data[0]
        #convert the byte data to message
        email_message = email.message_from_bytes(bytes_data)
        print("\n===========================================")

        #access data
        print("Subject: ",email_message["subject"])
        print("To:", email_message["to"])
        print("From: ",email_message["from"])
        print("Date: ",email_message["date"])
        for part in email_message.walk():
            if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                message = part.get_payload(decode=True)
                print("Message: \n", message.decode())
                print("==========================================\n")
                break
        # close the connection and logout
    mail.close()
    mail.logout()
except Exception as e:
    traceback.print_exc()
    print(str(e))