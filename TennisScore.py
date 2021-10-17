class MatchMode:
  On3Sets = 3
  On3SetsLTB = 3
  On5Sets = 5

class NumberOfGames:
  Standard = 6 #On6Games
  On4Games = 4

class GameMode:
  Standard = "classic advantages"
  NoAdv = "killer point"
  NoAdvAfter1stAdv = "killer point after 1st advantage"

class WhenStartTieBreakInShortGames:
  On3All = 3
  On4All = 4

class CurrentGameMode:
  Standard = 50 # 15, 30, 40, game
  TieBreak = 7
  LongTieBreak = 10

class Match:
  def __init__(self, player1, player2, matchMode = MatchMode.On3Sets, numberOfGames = NumberOfGames.On4Games, gameMode = GameMode.NoAdv, whenStartTieBreakInShortGames = WhenStartTieBreakInShortGames.On3All, startToServe = 1):
    self.player1 = player1
    self.player2 = player2
    self.matcMode = matchMode
    self.NumberOfGames = NumberOfGames
    self.gameMode = gameMode
    self.whenStartTieBreakInShortGames = whenStartTieBreakInShortGames
    self.startToServe = startToServe

    self.currentGameMode = CurrentGameMode.Standard
    
    # (player, [in game, in set, in match])
    self.score = {1: [0, 0, 0], 2: [0, 0, 0]}
    self.talkingScore = [] # es: ['6-7(5)', '6-3', '10-8']

    self.currentSet = 0 #primo set
  
  def hasWonTheSet(self):
    # vinto il set?
    if self.currentPlayerScore[1] >= self.NumberOfGames \
      and self.currentPlayerScore[1] - self.currentOtherPlayerScore[1] == 2:
      return True
    return False

  def hasWonTheMatch(self):
    # vinto il match?
    if self.currentPlayerScore[0] == self.matcMode:
      return True
    if self.currentPlayerScore[0] - self.currentOtherPlayerScore[0] == 2:
      if self.matcMode == 3:
        return True
      if self.matcMode == 5 and self.currentPlayerScore[0] > 2:
        return True
    return False
  
  def currentScore(self):
    return self.talkingScore

  def punto(self, player):
    self.player = player
    self.otherPlayer = 1 if player == 2 else 1
    
    if self.currentGameMode == CurrentGameMode.Standard: #6 games per set
      # ricavo i punteggi attuali dei due giocatori
      self.currentPlayerScore = self.score[player]
      self.currentOtherPlayerScore = self.score[self.otherPlayer]
      # aggiungo il 15 al giocatore che ha vinto il punto
      self.currentPlayerScore[2] += 15 if self.currentPlayerScore[2] <= 15 else self.currentPlayerScore[2] + 10
      # vinto il game?
      if self.currentPlayerScore[2] >= 50 \
        and self.currentPlayerScore[2] - self.currentOtherPlayerScore[2] >= 20:
        self.currentPlayerScore[2] = 0
        self.currentOtherPlayerScore[2] = 0
        self.currentPlayerScore[1] += 1 # un game in più
        if self.hasWonTheSet(self):
          self.talkingScore[self.currentSet] = f"{self.score(1)[1]}-{self.score(2)[1]}"
          self.currentPlayerScore[1] = 0
          self.currentOtherPlayerScore[1] = 0
          self.currentPlayerScore[0] += 1 # 1 set in più
          if self.hasWonTheMatch(self):
            return True
        return False
          
    elif self.currentGameMode == CurrentGameMode.TieBreak:
      pass

    #if self.matchMode == MatchMode.On3Sets:


    return False
    
incontro = Match(player1 = "Andrea", player2 = "Emanuele", matchMode = MatchMode.On3SetsLTB, numberOfGames = NumberOfGames.Standard, gameMode = GameMode.NoAdv, startToServe = 1)
incontro.punto(1)
print(incontro.currentScore())