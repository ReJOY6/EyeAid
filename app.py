import os
import gradio as gr
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np

# 1. Konstanten festlegen (exakt wie in deinem Training)
class_names = ['Cataract', 'Conjunctivitis', 'Eyelid', 'Normal', 'Uveitis']
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 2. Bild-Transformationen definieren
data_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# 3. Modellstruktur aufbauen und trainierte Gewichte laden
model = models.resnet18()
model.fc = nn.Linear(model.fc.in_features, len(class_names))

# Lädt die .pth Datei, die im selben Ordner liegen muss
model_path = 'resnet18_augen_modell.pth'
if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path, map_location=device))
    print("Modell erfolgreich geladen!")
else:
    print(f"HINWEIS: '{model_path}' wurde nicht gefunden. Bitte platziere deine heruntergeladene Modelldatei in diesen Ordner.")

model.to(device)
model.eval()

# 4. Verbesserte Vorhersage-Funktion
def predict_eye_image(inp_img):
    if inp_img is None:
        return "Bitte lade ein Bild hoch."
        
    try:
        if isinstance(inp_img, dict):
            inp_img = inp_img.get("background", inp_img)
            
        if isinstance(inp_img, np.ndarray):
            bild = Image.fromarray(inp_img.astype('uint8')).convert('RGB')
        else:
            bild = Image.open(inp_img).convert('RGB')
            
        transformiertes_bild = data_transforms(bild).unsqueeze(0).to(device)
        
        with torch.no_grad():
            ausgabe = model(transformiertes_bild)
            wahrscheinlichkeiten = torch.nn.functional.softmax(ausgabe, dim=1)
        
        ergebnisse = {class_names[i]: float(wahrscheinlichkeiten[i]) for i in range(len(class_names))}
        return ergebnisse

    except Exception as e:
        return f"Fehler bei der Bildverarbeitung: {str(e)}"

# 5. Gradio UI erstellen
demo = gr.Interface(
    fn=predict_eye_image,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=3),
    title="👁️ EyeAid - Augenkrankheiten Klassifizierung",
    description="Lade ein Foto des Auges hoch. Das Modell analysiert das Bild auf Cataract, Conjunctivitis, Eyelid-Erkrankungen, Uveitis oder Normal.\n\n*Hinweis: Dies ist ein Bildunprojekt zu Demonstrationszwecken und ersetzt keine ärztliche Diagnose.*\n\n**Disclaimer:** This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes."
)

if __name__ == "__main__":
    demo.launch()
