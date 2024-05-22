import pygame as pg
import game.resources as res

class Level():
    def __init__(self, index, platforms, enemies, obstacles, bonuses):
        self.index = index
        self.platforms_coord = platforms
        self.enemies = enemies
        self.obstacles = obstacles
        self.bonuses = bonuses
        self.bg = pg.sprite.Sprite()
        self.bg_group = pg.sprite.Group() # отдельная группа спрайтов для одного фона
        self.all_sprites = pg.sprite.Group()  # основные спрайты (колобок, враги, бонусы и т.п.)
        self.platforms = pg.sprite.Group()  # платформы - отдельно для проверки коллизий (для прыжков и падений)

    def create_level(self):
    # создание фона
        self.bg.image = pg.image.load(f"res/graphics/fon_0{self.index}.jpg")
        self.bg.rect = self.bg.image.get_rect()
        self.bg.rect.y = 0
        self.bg.rect.x = 0
        self.bg_group.add(self.bg)
    # создание платформ
        for platform in self.platforms_coord:
            self.create_grass(platform[0], platform[1], platform[2])


    def create_grass(self,x, y, length):  # вводные данные - стартовые координаты (х,у) и длина

        platform_end = x + length
        while x < platform_end:
            grass = pg.sprite.Sprite()
            grass.image = pg.image.load(f"res/graphics/grass_0{self.index}.png")
            grass.rect = grass.image.get_rect()
            grass.rect.y = y - grass.rect.height  # Позиционируем у нижнего края окна
            grass.rect.x = x
            self.platforms.add(grass)
            self.all_sprites.add(grass)
            x += grass.rect.width  # Перемещаем X на ширину спрайта для следующего спрайта

    def update(self):        # Обновление спрайтов
        self.bg_group.update()
        self.platforms.update()
        self.all_sprites.update()
        #print(self.all_sprites)

    def draw(self, screen):
        # Метод для отрисовки объектов уровня
        self.bg_group.draw(screen)
        self.platforms.draw(screen)
        self.all_sprites.draw(screen)




# Табло времени
class TextBox(pg.sprite.Sprite):
    def __init__(self, text, x, y):
        pg.sprite.Sprite.__init__(self)
        self.text = text
        self.font = pg.font.Font("res/font/arialbi.ttf", 30)
        self.image = self.font.render(self.text, False, res.RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.elapsed_time = 0
        self.formatted_time = self.format_time(self.elapsed_time)

    def format_time(self,milliseconds):
        # Преобразуем миллисекунды в секунды
        seconds = milliseconds // 1000
        # Получаем минуты и секунды
        minutes = seconds // 60
        seconds = seconds % 60
        # Форматируем время в строку MM:SS
        time_str = f"{minutes:02}:{seconds:02}"
        return time_str

    def update(self):
        self.text = self.format_time(self.elapsed_time)
        self.image = self.font.render(self.text, False, res.RED)




LEVEL1_PLATFORMS =[
    [0, 720, 1200],
    [200, 620, 300],
    [600, 520, 200],
    [450, 440, 50],
    [0, 320, 400],
    [500, 220, 200],
    [800, 300, 200],
    [1100, 400, 100]
]

LEVEL1_ENEMIES = []
LEVEL1_OBSTACLES = []
LEVEL1_BONUSES = []




LEVEL2_PLATFORMS =[
    [0, 720, 1200],
    [200, 620, 300],
    [700, 520, 200],
    [470, 430, 100],
    [500, 360, 400]
]

LEVEL2_ENEMIES = []
LEVEL2_OBSTACLES = []
LEVEL2_BONUSES = []