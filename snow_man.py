import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Christmas Scene with Snowman, Tree, Birds, and Crib")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (25, 25, 112)  # Night sky
GREEN = (0, 128, 0)
BROWN = (139, 69, 19)
YELLOW = (255, 223, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
PINK = (255, 182, 193)
STRAW = (218, 165, 32)  # Straw roof

# Snowflake positions
snowflakes = [[random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)] for _ in range(100)]

# Bird positions
birds = [{'x': random.randint(-200, SCREEN_WIDTH), 'y': random.randint(50, 200), 'speed': random.randint(2, 5)} for _ in range(5)]


# Draw snowman
def draw_snowman(x, y):
    pygame.draw.circle(screen, WHITE, (x, y + 60), 30)  # Bottom
    pygame.draw.circle(screen, WHITE, (x, y), 20)  # Middle
    pygame.draw.circle(screen, WHITE, (x, y - 30), 15)  # Head
    pygame.draw.circle(screen, BLACK, (x - 5, y - 35), 2)  # Left eye
    pygame.draw.circle(screen, BLACK, (x + 5, y - 35), 2)  # Right eye
    pygame.draw.polygon(screen, (255, 140, 0), [(x, y - 30), (x + 10, y - 28), (x, y - 25)])  # Nose
    pygame.draw.rect(screen, BLACK, (x - 10, y - 50, 20, 5))  # Hat brim
    pygame.draw.rect(screen, BLACK, (x - 7, y - 65, 14, 15))  # Hat


# Draw Christmas tree with blinking lights
def draw_tree(x, y, frame_count):
    pygame.draw.rect(screen, BROWN, (x - 10, y, 20, 40))  # Trunk
    pygame.draw.polygon(screen, GREEN, [(x - 50, y), (x, y - 100), (x + 50, y)])  # Base
    pygame.draw.polygon(screen, GREEN, [(x - 40, y - 40), (x, y - 120), (x + 40, y - 40)])  # Middle
    pygame.draw.polygon(screen, GREEN, [(x - 30, y - 80), (x, y - 140), (x + 30, y - 80)])  # Top
    pygame.draw.circle(screen, YELLOW, (x, y - 150), 10)  # Star

    # Add blinking lights
    lights = [
        (x - 30, y - 70),
        (x + 30, y - 50),
        (x - 20, y - 30),
        (x + 20, y - 90),
        (x, y - 110),
    ]
    light_colors = [RED, LIGHT_BLUE, PINK, YELLOW, WHITE]
    if (frame_count // 15) % 2 == 0:  # Blink every 15 frames
        for i, (lx, ly) in enumerate(lights):
            pygame.draw.circle(screen, light_colors[i % len(light_colors)], (lx, ly), 5)


# Draw Christmas crib with added elements
def draw_crib(x, y, frame_count):
    # Crib structure
    pygame.draw.rect(screen, GREEN, (x - 65, y + 20, 130, 20))  # Green mat
    pygame.draw.rect(screen, BROWN, (x - 60, y, 120, 60))  # Base
    pygame.draw.polygon(screen, STRAW, [(x - 70, y), (x, y - 50), (x + 70, y)])  # Straw roof

    # Baby Jesus
    pygame.draw.circle(screen, WHITE, (x, y + 20), 15)  # Body
    pygame.draw.circle(screen, PINK, (x, y + 10), 8)  # Head

    # Blinking lights around the crib
    lights = [
        (x - 60, y - 5), (x + 60, y - 5),
        (x - 40, y + 20), (x + 40, y + 20),
        (x, y + 40)
    ]
    light_colors = [RED, YELLOW, LIGHT_BLUE, PINK, GREEN]
    if (frame_count // 15) % 2 == 0:  # Blink every 15 frames
        for i, (lx, ly) in enumerate(lights):
            pygame.draw.circle(screen, light_colors[i % len(light_colors)], (lx, ly), 5)

    # # Text celebrating the birth of Jesus
    # font = pygame.font.Font(None, 36)
    # text = font.render("Celebrate the Birth of Jesus Christ", True, WHITE)
    # screen.blit(text, (x - 120, y + 70))


# Draw snowflakes
def draw_snowflakes(snowflakes):
    for flake in snowflakes:
        pygame.draw.circle(screen, WHITE, flake, 3)


# Move snowflakes
def move_snowflakes(snowflakes):
    for flake in snowflakes:
        flake[1] += random.randint(2, 5)  # Move down
        if flake[1] > SCREEN_HEIGHT:  # Reset to top if out of screen
            flake[1] = random.randint(-20, -1)
            flake[0] = random.randint(0, SCREEN_WIDTH)


# Draw birds
def draw_birds(birds):
    for bird in birds:
        # Draw bird as a simple triangle
        pygame.draw.polygon(screen, BLACK, [
            (bird['x'], bird['y']),
            (bird['x'] + 15, bird['y'] - 5),
            (bird['x'] + 15, bird['y'] + 5)
        ])


# Move birds
def move_birds(birds):
    for bird in birds:
        bird['x'] += bird['speed']  # Move to the right
        if bird['x'] > SCREEN_WIDTH + 20:  # Reset position if out of screen
            bird['x'] = random.randint(-200, -50)
            bird['y'] = random.randint(50, 200)
            bird['speed'] = random.randint(2, 5)

def draw_crib(x, y, frame_count):
    # Crib structure
    pygame.draw.rect(screen, GREEN, (x - 65, y + 20, 130, 20))  # Green mat
    pygame.draw.rect(screen, BROWN, (x - 60, y, 120, 60))  # Base
    pygame.draw.polygon(screen, STRAW, [(x - 70, y), (x, y - 50), (x + 70, y)])  # Straw roof

    # Baby Jesus
    pygame.draw.circle(screen, WHITE, (x, y + 20), 15)  # Body
    pygame.draw.circle(screen, PINK, (x, y + 10), 8)  # Head

    # Angels
    angel_positions = [
        (x - 80, y - 30),  # Left angel
        (x + 80, y - 30)   # Right angel
    ]
    for ax, ay in angel_positions:
        pygame.draw.circle(screen, WHITE, (ax, ay), 15)  # Head
        pygame.draw.circle(screen, WHITE, (ax, ay + 20), 10)  # Body
        pygame.draw.polygon(screen, WHITE, [(ax - 15, ay + 10), (ax, ay + 20), (ax - 15, ay + 30)])  # Left wing
        pygame.draw.polygon(screen, WHITE, [(ax + 15, ay + 10), (ax, ay + 20), (ax + 15, ay + 30)])  # Right wing
        pygame.draw.circle(screen, YELLOW, (ax, ay - 15), 5)  # Halo

    # Blinking lights around the crib
    lights = [
        (x - 60, y - 5), (x + 60, y - 5),
        (x - 40, y + 20), (x + 40, y + 20),
        (x, y + 40)
    ]
    light_colors = [RED, YELLOW, LIGHT_BLUE, PINK, GREEN]
    if (frame_count // 15) % 2 == 0:  # Blink every 15 frames
        for i, (lx, ly) in enumerate(lights):
            pygame.draw.circle(screen, light_colors[i % len(light_colors)], (lx, ly), 5)

    # Text celebrating the birth of Jesus
    # font = pygame.font.Font(None, 36)
    # text = font.render("Celebrate the Birth of Jesus Christ", True, WHITE)
    # screen.blit(text, (x - 120, y + 70))


def main():
    running = True
    frame_count = 0
    font = pygame.font.Font(None, 74)
    message = font.render("Happy X'mas!", True, WHITE)
    message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, 50))

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Background
        screen.fill(BLUE)  # Night sky

        # Draw moon
        pygame.draw.circle(screen, YELLOW, (700, 100), 40)

        # Draw elements
        draw_snowflakes(snowflakes)
        draw_tree(600, 400, frame_count)
        draw_snowman(200, 400)
        draw_crib(400, 450, frame_count)
        draw_birds(birds)

        # Move elements
        move_snowflakes(snowflakes)
        move_birds(birds)

        # Display blinking message every 30 frames
        if (frame_count // 30) % 2 == 0:  # Toggle visibility every 30 frames
            screen.blit(message, message_rect)

        # Update the screen
        pygame.display.flip()
        clock.tick(30)  # 30 frames per second
        frame_count += 1

    pygame.quit()

# Run the program
main()
