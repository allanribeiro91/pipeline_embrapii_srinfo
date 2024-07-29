import os
from urllib.parse import quote
import webbrowser
from time import sleep
from datetime import datetime
import pyautogui
from dotenv import load_dotenv

load_dotenv()
ROOT = os.getenv('ROOT')
PATH_SETA_ENVIAR_GRUPO = os.path.abspath(os.path.join(ROOT, 'scripts_public', 'seta_enviar_grupo.png'))
PATH_SETA = os.path.abspath(os.path.join(ROOT, 'scripts_public', 'seta.png'))
PATH_NOME_GRUPO = os.path.abspath(os.path.join(ROOT, 'scripts_public', 'nome_grupo.png'))

def enviar_whatsapp(mensagem):
    try:
        # whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        grupo = 'GED Embrapii'
        whatsapp = f'https://web.whatsapp.com/send?text={quote(mensagem)}&app_absent=0&selectedContactName={quote(grupo)}'
        webbrowser.open(whatsapp)
        sleep(50)
        
        #selecionar o grupo
        pyautogui.typewrite(grupo)
        sleep(2)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

        #enviar a mensagem
        sleep(2)
        pyautogui.press('enter')
        sleep(10)

        #fechar
        pyautogui.hotkey('ctrl', 'f4')
    except:
        print('Não foi possível enviar a mensagem.')
