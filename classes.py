from PIL import Image

class IoTEntity:

    def __init__(self, name, type, xpos, ypos):
        self.name = name
        self.type = type
        self.x = 0.0
        self.y = 0.0
        self.icon = "resources/" + type + ".png"
        self.state = 0
        self.msg = ""

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
        if message == "off":
            self.state = 0
        print(str(self.state))
        
    def handle_sensor(self, message):
        self.message = message

    def handle_window(self, message):
        if message == "open":
            self.state = 1
        if message == "closed":
            self.state = 0

    def handle_door(self, message):
        if message == "open":
            self.state = 1
        if message == "closed":
            self.state = 0

class HousePlan:

    def __init__(self, path):
        self.path = path
        self.im = Image.open(path)
        self.x = 0
        self.y = 0
        self.x_size, self.y_size = self.im.size
        
