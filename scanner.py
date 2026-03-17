import socket
import threading

def scanner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    val = s.connect_ex((host, port))

    if (val == 0):
        try:
            service = socket.getservbyport(port)
            print(f"Port open: {port} | {service}")
        except Exception:
            print(f"Port open: {port} | Service unknown")
    s.close()

def get_input(prompt: str, type):
    while True:
        try:
            return type(input(f"{prompt}"))
        except ValueError:
            print("Invalid input, please enter a number")

if __name__ == "__main__":
    timeout = get_input("Enter scanner timeout length: ", float)

    socket.setdefaulttimeout(timeout)

    start = get_input("Enter start of port range: ", int)
    end = get_input("Enter end of port range: ", int)

    while True:
        try:  
            host = input("Enter host IP address: ")
            socket.inet_aton(host)
            break
        except OSError:
            print("Invalid IP Address")

    print(f"\nStarting scan from ports {start} - {end} on host {host}")
    print(f"Timeout length is {timeout} seconds\n")

    threads = []
    for port in range(start, end + 1):
        t = threading.Thread(target=scanner, args=(host, port))
        threads.append(t)
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()