
import subprocess
import optparse
import re

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Used to select interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="Used to select mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("interface is not specified! use --help to get more info")
    elif not options.new_mac:
        parser.error("Mac id is not specified! use --help to get more info")
    else:
        return options

def change_macip(interface, new_mac):
    print("Changeing Your " + interface + " To " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", options.new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if filter_result:
        return filter_result.group(0)
    else:
        print("Mac address not found")

options =  get_options()

mac_address_filter_result = get_mac_address(options.interface)
print("current mac = " + str(mac_address_filter_result))

change_macip(options.interface, options.new_mac)

mac_address_filter_result = get_mac_address(options.interface)
if mac_address_filter_result == options.new_mac:
    print("Mac Address Change To: " + mac_address_filter_result)
else:
    print("Mac Address Is Not changed")