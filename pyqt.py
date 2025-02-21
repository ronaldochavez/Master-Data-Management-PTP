from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QTextBrowser, QSplitter, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
import sys
import os
import markdown

class MarkdownViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Documentación Markdown")
        self.resize(1000, 600)
        self.initUI()
        self.loadMarkdownFiles()

    def initUI(self):
        # Create a splitter (Left = Menu | Right = Content)
        self.splitter = QSplitter(Qt.Horizontal, self)

        # Left panel: List of markdown files
        self.listWidget = QListWidget()
        self.listWidget.clicked.connect(self.onListItemClicked)

        # Right panel: Markdown Viewer (QTextBrowser)
        self.contentWidget = QWidget()
        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(5, 5, 5, 5)

        # Markdown Display
        self.textBrowser = QTextBrowser()  # <-- Add back QTextBrowser
        self.contentLayout.addWidget(self.textBrowser)

        # Add widgets to the splitter
        self.splitter.addWidget(self.listWidget)
        self.splitter.addWidget(self.contentWidget)
        self.splitter.setStretchFactor(1, 1)

        self.setCentralWidget(self.splitter)

    def loadMarkdownFiles(self):
        self.markdown_files = ["index.md", "materiales.md", "proveedores.md"]

        for file in self.markdown_files:
            if not os.path.exists(file):
                with open(file, "w", encoding="utf-8") as f:
                    f.write(f"# {file.split('.')[0].capitalize()}\n\n"
                            f"Este es un contenido de ejemplo en **Markdown** para {file}.\n\n")

        self.listWidget.addItems(self.markdown_files)

    def onListItemClicked(self, index):
        file_name = self.listWidget.currentItem().text()
        file_path = os.path.abspath(file_name)

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                md_text = f.read()

            # Convert Markdown to HTML
            html_content = markdown.markdown(md_text)

            # Load Markdown into QTextBrowser
            self.textBrowser.setHtml(html_content)  # <-- Fixing the AttributeError

            print("Markdown Loaded Successfully!")  # Debugging
        else:
            print(f"File NOT found: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MarkdownViewer()
    window.show()
    sys.exit(app.exec_())
