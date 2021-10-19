# TODO add verifications ?

class Deck:
    """Deck object"""
    def __init__(self, deck_list):
        self.list = deck_list

    def shuffle(self):
        # shuffle order
        pass


class QuestsDeck(Deck):
    def __init__(self, deck_list):
        super().__init__(deck_list)

    def beginning_draw(self):
        # draw until five commons
        # select all commons
        # put them in quest log zone

        # put other cards in decks
        self.shuffle()

    def draw(self):
        pass

    # TODO : is it possible to link objectsq of different classes
    # quests deck and quest log zone for example


class BountiesDeck(Deck):
    def __init__(self, deck_list):
        super().__init__(deck_list)

    def draw(self, player):
        # give a certain player the top card of the deck
        pass


if __name__ == '__main__':
    pass
