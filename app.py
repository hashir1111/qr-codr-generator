from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        link = request.form.get("link", "").strip()
        filename = request.form.get("filename", "qrcode").strip()

        if not link:
            return "A link is required.", 400

        # Generate QR code in memory
        img = qrcode.make(link)

        img_io = io.BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)

        return send_file(
            img_io,
            mimetype="image/png",
            as_attachment=True,
            download_name=f"{filename}.png"
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)