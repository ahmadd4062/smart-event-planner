# 🎉 Smart Event Planner with AI Recommendations

A comprehensive **AI-powered Event Management System** built with **Django** that helps users efficiently plan, organize, and manage events. The platform streamlines event planning by providing tools for guest management, budget tracking, task scheduling, and AI-generated event recommendations.

---

## 🚀 Features

### 👤 User Authentication
- User Registration & Login
- Secure Authentication
- Personalized Dashboard

### 📅 Event Management
- Create, Update, and Delete Events
- Multiple Event Categories
  - Wedding
  - Corporate Event
  - Birthday Party
  - Conference
  - Meeting
  - Party
  - Other
- Event Status Tracking
- Event Description, Date, Time & Location

### 👥 Guest Management
- Add and Manage Guests
- RSVP Tracking
- Guest Contact Information
- Guest Notes

### 💰 Budget & Expense Tracking
- Set Event Budget
- Record Expenses
- Expense Categories
- Budget Utilization Monitoring

Expense Categories:
- Venue
- Catering
- Entertainment
- Decorations
- Transportation
- Staff
- Marketing
- Other

### 📋 Timeline & Task Management
- Create Event Tasks
- Task Deadlines
- Progress Tracking
- Task Status Management

### 🤖 AI Recommendations
- AI-powered event planning suggestions
- Intelligent recommendations for organizing events
- Personalized planning assistance using Google Gemini API

### 📊 Dashboard
- Overview of all events
- Budget Summary
- Guest Statistics
- Task Progress

---

# 🛠️ Tech Stack

### Backend
- Python
- Django 

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript

### Database
- SQLite

### AI Integration
- Google Gemini API

### Additional Libraries
- Pillow
- python-dotenv

---

# 📂 Project Structure

```
smart_event_planner/
│
├── accounts/
├── events/
├── media/
├── templates/
├── static/
├── smart_event_planner/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/smart-event-planner.git
cd smart-event-planner
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=True
```
Replace the values with your own credentials.

---

## 5. Apply Migrations

```bash
python manage.py migrate
```

---

## 6. Run the Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 🎯 Future Improvements

- Email Invitations
- Calendar Integration
- QR Code Event Tickets
- AI Budget Optimization
- AI Vendor Recommendations
- Notification System
- Analytics Dashboard
- Payment Integration

---

# 📦 Requirements

```
Django
python-dotenv
google-generativeai
Pillow
```

---

# 👨‍💻 Author

**Ahmad Arshad**

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub and feel free to contribute!