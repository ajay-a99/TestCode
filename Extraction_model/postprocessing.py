import os,re
import pandas as pd
import sys 


content = ''
user_details = {}
name_lst, user_mail_lst, centre_mail_lst,dob_value_lst,phone_value_lst = ([] for i in range(5))

# Method to get the expected values
def user_details_fn(content,user_details):
    user_name = re.search('name\s*:.{1,50}(?=user)',content,re.IGNORECASE)
    user_name_value = user_name.group().split(':')[-1].strip()
    name_lst.append(user_name_value)

    user_gmail = re.search(r'user\s*email.{1,30}',content,re.IGNORECASE)
    gmail_pattern = re.search(r'[a-zA-Z0-9]+@gmail\.com',user_gmail.group(),re.IGNORECASE)
    user_gmail_value = gmail_pattern.group() if gmail_pattern else "N/A"
    user_mail_lst.append(user_gmail_value)

    centre_gmail = re.search(r'centre\s*email.{1,70}',content,re.IGNORECASE)
    gmail_pattern = re.search(r'[a-zA-Z0-9_]+@[A-z]*\.com',centre_gmail.group(),re.IGNORECASE)
    centre_gmail_value = gmail_pattern.group() if gmail_pattern else 'N/A'
    centre_mail_lst.append(centre_gmail_value)    

    dob = re.search(r'dob.{1,30}(?=phone)',content,re.IGNORECASE)
    dob_pattern = re.search(r'\d{1,2}\/\d{1,2}\/\d{4}',dob.group(),re.IGNORECASE)
    dob_value = dob_pattern.group() if dob_pattern else "N/A"
    dob_value_lst.append(dob_value)

    phone = re.search(r'phone.{1,30}',content,re.IGNORECASE)
    phone_pattern = re.search(r'\d{10}',phone.group(),re.IGNORECASE)
    phone_value = phone_pattern.group() if phone_pattern else "N/A"
    phone_value_lst.append(phone_value)

    user_details['Name'] = name_lst
    user_details['User Email'] = user_mail_lst
    user_details['Centre Email'] = centre_mail_lst
    user_details['DOB'] = dob_value_lst
    user_details['Phone'] = phone_value_lst
    return user_details


#Get inside the directory
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
directory = f'{script_directory}\\input\\'

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Check if the file is a text file
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            details_dict = user_details_fn(content,user_details)
            
df = pd.DataFrame(details_dict)
df.to_csv('output.csv',index = False) # Writing the output in csv format
