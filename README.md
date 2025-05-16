# Inventory-App
This repo entails a Flask-based CRUB web appliation to manage my electronics inventory which I intend to use for my own personal projects in the near future. It will serve as a bill of material(BMO). 

---
## Features

- **Create** new inventory records.
- **Read** (view) all existing inventory.
- **Update** existing inventory items.
- **Delete** inventory records.
- It can and will be deployed on Render.com

---
## Project structure
Inventory-App/
│
├── app/
│ ├── init.py # Initializes Flask app and DB
│ ├── views.py # Application routes and logic (CRUD)
│ ├── models.py # Database models (SQLAlchemy)
│ ├── templates/ # HTML templates (base.html, index.html, etc.)
│ └── static/ # Static files (optional - CSS, JS, etc.)
│
├── requirements.txt # Python dependencies
├── Procfile # Deployment config for Render
├── README.md # Project documentation
└── .gitignore # Files/folders to ignore in git


## 🛠 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Inventory-App.git
   cd Inventory-App
