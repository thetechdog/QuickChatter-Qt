# This Python file uses the following encoding: utf-8
import sys
import huggingface_hub
from llama_cpp import Llama
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from PySide6.QtCore import Qt
from rivescript import RiveScript
global llm
print("QuickChatter - (C) 2024 Andrei Ionel")
print("Loading model... If not cached, it will take some time.")
llm = Llama.from_pretrained(
	repo_id="bartowski/SmolLM2-360M-Instruct-GGUF",
	filename="SmolLM2-360M-Instruct-Q5_K_L.gguf", n_ctx=8192
)


rs=RiveScript()
rs.load_directory("./rive")
rs.sort_replies()
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_QCWindow

class QCWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QCWindow()
        self.ui.setupUi(self)
        self.setFixedSize(902,654)
        self.ui.sendButton.clicked.connect(self.pushSend)
        self.ui.methodBox.currentIndexChanged.connect(self.methodChanged)
        self.conv_history = [
            {"role": "system", "content": "You are a polite assistant that helps the user no matter the request. Your name is Chatty. You end your messages with the \0 character."}
        ]
    def pushSend(self):
        if(self.ui.methodBox.currentText()=="RiveScript"):
            self.pushSendRive()
        else:
            text=self.ui.lineEdit.text()
            self.ui.convoBox.appendPlainText("You: "+text)
            self.ui.lineEdit.clear()
            self.ui.sendButton.setEnabled(False)
            self.conv_history.append({"role": "user", "content": text})
            
            output = llm.create_chat_completion(
                messages=self.conv_history,
                temperature=0.50,
                max_tokens=768,
                stop=["Q:", "\0"],
            )
            print(output)
            response=output['choices'][0]['message']['content']
            
            self.ui.convoBox.appendPlainText("Bot: "+response)
            self.conv_history.append({"role": "assistant", "content": response})
            self.ui.sendButton.setEnabled(True)
            

    def methodChanged(self):
        self.ui.convoBox.clear()
        QMessageBox.information(self, "Changed method", "Method changed to " + self.ui.methodBox.currentText())
        self.conv_history = [
            {"role": "system", "content": "You are a polite assistant that helps the user no matter the request. Your name is Chatty. You end your messages with the \0 character."}
        ] #reset LLM conv 
    
    def pushSendRive(self):
        text=self.ui.lineEdit.text()
        self.ui.convoBox.appendPlainText("You: "+text)
        self.ui.lineEdit.clear()
        self.ui.sendButton.setEnabled(False)
        response=rs.reply("user",text)
        self.ui.convoBox.appendPlainText("Bot: "+response)
        self.ui.sendButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QCWindow()
    widget.show()
    sys.exit(app.exec())
