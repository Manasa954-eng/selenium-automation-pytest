# 🧪 Selenium Automation Framework (Python | Pytest | POM | Data-Driven)

## 📌 Project Overview
This project demonstrates my hands-on learning and implementation of a scalable Selenium automation framework using Python.

It started with a basic Selenium script, evolved into a Pytest-based structure, and is now enhanced with the Page Object Model (POM) design pattern for better maintainability, reusability, and scalability.

---

## 🚀 Key Highlights
- End-to-end UI automation using Selenium WebDriver
- Implementation of Page Object Model (POM)
- Data-driven testing using JSON inputs
- Structured test execution using Pytest
- Use of parameterization and assertions
- Real-world e-commerce workflow automation

---

## 🧠 Learning & Implementation Journey

### 🔹 Step 1: Basic Automation (`Project1.py`)
- Developed a basic Selenium script
- Automated login, product selection, and checkout flow
- Focused on understanding WebDriver interactions and locators

### 🔹 Step 2: Pytest Framework (`test_project1.py`)
- Refactored the same flow using Pytest
- Implemented:
  - `@pytest.mark.parametrize` for data-driven testing
  - Assertions for validation
- Improved test structure and readability

### 🔹 Step 3: Page Object Model (POM) (`POM_Project1/`)
- Separated page logic into individual classes
- Created reusable methods for each page
- Improved maintainability and scalability of test code
- Reduced code duplication

👉 This demonstrates progression from basic scripting → structured testing → scalable framework design.

---

## 🧪 Test Scenario
- Authenticate user with valid credentials
- Identify and select products priced at **$15.99**
- Add selected items to cart
- Validate that only the correct items are present in the cart
- Complete checkout process and verify order confirmation

---

## 🏗 Framework Design (POM)

- `LoginPage` → Handles login functionality  
- `ProductsPage` → Handles product selection  
- `CartPage` → Handles cart validation  
- `CheckoutPage` → Handles checkout process  

👉 Each page contains:
- Locators
- Actions (methods)
- Reusable logic

---

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- Pytest
- JSON (Test Data)

---

## 📂 Project Structure
Practice/
│
├── Project1.py # Basic Selenium script
├── test_project1.py # Pytest implementation
├── test_data.json # Test data (JSON)
├── conftest.py # Pytest fixtures
│
└── POM_Project1/
├── a_login_page.py
├── b_products.py
├── c_cart_page.py
├── d_checkout_page.py
└── test_project1_POM.py


---

## ▶️ How to Run

### 🔹 Install dependencies

pip install selenium pytest


### 🔹 Run all tests

pytest


### 🔹 Run POM test specifically

pytest POM_Project1/test_project1_POM.py


---

## 📈 Future Enhancements
- Add logging framework
- Integrate test reporting (Allure / HTML reports)
- Improve locator strategies (more robust selectors)
- Integrate CI/CD using GitHub Actions

---
## 💡 Note
This project reflects my practical learning and progression in automation testing, focusing on writing clean, maintainable, and scalable test frameworks using industry best practices.