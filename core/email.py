'''
Created on 20-Dec-2017

@author: devasish ghosh
'''


import smtplib
from email.mime.text import MIMEText

emailtemplates = {
    "default": "<div>{content}</div>",
    
    "template1" : """\
    <div style="width:100%">
        <p>{para1}</p>
        <p>{para2}</p>
    </div>
    """,
    
    "template2" : """\
    <div>
        <h2>{header}</h2>
    </div>
    """,
    
}


def sendmail(to, body, subject, template = "default"):
    """
        @param to: list of receivers mail
        @param body: dict of keys exists in template
        @param subject: string
        @param template: string template name
        
        @return: True if success else dict or string
    """
    if isinstance(body, str):
        body = {"content" : body}
        
    msg_content = emailtemplates[template].format(**body)
    
    message = MIMEText(msg_content, 'html')
    message['From'] = 'Devasish Ghosh <abc@xyz.com>'
    message['To'] = to
    message['Cc'] = 'Devasish Ghosh <dev.achieve@gmail.com>'
    message['Subject'] = subject
    
    try:
        msg_full = message.as_string()
        
        server = smtplib.SMTP_SSL('smtp.mailserver.com:586')
        server.login('abc2@xyz.com', '123456')
        resp = server.sendmail('abc@xyz.com', to , msg_full)
        
        server.quit()
        
        return True if resp == {} else resp 
    except Exception as detail:
        return detail
    

