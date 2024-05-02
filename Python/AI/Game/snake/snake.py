import pygame # 1. pygame 선언
import random
from datetime import datetime
from datetime import timedelta
 
pygame.init() # 2. pygame 초기화
 
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK= (0,0,0)

unit_size=20
size_range=50
size = [unit_size*size_range,unit_size*size_range]
screen = pygame.display.set_mode(size)
 
done= False
clock= pygame.time.Clock()
last_moved_time = datetime.now()
 
KEY_DIRECTION = {
    pygame.K_UP: 'U',
    pygame.K_DOWN: 'D',
    pygame.K_LEFT: 'L',
    pygame.K_RIGHT: 'R',
}
 
def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * unit_size, position[0] * unit_size),
                        (unit_size, unit_size))
    pygame.draw.rect(screen, color, block)
 
class Wall:
    def __init__(self) -> None:
        self.positions=[]
        for i in range(size_range):
            for j in range(size_range):
                if i==0 or i==size_range-1 or j==0 or j==size_range-1: self.positions.append((i,j))

    def create_wall(self):
        for i, j in self.positions:
            draw_block(screen,BLACK,(i,j))

class Snake:
    def __init__(self):
        self.positions = [(1,3),(1,2),(1,1)]  # 뱀의 위치
        self.direction = ''
 
    def draw(self):
        for position in self.positions: 
            draw_block(screen, GREEN, position)
 
    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'U':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'D':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'L':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'R':
            self.positions = [(y, x + 1)] + self.positions[:-1]
 
    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'U':
            self.positions.append((y - 1, x))
        elif self.direction == 'D':
            self.positions.append((y + 1, x))
        elif self.direction == 'L':
            self.positions.append((y, x - 1))
        elif self.direction == 'R':
            self.positions.append((y, x + 1))    
 
 
class Apple:
    def __init__(self, position=(size_range//2, size_range//2)):
        self.position = position
 
    def draw(self):
        draw_block(screen, RED, self.position)

def find_direction(snake,apple,wall):
    snake_head_p=snake.positions[0]
    apple_p=apple.position
    horizontal_direction=apple_p[1]-snake_head_p[1]
    vertical_direction=apple_p[0]-snake_head_p[0]
    if abs(horizontal_direction)>=abs(vertical_direction):
        if horizontal_direction>0: direction="R"
        else: direction="L"
    else:
        if vertical_direction>0: direction="D"
        else: direction="U"

    y, x = snake_head_p
    roop_count=0
    while(1):
        if direction == 'U':
            if (y - 1, x) in snake.positions[1:] or (y - 1, x) in wall.positions: direction = 'D'
            else: break
        elif direction == 'D':
            if (y + 1, x) in snake.positions[1:] or (y + 1, x) in wall.positions: direction = 'L'
            else: break
        elif direction == 'L':
            if (y, x - 1) in snake.positions[1:] or (y, x - 1) in wall.positions: direction = 'R'
            else: break
        elif direction == 'R':
            if (y, x + 1) in snake.positions[1:] or (y, x + 1) in wall.positions: direction = 'U'
            else: break
        roop_count+=1
        if roop_count>=3: break

    print(f"{snake_head_p} {apple_p} {direction}")
    return direction
 
# 4. pygame 무한루프
def runGame():
    global done, last_moved_time
    #게임 시작 시, 뱀과 사과를 초기화
    snake = Snake() 
    apple = Apple()
    wall = Wall()
        
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        wall.create_wall()
        snake.draw()
        apple.draw()
        pygame.display.update()
    
        # 키보드 입력 조작
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         done=True
        #     if event.type == pygame.KEYDOWN:
        #         if event.key in KEY_DIRECTION:
        #             snake.direction = KEY_DIRECTION[event.key]

        # 자동조작
        pygame.event.get()
        snake.direction = find_direction(snake,apple,wall)
 
        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()
 
        if snake.positions[0] == apple.position:
            snake.grow()    
            apple.position = (random.randint(1, size_range-2), random.randint(1, size_range-2))
        
        if snake.positions[0] in snake.positions[1:] or snake.positions[0] in wall.positions:
            done = True
 
 
        
 
runGame()
pygame.quit()
