import pikepdf
import os

def try_unlock_pdf(pdf_path, password):
    try:
        # Verify input file exists
        if not os.path.exists(pdf_path):
            print(f"Error: File not found at {pdf_path}")
            return False

        # Try to open PDF with password
        pdf = pikepdf.open(pdf_path, password=password)
        
        # Generate output filename in same directory as input
        input_dir = os.path.dirname(pdf_path)
        input_filename = os.path.basename(pdf_path)
        output_filename = os.path.join(input_dir, f"unlocked_{input_filename}")
        
        # Save unlocked PDF
        pdf.save(output_filename)
        print(f"Success! PDF unlocked and saved as: {output_filename}")
        return True
        
    except pikepdf.PasswordError:
        print("Error: Incorrect password")
        return False
    except pikepdf.PdfError as e:
        print(f"Error: Invalid or corrupted PDF file - {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        return False

# Get inputs from user
pdf_path = input("Enter the path to your PDF file: ").strip()
password = input("Enter the password: ").strip()
try_unlock_pdf(pdf_path, password)