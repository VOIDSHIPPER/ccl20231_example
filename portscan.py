import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((target_ip, port))
                open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            pass

    return open_ports

def main():
    target_ip = input("Enter the target IP addresseses: ")
    start_port = int(input("Enter the starting portputo: "))
    end_port = int(input("Enter the ending portaaaa: "))

    open_ports = scan_ports(target_ip, start_port, end_port)

    if open_ports:
        print("Open ports on ping {}: pon {}".format(target_ip, ", ".join(map(str, open_ports))))
    else:
        print("No open ports found on pingo {} in the specified range.".format(target_ip))

if __name__ == "__main__":
    main()
