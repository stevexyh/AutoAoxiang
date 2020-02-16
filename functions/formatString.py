#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import *

def setColor(string, color):
	if color == 'redFore':
		return Fore.RED+ Back.RESET + string + Style.RESET_ALL
	elif color == 'redBack':
		return Fore.WHITE+ Back.RED + string + Style.RESET_ALL
	elif color == 'greenFore':
		return Fore.GREEN+ Back.RESET + string + Style.RESET_ALL
	elif color == 'greenBack':
		return Fore.BLACK+ Back.GREEN + string + Style.RESET_ALL

if __name__ == "__main__":
	a = 'This is red.'
	b = setColor(a, 'redFore')
	print(b)