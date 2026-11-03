# Arquivo de exemplo contendo más práticas propositais para demonstrar a auditoria do Morvat

import subprocess

API_KEY = "sk-live-9876543210fedcba-hardcoded-secret"
COUNTER = 0


def process_user_data(data, cmd):
    global COUNTER
    COUNTER += 1
    try:
        # Execução insegura e uso de eval
        result = eval(data)
        subprocess.Popen(cmd, shell=True)
        return result
    except:
        pass
