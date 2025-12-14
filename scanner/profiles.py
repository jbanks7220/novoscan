# scanner/profiles.py

SCAN_PROFILES = {
    "quick": [
        21, 22, 23, 25, 53, 80, 110, 139, 143,
        443, 445, 3306, 3389, 5432, 8080, 27017
    ],

    "stealth": [
        22, 80, 443, 3389, 3306, 5432
    ],

    "full": list(range(1, 65536))
}
