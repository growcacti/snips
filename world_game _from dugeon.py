






OFFSETS = {"n": (0, -1), "s": (0, 1), "e": (1, 0), "w": (-1, 0)}

class Gameplay
def __init__(self, num_levels, num_rooms_per_floor, cell_size):
    self.levels = {}
    for x in range(num_levels):
        level_num = x + 1
        num_rooms = randint(*num_rooms_per_floor)
        while True:
            try:
                level = WorldLevel(level_num, num_rooms, cell_size)
                break
            except Exception as e:
                pass
        self.levels[level_num] = level
      def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.quit = True

    def update(self, dt):
        mouse_pos = pg.mouse.get_pos()
        self.world.update(dt, mouse_pos)
        if self.world.done:
            self.next = self.world.next
            self.done = True
            self.world.done = False
            self.persist["world"] = self.world

    def draw(self, surface):
        self.world.draw(surface)

class World(object):
    def __init__(self, num_levels, num_rooms_per_floor, cell_size):
        self.levels = {}
        for x in range(num_levels):
            level_num = x + 1
            num_rooms = randint(*num_rooms_per_floor)
            while True:
                try:
                    level = WorldLevel(level_num, num_rooms, cell_size)
                    break
                except Exception as e:
                    pass
            self.levels[level_num] = level
        self.current_level = self.levels[1]
        indx = (
            self.current_level.entrance_index[0] + 1,
            self.current_level.entrance_index[1],
        )
        cell = self.current_level.level_grid.cells[(indx[0], indx[1])]
        self.player = Player(cell)
        self.done = False
        self.next = None
        self.ui = worldUI(self)

    def update(self, dt, mouse_pos):
        self.player.update(dt, self)
        self.current_level.update(dt, mouse_pos, self.player)
        self.ui.update(self)

    def show_item(self, item_name):
        self.done = True
        self.next = "SHOW_ITEM"
        self.args = [item_name]

    def draw(self, surface):
        self.current_level.draw(surface, self.player)
        self.ui.draw(surface)

class worldLevel(object):
    connection_distance_range = (3, 16)
    room_size_range = (7, 23)
    opposites = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e",
        "top": "bottom",
        "bottom": "top",
        "left": "right",
        "right": "left",
        "-inner": "-outer",
        "-outer": "-inner",
    }
    grid_size = 600
    scroll_speed = 4

    def __init__(self, level_num, num_rooms, cell_size):
        self.topleft = [
            -(cell_size * (self.grid_size // 2)) + (prepare.SCREEN_SIZE[0] // 2),
            -(cell_size * (self.grid_size // 2)) + (prepare.SCREEN_SIZE[1] // 2),
        ]
        self.num_rooms = num_rooms
        num_branches = randint(1, int(sqrt(num_rooms)) + 1)
        self.level_num = level_num
        self.level_grid = LevelGrid(self.grid_size, self.grid_size, cell_size)
        apportioned = self.apportion_branches(num_rooms, num_branches)
        numbered = self.number_rooms(apportioned)
        entrance_num = numbered[0][0]
        exit_num = numbered[0][-1]
        splits = self.pick_split_spots(numbered)
        connections = self.make_connections(numbered, splits)
        room_map = self.make_room_map(numbered)
        self.make_rooms(connections, room_map, cell_size)
        self.entrance_index = self.rooms[entrance_num].center_index
        self.exit_index = self.rooms[exit_num].center_index
        self.staircases = pg.sprite.Group()
        Staircase(self.entrance_index, -1, self, self.staircases)
        Staircase(self.exit_index, 1, self, self.staircases)

        self.monsters = pg.sprite.Group()
        self.add_monsters()
        self.add_items()

    def add_monsters(self):
        num_encounters = randint(self.level_num * 2, self.level_num * 4)
        while num_encounters:
            room_num = choice(list(self.rooms.keys()))
            monster = choice(list(monster_images.keys()))
            self.rooms[room_num].add_monster(monster, self)
            num_encounters -= 1

    def add_items(self):
        items = LEVEL_ITEMS[self.level_num]
        for item_type, name in items:
            while True:
                room = choice(list(self.rooms.values()))
                cell = room.get_open_cell()
                if cell:
                    item = ItemIcon(item_type, name, cell, room.items)
                    cell.occupant = item
                    break

    def update(self, dt, mouse_pos, player):
        if player.acted:
            self.monsters.update(self, player)
        player.acted = False

    def get_random_room_size(self):
        w = randint(*self.room_size_range)
        h = randint(*self.room_size_range)
        return w, h

    def apportion_branches(self, num_rooms, num_branches):
        if num_branches == 1:
            return [num_rooms]
        rooms_left = num_rooms
        branches_left = num_branches
        branches = []
        for _ in range(num_branches):
            num = randint(1, (rooms_left - branches_left) + 1)
            branches.append(num)
            rooms_left -= num
            branches_left -= 1
        return sorted(branches, reverse=True)

    def number_rooms(self, branches):
        total = sum(branches)
        branch_rooms = []
        current = 0
        for b in branches:
            branch = []
            for x in range(b):
                branch.append(current)
                current += 1
            branch_rooms.append(branch)
        return branch_rooms

    def pick_split_spots(self, branch_rooms):
        num_splits = len(branch_rooms) - 1
        valid = branch_rooms[0][:-1]
        split_spots = []
        for i, branch in enumerate(branch_rooms):
            if num_splits:
                while True:
                    spot = choice(valid)
                    if split_spots.count(spot) < 2:
                        split_spots.append((spot, i + 1))
                        num_splits -= 1
                        break
        return split_spots

    def make_connections(self, branch_rooms, split_spots):
        connections = []
        for branch in branch_rooms:
            for i, room_num in enumerate(branch, start=1):
                try:
                    connections.append((room_num, branch[i]))
                except IndexError:
                    pass
                for split_num, branch_num in split_spots:
                    if room_num == split_num:
                        connections.append((room_num, branch_rooms[branch_num][0]))
        return connections

    def make_room_map(self, branch_rooms):
        room_map = {}
        for b in branch_rooms:
            for n in b:
                room_map[n] = [self.get_random_room_size(), ["e", "w", "n", "s"]]
        return room_map

    def make_rooms(self, connections, room_map, cell_size):
        start_index = self.level_grid.center_index
        rooms = {0: Room(0, room_map[0][0], start_index, cell_size, self.level_grid)}
        rooms[0].discovered = True
        paths = []
        for connection in connections:
            self.add_room(connection, rooms, paths, room_map, cell_size)
        self.hallways = []
        for path in paths:
            hallway = Hallway(path, self.level_grid)
            self.hallways.append(hallway)
        for hall in self.hallways:
            hall.add_floors(self.level_grid)
        for h in self.hallways:
            h.add_walls(self.level_grid)
        self.rooms = rooms

        for room in self.rooms.values():
            room.make_image()
        for hallway in self.hallways:
            hallway.make_image()

    def add_room(self, connection, rooms, paths, room_map, cell_size):
        origin_num, dest_num = connection
        try:
            origin = rooms[origin_num]
        except KeyError:
            pass
        room_rects = [room.rect for room in rooms.values()]
        room_rects.extend([cell.rect for p in paths for cell in p])
        left, top = origin.topleft_index
        bottom = top + origin.cells_high
        right = left + origin.cells_wide
        cw, ch = room_map[connection[1]][0]
        dist = randint(*self.connection_distance_range)
        buffer_w = (cw // 2) + 1
        buffer_h = (ch // 2) + 1
        spots = {
            "n": (origin.center_index[0], top - (dist + buffer_h)),
            "s": (origin.center_index[0], bottom + (dist + buffer_h)),
            "e": (right + (dist + buffer_w), origin.center_index[1]),
            "w": (left - (dist + buffer_w), origin.center_index[1]),
        }
        new_dimensions = room_map[dest_num][0]
        new_size = [x * cell_size for x in new_dimensions]
        directions = room_map[origin_num][1][:]
        shuffle(directions)
        for direction in directions:
            opposite = self.opposites[direction]
            spot = spots[direction]
            center = [s * cell_size for s in spot]
            new_rect = pg.Rect((0, 0), new_size)
            new_rect.center = center
            for rect in room_rects:
                if rect.colliderect(new_rect):
                    break
            else:
                new_room = Room(
                    dest_num, new_dimensions, spot, cell_size, self.level_grid
                )
                rooms[dest_num] = new_room
                room_map[origin_num][1].remove(direction)
                room_map[dest_num][1].remove(opposite)
                origin_door = origin.door_indices[direction]
                dest_door = new_room.door_indices[opposite]
                origin.door_directions.append(direction)
                new_room.door_directions.append(opposite)
                o_cell = self.level_grid.cells[origin_door]
                d_cell = self.level_grid.cells[dest_door]
                o_cell.occupant = Door(o_cell, direction, origin_num, origin.doors)
                d_cell.occupant = Door(d_cell, opposite, dest_num, new_room.doors)
                o_cell.terrain = "door"
                d_cell.terrain = "door"
                path = self.level_grid.find_path(
                    origin_door, dest_door, ["empty"], "Moore", 1
                )
                paths.append(path)
                return

    def make_level_image(self):
        surf = pg.Surface(self.level_grid.rect.size)
        for room in self.rooms.values():
            surf.blit(room.image, room.rect)
        for hallway in self.hallways:
            surf.blit(hallway.image, hallway.rect)
        self.image = surf

    def draw(self, surface, player):
        surface.fill(pg.Color("gray5"))
        doors = []
        for room in self.rooms.values():
            if room.discovered:
                surface.blit(room.image, room.rect.move(self.topleft))
                for item in room.items:
                    surface.blit(item.image, item.rect.move(self.topleft))
                for door in room.doors:
                    doors.append((door.image, door.rect.move(self.topleft)))
        for hallway in self.hallways:
            if hallway.discovered:
                surface.blit(hallway.image, hallway.rect.move(self.topleft))
                for door in hallway.doors:
                    doors.append((door.image, door.rect.move(self.topleft)))
        for stairs in self.staircases:
            surface.blit(stairs.image, stairs.rect.move(self.topleft))
        for monster in self.monsters:
            if monster.room.discovered:
                surface.blit(monster.image, monster.rect.move(self.topleft))
        surface.blit(player.image, player.rect.move(self.topleft))
        for img, rect in doors:

class worldUI(object):
    def __init__(self, world):
        left = prepare.SCREEN_RECT.right - 48
        style = {"font_size": 24, "text_color": "gray80"}
        self.labels = pg.sprite.Group()
        self.attack_label = Label("0", {"topleft": (left, 8)}, self.labels, **style)
        self.defense_label = Label("0", {"topleft": (left, 56)}, self.labels, **style)
        self.update_labels(world)
        sheet = prepare.GFX["sheet"]
        self.sword = strip_from_sheet(sheet, (1312, 1504), (32, 32), 1)[0]
        self.shield = strip_from_sheet(sheet, (1408, 1408), (32, 32), 1)[0]
        left = prepare.SCREEN_RECT.right - 96
        self.sword_rect = self.sword.get_rect(topleft=(left, 8))
        self.shield_rect = self.shield.get_rect(topleft=(left, 56))
        self.health_bar = HealthBar()

    def update_labels(self, world):
        player = world.player
        att = player.strength
        if player.items["Melee Weapon"]:
            att += player.items["Melee Weapon"].stats["Attack"]
        if "{}".format(att) != self.attack_label.text:
            self.attack_label.set_text("{}".format(att))
        defense = player.reflexes
        if player.items["Armor"]:
            defense += player.items["Armor"].stats["Defense"]
        if "{}".format(defense) != self.defense_label.text:
            self.defense_label.set_text("{}".format(defense))

    def update(self, world):
        self.update_labels(world)
        self.health_bar.update(world)

    def draw(self, surface):
        surface.blit(self.sword, self.sword_rect)
        surface.blit(self.shield, self.shield_rect)
        self.labels.draw(surface)
        self.health_bar.draw(surface)


class HealthBar(object):
    def __init__(self):
        self.rect = pg.Rect(8, 8, 160, 16)
        self.fill_color = "gray30"
        self.frame_color = "gray40"
        self.bar_color = (0, 128, 64)

    def update(self, world):
        player = world.player
        val = player.health / float(player.max_health)
        w = int(val * self.rect.w)
        self.bar = pg.Rect(self.rect.topleft, (w, self.rect.h))

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color(self.fill_color), self.rect)
        pg.draw.rect(surface, pg.Color(*self.bar_color), self.bar)
        pg.draw.rect(surface, pg.Color(self.frame_color), self.rect, 2)



class GridCell(object):
    def __init__(self, cell_index, cell_size, terrain=None):
        self.cell_index = cell_index
        self.terrain = "empty" if terrain is None else terrain
        self.occupant = None
        self.rect = pg.Rect(
            cell_index[0] * cell_size, cell_index[1] * cell_size, cell_size, cell_size
        )


class LevelGrid(object):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, width, height, cell_size):
        self.cells = {
            (x, y): GridCell((x, y), cell_size)
            for x in range(width)
            for y in range(width)
        }
        self.rooms = []
        self.rect = pg.Rect(0, 0, width * cell_size, height * cell_size)
        self.center_index = (width // 2, height // 2)
        self.empty_color = (30, 17, 40)

    def get_neighbors(self, cell_index, neighborhood="Moore", depth=1):
        x, y = cell_index
        neighbors = []
        if neighborhood == "vonNeuman":
            offsets = [
                (1, -1),
                (1, 0),
                (1, 1),
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
            ]
        else:
            offsets = self.offsets
        for off in offsets:
            try:
                nx, ny = x + off[0], y + off[1]
                n = self.cells[(nx, ny)]
                neighbors.append(n)
            except KeyError:
                pass
        return neighbors

    def find_path_to(
        self, origin, destination, valid_terrains, neighborhood="Moore", depth=1
    ):
        origin = self.cells[origin]
        destination = self.cells[destination]
        visited = set()
        levels = [[(origin, origin)]]
        while True:
            neighbors = []
            for cell, parent in levels[-1]:
                candidates = self.get_neighbors(cell.cell_index, neighborhood, depth)
                for c in candidates:
                    if c == destination:
                        levels.append([(c, cell)])
                        return levels
                    if c not in visited and c.terrain in valid_terrains:
                        neighbors.append((c, cell))
                    visited.add(c)
            if neighbors:
                levels.append(neighbors)
            else:
                return None

    def backtrack(self, path_cells):
        dest = path_cells[-1][0][0]
        route = [dest]
        for level in path_cells[::-1]:
            for cell, parent in level:
                if parent == path_cells[0][0][0]:
                    route.append(parent)
                    return route[::-1]
                if cell == route[-1]:
                    route.append(parent)
                    break

    def find_path(
        self, origin, destination, valid_terrains, neighborhood="Moore", depth=1
    ):
        to = self.find_path_to(origin, destination, valid_terrains, neighborhood, depth)
        if to:
            return self.backtrack(to)
          surface.blit(img, rect)


image_info = {"Snake": [(1088, 128), (32, 32)], "Gargoyle": [(1024, 192), (32, 32)]}

IMAGES = {}
for name in image_info:
    spot, size = image_info[name]
    IMAGES[name] = strip(prepare.GFX["sheet"], spot, size, 1)[0]


class Monster(pg.sprite.Sprite):
    def __init__(self, name, cell_index, room, level, *groups):
        super(Monster, self).__init__(*groups)
        self.image = IMAGES[name]
        self.cell_index = cell_index
        self.rect = level.level_grid.cells[cell_index].rect
        self.room = room
        self.state = "Idle"
        self.speed = 2
        self.range = 1
        self.attack_bonus = 5
        self.damage = (1, 3)
        self.defense = 8
        self.health = 5

    def move_to(self, cell, level):
        old_cell = level.level_grid.cells[self.cell_index]
        old_cell.occupant = None
        self.cell_index = cell.cell_index
        cell.occupant = self
        self.rect = cell.rect.copy()

    def attack(self, player):
        attack = randint(1, 21) + self.attack_bonus
        if attack > player.defense:
            damage = randint(*self.damage)
            player.health -= damage

    def die(self, level):
        level.level_grid.cells[self.cell_index].occupant = None
        self.kill()

    def update(self, level, player):
        if self.health <= 0:
            self.die(level)
            return
        moves_left = self.speed

        if level.level_grid.cells[player.cell_index] in self.room.floor_cells:
            self.state = "Attacking"
        if self.state == "Attacking":
            neighbors = level.level_grid.get_neighbors(self.cell_index)
            floors = [x for x in neighbors if x.terrain == "floor"]
            open = [x for x in floors if x.occupant is None]
            for n in neighbors:
                if n.occupant == player:
                    self.attack(player)
                    break
            else:
                path = level.level_grid.find_path(
                    self.cell_index, player.cell_index, ["floor"], "Moore"
                )
                if path:


image_coords = {
    "Club": (0, 1152),
    "Short Sword": (160, 1152),
    "Long Sword": (192, 1152),
    "Chain Mail": (192, 1024),
    "Armor Suit": (192, 1056),
    "Spike Armor": (96, 1024),
}

IMAGES = {}
for name, coord in image_coords.items():
    img = strip_from_sheet(prepare.GFX["sheet"], coord, (32, 32), 1)[0]
    IMAGES[name] = img
icon_coords = {
    "Club": (0, 896),
    "Short Sword": (1024, 896),
    "Long Sword": (640, 896),
    "Chain Mail": (1056, 672),
    "Armor Suit": (992, 672),
    "Spike Armor": (1312, 672),
}
ICONS = {}
for name, coord in icon_coords.items():
    img = strip_from_sheet(prepare.GFX["sheet"], coord, (32, 32), 1)[0]
    ICONS[name] = img

STAT_NAMES = {"Melee Weapon": ["Attack", "Damage"], "Armor": ["Defense"]}
ITEM_STATS = {
    "Melee Weapon": {
        "Club": [5, (1, 4)],
        "Short Sword": [10, (2, 13)],
        "Long Sword": [10, (3, 25)],
    },
    "Armor": {"Chain Mail": [5], "Armor Suit": [10], "Spike Armor": [15]},
}
LEVEL_ITEMS = {
    1: [("Melee Weapon", "Club"), ("Armor", "Chain Mail")],
    2: [("Melee Weapon", "Short Sword")],
    3: [("Armor", "Armor Suit")],
    4: [("Melee Weapon", "Long Sword"), ("Armor", "Spike Armor")],
    5: [],
}


class ItemIcon(pg.sprite.Sprite):
    def __init__(self, item_type, item_name, cell, *groups):
        super(ItemIcon, self).__init__(*groups)
        self.cell = cell
        self.cell_index = cell.cell_index
        self.image = ICONS[item_name]
        self.rect = cell.rect.copy()
        self.item = PlayerItem(item_type, item_name)

    def interact(self, world):
        world.show_item(self)


class PlayerItem(object):
    def __init__(self, item_type, item_name):
        self.item_type = item_type
        self.name = item_name
        self.image = IMAGES[item_name]
        self.rect = self.image.get_rect()
        self.stats = {
            k: v
            for k, v in zip(STAT_NAMES[item_type], ITEM_STATS[item_type][item_name])
        }

    def draw(self, surface):
        surface.blit(self.image, self.rect)

             self.move_to(path[1], level)


