import pygame, sys, math

class Cam:
	def __init__(self, pos = (0,0,0), rot = (0,0)):
		self.pos = list(pos)
		self.rot = list(rot)

	def update(self, dt, key):
		s = dt * 10

		print self.pos
		if key[pygame.K_q]: self.pos[1] += s
		if key[pygame.K_e]: self.pos[1] -= s

		if key[pygame.K_w]: self.pos[2] += s
		if key[pygame.K_s]: self.pos[2] -= s
		if key[pygame.K_a]: self.pos[0] -= s
		if key[pygame.K_d]: self.pos[0] += s


pygame.init()

w = 400
h = 400

cx = w//2
cy = h//2

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

verts = (-1, -1, -1), (1, -1, -1), (-1, 1, -1), (1, 1, -1), (-1, -1, 1), (1, -1, 1), (-1, 1, 1), (1, 1, 1)
edges = (0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (3, 7), (2, 6), (4, 5), (5, 7), (7, 6), (6, 4)

cam = Cam((0, 0, -5))

while True:
	dt = float(clock.tick()) / float(1000)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: pygame.quit(); sys.exit()

	screen.fill((255, 255, 255))

	for edge in edges:

		points = []
		for x, y, z in (verts[edge[0]], verts[edge[1]]):
			

			x -= cam.pos[0]
			y -= cam.pos[1]
			z -= cam.pos[2]

			f = (w / 2) / z
	
			x, y = x * f, y * f

			points += [(cx + int(x), cy + int(y))]
			
		pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)

	pygame.display.flip()

	key = pygame.key.get_pressed()

	cam.update(dt, key)
