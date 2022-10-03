#Librerías necesarias
import imaplib
import email
import re
import traceback
import pandas as pd
import base64
import quopri

#Función para descodificar textos
def encoded_words_to_text(encoded_words):
    try:
        encoded_word_regex = r'=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}='
        charset, encoding, encoded_text = re.match(encoded_word_regex, encoded_words).groups()
        if encoding == 'B':
            byte_string = base64.b64decode(encoded_text)
        elif encoding == 'Q':
            byte_string = quopri.decodestring(encoded_text)
        if bool:
            return byte_string.decode(charset)
        else:
            return byte_string.decode(charset)
    except:
        return encoded_words

#Lectura de correos
def ExtraccionCorreos(mail_direction, password, imap_server, port, folder):
    try:
        mail = imaplib.IMAP4_SSL(imap_server, port)
        mail.login(mail_direction, password)
        _, selected_mails = mail.select(folder)
        #Seleccionar a los correos 'UNSEEN'
        _, selected_mails = mail.search(None, 'SEEN')
        for num in selected_mails[0].split():
            _, data = mail.fetch(num , '(RFC822)')
            _, bytes_data = data[0]
            #Convertir desde Byte data al mensaje de correo
            email_message = email.message_from_bytes(bytes_data)
            for part in email_message.walk():
                if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                    message = part.get_payload(decode=True)
                    break
            lista_filas.append([encoded_words_to_text(email_message["subject"]), encoded_words_to_text(email_message["from"]), str(message.decode()), len(str(message.decode())), 1])
            #Cerrado de conexión
        mail.close()
        mail.logout()
    except Exception as e:
        traceback.print_exc()
        print(str(e))

#Variables para generar el dataset
lista_filas = []

ExtraccionCorreos("mrjofre4_joffre@hotmail.com", "youtube", "outlook.office365.com", 993, "JUNK")
ExtraccionCorreos("joffregvz00@gmail.com", "ljirhmuztysissru", "imap.gmail.com", 993, "[Gmail]/Spam")
ExtraccionCorreos("joffre_g2013@hotmail.com", "Tikotiko16", "outlook.office365.com", 993, "JUNK")
ExtraccionCorreos("elgamerplox@gmail.com", "umvesbrqizjooqkh", "imap.gmail.com", 993, "[Gmail]/Spam")


#Creación del Dataframe
df = pd.DataFrame(lista_filas, columns=['Asunto', 'Emisor', 'Mensaje', 'Longitud', 'Spam'])
print(df.head(26))
print(df.size)