import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# إعداد Flask
app = Flask(__name__)

# إعداد بيانات Twilio من المتغيرات البيئية
TWILIO_ACCOUNT_SID = os.getenv('ACCOUNT_SID', 'your_account_sid')
TWILIO_AUTH_TOKEN = os.getenv('AUTH_TOKEN', 'your_auth_token')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '+1234567890')

# عميل Twilio
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# نقطة النهاية لاستقبال الرسائل النصية
@app.route('/sms', methods=['POST'])
def sms_reply():
    """استقبال الرسائل النصية والرد عليها."""
    incoming_message = request.form.get('Body')  # محتوى الرسالة
    sender = request.form.get('From')  # رقم المرسل

    # معالجة الرسالة الواردة (هنا مجرد رد تلقائي)
    response_message = f"مرحبًا! تم استلام رسالتك: '{incoming_message}'. شكرًا لتواصلك معنا!"
    print(f"رسالة مستلمة من {sender}: {incoming_message}")

    # إنشاء رد باستخدام Twilio
    resp = MessagingResponse()
    resp.message(response_message)

    return str(resp)

# وظيفة لإرسال رسالة نصية
def send_sms(to_number, message_body):
    """إرسال رسالة نصية باستخدام Twilio."""
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print(f"تم إرسال الرسالة إلى {to_number} برقم تعريف: {message.sid}")
    except Exception as e:
        print(f"فشل إرسال الرسالة: {e}")

# نقطة البداية لتشغيل الخادم أو إرسال رسالة (اختياري)
if __name__ == '__main__':
    import argparse

    # إعداد خيارات التشغيل
    parser = argparse.ArgumentParser(description="نظام استلام وإرسال الرسائل النصية")
    parser.add_argument('--run-server', action='store_true', help='تشغيل الخادم لاستقبال الرسائل النصية')
    parser.add_argument('--send-sms', nargs=2, metavar=('TO', 'MESSAGE'),
                        help='إرسال رسالة نصية. أدخل الرقم والمحتوى.')

    args = parser.parse_args()

    if args.run_server:
        # تشغيل الخادم
        app.run(debug=True, host='0.0.0.0', port=5000)
    elif args.send_sms:
        # إرسال رسالة نصية
        to_number, message_body = args.send_sms
        send_sms(to_number, message_body)
    else:
        print("يرجى تحديد خيار تشغيل: --run-server أو --send-sms")
