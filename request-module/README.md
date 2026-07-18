# 🌐 Python Requests Module Practice

This folder contains my practice programs while learning the **Python Requests module** and working with APIs.

The goal of this practice was to understand how Python communicates with servers, how APIs work, how to handle JSON responses, and how to build programs using real-world data.

---

## 📌 Topics Covered

- HTTP Request and Response
- Client-Server Communication
- HTTP Status Codes
- Python `requests` module
- GET Requests
- API Endpoints
- JSON Data Handling
- Converting JSON response into Python objects
- Accessing nested dictionaries and lists
- API Error Handling
- `response.raise_for_status()`
- Searching and filtering API data
- Working with user input

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- REST APIs
- JSON

---


## 🚀 Programs Included

### 01_status_code.py
- Sends a GET request to an API.
- Checks HTTP response status.

### 02_first_post_title.py
- Fetches posts using an API.
- Converts JSON response into Python data.
- Extracts post information.

### 03_fifth_user_details.py
- Accesses specific user data from API response.
- Practices list indexing and dictionary access.

### 04_all_user_names.py
- Uses loops to iterate through API data.
- Prints all user names.

### 05_users_company_r.py
- Filters users based on company name.
- Practices conditions with nested JSON data.

### 06_name_and_company.py
- Extracts and displays nested information.
- Works with dictionaries inside dictionaries.

### 07_search_user.py
- Takes username input from the user.
- Searches API data.
- Displays user details:
  - Name
  - Email
  - Company
  - City

---

## 🧠 Key Learnings

- APIs allow different applications to communicate with each other.
- `requests.get()` sends a GET request to a server.
- API responses are commonly returned in JSON format.
- `response.json()` converts JSON data into Python objects.
- Nested JSON requires understanding the structure before accessing data.
- Error handling is important while working with external services.
- Debugging errors improves problem-solving skills.

---

## 🔮 Future Improvements

- Add POST requests practice.
- Work with query parameters.
- Build real-world API projects.
- Add environment variables for API keys.
- Create GUI-based API applications.
