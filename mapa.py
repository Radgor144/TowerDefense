import pygame

class Mapa():
    def __init__(self, data, map_image):
        self.image = map_image
        self.level_data = data
        self.waypoints = []

    def proccess_data(self):
        # wczytanie danych z jsona
        for layer in self.level_data["layers"]:
            if layer["name"] == "trasy":
                for obj in layer["objects"]:
                    waypoint_data = obj["polyline"]
                    self.process_waypoints(waypoint_data)

    def process_waypoints(self, data):
        #iterate through waypoints to extract invidual sets of x and y coordinates
        for point in data:
            temp_x = point.get("x")
            temp_y = point.get("y") + 316
            self.waypoints.append((temp_x, temp_y))


    def draw(self, surface):
        surface.blit(self.image, (0, 0))