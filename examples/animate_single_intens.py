'''Animates distances using single measurment mode'''
from hokuyolx import HokuyoLX
import matplotlib.pyplot as plt

DMAX = 2000
IMIN = 300.
IMAX = 2000.

bord = 20


import logging

# Configuration du niveau de logs
logging.basicConfig(level=logging.INFO)

# Instanciation d'un objet logger
logger = logging.getLogger()

# Ajout d'un handler qui envoie les logs sur la sortie standard (console)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# Utilisation du logger
logger.info("Message de log à destination de la sortie standard")

def nearest(scan):
    distances = [i[1] for i in scan]
    if not distances :
        print("Pas d'objet le plus proche")
        return
    print("Obstacle le plus proche : ", min(distances))
    return 

def get_colors(intens):
    max_val = intens.max()
    return np.repeat(intens, 3).reshape((4,3))/max_val 

def update(laser, plot, text):
    timestamp, scan = laser.get_filtered_intens(dmax=DMAX)
    scan = scan[bord:-bord]
    nearest(scan)
    # print("timestamp, scan :", timestamp, scan)
    plot.set_offsets(scan[:, :2])
    plot.set_array(scan[:, 2])
    text.set_text('t: %d' % timestamp)
    plt.show()
    plt.pause(0.001)

def run():
    plt.ion()
    laser = HokuyoLX(logger=logger)
    ax = plt.subplot(111, projection='polar')
    plot = ax.scatter([0, 1], [0, 1], s=5, c=[IMIN, IMAX], cmap=plt.cm.Greys_r, lw=0)
    text = plt.text(0, 1, '', transform=ax.transAxes)
    ax.set_rmax(DMAX)
    ax.grid(True)
    plt.show()
    while plt.get_fignums():
        update(laser, plot, text)
    laser.close()

if __name__ == '__main__':
    run()
