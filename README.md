# Dynamic Dataset Generator

A simple web application built with **Flask** and **Pandas** that allows you to generate custom datasets in CSV format.  
You can define the number of rows, columns, and data types (Integer, Float, String, UUID) and download the dataset instantly.

---

## Features
- Choose number of rows and columns
- Select data types for each column
- Download the generated dataset as a CSV file
- Clean and simple UI built with HTML, CSS, and JavaScript

---

## Tech Stack
- **Backend:** Python, Flask, Pandas
- **Frontend:** HTML, CSS, JavaScript
- **Other:** Git for version control

---

## Project Structure

```plaintext
dynamic-dataset-generator/
├── app.py              # Flask backend (main application file)
├── requirements.txt    # Python dependencies
├── static/
│   ├── app.js          # Frontend logic (JavaScript)
│   └── style.css       # Styling (CSS)
├── templates/
│   └── index.html      # Frontend template (HTML)
└── README.md           # Project documentation

```
---

## Installation & Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/dynamic-dataset-generator.git
   cd dynamic-dataset-generator
---
## Create virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

---
## Install dependencies
pip install -r requirements.txt


---
## Run the Flask server
python app.py

