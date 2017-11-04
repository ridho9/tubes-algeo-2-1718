#File konfigurasi untuk mengatur ukuran window OpenGl dan skala yang ada
#Terdapat juga state-state/keadaan untuk menandakan status program saat ini

window = {}
window['width'] = 800
window['height'] = 600
window['title'] = b"Tubes algeo"
window['state'] = 'free'
window['scale'] = 1.9

anim = {}

def get_window():
    global window
    return window

#Mengembalikan state saat ini
def get_state():
    global window
    return window['state']

#Mengembalikan value animasi  berdasarkan key yang diinput
def get_anim(k):
    return anim[k]

#Menentukan state window saat ini, ada dua state yaitu free (dapat menerima input)
#dan anim, yaitu sedang melakukan animasi
def set_state(state):
    global window
    window['state'] = state

#Set data animasi
def set_anim(key, value):
    global anim
    anim[key] = value