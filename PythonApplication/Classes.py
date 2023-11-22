class PlayerCharacter:

    def _init_(self, name, x_pos, health):
        self.name = name
        self.x_pos = x_pos
        self.health = health

    def move(self, by_amount):
        self.x_pos += by_amount

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def check_is_dead(self):
        #returns true if health is 0
        return self.health <= 0
