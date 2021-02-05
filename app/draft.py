import json
import random
import uuid

from enum import Enum
from .cards import *
from .errors import ApplicationError


class DraftUser(object):

    def __init__(self, name, user_id=None):
        self.name = name
        if not user_id:
            self.user_id = uuid.uuid1()
        self.picked_cards = []

    def add_card_pile(self, draft_pile):
        self.picked_cards.extend(draft_pile.clear_pile())
        return self.picked_cards

    def set_hidden_pile(self, card_list):
        self.hidden_pile = card_list

    def json(self):
        return {'name': self.name, 'user_id': self.user_id}

class DraftOptions(object):

    min_players = 2
    max_players = 2
    order = 0  # 0 for in order, 1 for reverse
    draft_set = 'KHM'
    packs_per_player = 3
    draft_piles_per_player = 2
    booster_options = None

    def __init__(self):
        self.__dict__.update(kwargs)


class DraftPile(object):

    def __init__(self, user_id):
        self.pile_id = uuid.uuid1()
        self.user_to_add_cards = user_id
        self.displayed_cards = []

    def add_card(self, card):
        self.displayed_cards.append(card)

    def clear_pile(self):
        cards_in_pile = self.displayed_cards
        self.displayed_cards = []
        return cards_in_pile

    def json(self):
        return {
            'pile_id': self.pile_id,
            'user_to_add_cards': self.user_to_add_cards,
            'cards': [c.json for c in self.displayed_cards],
        }


class DraftState(Enum):
    UNDEFINED = 0
    CREATED = 1
    STARTED = 2
    COMPLETE = 3
    TO_BE_DELETED = 4


class DraftController(object):

    self.draft_state = DraftState.UNDEFINED

    def __init__(self, id=None):
        # If ID is present, grab it from the database and populate the object.
        # Otherwise, just return empty object.
        if not id:
            return
        self.id = id
        self.load()


    def create_game(self, user, draft_options=None):
        if self.draft_state != DraftState.UNDEFINED:
            return ApplicationError('Game has already been created')
        if not draft_options:
            self.draft_options = DraftOptions()
        self.users = [user]
        self.active_user = user
        self.draft_state = DraftState.CREATED
        # Save
        return self

    def add_user(self, user):
        if self.draft_state != DraftState.CREATED:
            return ApplicationError(
                'Cannot add new players to a draft that is already started or not yet created.')
        if len(self.users) >= self.draft_options.max_players:
            return ApplicationError('Draft is already at max users.')
        for u in self.users:
            if u.name == user.name:
                return ApplicationError('User with that name already exists')
            if u.user_id = user.user_id:
                return ApplicationError('That user is already in the game')
        self.users.append(user)
        # Save
        return self


    def get_cards_for_user(self, user_id):
        user = None
        for u in self.users:
            if u.user_id = user_id:
                user = u
                break
        if not user:
            return ApplicationError('User id does not exist in draft')
        return user.card_pool

    def generate_hidden_pile(self, booster_options=None):
        booster_pile = []
        for i in range(packs_per_player):
            booster = cards.get_booster(
                self.draft_options.draft_set,
                self.draft_options.booster_options)
            booster_pile.extend(booster)
        booster_pile.shuffle()
        return booster_pile

    def start_game(self):
        if self.draft_state != DraftState.CREATED:
            return ApplicationError('Cannot start a draft that has already started or not yet been created')
        self.draft_state = DraftState.STARTED
        # Create empty draft piles
        self.piles = []
        for u in self.users:
            u.set_hidden_pile(self.generate_hidden_pile())
            for x in range(self.draft_options.draft_piles_per_player):
                self.piles.append(DraftPile(u.user_id))
        # Save
        return self

    def add_to_piles(self):
        user_hidden_piles = {
            u.user_id: u.hidden_pile
            for u in self.users
        }
        for p in self.piles:
            user_pile_to_pick_from = user_hidden_piles[p.user_to_add_cards]
            p.add_card(user_pile_to_pick_from.pop())
        return self.piles

    def draft_pile(self, user_id, pile_id):
        if self.draft_state != DraftState.STARTED:
            return ApplicationError('Cannot draft piles in a draft that is not in progress')
        user = None
        for u in self.users:
            if u.user_id = user_id:
                user = u
        if not user:
            return ApplicationError('User does not exist in this draft')
        pile = None
        for p in self.piles:
            if p.pile_id = pile_id:
                pile = p
                break
        if not pile:
            return ApplicationError('Pile with that ID does not exist in this draft')
        user.add_card_pile(pile)
        self.add_to_piles()
        # Save
        return self

    def load(self):
        assert self.id
        pass

    def save(self):
        # Get DB connection
        # Get info to save
        pass

    def json(self):
        return {
            'id': self.id,
            'draft_state': self.draft_state,
            'users': [u.json() for u in self.users],
            'piles': [p.json() for p in self.piles]
        }
