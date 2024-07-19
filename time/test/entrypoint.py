import sys

sys.path.append('/Users/aditya.unal/Presentation/time')

from know_time import knowtime


def main():
    server_url = input("Enter the server URL (or press Enter for default http://time-server:8000/time): ")
    if not server_url:
        server_url = "http://time-server:8000/time"

    api_token = input("Enter the API token: ")
    while not api_token:
        print("API token cannot be empty.")
        api_token = input("Enter the API token: ")

    print(f"Attempting to get time from: {server_url}")

    result = knowtime(api_token, server_url)

    if "error" in result:
        print(f"Error occurred: {result['error']}")
    else:
        print(f"Current time: {result['current_time']}")


if __name__ == "__main__":
    main()
