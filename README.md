# SauceDemo QA Automation (Python + Selenium + Pytest + POM)

![pytest](https://github.com/LeenaBGit/saucedemo_pom_pytest/actions/workflows/pytest.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

This project automates key user flows on [SauceDemo](https://www.saucedemo.com) using:

- ✅ Python
- ✅ Selenium WebDriver
- ✅ Pytest for running test suites
- ✅ Page Object Model (POM) for test structure


## Project Structure
saucedemo_pom_pytest/
├── pages/ # Page Object classes
│ ├── login_page.py
│ └── inventory_page.py
│
├── tests/ # Test files using pytest
│ ├── test_login.py
│ └── test_cart.py
│
├── conftest.py # Pytest fixtures (e.g., driver setup)


## How to Run Tests

```bash
# Run all tests
PYTHONPATH=. pytest tests/

# Run a specific test file
PYTHONPATH=. pytest tests/test_cart.py


