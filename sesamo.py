#!/usr/bin/env python3

import os, sys, time, configparser, getpass

# ConfigParser configurate
home = os.environ['HOME']
config = configparser.ConfigParser()
config.read('%s/.config/sesamo/sesamo.ini' % home)

# Global variables
version = config.get('SESAMO', 'version')
username = config.get('AHGORA', 'user')
hostname = config.get('AHGORA', 'host')

# Functions
def verify_user():
    user = getpass.getuser()

    if user == 'root':
        print("Você está acessando com o usuário %s. Favor acessar com seu usuário." % user)
        sys.exit(3)
    else:
        pass

def bro():
    os.system("ssh %s@bro.%s" % (username, hostname))

def bro2():
    os.system('ssh %s@bro2.%s' % (username, hostname))

def bro3():
    os.system('ssh %s@bro3.%s' % (username, hostname))

def bro4():
    os.system('ssh %s@bro4.%s' % (username, hostname))

def bro5():
    os.system('ssh %s@bro5.%s' % (username, hostname))

def mapa():
    vpn = config.get('MAPA', 'dns')
    user_mapa = config.get('MAPA', 'user_mapa')
    host_mapa = config.get('MAPA', 'host_mapa')
    is_connected = os.system('ifconfig %s > /dev/null 2>&1' % vpn)

    if is_connected == 0:
        os.system('ssh %s@%s' % (user_mapa, host_mapa))
    else:
        print("VPN não está conectada ou houve alteração na configração. Favor verificar e tente novamente!")
        sys.exit(2)

def deploy():
    os.system('ssh %s@deploy.%s' % (username, hostname))

def arb():
    os.system('ssh %s@arb.%s' % (username, hostname))

def depen():
    user_depen = config.get('DEPEN', 'usr_depen')
    pass_depen = config.get('DEPEN', 'passwd')

    os.system("rdesktop -g 1500x1024 -k pt-br  -u %s -p '%s' ec2-54-207-50-146.sa-east-1.compute.amazonaws.com" % (user_depen, pass_depen))

def qst():
    os.system('ssh %s@qst.%s' % (username, hostname))

def bastion():
    user_bast = config.get('BASTION', 'usr_bastion')
    host_bast = config.get('BASTION', 'host_bastion')

    os.system('ssh %s@%s' % (user_bast, host_bast))

def config_server():
    os.system('ssh %s@config.%s' % (username, hostname))

def config_server2():
    os.system('ssh %s@config2.%s' % (username, hostname))

def aws():
    host_aws = config.get('BASTION_AWS', 'host_aws')
    os.system('ssh -A %s@%s' % (username, host_aws))

# Front function
def menu():
    print('########################################')
    print('#         Sésamo Version: %s        #' % version)
    print('########################################')
    print('#         Servers Disponíveis          #')
    print('########################################')
    print('#            1 - Bro                   #')
    print('#            2 - Bro2                  #')
    print('#            3 - Bro3                  #')
    print('#            4 - Bro4                  #')
    print('#            5 - Bro5                  #')
    print('#            6 - Mapa                  #')
    print('#            7 - Deploy (Gitlab)       #')
    print('#            8 - Arb (Gitlab)          #')
    print('#            9 - Depen                 #')
    print('#            10 - Qst                  #')
    print('#            11 - Bastion (OC)         #')
    print('#            12 - Config               #')
    print('#            13 - Config2              #')
    print('#            14 - Bastion (AWS)        #')
    print('#            0 - Sair                  #')
    print('########################################')
    print('#        Mantenedor: Peronium          #')
    print('########################################')

# Main function - C Like :)
def main():
    verify_user()

    menu()

    opt = input("Opção desejada: ")

    if opt == '1':
        bro()
    elif opt == '2':
        bro2()
    elif opt == '3':
        bro3()
    elif opt == '4':
        bro4()
    elif opt == '5':
        bro5()
    elif opt == '6':
        mapa()
    elif opt == '7':
        deploy()
    elif opt == '8':
        arb()
    elif opt == '9':
        depen()
    elif opt == '10':
        qst()
    elif opt == '11':
        bastion()
    elif opt == '12':
        config_server()
    elif opt == '13':
        config_server2()
    elif opt == '14':
        aws()
    elif opt == '0':
        print('Bye!')
        sys.exit(0)
    else:
        os.system('clear')
        print("Opção inválida. Tente novamente!")
        main()

if __name__ == '__main__':
    try:
        main()
    except(Exception):
        print('')
        print('Bye!')
        sys.exit(0)
    except(KeyboardInterrupt):
        print('')
        print('Você executou um comando inválido. Sésamo fechando!')
        time.sleep(1)
        sys.exit(1)
