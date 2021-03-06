import pygame
import camera as Camera
import background as Background
import player as Player
import npc as NPC
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
    camera.update(player.camera_position)
    print(player.position)
    enemies.update(player.position)
    screen.blit(background.surface, camera.position)
    for blop in enemies:
        screen.blit(surf, blop.destination)
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