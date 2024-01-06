"""
complex_assignment_20:

Write A Python Program To Get Phone Number From User. And System Should Put a ‘-’ After Country And Area Code Automatically on Web

"""
def format_phone_number(phone_number):
    # Remove any existing hyphens
    phone_number = phone_number.replace("-", "")

    # Insert hyphens after country code and area code
    formatted_number = phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:]

    return formatted_number

# Get user input
phone_number = input("Enter a phone number: ") #+201054487964

# Format the phone number
formatted_number = format_phone_number(phone_number)

# Print the formatted phone number
print("Formatted phone number:", formatted_number) #+20-105-4487964