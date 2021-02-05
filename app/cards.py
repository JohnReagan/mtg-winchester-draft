import json
import os
import random

from .singleton import Singleton

basedir = os.path.abspath(os.path.dirname(__file__))
card_data_file = os.path.join(basedir, 'static/AllPrintings.json')


def _split_by_color(card_list):
    cards = {'W': [], 'U': [], 'B': [], 'R': [], 'G': [], 'other': []}
    for card in card_list:
        if len(card.colors) != 1:
            cards['other'].append(card)
        else:
            cards.get(card.colors[0]).append(card)
    return cards


def _split_by_rarity(card_list):
    cards = {'mythic': [], 'rare': [], 'uncommon': [], 'common': []}
    for card in card_list:
        try:
            cards.get(card.rarity).append(card)
        except (KeyError, AttributeError) as e:
            continue
    return cards


def _split_by_rarity_and_color(card_list):
    rarity_split = _split_by_rarity(card_list)
    for rarity, cards in rarity_split.items():
        rarity_split[rarity] = _split_by_color(cards)
    return rarity_split


ALLOWED_CARD_ARGS = [
    'name',
    'colors',
    'convertedManaCost',
    'scryfallId',
    'uuid',
    'rarity',
    'text',
    'setCode',
    'types',
    'supertypes'
]

class Card(object):

    def __init__(self, **kwargs):
        self.__dict__.update(
            (k, v) for k, v in kwargs.items() if k in ALLOWED_CARD_ARGS)

    @classmethod
    def from_json(cls, card_json):
        return cls(
            name=card_json.get('name', ''),
            colors=card_json.get('colors', ''),
            convertedManaCost=card_json.get('convertedManaCost', ''),
            scryfallId=card_json['identifiers'].get('scryfallId', ''),
            uuid=card_json.get('uuid', ''),
            rarity=card_json.get('rarity'),
            text=card_json.get('text', ''),
            setCode=card_json.get('setCode', ''),
            types=card_json.get('types', ''),
            supertypes=card_json.get('supertypes', '')
        )

    def json(self):
        return dict(
            (k, v) for k, v in self.__dict__.items() if (k in ALLOWED_CARD_ARGS))


class BoosterOptions(object):
    num_cards = 15
    is_custom_list = False
    rares_per_pack = 1
    uncommons_per_pack = 3
    mythic_replace_rate = 0.125
    contains_foil = True

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Booster(object):

    def __init__(self, card_list, booster_options=None):
        self.card_list = card_list
        if not booster_options:
            booster_options = BoosterOptions()
        self.booster_options = booster_options

    def pick_colors(self, card_list, amount):
        # Assume card list is a dictionary keyed off color
        picked_cards = []
        while len(picked_cards) < amount:
            color_list = ["W", "B", "U", "R", "G", "other"]
            random.shuffle(color_list)
            for color in color_list:
                if len(picked_cards) >= amount:
                    break
                color_card_list = card_list.get(color)
                if not color_card_list:
                    continue
                else:
                    card = random.choice(color_card_list)
                    if 'Basic' in card.supertypes:
                        # We never want to pick basic lands in Winchester draft.
                        continue
                    color_card_list.remove(card)
                    picked_cards.append(card)
                if random.random() < 0.15:
                    # 15% chance to break the color balance a little bit
                    break
        return picked_cards



    def generate(self):
        if False: # self.booster_options.is_custom_list:
            # Rates do not matter
            cards = _split_by_color(self.card_list)
            picked_cards = self.pick_colors(
                cards, self.booster_options.num_cards)
        else:
            # Rates do matter
            cards = _split_by_rarity_and_color(self.card_list)
            picked_cards = []
            # Choose rares
            num_mythics = sum([
                random.random() < self.booster_options.mythic_replace_rate
                for x in range(self.booster_options.rares_per_pack)])
            print('Num mythics: {}'.format(num_mythics))
            num_rares = self.booster_options.rares_per_pack - num_mythics
            print('Num rares: {}'.format(num_rares))
            if num_mythics:
                picked_mythics = self.pick_colors(cards['mythic'], num_mythics)
                picked_cards.extend(picked_mythics)
            picked_rares = self.pick_colors(cards['rare'], num_rares)
            picked_cards.extend(picked_rares)
            picked_uncommons = self.pick_colors(
                cards['uncommon'],
                self.booster_options.uncommons_per_pack)
            picked_cards.extend(picked_uncommons)
            picked_cards.extend(
                self.pick_colors(cards['common'],
                self.booster_options.num_cards - len(picked_cards)))
        self.cards = picked_cards
        return picked_cards



@Singleton
class CardDatabase(object):

    def __init__(self):
        with open(card_data_file, 'r', encoding='utf8') as jsonfile:
            file_data = json.loads(jsonfile.read())
        self.card_data = file_data['data']

    def get_card_data(self, set=None):
        if set:
            try:
                return self.card_data[set]['cards']
            except KeyError:
                return []
        return self.card_data


CARD_DB = CardDatabase.Instance()


def get_booster(set, booster_options=None):
    card_list = [Card.from_json(c) for c in CARD_DB.get_card_data(set)]
    booster = Booster(card_list, booster_options)
    return booster.generate()

def card_internal(card_json):
    return Card.from_json(card_json).json()

def get_all_cards(set=None):
    card_data = CARD_DB.get_card_data(set)
    return card_data
