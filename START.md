Run locally

Create a virtual environment, install dependencies, and start the dev server:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

Open http://127.0.0.1:8000/ in your browser (or use the forwarded port in your dev container).
