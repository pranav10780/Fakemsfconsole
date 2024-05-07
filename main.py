#logo part
def banner():
  print('WARNING: Nokogiri was built against libxml version 2.11.5, but has dynamically loaded 2.12.4')
  print('WARNING: Nokogiri was built against libxslt version 1.1.38, but has dynamically loaded 1.1.39')
  print('Metasploit tip: Search can apply complex filters such as search cve:2009')
  print('type:exploit, see all the filters with help search')
  print('')
  print('               .;lxO0KXXXK0Oxl:.')
  print('           ,o0WMMMMMMMMMMMMMMMMMMKd,')
  print('         NMMMMMMMMMMMMMMMMMMMMMMMMMWx,')
  print('      :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:')
  print('    .KMMMMMMMMMMMMMMMWNNNWMMMMMMMMMMMMMMMX,')
  print('   lWMMMMMMMMMMMXd:..     ..;dKMMMMMMMMMMMMo')
  print('  xMMMMMMMMMMWd.               .oNMMMMMMMMMMk')
  print(' oMMMMMMMMMMx.                    dMMMMMMMMMMx')
  print('.WMMMMMMMMM:                       :MMMMMMMMMM,')
  print('xMMMMMMMMMo                         lMMMMMMMMMO')
  print('NMMMMMMMMW                    ,cccccoMMMMMMMMMWlccccc;')
  print('MMMMMMMMMX                     ;KMMMMMMMMMMMMMMMMMMX:')
  print('NMMMMMMMMW.                      ;KMMMMMMMMMMMMMMX:')
  print('xMMMMMMMMMd                        ,0MMMMMMMMMMK;')
  print('.WMMMMMMMMMc                         \'OMMMMMM0,')
  print(' lMMMMMMMMMMk.                         .kMMO')
  print('  dMMMMMMMMMMWd\'                         ..')
  print('   cWMMMMMMMMMMMNxc\'.                ##########')
  print('    .0MMMMMMMMMMMMMMMMWc            #+#    #+#')
  print('      ;0MMMMMMMMMMMMMMMo.          +:+')
  print('        .dNMMMMMMMMMMMMo          +#++:++#+')
  print('           \'oOWMMMMMMMMo                +:+')
  print('               .,cdkO0K;        :+:    :+:                 ')
  print('                                :::::::+:')
  print('                      Metasploit')
  print('')
  print('       =[ metasploit v6.3.37-dev-92867ce                  ]')
  print('+ -- --=[ 2363 exploits - 1228 auxiliary - 413 post       ]')
  print('+ -- --=[ 1388 payloads - 46 encoders - 11 nops           ]')
  print('+ -- --=[ 9 evasion                                       ]')
  print()

version = 1.8

def showhistory() -> None:
  j = 1
  for i in history:
    print(f"{j}: {i}")
    j+=1

def save() -> None:
    with open("./config/saved/saved.txt","w") as f:
        for i in history:
            f.write(i+"\n")

def showSaved() -> None:
    with open("./config/saved/saved.txt","r") as f:
        con = f.read()
        print("\n"+con)

from config import helper as hp
import subprocess
import sys
history = []

#parse -h and stuff
try:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        with open('config/help.txt','r') as f:
            helptext = f.read()
            print(helptext)
            exit()
    elif sys.argv[1] == "-v" or sys.argv[1] == '--version':
        print(f"Version == {version}")
        exit()
    else:
        print("Usage: python main.py [options]")
        print("Available options: -h,-v,--help,--version")
        exit()
except IndexError as e: pass

#takes input
banner()
try:
    while True:
        data = input('msf6>')
        history.append(data)
        parsed = data.split()

        if len(parsed) <= 0:
            pass
        elif parsed[0] == 'exit':
            exit()
        elif parsed[0] == 'help' or parsed[0] == "?":
            if len(parsed) == 1:
                with open('config/help.txt', 'r') as f:
                    helptext = f.read()
                    print(helptext)
            elif len(parsed) == 2:
                data = hp.helper(parsed[1])
                print(data)
            else:
                print("\nSorry too many arguments!\n")
        elif parsed[0] == "banner":
            banner()
        elif parsed[0] == "connectivity":
            # ping google.com
            command = ['ping', '-c', '1', 'google.com']
            pinged = subprocess.call(command)
            if pinged == 0:
                print("\nInternet access is available\n")
            else:
                print("\nNo internet access\n")
        elif parsed[0] == "version":
            print(f"\nFakemsfconsole version : {version}\n")
        elif parsed[0] == "history":
            showhistory()
        elif parsed[0] == "save":
            save()
            print("Successfully saved")
        elif parsed[0] == "showsaved":
            showSaved()
            print("End of saved history")
        else:
            print(f'\nUnknown commnad {parsed[0]}\n')
except EOFError as e: print("\nBye bye")
except KeyboardInterrupt as e: print("\nBye bye")
