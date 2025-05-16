# 📦 Inventory-App

This repo contains a **Flask-based CRUD web application** to manage my electronics inventory, which I intend to use for personal projects in the near future.  
It will serve as a **Bill of Materials (BOM)** management tool.

---

## 🚀 Features

- **Create** new inventory records.
- **Read (view)** all existing inventory.
- **Update** existing inventory items.
- **Delete** inventory records.
- Deployed on **Render.com**.
https://inventory-app-skt8.onrender.com

---

## Project Structure
Within the app folder:
1. __init__.py :This code sets up my Flask app. The create_app() function creates the app and tells it to use a SQLite database called inventory.db stored just outside the app folder. It turns off some extra tracking in SQLAlchemy to keep things simple. Then, it connects the database to the app. After that, it brings in my routes from the views file and hooks them up to the app. Inside the app’s context, it loads my InventoryItem model and makes sure the database tables are created if they’re not there yet. In the end, it gives me the fully ready Flask app to run.
   
2. views.py : This code sets up the main parts of my Flask app for managing the electronics inventory. It creates routes to show all items, add new ones, update existing ones, and delete items by their ID. When I visit the main page, it pulls all inventory items from the database and displays them. For creating or updating items, it shows a form, and when I submit it, the data is saved to the database. After adding, updating, or deleting an item, it sends me back to the main list. The different pages are rendered using HTML templates like index.html, create.html, and update.html
   
3. Models.py : This code defines a database model for my Flask app using SQLAlchemy, which is an Object Relational Mapper. Each attribute in the class corresponds to a column in the database table: id is a unique identifier for every inventory item, an integer that auto-increments with each new item added, making it easy to reference or update specific records; name stores the name of the electronic item and is required (nullable=False), ensuring every inventory item has a name; category groups the item into categories to help organize the inventory for easier searching; quantity tracks how many units of the item are needed, and price stores the cost or price per unit as a floating-point number to accommodate decimal values.
   
4. Templates : Within the foler, I have multiple html templates all inheriting from the base.html file to establish the main outlook and design of the different views. Create file is triggered by 'Add New Item' button and Udpdate is for routed to by the edit button. The pictures below show the rendered Create and update templates, respectfully.![image](https://github.com/user-attachments/assets/dbfa81de-d658-4b13-8a7a-3e87f575d952)
![image](https://github.com/user-attachments/assets/1fca2fac-c150-4d58-8630-ffd484a3765a)

5. This code is what actually runs my Flask app. It starts by importing the create_app() function from my app package, then calls it to create the app instance. The if __name__ == '__main__': part makes sure the app only runs when I run this file directly (not when it's imported somewhere else). Inside that block, it starts the Flask development server with debugging turned on, so I get helpful error messages and automatic reloads while I’m working on the app.

6. Requirements.txt: This file lists all the Python packages my app depends on, along with their versions. When someone else (or a server) sets up the project, they can run pip install -r requirements.txt to install all the necessary libraries, making sure the app runs exactly as expected. Lastly the Procfile defines how my program should execute on deployment platforms like the one I have used Render. It should be noted that render has settings that force app:app so for my case since I have a run.py I had to have rup:app. this can be changed within render settings to fix it.
Below are pictures of my website for all of the views:
Home page
![image](https://github.com/user-attachments/assets/daf03766-fe54-4e2e-a41b-bd0f9f44d751)

Add new Item
![image](https://github.com/user-attachments/assets/2057ea95-7573-47e2-979c-efd0b5452a5e)

Delete Item: the delete function stays on the home page.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Inventory-App.git
   cd Inventory-App







