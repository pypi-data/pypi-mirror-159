import transistordatabase as tdb
import webbrowser
import json
import base64
#t1 = tdb.import_json('/home/nikolasf/Downloads/TDB_MOSFETs/template_SCT3060AW7/Rohm_SCT3060AW7.json')
#t1 = tdb.import_json('/home/nikolasf/Downloads/TDB_MOSFETs/template_IPBE65R050CFD7A/Infineon_IPBE65R050CFD7A.json')


print("## initial state")
#t1 = tdb.load('GaNSystems_GS66506T')
#tdb.print_tdb()


# Lösung 1
#
# recipient = 'emailaddress'
# subject = 'mysubject'
#
# #with open('body.txt', 'r') as b:
# body = 'dooenr'#b.read()
#
# body = body.replace(' ', '%20')
#
# webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)


# Lösung 2
# https://support.interact.technology/support/solutions/articles/17000003731-how-to-use-mailto-links-to-send-attachments-

d = { "type":"ecfg",
  "version":"1",
  "email_to" : "someone@yoursite.com",
  "email_cc" : ["john@yoursite.com", "jane@yoursite.com"],
  "email_bcc" : ["bob@yoursite.com"],
  "email_subject" : "Requested documents!!!!!!!!",
  "email_body" : "<html><body>Text</body></html>",
  "email_attachments" : [{
    "path" : "email/ClinicalStudy.pdf",
    "mime_type" : "application/pdf" }]
}



s = json.dumps(d)

encoded_string = base64.b64encode(s.encode('utf-8'))
print(f"{encoded_string = }")

#html_string = 'mailto:YourName@YourSite.com?cc=someone@YourSite.com&bcc=someoneElse@YourSite.com&subject=Shipping%20Information%20Request&body=Please%20tell%20me%20if%20my%20order%20has%20shipped!&ni_email_cfg_file=/home/nikolasf/Dokumente/01_git/30_Python/TDB/transistordatabase/gui/email/email.config'

#html_string = 'mailto:YourName@YourSite.com?cc=someone@YourSite.com&bcc=someoneElse@YourSite.com&subject=Shipping%20Information%20Request&body=Please%20tell%20me%20if%20my%20order%20has%20shipped!&attachment=""/home/nikolasf/Dokumente/01_git/30_Python/TDB/transistordatabase/gui/email/email/ClinicalStudy.pdf""'

#print(f"<{encoded_string = }>")
#webbrowser.open(f"mailto:someone@yoursite.com?cc=john@yoursite.com&bcc=bob@yoursite.com&subject=Requested%20documents&ni_email_cfg_base64json='{encoded_string}'", new=2)







import pathlib
transistor = tdb.load('CREE_C3M0120065J')


email_body = f"Do not forget to attach the transistor file <b>{transistor.name}</b> to this email!! Link to File: <a href={pathlib.Path.cwd().as_uri()}>{pathlib.Path.cwd().as_uri()}</a>"
email_subject = '<html><head></head><body><p>Request to add transistor {transistor.name} to the transistordatabase file exchange (TDB-FE)</p></body></html>'
webbrowser.open(f'mailto:?to=tdb@lea.upb.de&subject=' + email_subject + '&body=' + email_body, new=2)