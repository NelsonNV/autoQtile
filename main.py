#librerias
import os, time


class clColor():
    def red():
        pass


mensaje = """
╔═══╗███╔╗███╔═══╗╔╗█╔╗████
║╔═╗║██╔╝╚╗██║╔═╗╠╝╚╗║║████
║║█║╠╗╔╬╗╔╬══╣║█║╠╗╔╬╣║╔══╗
║╚═╝║║║║║║║╔╗║║█║║║║╠╣║║║═╣
║╔═╗║╚╝║║╚╣╚╝║╚═╝║║╚╣║╚╣║═╣
╚╝█╚╩══╝╚═╩══╩══╗║╚═╩╩═╩══╝
████████████████╚╝█████████

"""

def menu():
 
    print(mensaje)

    time.sleep(0.3)
    print("1 -> Instalar Requerimientos")
    time.sleep(0.3)
    print("\n2 -> Instalar Qtile")
    time.sleep(0.3)
    print("\n3 -> instalar configuracion ranger, zsh y neovim")
    time.sleep(0.3)
    print("\n4 -> All In One")
    time.sleep(0.3)
    print("\n0 -> Salir")
    time.sleep(0.3)

    option = input("\n-->> ")

    if option == "1":
        fnRequisitos()
    if option == "2":
        fnQtile()
    if option == "3":
        fnPrograma()
    if option == "4":
        fnRequisitos()
        fnQtile()
        fnPrograma()
    if option == "0":
        print('Adios')
        exit()



def fnInsAPT(paque:str) -> None:
    """instalador de paquetes utilizando apt

    Args:
        paque (str): nombre de los paquetes que se desea instalar
    """
    fnShell(f'sudo apt install {paque} -y')
    time.sleep(1)

def fnShell(comando:str) -> None:
    """ejecutador de comandos en la shell

    Args:
        comando (str): comando o intrucciones a ejecutar en la shell
    """
    os.system(comando)
    time.sleep(1)

def fnRequisitos():
    """instalador de paquetes y dependencias necesarias para el entorno qtile"""
    fnShell('sudo apt update -y')
    fnInsAPT('xorg python3-xcffib python3-pip python3-cairocffi libcairo2 lightdm python3-psutil python3-pip wget kmix picom zsh bat neofetch')
    fnShell('sudo pip3 install qtile pillow')

def fnQtile():
    """instalardor de el tema del enterno de qtile"""
    # copiar configuracion
    fnShell('cp -r ./tools/qtile ~/.config/')
    fnShell('sudo cp ./tools/qtile-venv.desktop /usr/share/xsessions/')

def fnPrograma():
    fnShell('cp -r ./tools/nvim ~/config/')
    fnShell('cp -r ./tools/ranger ~/config/')
    # ejecutar ajusto de ranger
    fnShell('~/.config/ranger/install-plugs.sh')
    # configuracon powerlevel10k
    fnShell('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k')
    fnShell('echo "source ~/.powerlevel10k/powerlevel10k.zsh-theme" >> ~/.zshrc')
    # zsh plugins clonar
    fnShell('git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions')
    fnShell('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting')
    fnShell('git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git ~/.zsh/zsh-autocomplete')
    # zsh add plugins
    fnShell('echo "#################### PLUGINS ZSH ################### " >> ~/.zshrc')
    fnShell('echo "source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc')
    fnShell('echo "source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc')
    fnShell('echo "source ~/.zsh/zsh-autocomplete/zsh-autocomplete.plugin.zsh" >> ~/.zshrc')
    # descargar .deb
    fnShell('wget https://github.com/Peltoche/lsd/releases/download/0.23.1/lsd_0.23.1_amd64.deb -P ./tools/deb')
    fnShell('wget https://gitlab.com/volian/volian-archive/uploads/d6b3a118de5384a0be2462905f7e4301/volian-archive-nala_0.1.0_all.deb -P ./tools/deb')
    fnShell('wget https://gitlab.com/volian/volian-archive/uploads/b20bd8237a9b20f5a82f461ed0704ad4/volian-archive-keyring_0.1.0_all.deb -P ./tools/deb')
    #install deb
    fnInsAPT('./tools/deb/*.deb')
    fnInsAPT('nala')
    
    fnShell('echo "#################### ALIAS ################### " >> ~/.zshrc')
    fnShell('curl file:$(pwd)/tools/alias.txt >> ~/.zshrc')

    # configurande neofecht
    fnShell(" mkdir -p ~/.config/neofetch")
    fnShell(" curl https://raw.githubusercontent.com/mmsaeed509/neofetch-themes/main/normal/ozozPredatorFetch.conf >> ~/.config/neofetch/config.conf")


menu()