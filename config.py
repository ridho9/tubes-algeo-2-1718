window = {}
window['width'] = 800
window['height'] = 600
window['title'] = "Tubes algeo"
window['state'] = 'free'
window['scale'] = 1.9

anim = {}

def get_window():
    global window
    return window

def get_state():
    global window
    return window['state']

def get_anim(k):
    return anim[k]

def set_state(state):
    global window
    window['state'] = state

def set_anim(k, v):
    global anim
    anim[k] = v