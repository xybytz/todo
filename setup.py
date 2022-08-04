from setuptools import setup

NAME = "todo"
VERSION = "0.4"

plist = {
    "CFBundleIconFile": NAME,
    "CFBundleName": NAME,
    "CFBundleShortVersionString": VERSION,
    "CFBundleGetInfoString": " ".join([NAME, VERSION]),
    "CFBundleExecutable": NAME,
}

setup(
   
    app=["main.py"],
    setup_requires=["py2app"],
    options={
        "py2app": {
            "arch": "x86_64",
        }
    },
)
