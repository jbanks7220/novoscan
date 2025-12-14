import unittest
from scanner.safe_scan import run_safe_scan
from scanner.port_scanner import detect_services

class TestNovoScan(unittest.TestCase):

    def test_safe_scan_returns_list(self):
        results = run_safe_scan("127.0.0.1")
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)

    def test_detect_services(self):
        ports = [22, 80, 3306]
        services = detect_services(ports)
        self.assertEqual(services[22], "SSH")
        self.assertEqual(services[80], "HTTP")
        self.assertEqual(services[3306], "MySQL")

    def test_cvss_range(self):
        from utils.threat_rating import cvss
        scores = [cvss(sev) for sev in ["Low", "Medium", "High", "Critical"]]
        for s in scores:
            self.assertGreaterEqual(s, 0)
            self.assertLessEqual(s, 10)

if __name__ == "__main__":
    unittest.main()
