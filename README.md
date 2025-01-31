# HNG12 Stage 0 Backend Task – Public API  

Welcome to the **HNG12 Stage 0 Backend Task**! This project is a simple public API that returns basic information such as the developer's registered email, the current datetime, and the GitHub repository URL.

## 📝 Project Description  

This API provides the following JSON response:  

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Ecode2/hng_12_stage_0"
}
```

It is built using **Django REST Framework (DRF)** with the following features:  
- **CORS Handling** using `django-cors-headers`
- **Environment Variables** using `python-dotenv`
- **APIView** from DRF to handle requests  
- **Deployed to a publicly accessible endpoint**

---

## 🛠️ Tech Stack  

- **Backend:** Django with Django REST Framework (DRF)  
- **Environment Configuration:** `python-dotenv`  
- **CORS Management:** `django-cors-headers`  
- **Version Control:** Git & GitHub  
- **Deployment:** Hosted on Render

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/Ecode2/hng_12_stage_0.git
cd hng_12_stage_0
```

### 2️⃣ Create a Virtual Environment  

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies  

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  

Create a **.env** file in the project root and add the following:  

```
EMAIL=your-email@example.com
GITHUB_URL=https://github.com/Ecode2/hng_12_stage_0
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,hng-12-stage-0-9sef.onrender.com
```

---

## 📡 Running the Project  

### 1️⃣ Apply Migrations  

```bash
python manage.py migrate
```

### 2️⃣ Start the Development Server  

```bash
python manage.py runserver
```

The API will be available at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📌 API Documentation  

### **Endpoint:**  

`GET /api/info/`  

### **Response Format:**  

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Ecode2/hng_12_stage_0"
}
```

### Example Usage  

#### **cURL Request**  

```bash
curl -X GET [https://hng-12-stage-0-9sef.onrender.com/api/info/](https://hng-12-stage-0-9sef.onrender.com/api/info/)
```

#### **Python (requests module)**  

```python
import requests

response = requests.get("https://hng-12-stage-0-9sef.onrender.com/api/info/")
print(response.json())
```
