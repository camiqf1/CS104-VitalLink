# VitalLink Healthcare Network Onboarding

## Overview
`onboarding.py` is a simple onboarding script for new members of the VitalLink Healthcare Network. The script collects user information, stores it locally, and allows users to update their details.

## Features
- Collects user information: name, phone number, address, and reason for joining.
- Saves information to a local JSON file (`user_information.json`).
- Allows returning users to review and update their information.

## Usage
1. **Run the script:**
   ```bash
   python onboarding.py
   ```
2. **Follow the prompts:**
   - Enter your name, phone number, address, and reason for joining.
   - If you have previously registered, your information will be loaded and you can choose to update it.

## File Details
- `onboarding.py`: Main onboarding script.
- `user_information.json`: Stores user information locally (created after running the script).

## Requirements
- Python

## Example Output
```
-----------------------------------------------
    VitalLink Healthcare Network Onboarding
-----------------------------------------------

Enter your name: John Doe
Enter your phone number: 555-1234
Enter your address: 123 Main St
Reason for joining the network: Improve healthcare access

✅ Registration complete. Welcome to VitalLink, John Doe!
```

## License
This project is for educational purposes.
