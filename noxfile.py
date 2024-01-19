import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["./handbook"]

@nox.session
def handbook(session): 
    session.install("-r", "./images/handbook-authoring-image/requirements.txt")
    if "live" in session.posargs:
        session.run("jupyter-book", "config", "sphinx", "./handbook")
        AUTOBUILD_IGNORE = [
            "_build",
            "build_assets",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])
        cmd.extend(build_command)
        session.run(*cmd, "./handbook/_build/html")
    else:
        session.run("jupyter-book", "build", *build_command)
