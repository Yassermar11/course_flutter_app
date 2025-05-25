# 📚 Course Management App

A full-stack application for managing university courses, built with a Flutter frontend and a Flask backend.

## ✨ Features

- 📄 View a list of courses
- ➕ Add new courses
- ✏️ Edit existing courses
- ❌ Delete courses

## 🛠️ Tech Stack

- **Frontend:** Flutter (Dart)
- **Backend:** Flask (Python)
- **API Communication:** RESTful HTTP
- **State Management:** BLoC pattern (Flutter)

---

## 🚀 Getting Started

### ✅ Prerequisites

- [Flutter](https://flutter.dev/docs/get-started/install)
- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

---

### Backend Setup

1. 📂 Navigate to the backend folder:
    ```bash
    cd "Flask Backend"
    ```

2. 📦 Install dependencies:
    ```bash
    pip install flask flask-cors
    ```

3. ▶️ Run the Flask server:
    ```bash
    python server.py
    ```
    The backend will be available at `http://localhost:3400`.

---

### Frontend Setup (Another terminal)

1. 📂 Navigate to the Flutter app root:
    ```bash
    cd App
    ```

2. 📦 Get Flutter dependencies:
    ```bash
    flutter pub get
    ```

3. ▶️ Run the app:
    ```bash
    flutter run -d edge
    ```

---

## 🔗 API Endpoints

- `GET /courses` — 📄 List all courses
- `POST /courses` — ➕ Create a new course (fields: `title`, `code`, `description`, `ects`)
- `PUT /courses/<id>` — ✏️ Update a course by ID
- `DELETE /courses/<id>` — ❌ Delete a course by ID

---

## 📁 Folder Structure

```
/Flask Backend
    server.py         # Flask REST API

/App
    /lib
        ....          # Flutter app source code (BLoC, repository, UI screens, etc.)
```

---

## 📝 Notes

- 🧠 The backend uses in-memory storage; data will reset when the server restarts.
- 🔄 The frontend communicates with the backend using HTTP requests.

---

## 📈 Sequence Diagram

![1](https://github.com/user-attachments/assets/52cca669-9de8-4fee-b59f-f91b8da97736)


## 📲 Follow Me

<a href="https://linkedin.com/in/yasser-marzouhi-590a23260"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/960px-LinkedIn_logo_initials.png" width="30" height="30" alt="LinkedIn"></a>
<a href="https://github.com/Yassermar11"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="30" height="30" alt="GitHub"></a>
<a href="https://www.instagram.com/its_yasser_33/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png" width="30" height="30" alt="Instagram"></a>

### 📌 Made by Yasser Marzouhi  
