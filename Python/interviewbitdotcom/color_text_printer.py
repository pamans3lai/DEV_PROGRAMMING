import colorama
# back for background, fore for text colorama

from colorama import Back, Fore

# baris ini memastikan bahwa style color reset dimana eksekusi program telah selesai
colorama.init(autoreset = True)

text = input("Enter a pharse or sentence: ")

# Colorama has limited color options
print(Fore.BLACK + Back.WHITE + text)
print(Fore.RED + Back.CYAN + text)
print(Fore.GREEN + Back.MAGENTA + text)
print(Fore.YELLOW + Back.BLUE + text)
print(Fore.BLUE + Back.YELLOW + text)
print(Fore.MAGENTA + Back.BLUE + text)
print(Fore.CYAN + Back.RED + text)
print(Fore.WHITE + Back.BLACK + text)
