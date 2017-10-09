import numpy
import sklearn.cluster
import pygame, sys
from pygame.locals import *

positions = numpy.random.randint(0, 400, size =(30, 2))

positions_norms = numpy.sum(positions ** 2, axis = 1)
S = - positions_norms[:, numpy.newaxis] - positions_norms[numpy.newaxis, :] + 2 * numpy.dot(positions, positions.T)

aff_pro = sklearn.cluster.AffinityPropagation().fit(S)
labels = aff_pro.labels_

polygon_points = []

for i in xrange(max(labels) + 1):
    polygon_points.append([])

# Sorting each point by cluster
for i, l in enumerate(labels):
    polygon_points[1].append(positions[i])

pygame.init()
screen = pygame.dispaly.set_mode((400, 400))

while True:
    for point in polygon_points:
        pygame.draw.polygon(screen, (255, 0, 0), point)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            sys.exit()

    pygame.display.update()
    
