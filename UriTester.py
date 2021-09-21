import urllib.request
import threading


def get():
    contents = urllib.request.urlopen("https://env06-my-dev.dev.digitalsse.cloud/your-account/login?ReturnUrl=%2Fyour-products&mmcore.enc.pr=uJVp0WqMXhs06nj8mTqgTlX3Y4scebimqCOwBzt0zDS8wqtWgsryC0EYlv2tSgJgtVjiegqASm3dlHRElVgwUBYveyejB179Mf83q2M48u%2bPyhXbGpO%2fKa1JXgQShKZXNzyO0ZbYboYHeLn8Yf%2bv3ZVxMqaG54W3j3Y7ZB0fCBRLfSAN6IiJx4pPdPfbJb0plgFKA3DvhEE9OPABj5DsqluL7hK37s8wNVbcCciwdfgPdQMuK7LDUyZlAFjImJv%2f&mmcore.cfgid=1").read()

    if 'Uncaught TypeError: Cannot read property \'dn\' of undefined' in contents.decode('utf-8'):
        raise Exception('Error')


for i in range(100):
    print(i)
    get()
