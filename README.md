# Multi-Purpose Calculator

A beginner-friendly web calculator with 17 operations: arithmetic (add, subtract, multiply, divide, floor division, power) and geometry (areas, perimeters and surface areas of common shapes). Built with Python, FastAPI, HTML, CSS and JavaScript.

The page works like the original console program: enter a condition number (1-18), then enter only the values that option needs. The original program is kept unchanged in `original_console.py`.

## Project Structure

```
.
├── main.py              # FastAPI app and API routes
├── calculator.py        # Calculator logic (same formulas and checks as the console program)
├── original_console.py  # The original console program
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment config
├── .python-version      # Python version for deployment
└── static/
    ├── index.html
    ├── style.css
    └── script.js
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## API

| Method | Route | What it does |
|--------|-------|--------------|
| GET | `/api/operations` | The menu: condition numbers, names and the inputs each needs |
| POST | `/api/calculate` | Run one option |

`POST /api/calculate`

```json
{ "condition": 4, "values": [10, 4] }
```

Response:

```json
{ "result": "2.5" }
```

Not-allowed inputs (for example dividing by zero or a negative radius) return a 400 error with the same message as the console program, such as `Cannot divide by zero`.

## Deploy on Render

Push this folder to the root of a GitHub repo (`main.py` and `static/` must be at the top level), create a new Web Service on Render and connect the repo. `render.yaml` already sets the build and start commands.

## License

MIT
