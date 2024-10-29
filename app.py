from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image, ImageFilter
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-image", methods=["POST"])
def process_image():
    file = request.files["image"]
    input_image = Image.open(file.stream).convert("RGBA")
    
    # Remove background
    output_image = remove(input_image)
    
    # Apply edge smoothing for better quality
    output_image = output_image.filter(ImageFilter.SMOOTH_MORE)
    
    # Save result in high quality
    img_io = io.BytesIO()
    output_image.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
