from nmap_checker import check_nmap
from ui import get_target, choose_scan_type

def main():
    if not check_nmap():
        print("Exiting program.")
        return

    target = get_target()
    scan_choice = choose_scan_type()

    print("\nTarget: ", target)
    print("Scan type: ", scan_choice)

if __name__ == "__main__":
    main()
