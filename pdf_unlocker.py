import pikepdf
from tqdm import tqdm

def try_unlock_pdf(pdf_path, password_string):
    # Split the password string into a list of passwords
    passwords = password_string.splitlines()
    # Try each password
    for password in tqdm(passwords):
        if not password:  # Skip empty lines
            continue
        try:
            pdf = pikepdf.open(pdf_path, password=password)
            print(f"Success! Password is: {password}")
            pdf.save(r'C:\Users\downloads\unlocked_file.pdf')
            return True
        except Exception as e:
            continue
    print("No password worked")
    return False
# Usage 
pdf_path = r"C:\Users\downloads\file_to_unlocked.pdf"
# Password list as a string with just the working password
password_string = """add_your_password_here"""
try_unlock_pdf(pdf_path, password_string)