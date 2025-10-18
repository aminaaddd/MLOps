<h1 align="center">Lab 1 — Testing & Version Control with Git</h1>

<p align="center">
  <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python%2B-blue" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/tests-passing-brightgreen" alt="Tests passing"></a>
  <a href="#"><img src="https://img.shields.io/badge/linter-flake8-blueviolet" alt="Linter status"></a>
</p>

<p align="center">
  <em>Python • Git • Pytest • Flake8 • Collaboration</em><br>
  <strong>MLOps | AIVANCITY 2025–2026</strong>
</p>

---

## Overview

This lab project was developed to practice **version control**, **branching**, and **testing** in a collaborative environment.  
It simulates a real-world Python project where two partners contribute to a shared calculator library.

---

## Features

✅ Arithmetic operations (`add`, `substract`, `multiply`, `divide`)  
✅ Input validation & error handling  
✅ Interactive command-line calculator  
✅ Unit and integration testing with `pytest`  
✅ Code linting with `flake8`  
✅ ≥ 90% test coverage  

---

##  Project Structure

```bash
Lab1/
├── src/
│   ├── __init__.py
│   ├── utils.py            # core functions
│   └── calculator.py       # CLI calculator using utils
│
├── tests/
│   ├── test_utils.py               # unit tests
│   └── test_calculator_integration.py  # integration tests
│
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions 
<h3 style="color:#999"> Clone the Repository</h3>
```bash
git clone https://github.com/aminaaddd/Testing_versionControl.git
cd Testing_versionControl/Lab1
```

<h3 style="color:#999"> Virtual Environment</h3>
```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

<h3 style="color:#999"> Install Dependencies</h3>
```bash
pip install -r requirements.txt
```

---


<h3 style="color:#999"> Run the calculator</h3>
```bash
python src/calculator.py     # or python3 src/calculator.py
```

---


<h3 style="color:#999"> Run all tests</h3>
```bash
pytest
```

---


<h3 style="color:#999"> Run the linter</h3>
```bash
flake8
```

---



