# 💰 Finance Tracker

A full-stack personal expense management web app built with **Django** and **Python**. Track your daily expenses, visualize spending patterns by category, set budget limits, and export your data — all with secure user authentication.

🔗 **Live Demo:** [finance-tracker-by-shashank.onrender.com](https://finance-tracker-by-shashank.onrender.com/login/)

---

## 📸 Screenshots

> _Add screenshots here after deployment — login page, dashboard, add expense form_
> 
> Tip: Drag and drop images directly into this README on GitHub.

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, and logout securely using Django's built-in auth system
- ➕ **Add / Edit / Delete Expenses** — Full CRUD operations for managing your expenses
- 📂 **Category Management** — Organize expenses by category (Food, Travel, Bills, etc.)
- 🔍 **Search & Filter** — Filter expenses by category, date, or keyword
- 📄 **Pagination** — Clean, paginated expense listing for easy navigation
- 📊 **Dashboard Analytics** — Visual summary including:
  - Total expenses
  - Monthly spending total
  - Latest expense
  - Budget warning alert
- 🍩 **Category Chart** — Interactive pie/doughnut chart (Chart.js) showing spending by category
- 📥 **CSV Export** — Download all your expenses as a `.csv` file
- ⚠️ **Budget Warning** — Get alerted when spending exceeds your set limit

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap |
| Charts | Chart.js |
| Database | SQLite (dev) |
| Deployment | Render |
| Auth | Django built-in authentication |

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
cd finance-tracker
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin panel)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```
finance_tracker/
├── expenses/
│   ├── models.py        # Expense & Category models
│   ├── views.py         # All view logic (CRUD, export, dashboard)
│   ├── forms.py         # RegisterForm & ExpenseForm
│   ├── urls.py          # App-level URL routing
│   └── templates/
│       ├── base.html
│       ├── home.html    # Dashboard with charts
│       ├── add_expense.html
│       ├── login.html
│       └── register.html
├── finance_tracker/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

## 📊 Data Models

### `Category`
| Field | Type |
|---|---|
| name | CharField |

### `Expense`
| Field | Type |
|---|---|
| user | ForeignKey (User) |
| amount | FloatField |
| category | ForeignKey (Category) |
| date | DateField |
| description | TextField |

---

## 🌐 Deployment (Render)

This app is deployed on [Render](https://render.com). To deploy your own instance:

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command:** `gunicorn finance_tracker.wsgi:application`
5. Add environment variables:
   - `SECRET_KEY` = your Django secret key
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = your `.onrender.com` domain

---

## 🔮 Upcoming Features

- [ ] Income tracking (not just expenses)
- [ ] User-defined budget limits
- [ ] Monthly/yearly expense reports
- [ ] Dark mode

---

## 🙋‍♂️ Author

**Shashank**  
[GitHub](https://github.com/shashanksingh945/finance-tracker) • [LinkedIn](http://www.linkedin.com/in/shashank-singh-781860263)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).