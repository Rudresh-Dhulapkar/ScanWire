SCAN_TYPES = {
        "1": "Quick Scan",
        "2": "Full Port Scan",
        "3": "Service Scan",
        "4": "OS Detection"
        }

def get_target():
    target = input("Enter target (IP or Domain):")
    return target.strip()

def choose_scan_type():
    print("\nSelect scan Type: \n")

    for key, value in SCAN_TYPES.items():
        print(f"{key}. {value}")

    choice = input("\nEnter your choice (1-4): ").strip()
    return SCAN_TYPES.get(choice)
