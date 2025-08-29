# Community Skill Share Hub

A **Command Line Interface (CLI)** application where community members can share and book skills. Users can register, list their skills, browse available skills, and book sessions with other members.  

This project is built with **Python** and uses **SQLite (via SQLAlchemy)** for data persistence.  

---

## Features

-  **Manage Users**: Add, list, and view community members.  
-  **Manage Skills**: Add new skills to a user, view all available skills.  
- **Bookings**: Book a skill session with another user.  
-  **Delete Bookings**: Cancel a booking if needed.  
-  **View Bookings**: See which user booked which skill.  

---

## User Stories

1. As a user, I can **create an account** so I can join the hub.  
2. As a user, I can **add skills** I want to share.  
3. As a user, I can **browse other users' skills** to see what’s available.  
4. As a user, I can **book a skill session** from another member.  
5. As a user, I can **cancel my bookings** if I change my mind.  

---

## Project Structure

── Pipfile # dependencies
├── Pipfile.lock
├── README.md # project documentation
└── lib
├── cli.py # main CLI loop
├── helpers.py # helper functions (UI + logic)
├── debug.py # debug REPL entry point
└── models
├── init.py # database setup
├── user.py # User model
├── skill.py # Skill model
└── booking.py # Booking model

---

## Installation & Setup

1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd community-skillshare-hub
