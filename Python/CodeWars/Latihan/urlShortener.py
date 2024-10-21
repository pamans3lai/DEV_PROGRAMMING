import pyshorteners

long_url = input('Masukkan URL yang akan disingkat: ')

# TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print('URL singkat: ' + short_url)
