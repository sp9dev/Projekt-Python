from PIL import Image
import json
import pygame
pygame.font.init()
descfont = pygame.font.SysFont("Arial", 12, bold=1)

class IoTEntity:

    def __init__(self, name, type, xpos, ypos, window):
        self.name = name
        self.desctxt = descfont.render(self.name, True, (0,0,0), (200,200,200))
        self.type = type
        self.area = window.get_rect()
        self.x = xpos * float(self.area[2])
        self.y = ypos * float(self.area[3])
        self.icon = "resources/" + type + ".png"
        self.window = window
        self.ic = pygame.image.load(self.icon)
        self.ic = pygame.transform.scale(self.ic, (int(0.1 * self.area[2]), int(0.1 * self.area[2])))
        self.rect = self.ic.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.state = 0
        self.show_description = False
        self.msg = ""
        self.msgtxt = descfont.render(self.msg, True, (0,0,0), (200,200,200))
        self.dragging = False
        
    def update_icon(self):
        self.ic = pygame.image.load(self.icon)
        self.ic = pygame.transform.scale(self.ic, (int(0.1 * self.area[2]), int(0.1 * self.area[2])))
        self.rect = self.ic.get_rect()
        self.rect.topleft = (self.x, self.y)

    def handle(self, message):
        if self.type == "light":
            self.handle_light(message)
        if self.type == "sensor":
            self.handle_sensor(message)
        if self.type == "window":
            self.handle_window(message)
        if self.type == "door":
            self.handle_door(message)
    
    def handle_light(self, message):
        if message == "on":
            self.state = 1
            self.icon = "resources/lighton.png"
            self.update_icon()
        if message == "off":
            self.icon = "resources/lightoff.png"
            self.state = 0
            self.update_icon()
        print(str(self.state))
        
    def handle_sensor(self, message):
        self.msg = message
        self.msgtxt = descfont.render(self.msg, True, (0,0,0), (200,200,200))

    def handle_window(self, message):
        if message == "open":
            self.state = 1
            self.icon = "resources/windowopen.png"
            self.update_icon()
        if message == "closed":
            self.state = 0
            self.icon = "resources/windowclosed.png"
            self.update_icon()

    def handle_door(self, message):
        if message == "open":
            self.state = 1
            self.icon = "resources/dooropen.png"
            self.update_icon()
        if message == "closed":
            self.state = 0
            self.icon = "resources/doorclosed.png"
            self.update_icon()
    
    def update_pos(self):
        with open('config.json', 'r') as file:
            json_data = json.load(file)
            for item in json_data:
                if item == self.name:
                    item['xpos'] = float(self.x) / float(self.area[2])
                    item['ypos'] = float(self.y) / float(self.area[3])
        with open('config.json', 'w') as file:
            json.dump(json_data, file, indent=2)

    def toggle_description(self):
        self.show_description = not self.show_description

    def blit(self):
        if self.dragging == True:
            self.update_icon()
        if self.show_description == True:
            w, h = descfont.size(self.name)
            offset = ((0.1 * self.area[2]) - w)/2
            self.window.blit(self.desctxt, (self.x + offset, self.y - 20))
            if self.type == "sensor":
                w, h = descfont.size(self.msg)
                offset = ((0.1 * self.area[2]) - w)/2
                self.window.blit(self.msgtxt, (self.x + offset, self.y + (0.1 * self.area[2]) + 10))
        self.window.blit(self.ic, self.rect)
        
        

class HousePlan:

    def __init__(self, path):
        self.path = path
        self.im = Image.open(path)
        self.x = 0
        self.y = 0
        self.x_size, self.y_size = self.im.size
        
