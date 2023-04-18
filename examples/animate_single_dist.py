'''Animates distances using single measurment mode'''
from hokuyolx import HokuyoLX
import matplotlib.pyplot as plt

DMIN = 300
DMAX = 500
AMIN = 40
AMAX = 1040
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
    print("Le plus proche est à : {}".format(min(distances)))
    return 

def update(laser, plot, text):
    timestamp, scan = laser.get_filtered_dist(dmax=DMAX)
    nearest(scan)
    print("timestamps, scan :", timestamp, scan) 
    # data = laser.get_dist(grouping=5)
    # print(data)
    plot.set_data(*scan.T)
    text.set_text('t: %d' % timestamp)
    plt.draw()
    plt.pause(0.001)

def run():
    plt.ion()
    laser = HokuyoLX(logger=logger)
    ax = plt.subplot(111, projection='polar')
    # ax = plt.subplot(111)
    plot = ax.plot([], [], '.')[0]
    text = plt.text(0, 1, '', transform=ax.transAxes)
    ax.set_rmax(DMAX)
    ax.grid(True)
    plt.show()
    while plt.get_fignums():
        update(laser, plot, text)
    laser.close()

if __name__ == '__main__':
    run()
