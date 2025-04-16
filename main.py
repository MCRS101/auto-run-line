import os
import requests
from datetime import datetime

schedule = {
    "Monday": ["08:00 - คณิต", "10:00 - วิทย์"],
    "Tuesday": ["09:00 - อังกฤษ", "11:00 - ประวัติศาสตร์"],
    "Wednesday": ["08:00 - ฟิสิกส์", "13:00 - เคมี"],
    "Thursday": ["10:00 - ชีวะ", "14:00 - ศิลปะ"],
    "Friday": ["09:00 - ภาษาไทย", "11:00 - พลศึกษา"],
}

LINE_ACCESS_TOKEN = os.environ.get("LINE_ACCESS_TOKEN")

def get_today_schedule():
    today = datetime.now().strftime("%A")
    lessons = schedule.get(today, ["ไม่มีเรียนวันนี้ 🎉"])
    return f"📚 ตารางเรียนวัน{today}:\n" + "\n".join(lessons)

def broadcast_message(message):
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [{
            "type": "text",
            "text": message
        }]
    }
    response = requests.post("https://api.line.me/v2/bot/message/broadcast", headers=headers, json=data)
    print("ส่งข้อความสำเร็จ" if response.status_code == 200 else f"เกิดข้อผิดพลาด: {response.text}")

if __name__ == "__main__":
    msg = get_today_schedule()
    broadcast_message(msg)
