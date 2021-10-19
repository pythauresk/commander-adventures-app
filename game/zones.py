# MAIN IDEA : Zone are objects where other objects can interfere
# FIXME

class QuestLogZone:
    def __init__(self):
        self.slots = [None, None, None, None, None]
        self.counters = []  # counters for each players : how to do ?

    def get_beginning_cards(self, something):
        self.slots = something

    def abandon(self, slot):
        # abandon card in the slot 0 to 4
        pass


class AbandonZone:
    def __init__(self):
        self.list = []

    def receive_abandon(self):
        pass


class PlayerHand:
    def __init__(self):
        pass

    def draw_bounties(self):
        pass


class Hands:
    def __init__(self, player_num):
        # set players hand
        pass


if __name__ == '__main__':
    pass
