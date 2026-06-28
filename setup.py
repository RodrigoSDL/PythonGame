from cx_Freeze import Executable, setup

build_exe_options = {
    "packages": ["pygame"],
    "include_files": [
        ("asset", "asset")
    ]
}
executables = [Executable('main.py')]

setup(
    name='Python Game',
    version='1.0',
    description='Mountain Shooter App',
    options={'build_exe': build_exe_options},
    executables=executables
)