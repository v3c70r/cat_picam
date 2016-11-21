import itchat
import capture
import file_manager

cap = capture.Capturerer()
fm = file_manager.FileManager()

def send_image(receiver):
    file_name = cap.caputre_n_save_avec_timestamp()
    itchat.send_image(file_name, receiver)
def send_video(receiver):
    file_name = cap.capture_video_avec_timestamp(5)
    itchat.send('@fil@'+file_name, receiver)

def list_files(receiver):
    itchat.send(fm.list(), receiver)
def clean_files(receiver):
    itchat.send(fm.clear(), receiver)

dispatchers = {
        "Image": send_image,
        "Video": send_video,
        "ls": list_files,
        "rm": clean_files
        }
@itchat.msg_register('Text')
def text_reply(msg):
    if msg["Text"] in dispatchers.keys():
        dispatchers[msg["Text"]](msg['FromUserName'])
    if msg["Text"] in ["help", "Help", "?"]:
        return "\n".join(dispatchers.keys())

itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
