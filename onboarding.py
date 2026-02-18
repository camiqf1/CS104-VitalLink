import json
import os

FILE_NAME = "user_information.json"

def get_user_info():

    name = input("\nEnter your name: ")
    number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    reason = input("Reason for joining the network: ")

    return {
        "name": name,
        "number": number,
        "address": address,
        "reason": reason
    }

def save_info(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def load_info():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def main():
    print("\n-----------------------------------------------"
          "\n    VitalLink Healthcare Network Onboarding"
          "\n-----------------------------------------------\n")

    if os.path.exists(FILE_NAME):
        user_data = load_info()
        print("Welcome back,", user_data["name"] + "!"
              "\n\nYour current information:"
              f"\n- Name: {user_data['name']}"
              f"\n- Phone Number: {user_data['number']}"
              f"\n- Address: {user_data['address']}"
              f"\n- Reason for Joining: {user_data['reason']}")
        
        choice = input("\nWould you like to update your information? (yes/no): ").lower().strip()

        if choice == "yes":
            user_data = get_user_info()
            save_info(user_data)
            print("\n✅ Information updated successfully.\n")
        else:
            user_data = load_info()
            print("\nThank you for choosing VitalLink!\n")
    else:
        print("Thank you for joining the VitalLink Healthcare Network!\n"
          "To get started, please provide the following information:")
        user_data = get_user_info()
        save_info(user_data)
        print("\n✅ Registration complete. Welcome to VitalLink, {}!\n".format(user_data["name"]))

if __name__ == "__main__":
    main()
