#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST MODULE
"""

import os, app, pprint
from termcolor import colored

def main():
    app.utils.helpers.logger.Log.info(app.env.APP_NAME+' (DEBUG) started, PID='+str(os.getpid()))
    if (not app.env.APP_DEBUG):
        print(colored("La modalità di APP_DEBUG non è attiva. Per debug approfondito, modificarla in 'app/env.py'.\n", 'red'))
    #Settings.main()
    #env()
    #log()
    #storage()
    #test_flow()
    #flag_regex()
    #pcap()
    #request()
    #gui()
    #Crypto.main()
    html_parsing()
    exit(0)

def html_parsing():
    print(colored("\nCHECK HTML PARSING:", 'yellow'))
    url_with_form_1 = 'https://www.fabriserver.party/login'
    url_with_form_2 = 'https://www.fabriserver.party/register'
    url_docker = 'http://172.17.0.2/'
    url_router = 'http://192.168.1.1/main.cgi?page=login.html'
    url_libero = 'https://login.libero.it/'
    url_relativeuniverse = 'https://www.relativeuniverse.net/'
    url_oleificio = 'https://dev.oleificiotulipano.com/products'
    url_cloudflare = 'https://dash.cloudflare.com/login'
    url_genndi = 'https://account.genndi.com/login'
    url_spectra = 'https://my.spectra.co/'
    url_myspace = 'https://myspace.com/'
    print("HTM (relevant):")
    result = app.utils.html.relevant_parse(url_myspace)
    app.utils.html.print_parsed(result)
    print("HTML (FORMS):")
    forms = app.utils.html.find_forms(result)
    app.utils.html.print_parsed(forms)
    #print("HTML (INPUTS):")
    #inputs = app.utils.html.find_inputs(result)
    #app.utils.html.print_parsed(inputs)


class Crypto:
    @staticmethod
    def main():
        print(colored("\nCHECK CRYPTO:", 'yellow'))
        strings = ['123 PROVA pRoVa','user','admin','Admin','website', 'password', 'Password']
        def test(string):
            print('')
            encrypted = Crypto.md5encrypt(string)
            decrypted = Crypto.md5decrypt(encrypted)
            print('')
            encoded = Crypto.b64encode(string)
            decoded = Crypto.b64decode(encoded)
        for string in strings: test(string)

    @staticmethod
    def md5encrypt(string):
        result = app.utils.crypto.md5.encrypt(string)
        print('md5encrypt('+string+'): ' + str(result))
        return result
    @staticmethod
    def md5decrypt(string):
        result = app.utils.crypto.md5.decrypt(string)
        print('md5decrypt('+string+'): ' + str(result))
        return result

    @staticmethod
    def b64encode(string):
        result = app.utils.crypto.base64.encrypt(string)
        print('b64encode('+string+'): ' + str(result))
        return result
    @staticmethod
    def b64decode(string):
        result = app.utils.crypto.base64.decrypt(string)
        print('b64decode('+string+'): ' + str(result))
        return result


def gui():
    app.gui.main.open()

def pcap():
    print(colored("\nCHECK PCAP:", 'yellow'))
    def pcap_callback(pkt_dict):
        pprint.pprint(pkt_dict)
        return
    test_pcap = app.env.APP_STORAGE+'/network_dump.pcap'
    test_pcap2 = app.env.APP_STORAGE+'/ironx_dump.pcap'
    test_pcap_out = app.env.APP_STORAGE_OUT+'/network_dump_out.pcap'
    filter1='http'
    filter2='udp.port eq 53 or tcp.port eq 53'
    filter3='tcp.port eq 25 or icmp'
    filter4='http and ip.addr==217.182.10.133'
    filter5='tcp.port eq 443 or udp.port eq 443'
    filter6='http.request.uri matches "www.beniculturali.it"'
    app.utils.sniffing.sniff_pcap(src_file=None, dest_file=test_pcap_out, filter=filter1, limit_length=10000, callback=pcap_callback)


def test_flow():
    print(colored("\nCHECK FLOW:", 'yellow'))
    # Setto il mio IP
    print(str(app.utils.settings.Set.my_ip('192.168.1.12')))
    # Setto l'interfaccia d'ascolto
    print(str(app.utils.settings.Set.my_interface('eth0')))
    # Svuoto la lista dei server da attaccare
    print(str(app.utils.settings.Remove.server_to_attack()))
    # Aggiungo io da attaccare
    print(str(app.utils.settings.Add.server_to_attack('192.168.1.1')))
    print(str(app.utils.settings.Add.server_to_attack('192.168.1.5')))
    print(str(app.utils.settings.Add.server_to_attack('192.168.1.7')))
    print(str(app.utils.settings.Add.server_to_attack('192.168.1.11')))
    print(str(app.utils.settings.Add.server_to_attack('192.168.1.13')))


def request():
    print(colored("\nCHECK REQUESTS:", 'yellow'))
    team_token = app.utils.settings.Get.team_token()
    stolen_flag = 'QWERTYUIOPASDFGHJKLZXCVBNM01234='
    data = {
        'team_token': team_token,
        'flag': stolen_flag,
    }
    # Funzione per il mapping (da <ip> a http://<ip>:80)
    def to_http(ip): return 'http://'+str(ip)+':80/'
    # Lista server da attaccare
    server_to_attack = app.utils.settings.Get.server_to_attack()
    # Creo lista del tipo http://<ip_da_attaccare>
    urls = list(map(to_http, server_to_attack))
    app.utils.requests.multi_request(urls, app.utils.requests.Type.GET, data)


def flag_regex():
    print(colored("\nCHECK FLAG REGEX:", 'yellow'))
    stolen_flag = 'QWERTYUIOPASDFGHJKLZXCVBNM01234='
    print("app.utils.helpers.util.regex_in_string(): " + str(app.utils.helpers.util.regex_in_string(app.env.FLAG_REGEX, stolen_flag)))
    print("app.utils.helpers.util.replace_regex(): " + str(app.utils.helpers.util.replace_regex(app.env.FLAG_REGEX, 'TEST', stolen_flag)))


class Settings:
    @staticmethod
    def main():
        print(colored("\nCHECK SETTINGS:", 'yellow'))
        Settings.imports()
        Settings.set()
        Settings.add()
        Settings.get()
        Settings.remove()

    @staticmethod
    def imports():
        print("app.utils.settings: " + str(dir(app.utils.settings)))
        print("app.utils.settings.Get: " + str(dir(app.utils.settings.Get)))
        print("app.utils.settings.Set: " + str(dir(app.utils.settings.Set)))

    @staticmethod
    def set():
        print("app.utils.settings.Set.my_ip()")
        print(str(app.utils.settings.Set.my_ip('127.0.0.1')))
        print("app.utils.settings.Set.game_server()")
        print(str(app.utils.settings.Set.game_server('192.168.1.1')))

    @staticmethod
    def get():
        print("app.utils.settings.Get.my_ip()")
        print(str(app.utils.settings.Get.my_ip()))
        print("app.utils.settings.Get.server_to_attack()")
        print(str(app.utils.settings.Get.server_to_attack()))
        print("app.utils.settings.Get.all()")
        print(str(app.utils.settings.Get.all()))

    @staticmethod
    def add():
        print("app.utils.settings.Add.server_to_attack()")
        print(str(app.utils.settings.Add.server_to_attack('8.8.8.8')))
        print(str(app.utils.settings.Add.server_to_attack('8.8.4.4')))
        print("app.utils.settings.Add.server_to_defend()")
        print(str(app.utils.settings.Add.server_to_defend('192.168.1.50')))
        print(str(app.utils.settings.Add.server_to_defend('192.168.1.51')))
        print("app.utils.settings.Add.team_player()")
        print(str(app.utils.settings.Add.team_player('192.168.1.155')))
        print(str(app.utils.settings.Add.team_player('192.168.1.78')))

    @staticmethod
    def remove():
        print("app.utils.settings.Remove.server_to_attack()")
        print(str(app.utils.settings.Remove.server_to_attack('8.8.8.8')))
        print("app.utils.settings.Remove.team_player()")
        print(str(app.utils.settings.Remove.team_player('192.168.1.78')))








def imports():
    # Check imports
    print(colored("\nCHECK IMPORTS:", 'yellow'))
    print("app: " + str(dir(app)))
    print("app.env: " + str(dir(app.env)))
    print("app.utils: " + str(dir(app.utils)))
    print("app.utils.helpers: " + str(dir(app.utils.helpers)))
    print("app.utils.helpers.logger: " + str(dir(app.utils.helpers.logger)))

def env():
    print(colored("\nCHECK ENVIRONMENTS:", 'yellow'))
    print("app.env.APP_DEBUG: " + str(app.env.APP_DEBUG))
    print("app.env.APP_PATH: " + str(app.env.APP_PATH))
    print("app.env.APP_SETTINGS: " + str(app.env.APP_SETTINGS))

def json_settings():
    print(colored("\nCHECK JSON SETTINGS", 'yellow'))

def log():
    print(colored("\nCHECK LOG:", 'yellow'))
    print("dir(app.utils.helpers.logger.Log): " + str(dir(app.utils.helpers.logger.Log)))
    app.utils.helpers.logger.Log.info('PROVA INFO')
    app.utils.helpers.logger.Log.error('PROVA ERROR')
    app.utils.helpers.logger.Log.success('PROVA SUCCESS')

def storage():
    print(colored("\nCHECK STORAGE:", 'yellow'))
    print("dir(app.utils.helpers.storage): " + str(dir(app.utils.helpers.storage)))
    file1 = '/tmp/'+app.env.APP_PROC+'1'
    print(str(app.utils.helpers.storage.file_contains('STRING_TEST_1', file1)))
    print(str(app.utils.helpers.storage.read_file(file1)))
    print(str(app.utils.helpers.storage.file_contains_regex('STRING.*1', file1)))
    print(str(app.utils.helpers.storage.replace_in_file('STR_TO_FIND', 'NEW_STR', file1)))
    print(str(app.utils.helpers.storage.read_file(file1)))
    print(str(app.utils.helpers.storage.replace_in_file_regex('RE.+X_T._F.ND', 'NEW_STR', file1)))
    print(str(app.utils.helpers.storage.read_file(file1)))
    app.utils.helpers.storage.overwrite_file('NEW FILE CONTENT\nSTRING_TEST_1\nSTR_TO_FIND\nREGEX_TO_FIND', file1)
    file2 = '/tmp/'+app.env.APP_PROC+'2'
    app.utils.helpers.storage.append_in_file('CONTENT FOR FILE2', file2)
    file1_copy = '/tmp/'+app.env.APP_PROC+'1_copy'
    app.utils.helpers.storage.copy(file1, file1_copy)
    app.utils.helpers.storage.copy(app.env.APP_TMP, '/tmp/'+app.env.APP_PROC+'_copy')
    app.utils.helpers.storage.move('/tmp/'+app.env.APP_PROC+'_copy', '/tmp/'+app.env.APP_PROC+'_copy2')

main()
