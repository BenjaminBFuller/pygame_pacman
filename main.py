import pygame

pygame.init()

tile = 40  # tile size in pixels

gameBoard = [  # 0 = wall, 1 = pill, 2 = super pill
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
(width, height) = (len(gameBoard[1]) * tile, len(gameBoard) * tile)
window = pygame.display.set_mode((width, height))
pygame.display.flip()
pacman = [10, 1]  # starting position
direction = 1  # cardinal direction for pacman to move
moveCount = 0
moveDelay = 50
pillColor = (222, 161, 133)


def moveCheck(row, col):
    if gameBoard[row][col] != 0:
        return True
    else:
        return False


def makeBoard():
    window.fill((0, 0, 0))

    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[0])):
            if gameBoard[i][j] == 0:
                pygame.draw.rect(window, (0, 0, 255), (j * tile, i * tile, tile, tile))
            elif gameBoard[i][j] == 1:
                pygame.draw.circle(window, pillColor, (j * tile + tile // 2, i * tile + tile // 2), tile // 8)

    pygame.draw.circle(window, (255, 255, 0), (pacman[1] * tile + tile // 2, pacman[0] * tile + tile // 2), tile // 4)
    pygame.display.update()


running = True
while running:
    moveCount += 1
    # print(moveCount) # tests if moveCount is working in concordance with running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = 0  # north
            elif event.key == pygame.K_d:
                direction = 1  # east
            elif event.key == pygame.K_s:
                direction = 2  # south
            elif event.key == pygame.K_a:
                direction = 3  # west
            elif event.key == pygame.K_q:
                running = False  # quit on key stroke q

    if moveCount == moveDelay:
        moveCount = 0
        if direction == 0:
            if moveCheck(pacman[0] - 1, pacman[1]):
                pacman[0] -= 1
        elif direction == 1:
            if moveCheck(pacman[0], pacman[1] + 1):
                pacman[1] += 1
        elif direction == 2:
            if moveCheck(pacman[0] + 1, pacman[1]):
                pacman[0] += 1
        elif direction == 3:
            if moveCheck(pacman[0], pacman[1] - 1):
                pacman[1] -= 1

    pacman[1] %= len(gameBoard[0])
    makeBoard()
