import cx_Freeze
exe = [cx_Freeze.Executable("jogo.py", icon = "assets/pikachu-icon.ico")]

cx_Freeze.setup(
    name="PyMon",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables = exe
)