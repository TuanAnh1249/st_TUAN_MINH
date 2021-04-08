import pygame
import sys
#khoi tao pygame
pygame.init()


width = 800
height = 450

#  khai bao khung tro choi
screen=pygame.display.set_mode((width,height))

# tai anh vao 1 bien
bg=pygame.image.load('./img/bg.jpg')

# ep khung anh 
bg = pygame.transform.scale(bg,(width,height))

# load anh nhan vat
character=pygame.image.load('./img/character.png')

# ep kich thuoc nhan vat
character=pygame.transform.scale(character,(200,180))

# tao rect-rectagle toa do
character_rect=character.get_rect(center=(400,225))

while True: #lap vo han
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # dung de hien thi:gia tri 1 : ten anh , gia tri 2 :toa do         
    screen.blit(bg,(0,0))
    screen.blit(character,character_rect)

    pygame.display.update()

