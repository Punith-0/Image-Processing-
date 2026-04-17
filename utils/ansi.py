# ANSI escape codes for colors and styles
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"
HIGHLIGHT = "\033[7m"
BLACK = "\033[30m"
BLUE      = "\033[34m"
YELLOW    = "\033[33m"

if __name__ == "__main__":  
    print(f"{RED}This is a red message.{RESET}")
    print(f"{BOLD}{GREEN}{BLACK}This is bold and green.{RESET}")