from flask import Flask, request, jsonify, render_template
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, GPT2Tokenizer, VisionEncoderDecoderConfig
import tempfile
import os

app = Flask(__name__)

#vrudit Patel
# Load the trained model
# model = VisionEncoderDecoderModel.from_pretrained(r'E:\Northeastern\Academic\Courses\EAI 6010\Module 4\Experiments\VIT_large_gpt2\VIT_large_gpt2')
model = VisionEncoderDecoderModel.from_pretrained('VIT_large_gpt2')

# Load the ViT feature extractor
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')

# Load the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def generate_caption(image_path):
    # Open the image
    img = Image.open(image_path).convert("RGB")

    # Generate caption using the loaded model and tokenizer
    generated_caption = tokenizer.decode(model.generate(feature_extractor(img, return_tensors="pt").pixel_values)[0])
    generated_caption = generated_caption.replace("<|endoftext|>", "")
    return generated_caption

@app.route('/')
def hello():
    # return "<p> Jay Jogani!<p>"
    # return render_template('Static_Website_Template-master/index.html')
    return render_template('index.html')
    # template_path = os.path.join(os.path.dirname(__file__), "Static_Website_Template-master", "index.html")
    # return render_template(template_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Assuming the image is sent as a file
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"})

        image_file = request.files['image']

        # Create a temporary file to save the image
        temp_image_fd, temp_image_path = tempfile.mkstemp(suffix='.jpg')
        with os.fdopen(temp_image_fd, 'wb') as temp_image:
            image_file.save(temp_image)

        # Generate caption
        caption = generate_caption(temp_image_path)

        # Remove the temporary file
        os.remove(temp_image_path)

        # Return the caption as JSON
        return jsonify({"caption": caption})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"),debug=True)
