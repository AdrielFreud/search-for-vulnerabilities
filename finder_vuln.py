#  Desenvolvido por Adriel Freud!
#  Contato: businessc0rp2k17@gmail.com 
#  FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=

import requests
import json, sys, os

menu = """
 _____                     _     _____           _       _ _   
/  ___|                   | |   |  ___|         | |     (_) |  
\ `--.  ___  __ _ _ __ ___| |__ | |____  ___ __ | | ___  _| |_ 
 `--. \/ _ \/ _` | '__/ __| '_ \|  __\ \/ / '_ \| |/ _ \| | __|
/\__/ /  __/ (_| | | | (__| | | | |___>  <| |_) | | (_) | | |_ 
\____/ \___|\__,_|_|  \___|_| |_\____/_/\_\ .__/|_|\___/|_|\__|
                                          | |                  
                                          |_|                  

[Modo De Uso];
root@localhost~# python finder_vuln.py "Joomla Exploit" 2008
or
root@localhost~# python finder_vuln.py "Joomla Exploit" 2010 dump_vulns.txt

Powered By Adriel Freud...\n\n"""

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

def run_process(nome_vuln, data, menu, nome_arquivo):
	url = "http://www.exploitalert.com/api/search-exploit?name={0}".format(nome_vuln)
	print(menu)
	r = requests.get(url, headers=header)
	if r.status_code == 200:
		html = r.text
		loads = json.loads(html)
		a = open(nome_arquivo, 'w')
		print("[!] Gerando arquivo!")
		for load in loads:
			try:
				if data:
					if data in load['date']:
						a.write("="*50)
						a.write('')
						a.write("\nData: %s\nID: %s\nNome: %s\n"%(load['id'], load['date'], load['name']))
						a.write('')
					else:
						pass
				else:
					a.write("="*50)
					a.write('')
					a.write("\nData: %s\nID: %s\nNome: %s\n"%(load['id'], load['date'], load['name']))
					a.write('')
			except:
				pass
	print('[+] Arquivo gerado: %s'%os.getcwd()+'\\'+nome_arquivo)
	a.close()

if len(sys.argv) < 2:
	print(menu)
	sys.exit(0)
else:
	nome_vulnerabilidade = sys.argv[1]
	data = sys.argv[2]
	nome_file = sys.argv[3]
	run_process(nome_vulnerabilidade, data, menu, nome_file)




		