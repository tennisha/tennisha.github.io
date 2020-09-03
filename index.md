Four Card Poker September 3, 2020

One of my favorite carnival games is called four card Poker. Four Card Poker is a variation of Poker where the dealer gets 6 cards and each of the players gets 5 cards and each player plays head to head with the dealer. The game is played such that you take the best four card hand out of your five cards and the dealer takes their best four card hand out of their six cards. The game is played with a single 52 card deck with no jokers.

Problem

I am learning python and my goal is to write a program that would determine the best four card poker hand between a player and the dealer. The game will be played one on one at the start but after that is functioning I am going to expand it to allow for 6 players all playing against the dealer. In one on one play the dealer is dealt the first 6 cards and the player is dealt the next 5 cards. Once the cards have been dealt, the player has the option to either fold or play. If the player folds they lose their bet. If the player plays the have the option of betting one time their ante, two times their ante or three times their ante. There is an optional side bet called Aces up which the player can also choose to play or not.

Evaluating Hands

A player is given 5 cards. Each of their cards has a suit and a alpha-numerical value. Even though the player has 5 cards, the hand ranking is determined by only the best 4 cards. Players win ties.

Suits

There are four suits Clubs, Spades, Diamonds and Hearts.

Values

There are 13 alpha-numerical cards in each suit

2,3,4,5,6,7,8,9,10,J,Q,K,A

Each card value has a rank within the game.

A - 1 or 14 *depending on the hand and Ace can be either weighted as a 1 (to form a 4 card straight, flush or straight flush) or a 14 (to form a 4 card straight, flush or straight flush) 2 - 2 3 - 3 4 - 4 5 - 5 6 - 6 7 - 7 8 - 8 9 - 9 10 - 10 J - 11 Q - 12 K - 13

Hands of Poker

Four of a Kind Royal Flush Straight Flush Full House * this is evaluated as a three of a kind for ranking purposes Three of A kind Flush Straight Two Pair Pair High Card
