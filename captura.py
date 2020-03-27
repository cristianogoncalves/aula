import pyautogui
import datetime
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--nome", required=True,
	help="Informe o nome da aula")
args = vars(ap.parse_args())


agora = datetime.datetime.now()
#pyautogui.screenshot(region=(0,0, 1920, 1080), 'imagem.png')
arquivo = r'.\Imagens\{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}_{}.png'.format(agora.year, agora.month, agora.day, agora.hour, agora.minute, agora.second,args["nome"])
pyautogui.screenshot(arquivo)

os.system("python scan.py -i {}".format(arquivo))