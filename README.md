🚀 PictoScribe: Image Caption Generator 🖼️📜

This is a deep learning-based Image Caption Generator Prototype! This project is a convergence of two powerful areas in AI: Computer Vision and Natural Language Processing (NLP), resulting in a model that can generate captions for images.

The architecture of the model leverages the Vision Transformer (ViT) as an Encoder and GPT-2 as a Decoder, creating a robust Seq2Seq model. I utilized Seq2SeqTrainer from Hugging Face for fine-tuning. Although my initial plan was to train the model on the entire Flickr8K dataset, resource constraints limited me to using only 2,000 images. Despite this, the model was trained in a very short span of time, due to limited GPU access on Colab.

Even with these constraints, I was able to build a prototype capable of identifying the core context of an image while overlooking finer details. This is a significant milestone, especially considering the computational limitations.

To take this further, I developed a Flask application with basic HTML to host the model. I then containerized the app using Docker and pushed the image to Google Cloud's Container Registry. Finally, I deployed it via Cloud Run, making the Image Caption Generator accessible as a live service.

You can check out the live demo here: https://lnkd.in/gcG4dPa4


#DeepLearning #ComputerVision #NLP #AI #ImageCaptioning #VisionTransformer #GPT2 #HuggingFace #GoogleCloud #Docker #CloudRun
