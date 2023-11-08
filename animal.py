import sys
def default():
    print("hello")
def main():
    if(sys.argv[1]=='hello'):
        pass
    else:
        default()
if __name__ == "__main__":
    main()
