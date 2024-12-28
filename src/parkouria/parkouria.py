import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Player position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = 40  # Size of the player rectangle

# Ducking state
is_ducking = False

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill("purple")

    # Get key states
    keys = pygame.key.get_pressed()
    
    # Check for ducking
    if keys[pygame.K_s]:
        player_pos.y += 5
    elif keys[pygame.K_w]:
        player_pos.y -= 5
    elif keys[pygame.K_a]:
        player_pos.x -= 5
    elif keys[pygame.K_d]:
        player_pos.x += 5

    # Keep the player within the screen bounds
    player_pos.y = max(0, min(player_pos.y, screen.get_height() - player_size))

    # Draw the player rectangle
    pygame.draw.rect(screen, "red", (player_pos.x, player_pos.y, player_size, player_size))

    # Flip the display to show the updated frame
    pygame.display.flip()

    # Limit FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
