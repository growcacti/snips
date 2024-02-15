# Old code in fire_spell
if angle > 90 and angle < 180:
    do_something()
elif angle > 180 and angle < 270:
    do_something_else()
# ...


# Refactored code
def perform_action_based_on_angle(angle):
    if angle > 90 and angle < 180:
        do_something()
    elif angle > 180 and angle < 270:
        do_something_else()


def fire_spell(self):
    angle = self.get_angle()
    self.perform_action_based_on_angle(angle)
