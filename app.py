
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image, ImageFilter
import io

app = Flask(__name__)

@app.route("/process-image", methods=["POST"])
def process_image():
    file = request.files["image"]
    input_image = Image.open(file.stream).convert("RGBA")  # Ensuring RGBA mode for transparent backgrounds
    
    # Remove background
    output_image = remove(input_image)
    
    # Optional post-processing for smoother edges
    output_image = output_image.filter(ImageFilter.SMOOTH_MORE)  # Apply smoothing to reduce rough edges
    
    # Save the result in high quality to a BytesIO stream
    img_io = io.BytesIO()
    output_image.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
