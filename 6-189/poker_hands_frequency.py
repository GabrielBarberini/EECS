"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

"""
Im aware that the solution I present bellow is not the best, but I like to save my struggles so I can look at them in the future and check if I've improved
by Gabriel Barberini
"""

from __future__ import print_function, division

from Card import Hand, Deck
from collections import Counter
import time


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has(self, n=2):
        self.rank_hist()
        if n in self.ranks.values(): return True
        return False

    def has_pair(self):
        return self.has(2) 

    def has_twopair(self):
        if list(self.ranks.values()).count(2) == 2: return True
        return False

    def has_three(self):
        return self.has(3) 

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_straight(self):
        if len(self.cards) < 5 or self.has((len(self.cards)%5)+1):
            return False

        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        ranks.sort()

        if ranks[-1] == 13 and ranks[0] == 1\
                and ranks[(len(ranks)-4):] == [10,11,12,13]:
                    self.straight = [10,11,12,13,1]
                    return True

        while len(ranks) >= 5:
            straight = list(range(ranks[0],ranks[0]+5))
            if ranks[0:5] == straight:
                self.straight = ranks[0:5]
                return True
            else:
                ranks.pop(0)
        return False

    def has_fullhouse(self):
        return self.has(3) and self.has(2)

    def has_foak(self):
        return self.has(4)

    def has_straightflush(self):
        if self.has_straight() and self.has_flush():
            suits = set() 
            for card in self.cards:
                if card.rank in self.straight:
                    suits.add(card.suit)
            return len(suits) == 1 

    def classify(self):
        classes = [ self.has_straightflush(), self.has_foak(), self.has_fullhouse(), self.has_straight(), self.has_flush(), self.has_three(), self.has_twopair(), self.has_pair() ]
        labels = { 
                0: "straightflush", 
                1: "foak",
                2: "fullhouse",
                3: "straight",
                4: "flush",
                5: "three",
                6: "twopair",
                7: "pair"
        }
        
        for i in range(len(classes)):
            if classes[i] == True:
                self.label = labels[i]
                return None
        self.label = None 

def givenLabelCards(amount=7):
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    labels = Counter() 
    for i in range(amount):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.classify()
        labels.setdefault(hand.label, 0)
        labels[hand.label] += 1
    return labels

def findLabelFreq(iterations=70000):
    freq = Counter() 
    for i in range(iterations):
        freq.update(givenLabelCards())
    total = sum(freq.values())
    for key in freq:
        print(key, 100*round((freq[key]/total),5))

findLabelFreq()
