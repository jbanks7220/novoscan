def generate_html(results):
    rows = ""
    for r in results:
        rows += f"""
        <tr>
            <td>{r['name']}</td>
            <td>{r['severity']}</td>
            <td>{r['cvss']}</td>
            <td>{r['owasp']}</td>
        </tr>
        """

    return f"""
    <html>
    <body style="background:#0b0b0d;color:#e6e6eb">
    <h1>NovoScan Report</h1>
    <table border="1">{rows}</table>
    </body>
    </html>
    """
