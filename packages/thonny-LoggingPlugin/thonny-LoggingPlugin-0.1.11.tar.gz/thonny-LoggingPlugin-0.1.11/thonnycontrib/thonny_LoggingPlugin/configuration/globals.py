from thonny import THONNY_USER_DIR, get_workbench

#Default config
DEFAULT_PATH = THONNY_USER_DIR+"/LoggingPlugin/"
DEFAULT_SERVER = 'http://127.0.0.1:8000'
DEFAULT_STORE = True
DEFAULT_SEND = False
DEFAULT_LOG_IN_CONSOLE = False
#VERSION = "0.1.6"

TERMS_OF_USE = "Acceptez vous que les données utilisateur issues de thonny soient collectées à des fins de recherche\n Plus d'informations dans le menu tools --> LoggingPlugin"
URL_TERMS_OF_USE = "https://www.cristal.univ-lille.fr"

#Dict of options name and default value
OPTIONS = {
    "local_path" : DEFAULT_PATH,
    "server_address" : DEFAULT_SERVER,
    "store_logs" : DEFAULT_STORE,
    "log_in_console" : DEFAULT_LOG_IN_CONSOLE,
    "send_logs" : DEFAULT_SEND,
    "first_run" : True,
}

#Get the thonny workbench object
WB = get_workbench()