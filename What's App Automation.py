# Step-1: Install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step-2: Twilio credentials
account_sid = 'AC7b3a89446e8357e24736f40f82b1b95d'
auth_token = 'ad87316044cd031f302405742ed59bd0'

client = Client(account_sid, auth_token)

# Step-3: Define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Step-4: User input 
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g., +12345): ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step-5: Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

# Combine and convert to datetime object
try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
except ValueError:
    print("Invalid date or time format. Please follow YYYY-MM-DD and HH:MM.")
    exit()

current_datetime = datetime.now()
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    # Wait until scheduled time
    time.sleep(delay_seconds)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)

