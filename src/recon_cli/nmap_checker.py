import shutil
import platform

def is_nmap_installed():
    return shutil.which("nmap") is not None

def check_nmap():
    if is_nmap_installed():
        print("Nmap is installed on your system and ready to use.")
        return True
    else:
        print("Nmap is not installed on your system.")
        
        os_name = platform.system()
        print("Install Instructions:\n")
        if os_name == "Linux":
            print("Debian/Ubuntu/Mint/PopOS! :")
            print("\t sudo apt install nmap")
        elif os_name == "Darwin":
            print("MacOS (Using Homebrew):")
            print("brew install nmap")
        elif os_name == "Windows":
            print("Windows")
            print("Download Nmap from \n https://nmap.org/download.html\n")
        return False

if __name__ == "__main__":
    check_nmap()
