# PDF Unlocker

This script attempts to unlock a password-protected PDF file by trying a list of passwords. It uses the `pikepdf` library to open the PDF and `tqdm` to display a progress bar while iterating through the passwords.

## Requirements

Ensure you have the following Python packages installed before running the script:

```sh
pip install pikepdf tqdm
```

## How It Works

1. The script takes a PDF file path and a string containing potential passwords.
2. It splits the string into individual passwords and tries each one to unlock the PDF.
3. If a correct password is found, the unlocked PDF is saved to `C:\Users\downloads\unlocked_file.pdf`.
4. If none of the passwords work, the script outputs "No password worked".

## Usage

Modify the following variables in the script before running:

- `pdf_path`: Path to the locked PDF file.
- `password_string`: A string containing potential passwords (one per line).

Example:

```python
pdf_path = r"C:\Users\downloads\file_to_unlocked.pdf"
password_string = """add_your_password_here"""
try_unlock_pdf(pdf_path, password_string)
```

Run the script using Python:

```sh
python script.py
```

## Notes

- Ensure you have permission to unlock the PDF file.
- The script does not attempt brute force attacks but works with a provided list of passwords.
- Modify the save path as needed to suit your system.

## Disclaimer

This script is intended for ethical use only. Do not use it to unlock files without proper authorization.
