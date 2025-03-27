from typing import List, Dict
import os
from dotenv import load_dotenv


load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Database Configuration
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Channel Configuration
DB_CHANNEL_ID = int(os.getenv("DB_CHANNEL_ID"))
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL"))

# Bot Information
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_NAME = os.getenv("BOT_NAME")
BOT_VERSION = "1.4"
# Privacy Mode Configuration
PRIVACY_MODE = os.getenv("PRIVACY_MODE", "off").lower() == "on"

# Your Modiji Url Api Key Here
MODIJI_API_KEY = os.getenv("MODIJI_API_KEY")
if not MODIJI_API_KEY:
    print("⚠️ Warning: MODIJI_API_KEY not set in environment variables")

# Links
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
DEVELOPER_LINK = os.getenv("DEVELOPER_LINK")
SUPPORT_LINK = os.getenv("SUPPORT_LINK")

# For Koyeb/render 
WEB_SERVER = bool(os.getenv("WEB_SERVER", True)) # make it True if deploying on koyeb/render else False
PING_URL = os.getenv("PING_URL") # add your koyeb/render's public url
PING_TIME = int(os.getenv("PING_TIME")) # Add time_out in seconds

# Admin IDs - Convert space-separated string to list of integers
ADMIN_IDS: List[int] = [
    int(admin_id.strip())
    for admin_id in os.getenv("ADMIN_IDS", "").split()
    if admin_id.strip().isdigit()
]

# File size limit (2GB in bytes)
MAX_FILE_SIZE = 2000 * 1024 * 1024

# Supported file types and extensions
SUPPORTED_TYPES = [
    "document",
    "video",
    "audio",
    "photo",
    "voice",
    "video_note",
    "animation"
]

SUPPORTED_EXTENSIONS = [
    # Documents
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    # Programming Files
    "py", "js", "html", "css", "json", "xml", "yaml", "yml",
    # Archives
    "zip", "rar", "7z", "tar", "gz", "bz2",
    # Media Files
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov",
    "webm", "3gp", "m4v", "ogg", "opus",
    # Images
    "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico",
    # Applications
    "apk", "exe", "msi", "deb", "rpm",
    # Other
    "txt", "text", "log", "csv", "md", "srt", "sub"
]

SUPPORTED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip",
    "application/x-rar-compressed",
    "application/x-7z-compressed",
    "video/mp4",
    "audio/mpeg",
    "audio/mp4",
    "image/jpeg",
    "image/png",
    "image/gif",
    "application/vnd.android.package-archive",
    "application/x-executable",
]

class Messages:
    START_TEXT = """
**🔥 Welcome to {bot_name}! 🔥**

Hey {user_mention}, you've entered the world of HUNTERX NETWORK! 🚀

**⚡ Power. Speed. Precision.

🔹 Seamless File Sharing
🔹 Exclusive Access
🔹 Built for the Elite

🎯 Stay Ahead – Join the Community:
📢 @HUNTERX_NETWORK

💬 Need Support? Contact @WizardBillu**

⚔ Type /help to begin your journey!
"""

    HELP_TEXT = """
📚 COMMAND PANEL

👤 User Commands:
🚀 `/start` – Activate the bot
ℹ️ `/help` – Display this menu
🔍 `/about` – Learn about the bot
✂️ `/short` [url] – Shorten links (e.g., /short example.com)

👑 Admin Commands:
📤 `/upload` – Upload files (reply to a file)
📊 `/stats` – View bot performance
📢 `/broadcast` – Message all users
⏳ `/auto_del` – Set auto-delete timer

🗑 Auto-Delete System:
⚡ Files auto-delete after the set time.
⚙️ Adjust with `/auto_del`.

🔗 Batch System:
📦 `/batch` – Combine multiple files into one link.
📩 Forward files & reply with `/batch`.

💬 Need Assistance? Contact @WizardBillu
"""

    ABOUT_TEXT = """
**ℹ️ About {bot_name}**

🔹 Version: {version}
🔹 Developer: WizardBillu
🔹 Language: Python 🐍
🔹 Framework: Pyrogram ⚡

**🚀 What Makes {bot_name} Powerful?**
✅ Seamless File Sharing
✅ Force Subscription System
✅ Advanced Admin Controls
✅ Real-Time Analytics
✅ Multi-Format Support
✅ Enhanced Security & Speed
✅ Smart File Type Detection

📢 Stay Updated: @X0557
🛠 Support & Queries: @WizardBillu

**🔥 Crafted with Passion by @WizardBillu ❤️**
"""

    FILE_TEXT = """
**📁 FILE INFORMATION**

🔹 Name: {file_name}
📦 Size: {file_size}
📂 Type: {file_type}
📥 Downloads: {downloads}
🕒 Uploaded: {upload_time}
👤 By: {uploader}

🔗 Share Link:
{share_link}

**🚀 Fast | Secure | Reliable**
"""

    FORCE_SUB_TEXT = """
**⚠️ Access Denied! ⚠️**

🔒 To use this bot, you must join our official channel.

🚀 Join Now: @X0557

🔹 Click the button below and try again!
"""

class Buttons:
    def start_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Help 📚", "callback_data": "help"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK},
                {"text": "Developer 👨‍💻", "url": DEVELOPER_LINK}
            ]
        ]

    def help_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def about_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "Help 📚", "callback_data": "help"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def file_buttons(file_uuid: str) -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Download 📥", "callback_data": f"download_{file_uuid}"},
                {"text": "Share 🔗", "callback_data": f"share_{file_uuid}"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]


class Progress:
    PROGRESS_BAR = "█"
    EMPTY_PROGRESS_BAR = "░"
    PROGRESS_TEXT = """
**{0}** {1}% 

**⚡️ Speed:** {2}/s
**💫 Done:** {3}
**💭 Total:** {4}
**⏰ Time Left:** {5}
"""
