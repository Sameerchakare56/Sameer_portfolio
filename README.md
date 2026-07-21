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
