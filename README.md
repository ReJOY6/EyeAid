# EyeAid — Eye Disease Classification with ResNet18

EyeAid is a PyTorch-based image classification project that uses a fine-tuned **ResNet18** model to classify eye images into five categories:

* Cataract
* Conjunctivitis
* Eyelid Disease
* Uveitis
* Normal

The project was built as an educational computer vision application and provides a simple interface for testing the trained model on eye images.

## Project Structure

Make sure the trained model file `resnet18_augen_modell.pth` is located in the same directory as `app.py`.

```text
EyeAid/
├── app.py
├── requirements.txt
├── README.md
└── resnet18_augen_modell.pth
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ReJOY6/EyeAid.git
cd EyeAid
```

Alternatively, you can download the repository as a ZIP file and extract it.

### 2. Install the Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Start the application with:

```bash
python app.py
```

The terminal will display a local address such as:

```text
http://127.0.0.1:7860
```

Open this address in your browser to use EyeAid.

## Usage

1. Start the application.
2. Upload an eye image.
3. The model processes the image and predicts one of the five supported categories.
4. The result is displayed in the application.

## Model

The classifier is based on **ResNet18** and was trained using **PyTorch**.

The trained weights are stored in:

```text
resnet18_augen_modell.pth
```

## Medical Disclaimer

EyeAid was developed for **educational and experimental purposes only**.

It is not a medical device and must not be used as a substitute for professional diagnosis or treatment. Model predictions can be inaccurate. If you have symptoms or concerns about your eye health, consult a qualified medical professional or ophthalmologist.
