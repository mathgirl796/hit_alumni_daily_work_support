import webbrowser
import design
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from functools import partial
import sys
from re import split

def go(ui):
    text = ui.plainTextEdit.toPlainText()
    raw = split(r' |,|;|，|；|：|\t|\n|\|', text)
    urls = [a.strip() for a in raw if a.strip().startswith('http')]
    for url in urls:
        webbrowser.open(url)

def search(ui):
    texts = ui.plainTextEdit.toPlainText().splitlines()
    for text in texts:
        if text.strip() == '':
            continue
        url = f'https://cn.bing.com/search?q={text}'
        webbrowser.open(url)
    

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui_MainWindow = design.Ui_MainWindow()
    ui_MainWindow.setupUi(MainWindow)

    ui_MainWindow.data = {}
    ui_MainWindow.pushButton.clicked.connect(partial(go, ui_MainWindow))
    ui_MainWindow.searchButton.clicked.connect(partial(search, ui_MainWindow))

    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()