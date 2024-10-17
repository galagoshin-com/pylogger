import time
import sys
from builtins import print as print_legacy
from .colors import IBlue, IWhite, White, IRed, Red, IGreen, IYellow
from .logfiles import write_log
import traceback

def print(message: str):
    timestr = time.strftime("%Y.%m.%d %H:%M:%S")
    print_legacy(f"{colors.IBlue}* {colors.IWhite}[{timestr}] {colors.White}> {colors.IWhite}{message}", file=sys.stdout)
    logfiles.write_log(f"[{timestr}] > {message}")

def warning(message: str):
    timestr = time.strftime("%Y.%m.%d %H:%M:%S")
    print_legacy(f"{colors.IYellow}* {colors.IWhite}[{timestr}] {colors.White}> {colors.IWhite}{message}", file=sys.stdout)
    logfiles.write_log(f"[{timestr}] WARNING > {message}")

def info(message: str):
    timestr = time.strftime("%Y.%m.%d %H:%M:%S")
    print_legacy(f"{colors.IGreen}* {colors.IWhite}[{timestr}] {colors.White}> {colors.IWhite}{message}", file=sys.stdout)

def debug(print_stack_trace: bool, data):
    timestr = time.strftime("%Y.%m.%d %H:%M:%S")
    print_legacy(f"{colors.ICyan}* {colors.IWhite}[{timestr}] {colors.White}> {colors.IWhite}{data}", file=sys.stdout)
    logfiles.write_log(f"[{timestr}] DEBUG > {data}")
    if print_stack_trace:
        try:
            raise Exception("debug")
        except Exception:
            logfiles.write_log(f"[{timestr}] DEBUG > {traceback.format_exc()}")
            print_legacy(traceback.format_exc())

def error(message: str):
    timestr = time.strftime("%Y.%m.%d %H:%M:%S")
    print_legacy(f"{colors.IRed}* {colors.IWhite}[{timestr}] {colors.White}> {colors.IWhite}{message}", file=sys.stderr)
    logfiles.write_log(f"[{timestr}] ERROR > {message}")

def fatal(message: str):
    timestr = time.strftime("%Y.%m.%d %H:%M:%S")
    print_legacy(f"{colors.Red}* {colors.IWhite}[{timestr}] {colors.White}> {colors.IWhite}{message}", file=sys.stderr)
    logfiles.write_log(f"[{timestr}] FATAL > {message}")
    exit(1)