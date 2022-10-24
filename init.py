#!/usr/bin/env python
import math

class kate(object):

	def __init__(self):
		#self.talk = talk
		#self.listen = listen
		#self.call_cate("hello", "you said welcome")
		#pass
		self.update_game()

	def area_map(self):
		print ("What game area do you want?")
		area = input(">> ")
		area = int(area)
		#find lenth and width of the game
		game_dim = int(math.sqrt(area))
		#find ball dimentions in the game
		ball_dim = game_dim * .1
		ball_area = int(math.pow(ball_dim, 2))
		#find position of ball
		ball_pos_x = (game_dim / game_dim) + 2
		ball_pos_y = (game_dim / game_dim) + 3
		print (f"Game area: {area}")
		print (f"Ball area: {ball_area}")
		print (f"Ball pos: {ball_pos_x}, {ball_pos_y}")


	def update_game(self):
		num  = 2
		#print ("Initializing game...")
		#print ("x" * 50)
		#self.area_map()
		#print ("x" * 50)
		#print ("Welcome to the game of numbers...")
		return num

	def pool_play(self):
		# 
		pool1 = self.area_map()
		gen_pool_width = self.width/4
		gen_pool_height = self.height/2
		gen_pool_area = gen_pool_width * gen_pool_height
		return gen_pool_area

	def pools(self):
		#number of pools
		#ref {mqs} in numbers, standard Afritek value management unit
		#mqs (meth, qure, sik).modules
		pool_num = self.area_map()/self.gen_pool()
		drawn_pools = []
		for i in range(int(pool_num)):
			if len(drawn_pools)!=pool_num:
				drawn_pools.append(i)
		return f"No of pools for area: {self.area_map()} mqs is {len(drawn_pools)} Each pool having {self.gen_pool()} mqs" 

	def ball(self):
		#ball area
		ball = self.gen_pool () * .0001
		return f"{ball} mqs"

	def call_cate(self, talk, listen):
		self.talk = talk
		self.listen = listen
		print (self.talk)
		print (self.listen)


start = kate()


