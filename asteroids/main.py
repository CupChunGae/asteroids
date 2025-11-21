import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          """)
    pygame.init() # loading in the pygame module
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # creating the screen
    
    in_game_clock = pygame.time.Clock() # making the clock for events to keep track of
    dt = 0
    
    updatable = pygame.sprite.Group() # making groups for easier handling of multiple sprites
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) # adding the sprites to the groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # default loading position
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        
        for event in pygame.event.get(): # allows the user to "x" out of the application
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)
        
        for a in asteroids:
            if a.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if a.collides_with(s) == True:
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()
            
            
        for object in drawable:
            object.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()
        in_game_clock.tick(60)
        dt = in_game_clock.tick(60)/1000
        #print(f"{dt}")
       



if __name__ == "__main__":
    main()
