import json
from lxml import etree
from exporter.html_template import generate_html


def export_report(results, file_path):
    """
    Export NovoScan results to disk.
    Supported formats: json, md, html, xml
    """
    fmt = file_path.split(".")[-1].lower()

    if fmt == "json":
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

    elif fmt == "md":
        md = "# NovoScan Security Report\n\n"

        md += "## Vulnerabilities\n\n"
        for v in results.get("vulnerabilities", []):
            md += (
                f"### {v['name']}\n"
                f"- Severity: {v['severity']}\n"
                f"- Port: {v['port']}\n"
                f"- Service: {v['service']}\n"
                f"- Impact: {v['impact']}\n"
                f"- MITRE: {', '.join(v['mitre'])}\n\n"
            )

        md += "## Attack Chains\n\n"
        for c in results.get("attack_chains", []):
            md += (
                f"### {c['name']}\n"
                f"- Risk: {c['risk']}\n"
                f"- Description: {c['description']}\n\n"
            )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md)

    elif fmt == "html":
        html = generate_html(results)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

    elif fmt == "xml":
        root = etree.Element("novoscan")

        vulns = etree.SubElement(root, "vulnerabilities")
        for v in results.get("vulnerabilities", []):
            vuln_el = etree.SubElement(vulns, "vulnerability")
            for key, value in v.items():
                etree.SubElement(vuln_el, key).text = str(value)

        chains = etree.SubElement(root, "attack_chains")
        for c in results.get("attack_chains", []):
            chain_el = etree.SubElement(chains, "chain")
            for key, value in c.items():
                etree.SubElement(chain_el, key).text = str(value)

        tree = etree.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)

    else:
        raise ValueError(f"Unsupported export format: {fmt}")
