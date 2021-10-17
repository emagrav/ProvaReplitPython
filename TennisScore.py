class MatchMode:
  On3Sets = 3
  On3SetsLTB = 3
  On5Sets = 5

class SetsGamesMode:
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
  # (player, [in game, in set, in match])
  score = {1: [0, 0, 0], 2: [0, 0, 0]}
  talkingScore = [] # es: ['6-7(5)', '6-3', '10-8']

  def __init__(self, player1, player2, 
              matchMode = MatchMode.On3Sets, 
              setsGamesMode = SetsGamesMode.On4Games, 
              gameMode = GameMode.NoAdv, 
              whenStartTieBreakInShortGames = WhenStartTieBreakInShortGames.On3All, 
              startToServe = 1):
    self.player1 = player1
    self.player2 = player2
    self.matcMode = matchMode
    self.setsGamesMode = setsGamesMode
    self.gameMode = gameMode
    self.whenStartTieBreakInShortGames = whenStartTieBreakInShortGames
    self.startToServe = startToServe

    self.currentGameMode = CurrentGameMode.Standard
  
  def punto(self, player):
    otherPlayer = 1 if player == 2 else 1
    
    if self.currentGameMode == CurrentGameMode.Standard: #6 games per set
      # ricavo i punteggi attuali dei due giocatori
      currentPlayerScore = self.score[player]
      currentOtherPlayerScore = self.score[otherPlayer]
      # aggiungo il 15 al giocatore che ha vinto il punto
      currentPlayerScore[2] += 15 if currentPlayerScore[2] <= 15 else currentPlayerScore[2] + 10
      # vinto il game?
      if currentPlayerScore[2] >= 50 \
        and currentPlayerScore[2] - currentOtherPlayerScore[2] >= 20:
        currentPlayerScore[2] = 0
        currentOtherPlayerScore[2] = 0
        currentPlayerScore[1] += 1 # un game in più
        if hasWonTheSet(self, player):
          if hasWonTheMatch(self, player):
            return True
            
        # vinto il set?
        if currentPlayerScore[1] >= self.setsGamesMode \
          and currentPlayerScore[1] - currentOtherPlayerScore[1] == 2:
          currentPlayerScore[1] = 0
          currentOtherPlayerScore[1] = 0
          currentPlayerScore[0] += 1 # 1 set in più
          # vinto il match?
          if currentPlayerScore[0] == self.matcMode:
            return True
          if currentPlayerScore[0] - currentOtherPlayerScore[0] == 2:
            if self.matcMode == 3:
              return True
            if self.matcMode == 5 and currentPlayerScore[0] > 2:
              return True
        return False
            

        
          
    elif self.currentGameMode == CurrentGameMode.TieBreak:
      pass



    #if self.matchMode == MatchMode.On3Sets:

    
incontro = Match(player1 = "Andrea", player2 = "Emanuele", 
            matchMode = MatchMode.On3SetsLTB, 
            setsGameMode = SetsGamesMode.Standard, 
            gameMode = GameMode.NoAdv, 
            startToServe = 1)

