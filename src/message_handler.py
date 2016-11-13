# Embedded file name: /home/pi/project/catFood/src/message_handler.py
import capture as _capture
import itchat

class MessageHandler:

    def __init__(self):
        self._cap = _capture.Capturerer()
        self._login()

    def _login(self):
        itchat.auto_login(enableCmdQR=2, hotReload=True)

    @itchat.msg_register('Text')
    def _handle_message(self, msg):
        if u'food' in msg['Text'] or u'cat' in msg['Text']:
            pic_file = self._cap.caputre_n_save_avec_timestamp()
            itchat.send('@img@' + pic_file, msg['FromUserName'])
        else:
            return 'Nothing to do'

    def run(self):
        itchat.run()