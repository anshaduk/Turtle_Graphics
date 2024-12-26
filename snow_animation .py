import pygame
import random

# Initialize Pygame
pygame.init()

# Define the screen size and create a window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Snowflake class definition
class Snowflake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))  # White snowflake
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = random.randint(-screen_height, 0)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.y = random.randint(-screen_height, 0)
            self.rect.x = random.randint(0, screen_width)

# Create a group to hold snowflakes
num_snowflakes = 100
snowflakes = [Snowflake() for _ in range(num_snowflakes)]

# Create a sprite group
all_sprites = pygame.sprite.Group(snowflakes)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the snowflakes
    all_sprites.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all snowflakes
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
