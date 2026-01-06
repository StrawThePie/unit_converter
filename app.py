from flask import Flask, render_template, request

# Conversion factors relative to meters
LENGTH_FACTORS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}

# Conversion factors relative to grams
WEIGHT_FACTORS = {
    'milligram': 0.001,
    'gram': 1,
    'kilogram': 1000,
    'ounce': 28.3495,
    'pound': 453.592
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    length_result = None
    weight_result = None
    temperature_result = None

    if request.method == 'POST':
        converter = request.form.get('converter')
        value = request.form.get('value', type=float)
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')

        if converter == 'length' and from_unit in LENGTH_FACTORS and to_unit in LENGTH_FACTORS:
            meters = value * LENGTH_FACTORS[from_unit]
            length_result = round(meters / LENGTH_FACTORS[to_unit], 5)

        elif converter == 'weight' and from_unit in WEIGHT_FACTORS and to_unit in WEIGHT_FACTORS:
            grams = value * WEIGHT_FACTORS[from_unit]
            weight_result = round(grams / WEIGHT_FACTORS[to_unit], 5)

        elif converter == 'temperature':
            if from_unit == to_unit:
                temperature_result = value
            elif from_unit == 'celsius':
                if to_unit == 'fahrenheit':
                    temperature_result = value * 9 / 5 + 32
                elif to_unit == 'kelvin':
                    temperature_result = value + 273.15
            elif from_unit == 'fahrenheit':
                if to_unit == 'celsius':
                    temperature_result = (value - 32) * 5 / 9
                elif to_unit == 'kelvin':
                    temperature_result = (value - 32) * 5 / 9 + 273.15
            elif from_unit == 'kelvin':
                if to_unit == 'celsius':
                    temperature_result = value - 273.15
                elif to_unit == 'fahrenheit':
                    temperature_result = (value - 273.15) * 9 / 5 + 32
            if temperature_result is not None:
                temperature_result = round(temperature_result, 2)

    return render_template(
        'combined.html',
        length_result=length_result,
        weight_result=weight_result,
        temperature_result=temperature_result
    )

@app.route('/length', methods=['GET', 'POST'])
def length():
    converted_value = None
    error = None

    if request.method == 'POST':
        value_raw = request.form.get('value')
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')

        try:
            value = float(value_raw)
        except (TypeError, ValueError):
            value = None

        if value is None:
            error = "Please enter a valid numeric value."
        elif from_unit not in LENGTH_FACTORS or to_unit not in LENGTH_FACTORS:
            error = "Please select valid units for conversion."
        else:
            meters = value * LENGTH_FACTORS[from_unit]
            converted_value = round(meters / LENGTH_FACTORS[to_unit], 5)

    return render_template('length.html',
                           converted_value=converted_value,
                           error=error)


@app.route('/weight', methods=['GET', 'POST'])
def weight():
    converted_value = None
    error = None

    if request.method == 'POST':
        value_raw = request.form.get('value')
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')

        try:
            value = float(value_raw)
        except (TypeError, ValueError):
            value = None

        if value is None:
            error = "Please enter a valid numeric value."
        elif from_unit not in WEIGHT_FACTORS or to_unit not in WEIGHT_FACTORS:
            error = "Please select valid units for conversion."
        else:
            grams = value * WEIGHT_FACTORS[from_unit]
            converted_value = round(grams / WEIGHT_FACTORS[to_unit], 5)

    return render_template('weight.html',
                           converted_value=converted_value,
                           error=error)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    converted_value = None
    error = None

    if request.method == 'POST':
        value_raw = request.form.get('value')
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')

        # Try to parse the numeric value
        try:
            value = float(value_raw)
        except (TypeError, ValueError):
            value = None

        # Basic validation
        valid_units = ('celsius', 'fahrenheit', 'kelvin')

        if value is None:
            error = "Please enter a valid numeric value."
        elif from_unit not in valid_units or to_unit not in valid_units:
            error = "Please select valid temperature units."
        else:
            # Conversion logic
            if from_unit == to_unit:
                converted_value = value
            elif from_unit == 'celsius' and to_unit == 'fahrenheit':
                converted_value = value * 9 / 5 + 32
            elif from_unit == 'celsius' and to_unit == 'kelvin':
                converted_value = value + 273.15
            elif from_unit == 'fahrenheit' and to_unit == 'celsius':
                converted_value = (value - 32) * 5 / 9
            elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
                converted_value = (value - 32) * 5 / 9 + 273.15
            elif from_unit == 'kelvin' and to_unit == 'celsius':
                converted_value = value - 273.15
            elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
                converted_value = (value - 273.15) * 9 / 5 + 32
            else:
                # Fallback in case a new unit combination slips through
                error = "Unsupported temperature conversion."

            if converted_value is not None and error is None:
                converted_value = round(converted_value, 2)

    return render_template(
        'temperature.html',
        converted_value=converted_value,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)
