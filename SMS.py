from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_reply():
    # استلام الرسالة من الطلب
    incoming_message = request.form.get('Body')
    sender = request.form.get('From')

    # إنشاء رد على الرسالة
    resp = MessagingResponse()
    resp.message(f"تم استلام رسالتك: '{incoming_message}' من الرقم: {sender}")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
