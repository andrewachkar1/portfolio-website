# Portfolio Website — Flask + Tailwind (Advanced)

## Description

A professional portfolio with a Flask backend and modern frontend using TailwindCSS and JavaScript for animations, smooth scroll, modals, and dynamic effects. The site includes:
* Pages: Home, Projects, Contact
* Contact form stored in `messages.json`
* Admin dashboard to view messages
* JS effects: typing headline, reveal animations, counters, smooth scroll, modals

---

## Project Structure

```
portfolio-flask/
├─ app.py                  # Flask backend
├─ requirements.txt        # Python dependencies
├─ run.sh                  # Script to run the app
├─ .env.example            # Environment variables
├─ messages.json           # Storage for contact messages
├─ templates/              # Jinja2 templates
│  ├─ base.html
│  ├─ index.html
│  ├─ projects.html
│  ├─ contact.html
│  └─ admin_messages.html
├─ static/
│  ├─ js/
│  │  └─ main.js
│  └─ css/
│     └─ styles.css
└─ README.md
```

---

## Installation

1. Clone the repository:
```bash
git clone <REPO_URL>
cd portfolio-flask
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env to set FLASK_SECRET and ADMIN_TOKEN
```

4. Run the Flask server:
```bash
flask run
# or python app.py
```

5. Access the site at `http://127.0.0.1:5000`

---

## Features

* **Home page** with hero section, introduction, and skills
* **Projects page** with modals for each project
* **Contact page** with form and dynamic feedback
* **Admin messages** page to view all submitted messages
* **JS effects**: smooth scroll, typing headline, counters, modals
* **Responsive design** using TailwindCSS

---

## Deployment

* Use Render, Railway, or any service that supports Flask
* For GitHub Pages frontend only, separate the Flask backend on another service

---

## Customization

* Change `ADMIN_TOKEN` and `FLASK_SECRET` in `.env`
* Update texts, colors, and projects in `templates` and `static/js/main.js`
* Add your CV files and images in `static/`

---

## Contributions

This project is intended as a personal demonstration. For production use:

* Clean or edit all comments
* Rename variables if necessary
* Add your personal projects and information

---

## License

MIT © Andrew Achkar
