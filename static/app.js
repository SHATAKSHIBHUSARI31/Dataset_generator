document.getElementById("generate-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const rowCount = document.getElementById("rows").value;
    const colCount = document.getElementById("cols").value;

    const types = [];
    document.querySelectorAll(".col-type").forEach(el => {
        types.push(el.value);
    });

    const payload = {
        rows: parseInt(rowCount),
        cols: parseInt(colCount),
        types: types
    };

    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    document.getElementById("status").innerText = `✅ Dataset generated with ${data.rows} rows and ${data.cols} columns`;
    document.getElementById("download-link").style.display = "block";
});

// Add column types dynamically
document.getElementById("add-col").addEventListener("click", function () {
    const container = document.getElementById("col-types");
    const select = document.createElement("select");
    select.className = "col-type";
    select.innerHTML = `
        <option value="int">Integer</option>
        <option value="float">Float</option>
        <option value="string">String</option>
        <option value="uuid">UUID</option>
        <option value="date">Date</option>
    `;
    container.appendChild(select);
});
