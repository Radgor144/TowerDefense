
class Mapa:
    def __init__(self, data, map_image):
        self.image = map_image
        self.level_data = data
        self.route1 = []
        self.route2 = []
        self.route3 = []

    def proccess_data(self):
        # wczytanie danych z jsona
        for layer in self.level_data["layers"]:
            if layer["name"] == "trasy":
                for obj in layer["objects"]:
                    route_name = obj.get("name")  # Pobieramy nazwę trasy
                    route_data = obj["polyline"]

                    if route_name == "trasa1":
                        self.route1 = self.process_waypoints(route_data, 0, 316)
                    elif route_name == "trasa2":
                        self.route2 = self.process_waypoints(route_data, 0, 545)
                    elif route_name == "trasa3":
                        self.route3 = self.process_waypoints(route_data, 770, 0)



    def process_waypoints(self, data, x, y):
        # iterate through waypoints to extract invidual sets of x and y coordinates
        waypoints = []
        for point in data:
            temp_x = point.get("x") + x
            temp_y = point.get("y") + y
            waypoints.append((temp_x, temp_y))
        return waypoints
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
