import urllib.request, urllib.parse, urllib.error
import json
import time
#import winsound
from plyer import notification

def notifier(values):
    notification.notify(
        title = 'Covid Alert',
        message = '''Increase: {increase}
Deaths: {deceased}'''.format(increase = values[0], deceased = values[1]),
        app_icon = None,
        timeout = 180
    )

def printer():
    data = urllib.request.urlopen('https://api.covid19india.org/v4/min/data.min.json')

    st = ''
    for line in data:
        st += (line.decode().strip())

    js = json.loads(st)

    increase = (js['TT']['delta']['confirmed'])
    deceased = (js['TT']['delta']['deceased'])

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    #print(current_time)

    values = [int(increase), int(deceased)]

    #print('Today, till now,' + ' ' + str(increase) + ' ' + 'got infected.')
    #print('Today, till now,' + ' ' + str(deceased) + ' ' + 'died.')

    return (values)

#b = 0
while(True):

    a = (printer())
    notifier(a)
    '''if a[0] != b:
         frequency = 2500  # Set Frequency To 2500 Hertz
         duration = 1000  # Set Duration To 1000 ms == 1 second
         winsound.Beep(frequency, duration)

         print(a[0]//1000, 'thousand!')
    b = a[0]'''
    time.sleep(180)

    print('\n')
