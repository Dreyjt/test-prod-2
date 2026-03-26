def calculate_internal_metric(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return {"error": "Cannot divide by zero"}
