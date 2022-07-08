import re
import os
from dotenv import load_dotenv

load_dotenv()

l = os.environ.get('AWS_ACCESS_KEY_ID')
print(l)