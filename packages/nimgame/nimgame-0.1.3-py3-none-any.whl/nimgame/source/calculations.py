"""The Nim Game calculation functions
"""


import functools
import random
from source.typedefs import Move, ErrorRate


class EndGameCheck():
    """Class for handling the end-game if it is misere type
    
    The instance can be checked in a bool context, indicating whether the status
    is the beginning of the end-game.
    
    Methods:
    - check_heap() gets a heap index and number of coins in the heap. It then
        sets the internal status attributes (see below). This method is called
        in a loop for all heaps and then provides the status of the game
        indicating whether it is the beginning of the end-game.
    - get_move() returns the required move at the beginning of end-game
    
    Attributes:
    - one_manycoins: Indicator whether all active heaps are single-coin, but
        one. This is when the end-game starts.
    - even_singlecoins: Indicator whether the number of single-coin heaps is
        even or odd. This is needed to figure out the move at the beginning of
        the end-game.
    """
    one_manycoins = None
    even_singlecoins = True
    
    def __bool__(self):
        return bool(self.one_manycoins)
    
    def check_heap(self,
                idx: int, 
                heapcount: int, 
    ) -> None:
        if heapcount>1:
            if self.one_manycoins is None:
                self.one_manycoins = True
                self.heapcount = heapcount
                self.heapidx = idx
            else:
                self.one_manycoins = False
        
        elif heapcount==1:
            self.even_singlecoins = not self.even_singlecoins
    
    def get_move(self) -> Move:
        #even number of heaps with 1 coin?
        if self.even_singlecoins:
            #remove all but 1 coin from the heap which has more coins
            removecount = self.heapcount-1
        else:
            #remove all coins from the heap which has more coins
            removecount = self.heapcount
        #remove coins so that odd number of 1-coin heaps remain
        return Move(self.heapidx, removecount)


class Mixin:
    """Class to implement the Nim game calculations

    Methods:
    - make_good_choice(): figure out whether to make a good decision
    - get_nimsum(): 'nimsum' is a special sum of the heaps
    - all_one_heaps(): it indicates whether all heaps have either 1 or zero
        coins
    - is_winning_for_next(): it indicates whether the current status is good for
        the player having the next turn
    - get_random_move(): just a utility to pick a heap and coins randomly
    - figure_out_best_move(): intelligently figure out the next best move
    """
    def make_good_choice(self) -> bool:
        """Figure out whether the good choise is to be made

        The required error rate indicates how bad decisions the Computer is to
        make. The higher the error rate percentage the higher the possibility
        that the Computer makes a bad move/decision. If error_rate is 0, this
        function always returns True, i.e. the Computer always makes a good
        decision. If error_rate is 100, the Computer always makes a bad decision.

        Returns:
            False forces to make the bad choise
        """
        #figure out the error rate for the current player
        if isinstance(self.error_rate, ErrorRate):
            activeplayer = self.activeplayer
            if activeplayer == 'start':
                activeplayer = 'Computer'
            error_rate = getattr(self.error_rate, activeplayer)
        else:
            error_rate = self.error_rate
        
        #get a random percentage
        randompercentage = random.randint(0, 99)
        
        #return true/false based on the required error rate
        return randompercentage >= error_rate


    def get_nimsum(self) -> int:
        """Calcualte the nimsum of the set of heaps

        Use the functools.reduce() on the heaps list, with a 0 initializing
        value and use XOR for the coin counts of the heaps.

        Returns:
            The nimsum of the heap-set
        """
        return functools.reduce(
            lambda a, b: a^b,
            self.heaps,
            0
        )


    def all_one_heaps(self) -> bool:
        """Check whether all non-zero heaps have 1 single coin

        Use the functools.reduce() on the heaps list, with a True initializing
        value and keep it true as long as the number of coins is at most one.

        Returns:
            Whether all relevant heaps have 1 single coin
        """
        return functools.reduce(
            lambda a,b: a&(b<=1),
            self.heaps,
            True
        )


    def is_winning_for_next(self) -> bool:
        """Is the current status good for the player having the next turn?

        Usually non-zero nimsum is the winning status, so that the player
        can change it to zero nimsum. This way this player can force the other
        player to make non-winning move, i.e. creating non-zero nimsum, which
        this player can change to zero nimsum again, end so on.

        However, in "misère" type game, the strategy changes in the end-game
        moves. When all heaps only have 1 coin left, the winning status is when
        nimsum is zero. I.e. the all-heaps-has-one-coin reverses the bool
        nimsum. The boolean reversal is done with an XOR.
        
        Returns:
            Whether the current status good for the player having the next turn
        """
        if self.misere:
            return bool(self.get_nimsum()) ^ self.all_one_heaps()
        else:
            return bool(self.get_nimsum())


    def get_random_move(self) -> Move:
        """Figure out a random but valid move
        
        This method is used when the algorithm does not care what to move, just
        figure out a random move.
        
        Returns:
            From which heap and how many coins are to be removed in the coming
                move
        """
        #pick a random index from the active (i.e. non-empty) heaps
        heapnumber = random.choice(
            [i for i in range(len(self.heaps)) if self.heaps[i]]
        )
        #pick a random remove count from the selected random heap
        removecount = random.randint(1, self.heaps[heapnumber])
        return Move(heapnumber, removecount)


    def figure_out_best_move(self) -> Move:
        """Figure out what to move so that we get into a winning position

        First handle the situation when all heaps only have 1 coin. If so,
        there is nothing to think about, just take that 1 coin from a heap
        randomly.

        Then check whether there is only 1 heap with more than 1 coins. This is
        the indicator for the end-game reversal in the "misère" type. The
        winning strategy here is to leave odd numbers of 1-coin heaps for the
        opponent. So, if the number of heaps with 1 coin is odd, take all
        coins from the heap that has more than 1 coin. If it is even, take all
        but 1 coin. Either way, this makes sure that odd number of 1-coin
        heaps are left for the opponent.

        Otherwise, we are in the middle of the game, so figure out the all-heap
        nimsum.
        If it is zero, the player in this current turn is in a losing position,
        because whatever we do we create a non-zero nimsum that the opponent
        can change to zero nimsum again in its turn. So, having no better
        option, we just take a random number of coins from a random heap and
        hope that the opponent makes a mistake.

        If nimsum is not zero, it can be made zero by removing a cretain number
        of coins from the right heap. Check each heap first calculating a
        "target" number of coins, which would null the nimsum. E.g. if the
        nimsum is 7, i.e. we need to remove a binary 4, 2 and 1, and the heap
        contains 9 coins, the target would be 9 XOR 7 = 14. However, we cannot
        remove 14 coins from 9, i.e. this is not a suitable heap to remove
        coins from. So, go on until finding a suitable heap.

        Returns:
            From which heap and how many coins are to be removed in the coming
                move
        """
        #first check whether all active heaps have 1 coin only
        if self.all_one_heaps():
            #empty one of the 1-coin heaps, does not matter which one
            return self.get_random_move()

        #need to handle the "only 1 heap with more than 1 coin" situation?
        if self.misere:
            #create an instance to analyse the heap for end-game
            endgamecheck = EndGameCheck()
            for idx, heapcount in enumerate(self.heaps):
                endgamecheck.check_heap(idx, heapcount)
            
            #entering end-game, i.e. only 1 heap with more than 1 coin?
            if endgamecheck:
                return endgamecheck.get_move()

        #calcualte the nimsum of the set of heaps
        nimsum = self.get_nimsum()

        #not a winning position, i.e. nimsum is zero?
        if not nimsum:
            #cannot do any better but initiate a random move
            return self.get_random_move()

        #look for suitable heap, so that nimsum can be nulled
        for idx, heapcount in enumerate(self.heaps):
            #calculate the wished count of this heap (i.e. so that it causes
            #zero overall nimsum)
            target_count = heapcount ^ nimsum
            #note that the required target count may be more than the heap has
            #altogether. Is this one big enough?
            if target_count < heapcount:
                removecount = heapcount - target_count
                return Move(idx, removecount) 

        #not finding a suitable heap is impossible, I must have screwed up some
        #programming
        raise Exception('Cannot find suitable heap')
