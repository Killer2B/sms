from twilio.rest import Client

# بيانات Twilio
account_sid = 'ACCOUNT_SID'  # استبدل بـ SID الخاص بك
auth_token = 'AUTH_TOKEN'    # استبدل بالتوكن الخاص بك
client = Client(account_sid, auth_token)

# إرسال رسالة
message = client.messages.create(
    body="مرحبًا، هذه رسالة تجريبية!",
    from_='+1234567890',  # رقم Twilio الخاص بك
    to='+0987654321'      # رقم المستلم
)

print(f"تم إرسال الرسالة برقم تعريف: {message.sid}")
