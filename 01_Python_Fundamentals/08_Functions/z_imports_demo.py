# Demo program to practice importing

def main():
    message = input("Enter message: ")
    convert_to_lower(message)
    covert_to_upper(message)

def convert_to_lower(text):
    print(text.lower())

def covert_to_upper(text):
    print(text.upper())

if __name__ == "__main__":
    main()