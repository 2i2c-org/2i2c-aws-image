import nox

nox.options.reuse_existing_virtualenvs = True

input_folder = ["./handbook"]
output_folder = [f"{input_folder[0]}/_build/html"]

@nox.session(venv_backend="venv")
def build(session):
    session.install("-r", "./images/handbook-authoring-image/requirements.txt")
    if session.posargs:
        input_folder = session.posargs
    else:
        input_folder = ["./handbook"]
    session.run("jupyter-book", "config", "sphinx", *input_folder)        
    session.run("jupyter-book", "build", *input_folder)

@nox.session(venv_backend="venv")
def preview(session):
    session.install("-r", "./images/handbook-authoring-image/requirements.txt")
    if session.posargs:
        input_folder = session.posargs
    else:
        input_folder = ["./handbook"]
    output_folder = [f"{input_folder[0]}/_build/html"]
    session.run("jupyter-book", "config", "sphinx", *input_folder)
    AUTOBUILD_IGNORE = [
        "_build",
        "build_assets",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend([*input_folder, *output_folder])
    session.run(*cmd)
