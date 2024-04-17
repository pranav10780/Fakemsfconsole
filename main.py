#!/data/data/com.termux/files/usr/bin/python

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
  print('Msome help to make it like the secondietasploit Documentation: https://docs.metasploit.com/')

banner()
from config import helper as hp
#takes input
while True:
  data = input('msf6>')

  #parsing/spliting
  parsed = data.split()
  if len(parsed) <= 0:
    pass
  elif parsed[0] == 'exit' :
    exit()
  elif parsed[0] == 'help' or parsed[0] == "?":
    if len(parsed) == 1:
      with open('config/help.txt','r') as f:
        helptext = f.read()
        print(helptext)
    elif len(parsed) == 2:
      hp.helper(parsed[1])
    else:
      print("Sorry too many arguments!")
  elif parsed[0] == "banner":
      banner()
  else:
    print(f'Unknown commnad {parsed[0]}')