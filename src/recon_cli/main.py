from nmap_checker import check_nmap

def main():
    if not check_nmap():
        print("Exiting program.")
        return

    print("Starting scan assitant....")

if __name__ == "__main__":
    main()
