"""Main entry point for the application."""

import sys
from PySide6.QtWidgets import QApplication
from .ui.window import MainWindow


def main():
    """Main entry point."""
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

