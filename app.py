from flask import Flask, request, render_template, send_file
import pikepdf
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["pdf_file"]
        password = request.form["password"]

        if file:
            input_path = f"temp_{file.filename}"
            file.save(input_path)
            try:
                pdf = pikepdf.open(input_path, password=password)
                output_path = f"unlocked_{file.filename}"
                pdf.save(output_path)
                os.remove(input_path)
                return send_file(output_path, as_attachment=True)
            except pikepdf.PasswordError:
                return render_template("form.html", message="❌ Incorrect password.")
            except Exception as e:
                return render_template("form.html", message=f"❌ Error: {str(e)}")
    return render_template("form.html")
