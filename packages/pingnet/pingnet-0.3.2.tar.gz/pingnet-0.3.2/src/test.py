class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   WHITE = '\033[97m'
   GRAY = '\033[90m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.RED + 'Hello World !' + color.END)