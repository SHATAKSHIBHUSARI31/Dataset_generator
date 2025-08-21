from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import uuid, random, string, io, time

app = Flask(__name__)

def generate_column(col_type, row_count):
    if col_type == "int":
        return np.random.randint(0, 1000, size=row_count)
    elif col_type == "float":
        return np.round(np.random.uniform(0, 1000, size=row_count), 2)
    elif col_type == "string":
        return [''.join(random.choices(string.ascii_letters, k=8)) for _ in range(row_count)]
    elif col_type == "uuid":
        return [str(uuid.uuid4()) for _ in range(row_count)]
    else:
        return np.random.randint(0, 100, size=row_count)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        num_cols = int(request.form.get("num_cols", 10))
        num_rows = int(request.form.get("num_rows", 1000))

        start = time.time()
        data = {}
        for i in range(num_cols):
            col_type = request.form.get(f"col_type_{i}", "int")
            data[f"col_{i}"] = generate_column(col_type, num_rows)

        df = pd.DataFrame(data)
        buf = io.BytesIO()
        df.to_csv(buf, index=False)
        buf.seek(0)
        elapsed = round(time.time() - start, 2)
        return send_file(buf, as_attachment=True, download_name="dataset.csv", mimetype="text/csv")
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
