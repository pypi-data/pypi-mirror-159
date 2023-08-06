from pathlib import Path
import os
from InquirerPy import prompt
import json
from shutil import copyfile
from .constant import ALERT2ME_CLI_PATH, CONFIGURE_PATH, CONFIGURE_QUESTIONS

FILE_PATH = Path(os.path.dirname(__file__))

def set_env():
    export_command = f'export PATH="$PATH:{str(ALERT2ME_CLI_PATH)}"'
    shell_type = os.getenv("SHELL").split("/")[-1]
    if shell_type in ["bash", "zsh"]:
        if shell_type == "bash":
            shell_config_path = f"{os.getenv('HOME')}/.bashrc"
        elif shell_type == "zsh":
            shell_config_path = f"{os.getenv('HOME')}/.zshrc"
        with open(shell_config_path, "a") as f:
            f.write(f"\n{export_command}")
    else:
        Warning(
            f'we cannot support your shell program, add "{export_command}" to your shell config file(ex. .bashrc, .zshrc)'
        )
    ALERT2ME_CLI_PATH.mkdir(exist_ok=True, parents=True)
    copyfile(
        FILE_PATH / "alme",
        ALERT2ME_CLI_PATH /"alme"
    )
    os.system(f'chmod 775 {ALERT2ME_CLI_PATH / "alme"}')

def set_configure():
    questions = CONFIGURE_QUESTIONS
    answers = prompt(questions)
    Path(CONFIGURE_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIGURE_PATH, "w") as f:
        json.dump(answers, f, indent=4, sort_keys=True)
    if os.system("which alme") != 0:
        set_env()
        
def get_configure():
    if not os.path.exists(CONFIGURE_PATH):
        os.system(f"alme-configure")
    with open(CONFIGURE_PATH) as f:
        credential = json.load(f)
    return credential