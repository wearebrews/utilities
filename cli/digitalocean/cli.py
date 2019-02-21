from digitalocean.get_kube_config import get_kube_config
import sys

def main(argv):
    if len(argv) <= 1:
        handle_invalid_input()
        sys.exit()

    cmd = argv[1]
    if cmd == "getkubeconfig":
        get_kube_config(argv[1:])

def handle_invalid_input():
    print("Invalid input")

if __name__ == "__main__":
    main(sys.argv)