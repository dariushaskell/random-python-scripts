import pandas as pd
import re

def clean_phone_number(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    if len(cleaned_number) == 7:
        cleaned_number = '506' + cleaned_number
    return cleaned_number

file_path = r'C:\Path\to\excel\file.xlsx'

df = pd.read_excel(file_path)

df['Office Tel'] = df['Office Tel'].astype(str).apply(clean_phone_number)
df['Office Fax'] = df['Office Fax'].astype(str).apply(clean_phone_number)
df.to_excel(file_path, index=False)
