# Sameer Chakravedi — Portfolio Website

A Django-based portfolio website with a dark, techy aesthetic.

## Local Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```
Then open: http://127.0.0.1:8000

---

## 🚀 Free Hosting on Render.com (Recommended)

1. Push this project to GitHub (create a new repo)
2. Go to https://render.com → Sign up free
3. Click **New → Web Service**
4. Connect your GitHub repo
5. Set these settings:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command:** `gunicorn sameer_portfolio.wsgi`
   - **Environment:** Python 3
6. Click **Create Web Service**
7. Your site is live at `https://yourname.onrender.com` ✅

### Set Environment Variable on Render:
- `SECRET_KEY` → any long random string
- `DEBUG` → `False`

---

## 🚂 Free Hosting on Railway.app (Alternative)

1. Go to https://railway.app → Sign up with GitHub
2. Click **New Project → Deploy from GitHub Repo**
3. Select this repository
4. Railway auto-detects Django and deploys!
5. Go to **Settings → Domains** to get your free URL

---

## Project Structure

```
sameer_portfolio/
├── main/              # Django app
│   ├── views.py       # All page data lives here
│   └── urls.py
├── templates/
│   └── index.html     # Main HTML template
├── static/
│   ├── css/style.css  # All styles
│   └── js/main.js     # Animations & interactions
├── requirements.txt
├── Procfile           # For deployment
└── manage.py
```

## Customization

To update your info, edit `main/views.py` → `context` dictionary.
To change colors, edit `static/css/style.css` → `:root` CSS variables.
