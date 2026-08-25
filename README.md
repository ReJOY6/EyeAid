# EyeAid - Augenkrankheiten Klassifizierung mit ResNet18

Dieses Projekt nutzt ein in PyTorch trainiertes ResNet18-Modell, um Augenaufnahmen in 5 Kategorien zu klassifizieren: Cataract, Conjunctivitis, Eyelid-Erkrankungen, Uveitis oder Normal.

## Projektstruktur vorbereiten

Damit das Programm läuft, musst du deine aus Google Colab heruntergeladene Datei `resnet18_augen_modell.pth` in denselben Ordner wie die `app.py` legen.

```text
EyeAid-App/
  ├── app.py
  ├── requirements.txt
  ├── README.md
  └── resnet18_augen_modell.pth  <-- DEINE HERUNTERGELADENE DATEI HIER PLATZIEREN
```

## Installation & Start (Lokal)

1. Klonen Sie dieses Repository oder laden Sie es als ZIP herunter.
2. Stellen Sie sicher, dass Sie Python installiert haben.
3. Öffnen Sie Ihr Terminal/Eingabeaufforderung im Projektordner und installieren Sie die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
4. Starten Sie die Anwendung:
   ```bash
   python app.py
   ```
5. Öffnen Sie den im Terminal angezeigten Link (z.B. `http://127.0.0.1:7860`) in Ihrem Webbrowser.

## Medizinischer Haftungsausschluss
This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes.
Dieses Modell wurde zu Bildungszwecken trainiert und bietet **keine medizinische Diagnostik**. Bei echten Beschwerden suchen Sie bitte immer einen Augenarzt auf.
