# 🔓 PDF Unlocker

A simple web app to remove password protection from PDF files. Upload a PDF, enter the password (if needed), and download the unlocked version — all in your browser.

## Features

- Drag & drop or click to upload
- Handles password-protected & non-password PDFs
- No files stored on the server (processed in memory)
- Clean, dark UI

---

## 🚀 Deploy in 1 Click

### Option A — Railway (Recommended, Free tier available)

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template)

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**
3. Select your repo — Railway auto-detects everything
4. Done! You'll get a public URL in ~60 seconds

### Option B — Render (Free tier available)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Deploy!

### Option C — Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/pdf-unlocker
cd pdf-unlocker

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
```

Open [http://localhost:5000](http://localhost:5000)

---

## Tech Stack

- **Backend:** Python + Flask
- **PDF processing:** pypdf
- **Server:** Gunicorn
- **Frontend:** Vanilla HTML/CSS/JS (zero dependencies)

## Notes

- Max file size: 50MB
- Files are processed in memory — nothing is written to disk
- Only the correct password can unlock a protected PDF
