import subprocess

def signMessageTron(hash):

    output = subprocess.check_output(['node', 'sign_message_tron.js', hash])

    signature = output.decode().strip()
    
    return signature