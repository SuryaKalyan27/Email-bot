import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
from email_list_cleanup import Email_list,Email_Addr

from_email = "SENDERS_EMAIL_ADDR"
to_email = "RECIEVER_EMAIL_ADDR"

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "Plant Disease Dummy Email"
html_txt = """<p>Good Morning Dr. {} ,<br />This email is to ask for help with upholding the <b>scientific integrity</b> of our research paper.<br />&nbsp;<br />Our team has been working on a research paper within the domain of <b>Plant Pathology and Artificial Intelligence</b>.<br />&nbsp;<br />
The study's topic is "Plant Disease Image Classification using AutoML and EfficientNet-V2". Which falls more concretely under <b>Applied Computer Vision</b>.<br />&nbsp;<br />Our dataset consists of <b>87,000 plant leaf images</b> that are categorized into <b>38 different types of plant diseases.</b> We train deep learning models on this dataset to perform a study on the 
viability of these architectures in this domain. We would appreciate your perspective and participation in a 
<b>double-blind experiment</b> since <b>this is your area of expertise</b>.<br />&nbsp;<br />For more information on our paper and the double-blind experiment kindly refer to the document attached to this email.<br />&nbsp;<br /><b>Anticipating hearing back from you.</b><br />&nbsp;<br />
Best Regards,<br />Full Name,<br />Year, Branch, College,<br />Email,<br />Phone number<br /><br /></p>"""

text1 = MIMEText(html_txt, "html")

filename = "Plant Disease Classification & Detection Double Blind Proposal.docx.pdf"
attachment = open("Plant Disease Classification & Detection Double Blind Proposal.docx.pdf", "rb")
p = MIMEBase('application', 'octet_stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
the_msg.attach(p)
the_msg.attach(text1)

#SERVER CONFIG FOR SENDER USING GMAIL 
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#LOGIN WITH YOU CREDENTIALS
server.login("SENDER EMAIL ADDRESS", "EMAIL_PASSWORD")
#SENDING EMAIL CONTENTS
server.sendmail(from_email, to_email, the_msg.as_string())
server.quit()
