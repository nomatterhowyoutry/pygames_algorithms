import pygame
import camera as Camera
import background as Background
import player as Player
import npc as NPC
import building as POI
from conf import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    COLLIDE_RATIO)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT)

pygame.init()

camera = Camera.Camera()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player.Player()
clock = pygame.time.Clock()
bg_image = pygame.image.load("Tile_12.png")
background = Background.Background(bg_image, (32, 32))

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
poi = POI.Building()
surf = pygame.surface.Surface((10, 10))
surf.fill((0, 255, 0))
new_enemy = NPC.NPC()
enemies.add(new_enemy)
all_sprites.add(new_enemy)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)


running = True
while running:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False
        # if event.type == ADDENEMY:
        #     new_enemy = NPC.NPC()
        #     enemies.add(new_enemy)
        #     all_sprites.add(new_enemy)

    player.update(pressed_keys)
<<<<<<< HEAD
    enemies.update()
    screen.blit(poi.rect, poi.position)
=======
    camera.update(player.camera_position)
    print(camera.position)
    enemies.update(player.position)
    screen.blit(background.surface, (0, 0), (camera.position[0], camera.position[1], SCREEN_WIDTH, SCREEN_HEIGHT))
>>>>>>> 01b9a0d2eef02d071b9ab4fc302c300ad0efc865
    for blop in enemies:
        screen.blit(surf, (blop.destination[0] + camera.position[0], blop.destination[1] + camera.position[1]))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    # if pygame.sprite.spritecollideany(
    #     player, 
    #     enemies, 
    #     collided=pygame.sprite.collide_rect_ratio(COLLIDE_RATIO)
    #     ):
    #     player.kill()
    #     running = False


    pygame.display.flip()
    clock.tick(120)

pygame.quit()
