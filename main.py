from os import environ as env
import requests
import socket


config = {
    "webhook": "",
    "webhook_name": "NoRepls",
    "webhook_title": "NoRepls Notification",
    "webhook_avatar": "f",
    "webhook_description": "We Hate Replit!",
}


class NoRepls:
    def __init__(this):
        this._session = requests.Session()
        this._os = socket.gethostname()
        this._adr = socket.gethostbyname(this._os)
        this._slug = env["REPL_SLUG"]
        this._repl_own = env["REPL_OWNER"]
        this._repl_id = env["REPL_ID"]
        this._payload = {
            "username": config["webhook_name"],
            "avatar_url": config["webhook_avatar"],
            "content": f"New `Replit` Run:\n* OS: {this._os}\n* Replit IP: {this._adr}\n* Repl Slug/Name: {this._slug}\n* Repl ID: {this._repl_id}\n* Repl Owner: {this._repl_own}",
            "embeds": [
                {
                    "title": config["webhook_title"],
                    "description": config["webhook_description"],
                    "color": 880808,
                }
            ],
        }

    def notify(this):
        try:
            this._session.post(config["webhook"], json=this._payload)
        except:
            pass


class ScanForRepl:
    def __init__(this):
        this._os = socket.gethostname()
        this._adr = socket.gethostbyname(this._os)

    def scan(this):
        if this._adr.startswith("172.31.128"):
            NoRepls().notify()
            quit()

        if "REPL_ID" or "REPL_SLUG" in env:
            NoRepls().notify()
            quit()


while True:
    # jus to see if the code ends or not.
    print(ScanForRepl().scan())
