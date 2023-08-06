import sys
from .slack import SlackClient

def success(cmd):
    client = SlackClient()
    client(f"[Success]\ncmd: {cmd} \nwhere: {client.server_id}")

def fail(cmd):
    client = SlackClient()
    client(f"[Fail]\ncmd: {cmd} \nwhere: {client.server_id}")

def run_slack(mode, cmd):
    MODE = {
    'success': success,
    'fail': fail
    }
    MODE[mode](cmd)

if __name__ == "__main__":
    mode = sys.argv[1]
    cmd = sys.argv[2]
    run_slack(mode, cmd)