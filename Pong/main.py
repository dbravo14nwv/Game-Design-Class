import pygame, sys, random

# Initialize all imported pygame modules
pygame.init()

# --- Screen Setup ---
WIDTH, HEIGHT = 1280, 720  # Window dimensions (width x height)

# Fonts for various UI elements:
# Regular font for scores
FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))
# Large font for title and win/lose messages
BIG_FONT = pygame.font.SysFont("Consolas", int(WIDTH / 10))
# Smaller font for instructions on screens
SMALL_FONT = pygame.font.SysFont("Consolas", int(WIDTH / 30))

# Create the main display window with the above dimensions
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Pong+ First To 50!")

# Create a clock object to manage frame rate
CLOCK = pygame.time.Clock()

# Maximum number of balls allowed on the screen simultaneously
MAX_BALLS = 5

# --- Paddle Setup ---
# Player paddle - positioned near right edge, vertically centered
player = pygame.Rect(WIDTH - 110, HEIGHT / 2 - 50, 10, 100)
# Opponent paddle - positioned near left edge, vertically centered
opponent = pygame.Rect(110, HEIGHT / 2 - 50, 10, 100)

# Initialize scores for both player and opponent
player_score, opponent_score = 0, 0

# Start with one ball in center, random color and initial speed
balls = [[
    pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20),  # Ball rectangle (position and size)
    (1, 1),  # Ball speed vector (x_speed, y_speed)
    random.choice(["white", "green", "red"])  # Ball color for scoring logic
]]

def reset_game():
    """
    Reset game state to initial setup:
    - Reset paddle positions
    - Reset scores
    - Reset balls to one centered ball
    """
    global player, opponent, player_score, opponent_score, balls
    player = pygame.Rect(WIDTH - 110, HEIGHT / 2 - 50, 10, 100)
    opponent = pygame.Rect(110, HEIGHT / 2 - 50, 10, 100)
    player_score, opponent_score = 0, 0
    balls = [[
        pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20),
        (1, 1),
        random.choice(["white", "green", "red"])
    ]]

def show_end_screen(text):
    """
    Display end game screen with given text (e.g. "You Win!" or "You Lose!").
    Show prompt to restart or quit.
    Wait for user input:
    - R to restart the game
    - Q to quit the program
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart game if R pressed
                    reset_game()
                    return  # Exit this screen and resume main game loop
                elif event.key == pygame.K_q:
                    # Quit if Q pressed
                    pygame.quit()
                    sys.exit()

        # Fill background with black before drawing
        SCREEN.fill("black")

        # Render the main message centered near top-middle
        message = BIG_FONT.render(text, True, "white")
        rect = message.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
        SCREEN.blit(message, rect)

        # Render instructions text below the main message
        instructions = SMALL_FONT.render("Press R to Restart or Q to Quit", True, "white")
        instr_rect = instructions.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        SCREEN.blit(instructions, instr_rect)

        # Update the display to show these changes
        pygame.display.update()

        # Cap the frame rate to 60 FPS to reduce CPU load
        CLOCK.tick(60)

def show_title_screen():
    """
    Display the title screen with the game name and start instructions.
    Wait for the user to press SPACE to begin the game.
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Start game on SPACE key press
                    return

        # Fill screen with black before drawing title
        SCREEN.fill("black")

        # Render large title text "PONG+" centered a bit above middle
        title_text = BIG_FONT.render("PONG+", True, "white")
        title_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
        SCREEN.blit(title_text, title_rect)

        # Render smaller instruction text below title
        start_text = SMALL_FONT.render("Press SPACE to Start", True, "white")
        start_rect = start_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        SCREEN.blit(start_text, start_rect)

        # Update display to show title and instructions
        pygame.display.update()

        # Cap frame rate to 60 FPS
        CLOCK.tick(60)

# Show the title screen before starting the game
show_title_screen()

# --- Main Game Loop ---
while True:
    # Detect keys currently held down for paddle movement
    keys_pressed = pygame.key.get_pressed()

    # Base speed for player paddle movement
    speed = 2
    # Double speed if either shift key is pressed (speed boost)
    if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT]:
        speed = 4

    # Move player paddle up if UP arrow pressed and paddle is not at screen top
    if keys_pressed[pygame.K_UP] and player.top > 0:
        player.top -= speed
    # Move player paddle down if DOWN arrow pressed and paddle is not at screen bottom
    if keys_pressed[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.bottom += speed

    # Fill background with black each frame to clear previous drawings
    SCREEN.fill("black")

    # Process window events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # List to hold indices of balls to remove (scored balls)
    balls_to_remove = []

    # --- Process each ball's movement and collision ---
    for i in range(len(balls)):
        ball, (x_speed, y_speed), color = balls[i]  # Unpack ball properties

        # Bounce off bottom boundary by reversing vertical direction upwards
        if ball.y >= HEIGHT:
            y_speed = -abs(y_speed)
        # Bounce off top boundary by reversing vertical direction downwards
        if ball.y <= 0:
            y_speed = abs(y_speed)

        # Check collision with player paddle
        if ball.colliderect(player):
            # Reverse horizontal direction left and increase speed slightly
            x_speed = -abs(x_speed) - 0.2
        # Check collision with opponent paddle
        if ball.colliderect(opponent):
            # Reverse horizontal direction right and increase speed slightly
            x_speed = abs(x_speed) + 0.2

        # Check if ball crossed left edge (player scores)
        if ball.x <= 0:
            if color == "white":
                player_score += 1  # White ball = +1 point
            elif color == "green":
                player_score += 2  # Green ball = +2 points
            elif color == "red":
                # Red ball = -1 point, but don't go below 0
                player_score = max(0, player_score - 1)
            balls_to_remove.append(i)  # Mark ball to remove
            continue  # Skip further processing for this ball

        # Check if ball crossed right edge (opponent scores)
        if ball.x >= WIDTH:
            if color == "white":
                opponent_score += 1
            elif color == "green":
                opponent_score += 2
            elif color == "red":
                opponent_score = max(0, opponent_score - 1)
            balls_to_remove.append(i)
            continue

        # Update ball position by its speed (scaled by 1.6 for smoothness)
        ball.x += x_speed * 1.6
        ball.y += y_speed * 1.6
        # Save updated speed back to ball list
        balls[i][1] = (x_speed, y_speed)

    # Remove balls that scored (from highest index to lowest to avoid index issues)
    for i in sorted(balls_to_remove, reverse=True):
        del balls[i]

    # --- Opponent AI Movement ---
    if balls:
        # Extract all red balls (which opponent tries to avoid)
        red_balls = [ball for ball, _, color in balls if color == "red"]

        if red_balls:
            # Opponent paddle vertical center coordinate
            opponent_center = opponent.centery
            # Find red ball closest vertically to opponent paddle
            closest_red = min(red_balls, key=lambda b: abs(b.centery - opponent_center))

            # Move opponent paddle away from closest red ball vertically
            if opponent.centery < closest_red.centery:
                opponent.top -= 2  # Move paddle up
                # Clamp paddle top to screen boundary
                if opponent.top < 0:
                    opponent.top = 0
            elif opponent.centery > closest_red.centery:
                opponent.bottom += 2  # Move paddle down
                # Clamp paddle bottom to screen boundary
                if opponent.bottom > HEIGHT:
                    opponent.bottom = HEIGHT
        else:
            # If no red balls, opponent follows the first ball vertically
            first_ball = balls[0][0]
            if opponent.y < first_ball.y:
                opponent.top += 2  # Move paddle down
                # Clamp paddle position to screen bottom
                if opponent.top > HEIGHT - opponent.height:
                    opponent.top = HEIGHT - opponent.height
            if opponent.bottom > first_ball.y:
                opponent.bottom -= 2  # Move paddle up
                # Clamp paddle position to screen top
                if opponent.bottom < 0:
                    opponent.bottom = 0

    # --- Ball spawning logic ---
    # Number of balls depends on total score, max capped by MAX_BALLS
    total_score = player_score + opponent_score
    while len(balls) < (total_score // 10) + 1 and len(balls) < MAX_BALLS:
        # Create new ball in center with random direction and color
        new_ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
        new_speed = (random.choice([1, -1]), random.choice([1, -1]))
        new_color = random.choice(["white", "green", "red"])
        balls.append([new_ball, new_speed, new_color])

    # --- Win/Lose condition ---
    if player_score >= 50:
        # Player reached 50 points, show win screen
        show_end_screen("You Win!")
    elif opponent_score >= 50:
        # Opponent reached 50 points, show lose screen
        show_end_screen("You Lose!")

    # --- Drawing ---
    # Draw all balls as colored circles
    for ball, _, color in balls:
        pygame.draw.circle(SCREEN, color, ball.center, 10)

    # Render scores as white text
    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")

    # Draw paddles as white rectangles
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)

    # Display scores near the top center of the screen
    SCREEN.blit(player_score_text, (WIDTH / 2 + 50, 50))
    SCREEN.blit(opponent_score_text, (WIDTH / 2 - 50, 50))

    # Update the display to show everything drawn this frame
    pygame.display.update()

    # Cap frame rate to 300 FPS for smooth gameplay
    CLOCK.tick(300)


# Reference Video For Base Template = https://www.youtube.com/watch?v=iSZXroL4apY