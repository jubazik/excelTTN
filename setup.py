from setuptools import setup, find_packages
import sys

# Для создания исполняемых файлов
if sys.platform == "win32":
    import py2exe
elif sys.platform == "darwin":
    import py2app

setup(
    name="ttn-generator",
    version="1.0.0",
    author="Your Company",
    author_email="info@yourcompany.com",
    description="Генератор ТТН накладных для распределения цемента",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'openpyxl>=3.1.2',
    ],
    entry_points={
        'console_scripts': [
            'ttn-generator=main:main',
        ],
    },
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'includes': ['openpyxl', 'tkinter'],
            'excludes': ['tkinter.test'],
        },
        'py2app': {
            'argv_emulation': True,
            'packages': ['openpyxl', 'tkinter'],
            'iconfile': 'icon.icns' if sys.platform == "darwin" else None,
        }
    },
    windows=[{
        'script': 'src/gui.py',
        'dest_base': 'TTN_Generator',
        'icon_resources': [(1, 'icon.ico')] if sys.platform == "win32" else None,
    }] if sys.platform == "win32" else None,
    app=['src/gui.py'] if sys.platform == "darwin" else None,
    data_files=[
        ('import', ['import/ttnweight0.xlsx']),
        ('export', [])
    ],
    python_requires='>=3.6',
)