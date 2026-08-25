EyeAid - Eye Disease Classification with ResNet18

svg

This project uses a ResNet18 model trained with PyTorch to classify eye images into 5 categories: Cataract, Conjunctivitis, Eyelid Diseases, Uveitis, or Normal.

Prepare the Project Structure

svg

To run the program, place the resnet18_augen_modell.pth file downloaded from Google Colab in the same folder as app.py.

EyeAid-App/
  ├── app.py
  ├── requirements.txt
  ├── README.md
  └── resnet18_augen_modell.pth  <-- PLACE YOUR DOWNLOADED FILE HERE

svg

Installation & Run Locally

svg

Clone this repository or download it as a ZIP file.
Make sure Python is installed on your system.
Open a terminal or command prompt in the project directory and install the dependencies:
pip install -r requirements.txt

svg

Start the application:
python app.py

svg

Open the link displayed in the terminal, for example http://127.0.0.1:7860, in your web browser.
Medical Disclaimer

svg

This project is for informational and educational purposes only. It does not provide medical diagnosis or professional medical advice. AI-generated results may contain errors. If you have any actual symptoms or concerns, always consult a qualified ophthalmologist.
