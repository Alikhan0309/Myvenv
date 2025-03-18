import os
from dotenv import load_dotenv

load_dotenv()

email_login = os.getenv('EMAIL_LOGIN')
print(email_login)