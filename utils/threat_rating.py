def calculate_cvss(severity):
    return {
        "Low": 3.1,
        "Medium": 5.6,
        "High": 8.2,
        "Critical": 9.8
    }.get(severity, 0.0)
