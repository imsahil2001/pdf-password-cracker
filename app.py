from flask import Flask, request, send_file, render_template, jsonify
from pypdf import PdfReader, PdfWriter
import io
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50MB limit


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/unlock", methods=["POST"])
def unlock_pdf():
    if "pdf" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["pdf"]
    password = request.form.get("password", "")

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are supported"}), 400

    try:
        pdf_bytes = file.read()
        reader = PdfReader(io.BytesIO(pdf_bytes))

        # Try to decrypt if password-protected
        if reader.is_encrypted:
            if not password:
                return jsonify({"error": "This PDF is password protected. Please provide the password."}), 400
            result = reader.decrypt(password)
            if result == 0:
                return jsonify({"error": "Incorrect password. Please try again."}), 400

        # Write all pages to a new unencrypted PDF
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        output = io.BytesIO()
        writer.write(output)
        output.seek(0)

        original_name = os.path.splitext(file.filename)[0]
        output_filename = f"{original_name}_unlocked.pdf"

        return send_file(
            output,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=output_filename,
        )

    except Exception as e:
        return jsonify({"error": f"Failed to process PDF: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
