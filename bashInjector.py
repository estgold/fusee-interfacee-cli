import sys
import os
import fusee_launcher as fusee
import mock_arguments
import usb 
from argparse import ArgumentParser


class bashInjector:
    def __init__(self, args):
        self.payload_path = payload_path
        self.device_found = False
        self.lbl_length   = 22
        self.usb_backend  = fusee.HaxBackend.create_appropriate_backend()
        self.do_update()

    def do_update(self):
        print("Searching for device")
        device = self.usb_backend.find_device(0x0955, 0x7321)
        if device and not self.device_found:
            self.device_found = True
            print("Device found!")
            args = mock_arguments.MockArguments()
            args.payload   = self.payload_path
            args.relocator = self.build_relocator_path()
            fusee.do_hax(args)
            print("success")
        elif not device and not self.device_found:
            print("Device not found, please connect your switch in RCM mode and retry \nexit script")
            sys.exit()

    def build_relocator_path(self):
        try:
            path = sys._MEIPASS
        except Exception:
            path = os.path.abspath('.')

        return os.path.join(path, 'intermezzo.bin')

payload_path = ''
parser = ArgumentParser()
parser.add_argument('--payload', default="", help="payload.bin path")
parser.add_argument('-p', default="", help="payload.bin path")
args = parser.parse_args()
if not args.payload:
    if not args.p:
        payload_path = input("Please enter the path of your payload: ")
    else:
        payload_path = args.p
else:
    payload_path = args.payload

from pathlib import Path

payloadFile = Path(payload_path)
if not payloadFile.is_file():
    print("file not found\nexit script")
    sys.exit()

main = bashInjector(payload_path)