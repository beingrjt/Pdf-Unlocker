from flask import Flask, request, render_template, send_file
import pikepdf
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded PDF file and password from the form
        file = request.files["pdf_file"]
        password = request.form["password"]

        if file:
            # Save the uploaded PDF to a temporary location
            input_path = f"temp_{file.filename}"
            file.save(input_path)

            try:
                # Try to unlock the PDF with the provided password
                pdf = pikepdf.open(input_path, password=password)
                output_path = f"unlocked_{file.filename}"
                pdf.save(output_path)
                os.remove(input_path)  # Clean up the temporary file
                
                # Return the unlocked PDF as a download
                return send_file(output_path, as_attachment=True)

            except pikepdf.PasswordError:
                return "Incorrect password."
            except pikepdf.PdfError as e:
                return f"Error: Invalid or corrupted PDF file - {str(e)}"
            except Exception as e:
                return f"Unexpected error occurred: {str(e)}"
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
