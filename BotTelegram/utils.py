from datetime import datetime
import logging as LOG
from operator import length_hint

LOG.basicConfig(filename="messages.log", level=LOG.INFO, encoding="utf_8", format='%(message)s')

def save_log(date, message, status, *args): # *args são argumentos opcionais

    log = [date, message]

    for argument in args: # Adicionando argumentos opcionais (caso existam) no array que será enviado para o log
        log.append(argument)

    if status == 200:
        LOG.info(f'{log}\n')
    else:
        LOG.info(f'ERROR:\n{log}\n')
