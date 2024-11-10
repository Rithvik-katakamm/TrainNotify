import subprocess

def TrainNotify(phone_number, message_text):
    apple_script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message_text}" to targetBuddy
    end tell
    '''
    process = subprocess.Popen(['osascript', '-e', apple_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        print("Error:", stderr.decode())
    else:
        print("Message sent successfully!")


# Define the target phone number and message
phone_number = "+10000000000"
message_text = "Code done running!"

# Send the message
TrainNotify(phone_number, message_text)








