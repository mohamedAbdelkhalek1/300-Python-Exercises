"""
complex_assignment_23:

Write A Python Program To Generate OTP On User Request And Send Code To Mobile Number

"""
import random
import requests

def generate_otp():
    # Generate a 6-digit OTP
    return random.randint(100000, 999999)

def send_otp(mobile_number, otp):
    # Replace 'YOUR_SMS_GATEWAY_API_KEY' with your actual API key
    api_key = 'YOUR_SMS_GATEWAY_API_KEY'
    # Replace 'YOUR_SMS_GATEWAY_URL' with the URL of your SMS gateway service
    url = 'YOUR_SMS_GATEWAY_URL'

    message = f'Your OTP is: {otp}'

    # Send the OTP via SMS
    response = requests.post(url, data={
        'apikey': api_key,
        'number': mobile_number,
        'message': message,
        'sender': 'MyApp'
    })

    if response.status_code == 200:
        print('OTP sent successfully!')
    else:
        print('Failed to send OTP!')

# Main program
def main():
    mobile_number = input('Enter your mobile number: ')
    otp = generate_otp()
    send_otp(mobile_number, otp)

if __name__ == '__main__':
    main()