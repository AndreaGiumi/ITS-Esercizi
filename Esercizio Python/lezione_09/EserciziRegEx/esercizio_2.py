import re
def  extract_emails(text:str):
    email = re.split(["a-z0-9"],"@{1}, [a-z]/W, [a-z]{3}", text)
    return email

text = "Contattaci a info@azienda.com oppure support@help.org"
print(extract_emails(text))