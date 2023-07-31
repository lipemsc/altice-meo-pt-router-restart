import sys
from telnetlib import Telnet

def reboot(host: str, username: str, password: str):
    print("{0} {1} {2}".format(host, username, password))
    with Telnet(host, 23) as tn:
        tn.read_until(b'Login: ')
        tn.write(username.encode() + b'\n')
        tn.read_until(b"Password: ")
        tn.write(password.encode() + b"\n")
        tn.read_until(b"> ")
        tn.write(b"management/reboot \n")
        tn.read_until(b"] ")
        tn.write(b"Y\n")
        tn.read_all()


if __name__ == "__main__":
    try:
        reboot(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print("Error: Missing arguments")