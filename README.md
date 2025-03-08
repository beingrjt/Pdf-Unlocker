# PDF Unlocker

This script attempts to unlock a password-protected PDF file using a user-provided password. It uses the `pikepdf` library to open the PDF and verifies the file's existence before attempting to unlock it.

## Requirements

Ensure you have the following Python packages installed before running the script:

```sh
pip install pikepdf
```

## How It Works

1. The script prompts the user to enter the path of the locked PDF file and the password.
2. It checks whether the specified file exists before proceeding.
3. If the password is correct, the unlocked PDF is saved in the same directory with the prefix `unlocked_` added to the original filename.
4. If the password is incorrect or the file is corrupted, the script provides an appropriate error message.

## Usage

Run the script using Python:

```sh
python script.py
```

When prompted, enter:
- The path to the locked PDF file
- The password for the file

Example:

```sh
Enter the path to your PDF file: C:\Users\Downloads\locked_file.pdf
Enter the password: mysecurepassword
```

If the password is correct, the unlocked file will be saved as:

```
C:\Users\Downloads\unlocked_locked_file.pdf
```

## Error Handling
- If the file does not exist, the script prints an error message.
- If the password is incorrect, the script notifies the user.
- If the PDF is corrupted or invalid, an appropriate error message is displayed.

## Notes

- Ensure you have permission to unlock the PDF file.
- This script does **not** attempt brute force attacks but relies on a single provided password.
- Modify the save path logic as needed to suit your system.

## Disclaimer

This script is intended for ethical use only. Do not use it to unlock files without proper authorization.

