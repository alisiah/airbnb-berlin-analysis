# 🏠 Airbnb Price Analysis – Berlin

Dieses Data Science Projekt analysiert Airbnb-Angebote in Berlin mit Fokus auf die Vorhersage von Preisen. Es wurde zu Lern- und Demonstrationszwecken im Rahmen der Data-Science-Praxis erstellt und kann zukünftig weiter optimiert oder ausgebaut werden. Die aktuellen Modellwerte dienen lediglich der Veranschaulichung.

## 📌 Projektziele

- Verstehen, welche Merkmale den Preis beeinflussen
- Entwicklung eines Vorhersagemodells (Linear Regression, Random Forest, GradientBoosting und XGBoost)
- Visualisierung der wichtigsten Zusammenhänge

## 📂 Projektstruktur

- `notebooks/`: EDA & Modellierung im Jupyter Notebook
- `src/`: Reusable Python-Funktionen (Datenvorbereitung, Modelltraining)
- `data/`: Rohdaten (nicht in GitHub enthalten)
- `README.md`, `.gitignore`, `requirements.txt`: Standard Setup

## 📈 Datenquelle

Daten: [InsideAirbnb Berlin – Listings CSV](http://insideairbnb.com/get-the-data.html)

## 🧪 Installation

```bash
git clone https://github.com/dein-benutzername/airbnb-berlin-analysis.git
cd airbnb-berlin-analysis
pip install -r requirements.txt

```

## ✅ Ergebnisse (Beispiel)

- Wichtigste Merkmale: Mindestanzahl an Übernachtungen, Anzahl Reviews, Zimmertyp
- Modellgenauigkeit: RMSE ≈ 60 EUR, MAE ≈ 41 EUR, R2 ≈ 0.26

## 📝 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
