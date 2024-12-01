Here’s a **`README.md`** file for your project that you can upload to GitHub. It includes an overview, setup instructions, and other important details.

---

# Flask Google OIDC Authentication SPA

This project demonstrates a simple Single Page Application (SPA) built with Flask that integrates Google OAuth 2.0 for user authentication using OpenID Connect (OIDC). After a successful login, the app displays the authenticated user's name, email, and profile picture. The user can log out, and the session will not persist across logins.

---

## **Features**
- **Google Login**: Users can log in using their Google account via OIDC.
- **User Info Display**: Displays the user's name, email, and profile picture after login.
- **Session Management**: Ensures sessions are cleared after logout, requiring re-authentication.
- **Secure Configuration**: Includes best practices like cookie security and session expiration.

---

## **Technologies Used**
- **Flask**: A lightweight Python web framework.
- **Flask-OIDC**: For OpenID Connect integration with Google.
- **HTML/CSS**: For the frontend UI.
- **Google OAuth 2.0**: For authentication.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.7+ installed on your system.
- A Google Cloud project set up for OAuth 2.0. (See instructions below.)
- A virtual environment (optional but recommended).

---

### **2. Clone the Repository**
```bash
git clone https://github.com/yourusername/flask-google-oidc.git
cd flask-google-oidc
```

---

### **3. Set Up the Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### **5. Configure Google OAuth 2.0**
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Set up OAuth consent:
   - Navigate to **APIs & Services > OAuth consent screen**.
   - Configure the app name, support email, and authorized domain.
4. Create credentials:
   - Go to **APIs & Services > Credentials**.
   - Click **Create Credentials > OAuth Client ID**.
   - Choose "Web Application" and set the **Redirect URI** to:
     ```
     http://127.0.0.1:5000/oidc/callback
     ```
5. Download the JSON file for your credentials and save it as `client_secrets.json` in the root of your project directory.

---

### **6. Run the Application**
```bash
python app.py
```
Visit the app in your browser at `http://127.0.0.1:5000`.

---

### **7. Project Workflow**
1. Navigate to the login page.
2. Log in using your Google account.
3. View your name, email, and profile picture on the user information page.
4. Click "Logout" to clear the session and log out.

---

## **Folder Structure**
```
flask-google-oidc/
│
├── app.py                   # Main Flask application
├── client_secrets.json      # Google OAuth credentials (do not commit to GitHub!)
├── templates/
│   ├── login.html           # Login page template
│   └── user_info.html       # User information page template
├── static/
│   ├── styles.css           # CSS file for styling
├── requirements.txt         # Python dependencies               
```

---

## **Security Notes**
- **Environment Variables**: Avoid committing sensitive files like `client_secrets.json` to version control. Use environment variables to store secrets in production.
- **HTTPS**: Always use HTTPS in production to ensure secure communication.
