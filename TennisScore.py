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
    self.matchMode = matchMode
    self.NumberOfGames = NumberOfGames
    self.gameMode = gameMode
    self.whenStartTieBreakInShortGames = whenStartTieBreakInShortGames
    self.startToServe = startToServe

    self.currentGameMode = CurrentGameMode.Standard
    
    # (player, [in game, in set, in match])
    self.scorecard = {"1": {"games":0, "sets":0, "score":0}, "2": {"games":0, "sets":0, "score":0}}
    self.talkingScoreBySet = [] # es: ['6-7(5)', '6-3', '10-8']

    self.currentSet = 0 #primo set
  
  def hasWonTheSet(self):
    # vinto il set?
    if self.scorecard[self.player]["games"] >= self.NumberOfGames \
      and self.scorecard[self.player]["games"] - self.scorecard[self.otherPlayer]["games"] == 2:
      return True
    return False

  def hasWonTheMatch(self):
    # vinto il match?
    if self.scorecard[self.player]["sets"] == self.matcMode:
      return True
    if self.scorecard[self.player]["sets"] - self.scorecard[self.otherPlayer]["sets"] == 2:
      if self.matchMode== 3:
        return True
      if self.matchMode== 5 and self.currentPlayerScore[0] > 2:
        return True
    return False
  
  def currentScore(self):
      
    return self.talkingScoreBySet
  
  def updateVisualScoreCard(self):
      
    self.talkingScoreBySet.append (f'{self.scorecard["1"]["games"]}-{self.scorecard["2"]["games"]} : {self.scorecard["1"]["score"]}-{self.scorecard["2"]["score"]}')
  
  def newPoint(self, player):
    
    ret = False
    
    self.player = player
    self.otherPlayer = "1" if self.player == "2" else "2"
    
    if self.currentGameMode == CurrentGameMode.Standard: #6 games per set
            
      ###
      #self.scorecard[self.otherPlayer]
      ###
      
      # aggiungo il 15 al giocatore che ha vinto il punto
      self.scorecard[self.player]["score"] += 15 if self.scorecard[self.player]["score"] <= 15 else self.scorecard[self.player]["score"] + 10
      
      self.updateVisualScoreCard()
      
      # vinto il game?
      if self.scorecard[self.player]["score"] >= 50 \
        and self.scorecard[self.player]["score"] - self.scorecard[self.otherPlayer]["score"] >= 20:
        
        # azzero lo score nel game di entrambi
        self.scorecard[self.player]["score"] = 0
        self.scorecard[self.otherPlayer]["score"] = 0
        
        # un game in più
        self.scorecard[self.player]["games"] += 1 
        
        self.updateVisualScoreCard()
        
        # vinto il set?
        if self.hasWonTheSet(self):
          self.scorecard[self.player]["games"] = 0
          self.scorecard[self.otherPlayer]["games"] = 0
          
          # un set in più
          self.scorecard[self.player]["sets"] += 1
          
          self.updateVisualScoreCard()
                        
          # vinto il match?
          if self.hasWonTheMatch(self):
            return True
          else: #vinto solo il set non ancora il match
            self.currentSet += 1 #nuovo set  
    
    #elif self.currentGameMode == CurrentGameMode.TieBreak:
    #  pass

    return False

#########   
## inizio
#########
incontro = Match(player1 = "Andrea", player2 = "Emanuele", matchMode = MatchMode.On3SetsLTB, numberOfGames = NumberOfGames.Standard, gameMode = GameMode.NoAdv, startToServe = 1)
incontro.newPoint("1")
print(incontro.currentScore())