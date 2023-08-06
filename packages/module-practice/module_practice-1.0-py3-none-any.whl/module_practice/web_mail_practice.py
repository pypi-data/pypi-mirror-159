
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from email.mime.multipart import MIMEMultipart
from string import Template

from urllib3 import encode_multipart_formdata
# import webbrowser
# webbrowser.open("https://www.google.com/")

htmlobject = Path("module_practice\webpage.html").read_text()
string_object = Template(htmlobject)
payload_html = string_object.substitute(name="girish")
image_file = Path("chkbk.jpg")
payload_image = image_file.read_bytes()
message = MIMEMultipart()
message["from"] = "Girish C.Gowda"
message["to"] = "gowdagirishdevops@gmail.com"
message["subject"] = "hello software engineer"
message.attach(MIMEText(payload_html, "html"))  # uploading html page
message.attach(MIMEImage(payload_image))                        # uploading pic
with smtplib.SMTP("smtp.gmail.com", port=587) as gmail:
    gmail.ehlo()
    gmail.starttls()
    # need to authenticate with app passwd once
    gmail.login("gowdagirish333@gmail.com", "techdzbxaftwwskt")
    gmail.send_message(msg=message)
    print("message sent")
