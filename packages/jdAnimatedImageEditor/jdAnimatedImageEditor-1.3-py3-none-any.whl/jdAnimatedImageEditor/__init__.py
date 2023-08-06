from PyQt6.QtCore import QTranslator, QLocale, QLibraryInfo
from PyQt6.QtWidgets import QApplication
from .MainWindow import MainWindow
from .Environment import Environment
import PIL.Image
import sys
import os


def main():
    app = QApplication(sys.argv)

    env = Environment()

    app.setDesktopFileName("com.gitlab.JakobDev.jdAnimatedImageEditor")
    app.setApplicationName("jdAnimatedImageEditor")
    app.setWindowIcon(env.icon)

    app_translator = QTranslator()
    qt_translator = QTranslator()
    app_trans_dir = os.path.join(env.program_dir, "translations")
    qt_trans_dir = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    language = env.settings.get("language")
    if language == "default":
        system_language = QLocale.system().name()
        app_translator.load(os.path.join(app_trans_dir, "jdAnimatedImageEditor_" + system_language.split("_")[0] + ".qm"))
        app_translator.load(os.path.join(app_trans_dir, "jdAnimatedImageEditor_" + system_language + ".qm"))
        qt_translator.load(os.path.join(qt_trans_dir, "qt_" + system_language.split("_")[0] + ".qm"))
        qt_translator.load(os.path.join(qt_trans_dir, "qt_" + system_language + ".qm"))
    else:
        app_translator.load(os.path.join(app_trans_dir, "jdAnimatedImageEditor_" + language + ".qm"))
        qt_translator.load(os.path.join(qt_trans_dir, "qt_" + language.split("_")[0] + ".qm"))
        qt_translator.load(os.path.join(qt_trans_dir, "qt_" + language + ".qm"))
    app.installTranslator(app_translator)
    app.installTranslator(qt_translator)

    PIL.Image.preinit()

    w = MainWindow(env)
    w.show()

    if env.args.path:
        w.open_file(env.args.path)

    sys.exit(app.exec())
