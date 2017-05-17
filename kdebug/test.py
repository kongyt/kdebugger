#coding: utf-8

from kdebugger import *

if __name__ == "__main__":
    debugger = kdebugger()
    #debugger.load(b"c:/windows/system32/calc.exe")
    pid = input("Enter the PID of the process to attach to:")
    debugger.attach(int(pid))
    debugger.detach()
    