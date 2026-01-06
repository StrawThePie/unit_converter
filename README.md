# Unit Converter (Flask)

A simple Flask web application for converting between common **length**, **weight**, and **temperature** units.  
The app provides separate pages for each category as well as an all‑in‑one converter page.

Created for https://roadmap.sh/projects/unit-converter

---

## Features

- Length conversions  
  - Millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
- Weight conversions  
  - Milligram, gram, kilogram, ounce, pound.
- Temperature conversions  
  - Celsius, Fahrenheit, Kelvin.
- Individual converter pages and a combined converter page.
- Clean, consistent UI built with HTML and CSS.

---

## Tech Stack

- Python  
- Flask (routing and templates)  
- Jinja2 (HTML templating)  
- HTML & CSS (frontend)

---

## Project Structure

```text
unit_converter/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── home.html
    ├── combined.html
    ├── length.html
    ├── weight.html
    └── temperature.html
```

___

## Getting Started

1. Clone the repository:
    ```text
    git clone <https://github.com/StrawThePie/unit_converter>
    cd unit_converter
    ```
   
2. (Optional) Create and activate a virtual environment:
    ```text
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS / Linux
    source .venv/bin/activate
    ```
3. Install dependencies:
    ```text
    pip install flask
    ```

4. Run application:
    ```text
    python app.py
    ```
   
5. Open the app in your browser:
    ```text
    http://127.0.0.1:5000/
    ```

Use the navigation links or "Return Home" buttons to move between:

- ```/length```
- ```/weight```
- ```/temperature```
- ```/convert``` (all-in-one converter)

___
