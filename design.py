import pygame, random
import os, math, time
from datetime import datetime

time_delta = datetime.strptime('2018-03-21T14:35:18.000Z', '%Y-%m-%dT%H:%M:%S.000Z')
gg = False
ww = False
www = False
w = 1200
h = 600
rgb = (120, 120, 120)
fps = 60
a = -10
b = 15
bulletspeedx = 5
bulletspeedy = 5
wp = 25
hp = 50
wb = 10
hb = 10
particles = []
particles1 = []
particles2 = []
BLUE = (0, 0, 255)
fixspeed = 20
# Переменные для установки ширины и высоты окна
SCREEN_WIDTH = 1000  # 1500
SCREEN_HEIGHT = 600  # 700

directory = 'бег'
files = os.listdir(directory)
images = filter(lambda x: x.endswith('.gif'), files)
pers = list(images)
directory = 'прыг'
files = os.listdir(directory)
images = filter(lambda x: x.endswith('.gif'), files)
prig = list(images)
directory = 'стрельба'
files = os.listdir(directory)
images = filter(lambda x: x.endswith('.gif'), files)
sshot = list(images)
print(sshot)
# Подключение фото для заднего фона
# Здесь лишь создание переменной, вывод заднего фона ниже в коде
bg = pygame.image.load('blue.jpeg')
zzz = True
canshoot = True
cantp = True

# Класс, описывающий поведение главного игрока
class Player(pygame.sprite.Sprite):
    # Изначально игрок смотрит вправо, поэтому эта переменная True
    if zzz:
        right = True
    else:
        right = False
    change_y = 0

    # Методы
    def __init__(self):
        global rect
        self.change_tp = 60
        self.k = 0
        self.b = 15
        self.c = 0
        # Стандартный конструктор класса
        # Нужно ещё вызывать конструктор родительского класса
        super().__init__()

        # Создаем изображение для игрока
        # Изображение находится в этой же папке проекта
        self.image = pygame.image.load('imgonline-com-ua-Resize-7XzS01XpL1HN9.png')

        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()
        rect = self.rect
        self.change_tp_per = 0
        # Задаем вектор скорости игрока
        self.change_x = 0
        self.change_y = 0

    def update(self):
        global pers
        global rect
        global k
        global www
        global px, py
        # В этой функции мы передвигаем игрока
        # Сперва устанавливаем для него гравитацию
        self.calc_grav()
        # Передвигаем его на право/лево
        # change_x будет меняться позже при нажатии на стрелочки клавиатуры
        self.rect.x += self.change_x
        if self.change_y != 1 and self.change_y != 0:
            self.image = pygame.image.load('прыг/' + str(prig[15]))
            if not zzz:
                self.flip()
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        elif self.change_x != 0:
            if self.k != 60:
                self.image = pygame.image.load('бег/' + str(pers[int(self.k)]))
                www = True
                if not self.right:
                    self.flip()
                self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
                if not self.right:
                    px, py = self.rect.bottomright[0] - 10, self.rect.bottomright[1]
                else:
                    px, py = self.rect.bottomleft[0] + 10, self.rect.bottomleft[1]
                self.k += 1
            else:
                self.k = 0
        elif k == 0:
            self.image = pygame.image.load('imgonline-com-ua-Resize-7XzS01XpL1HN9.png')
            if not zzz:
                self.flip()
                self.right = True
                self.zzz = False
        if self.change_tp != 240:
            self.change_tp += self.change_tp_per
        # Следим ударяем ли мы какой-то другой объект, платформы, например
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # Перебираем все возможные объекты, с которыми могли бы столкнуться
        for block in block_hit_list:
            # Если мы идем направо,
            # устанавливает нашу правую сторону на левой стороне предмета, которого мы ударили
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # В противном случае, если мы движемся влево, то делаем наоборот
                self.rect.left = block.rect.right

        # Передвигаемся вверх/вниз
        self.rect.y += self.change_y

        # То же самое, вот только уже для вверх/вниз
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Устанавливаем нашу позицию на основе верхней / нижней части объекта, на который мы попали
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Останавливаем вертикальное движение
            self.change_y = 0
        rect = self.rect

    def calc_grav(self):
        global rect
        # Здесь мы вычисляем как быстро объект будет
        # падать на землю под действием гравитации
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # Если уже на земле, то ставим позицию Y как 0
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
        rect = self.rect

    def Shoot(self):
        global zzz
        global k
        global t1
        global canshoot
        if canshoot:
            speedx = 25
            if not zzz:
                speedx *= -1
            else:
                speedx *= 1
            if k == 8:
                shoot_sound = pygame.mixer.Sound('tetiva.wav')
                shoot_sound.play()
            # if self.change_y == 0 and self.change_x == 0:
            if self.c != 57:
                self.image = pygame.image.load('стрельба/' + str(sshot[self.c]))
                if not zzz:
                    self.flip()
                self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
                self.c += 1
                if self.c == 35:
                    shoot_sound = pygame.mixer.Sound('strela.wav')
                    shoot_sound.play()
                    t1 = datetime.now()
                if self.c == 45:
                    if speedx < 0:
                        bullet = Bullet(self.rect.centerx - 43, self.rect.centery - 15, speedx)
                    else:
                        bullet = Bullet(self.rect.centerx - 27, self.rect.centery - 15, speedx)
                    bullets.add(bullet)
                    active_sprite_list.add(bullet)
            else:
                self.c = 0
                canshoot = False
        else:
            self.reload()
            if canshoot:
                self.Shoot()

    def reload(self):
        global t1
        global time_delta
        global canshoot
        time_delta = datetime.now() - t1
        if time_delta.total_seconds() >= 10:
            canshoot = True

    def reload_tp(self):
        global t2
        global time_delta_tp
        global cantp
        time_delta_tp = datetime.now() - t2
        if time_delta_tp.total_seconds() >= 18:
            cantp = True

    def teleport(self):
        global gg
        global tx, ty
        tx = self.rect.x
        ty = self.rect.y
        if zzz:
            self.rect.x += self.change_tp
        else:
            self.rect.x -= self.change_tp
        self.change_tp = 60
        self.change_tp_per = 0
        gg = False

    def tele(self):
        global cantp
        if cantp:
            global gg
            global t2
            t2 = datetime.now()
            gg = True
            self.change_tp_per = 6
            cantp = False
        else:
            self.reload_tp()
            if cantp:
                self.tele()
            else:
                self.change_tp = 0

    def jump(self):
        global rect
        # Обработка прыжка
        # Нам нужно проверять здесь, контактируем ли мы с чем-либо
        # или другими словами, не находимся ли мы в полете.
        # Для этого опускаемся на 10 единиц, проверем соприкосновение и далее поднимаемся обратно
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        # Если все в порядке, прыгаем вверх
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -16
        rect = self.rect

    def down(self):
        global rect
        self.change_y = 16
        rect = self.rect

    # Передвижение игрока
    def go_left(self):
        global zzz
        self.change_x = -9  # Двигаем игрока по Х
        if self.right:  # Проверяем куда он смотрит и если что, то переворачиваем его
            self.flip()
            self.right = False
        zzz = False

    def go_right(self):
        global zzz
        self.change_x = 9
        if not self.right:
            self.flip()
            self.right = True
        zzz = True

    def stop(self):
        global www
        global zzz
        www = False
        # вызываем этот метод, когда не нажимаем на клавиши
        self.image = pygame.image.load('imgonline-com-ua-Resize-7XzS01XpL1HN9.png')
        if not self.right and self.k != 0:
            self.flip()
            self.right = True
            zzz = False
        self.k = 0
        self.change_x = 0

    def flip(self):
        # переворот игрока (зеркальное отражение)
        self.image = pygame.transform.flip(self.image, True, False)


# class Arrow(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.arr = pygame.image.load('Стрела.png')
#         self.arrect = self.arr.get_rect(topleft=(rect.x + 20, rect.y - 5))


# Класс для описания платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Конструктор платформ
        super().__init__()
        # Также указываем фото платформы
        self.image = pygame.image.load('platform.png')

        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()


class Rel_plat(pygame.sprite.Sprite):
    def __init__(self, width):
        # Конструктор платформ
        super().__init__()
        # Также указываем фото платформы
        if width == 0:
            self.image = pygame.image.load('Strel.png')
        else:
            self.image = pygame.image.load('Tp_Rel.png')

        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()


# Класс для расстановки платформ на сцене
class Level(object):
    def __init__(self, player):
        # Создаем группу спрайтов (поместим платформы различные сюда)
        self.platform_list = pygame.sprite.Group()
        self.reload_list = pygame.sprite.Group()
        # Ссылка на основного игрока
        self.player = player

    # Чтобы все рисовалось, то нужно обновлять экран
    # При вызове этого метода обновление будет происходить
    def update(self):
        self.platform_list.update()
        self.reload_list.update()

    # Метод для рисования объектов на сцене
    def draw(self, screen):
        # Рисуем задний фон
        screen.blit(bg, (0, 0))
        # Рисуем все платформы из группы спрайтов
        self.platform_list.draw(screen)
        self.reload_list.draw(screen)


# Класс, что описывает где будут находится все платформы
# на определенном уровне игры
class Level_01(Level):
    def __init__(self, player):
        # Вызываем родительский конструктор
        Level.__init__(self, player)

        # Массив с данными про платформы. Данные в таком формате:
        # ширина, высота, x и y позиция
        level = [
            [210, 32, 500, 500],
            [210, 32, 200, 400],
            [210, 32, 600, 300],
        ]
        rel = [[10, 10], [70, 10]]

        # Перебираем массив и добавляем каждую платформу в группу спрайтов - platform_list
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        for platform in rel:
            block = Rel_plat(rel.index(platform))
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.reload_list.add(block)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx):

        global ww
        ww = True
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Стрела.png')
        if speedx < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx

    def update(self):
        global ww
        global mx, my
        self.rect.x += self.speedx
        if self.speedx < 0:
            mx, my = self.rect.x - 4, self.rect.y + 2
        else:
            mx, my = self.rect.x + 67, self.rect.y + 2
        if self.rect.x > SCREEN_WIDTH + 200:
            self.kill()
        elif self.rect.x < -200:
            self.kill()


k = 0
bullets = pygame.sprite.Group()

active_sprite_list = pygame.sprite.Group()


# Основная функция прогарммы
def main():
    global k
    global screen
    global time_delta
    global time_delta_tp
    # Инициализация
    pygame.init()

    # Установка высоты и ширины
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Название игры
    pygame.display.set_caption("Платформер")

    # Создаем игрока
    player = Player()

    # Создаем все уровни
    level_list = list()
    level_list.append(Level_01(player))

    # Устанавливаем текущий уровень
    current_level_no = 0
    current_level = level_list[current_level_no]

    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    zu = 0
    # Цикл будет до тех пор, пока пользователь не нажмет кнопку закрытия
    done = False

    # Используется для управления скоростью обновления экрана
    clock = pygame.time.Clock()

    # Основной цикл программы
    while not done:
        # Отслеживание действий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если закрыл программу, то останавливаем цикл
                done = True
            if k == 0:
                # Если нажали на стрелки клавиатуры, то двигаем объект
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.go_left()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.go_right()
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.jump()
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.down()
                    if event.key == pygame.K_e:
                        player.tele()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0 or event.key == pygame.K_a and \
                            player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0 or event.key == pygame.K_d and \
                            player.change_x > 0:
                        player.stop()
                    if event.key == pygame.K_e:
                        player.teleport()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        if player.change_x == 0 and player.change_y == 0:
                            player.Shoot()
                            if canshoot:
                                k += 1
                                if k == 58:
                                    k = 0
        if k != 0:
            if canshoot:
                player.Shoot()
                k += 1
                if k == 58:
                    k = 0
        # Обновляем игрока
        active_sprite_list.update()

        # Обновляем объекты на сцене
        current_level.update()
        bullets.update()

        # Если игрок приблизится к правой стороне, то дальше его не двигаем
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        # Если игрок приблизится к левой стороне, то дальше его не двигаем
        if player.rect.left < 0:
            player.rect.left = 0

        # Рисуем объекты на окне
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        if ww:
            particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
            for particle in particles:
                particle[0][1] -= particle[1][0]

                particle[2] -= 0.1
                particle[1][1] += 0.1
                pygame.draw.circle(screen, (226, 88, 34), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 0:
                    particles.remove(particle)
        if www:
            particles1.append([[px, py], [random.randint(1, 2), 2], random.randint(2, 4)])
            for particle in particles1:
                particle[0][1] -= particle[1][0]
                particle[2] -= 0.1
                particle[1][1] += 0.1
                pygame.draw.circle(screen, rgb, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 2:
                    particles1.remove(particle)
        else:
            for particle in particles1:
                particle[0][1] -= particle[1][0]
                particle[2] -= 0.1
                particle[1][1] += 0.1
                pygame.draw.circle(screen, rgb, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                if particle[2] <= 2:
                    particles1.remove(particle)
        if gg:
            zu = 1
            if zzz:
                pygame.draw.circle(screen, (0, 0, 255),
                                   [int(player.rect.x + player.change_tp + 10), int(player.rect.centery - 5)], 6)
            else:
                pygame.draw.circle(screen, (0, 0, 255),
                                   [int(player.rect.x - player.change_tp + 30), int(player.rect.centery - 5)], 6)
            if zzz:
                particles2.append([[int(player.rect.x + player.change_tp + 10), int(player.rect.centery - 5)],
                                   [2, -2], random.randint(1, 2), random.randint(1, 3)])
            else:
                particles2.append([[int(player.rect.x - player.change_tp + 30), int(player.rect.centery - 5)],
                                   [2, -2], random.randint(1, 2), random.randint(1, 3)])
            for particle in particles2:
                particle[0][1] += particle[1][1]
                particle[2] -= 0.05
                particle[1][1] += 0.05
                f = [int(particle[0][0]), int(particle[0][0]) - 1, int(particle[0][0]) + 1, int(particle[0][0]) - 2,
                     int(particle[0][0]) + 2, int(particle[0][0]) - 5, int(particle[0][0]) + 5]
                pygame.draw.circle(screen, (0, 0, 255), [
                    random.choice(f),
                    int(particle[0][1]) - 3], int(particle[2]))
                if particle[2] <= particle[3]:
                    particles2.remove(particle)

        if len(particles2) != 0 and not gg:
            for particle in particles2:
                particles2.remove(particle)
        if ww:
            p = Player()
            p.reload()
            if time_delta.total_seconds() != 0 and int(time_delta.total_seconds()) < 10:
                f1 = pygame.font.Font(None, 45)
                text1 = f1.render(str(10 - int(time_delta.total_seconds())), True,
                                  (255, 0, 0))
                screen.blit(text1, (20, 25))
        if not gg and zu != 0:
            p = Player()
            p.reload_tp()
            if time_delta_tp.total_seconds() != 0 and int(time_delta_tp.total_seconds()) < 18:
                f1 = pygame.font.Font(None, 45)
                text1 = f1.render(str(18 - int(time_delta_tp.total_seconds())), True,
                                  (255, 0, 0))
                screen.blit(text1, (80, 25))

        # Устанавливаем количество фреймов
        clock.tick(30)
        # Обновляем экран после рисования объектов
        pygame.display.flip()
        pygame.display.update()

    # Корректное закртытие программы
    pygame.quit()


main()
