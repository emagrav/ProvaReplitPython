#####################
# enumeratori [start]
#####################
from enum import Enum

class MatchMode(Enum):
  On3Sets = 3
  On3SetsLTB = 3
  On5Sets = 5

class NumberOfGamesInSet(Enum):
  Standard = 6 #On6Games
  On4Games = 4

class AdvantageMode(Enum):
  Standard = "classic advantages"
  NoAdv = "killer point"
  NoAdvAfter1stAdv = "killer point after 1st advantage"

class WhenStartTieBreakInShortGames(Enum):
  On3All = 3
  On4All = 4

class CurrentGameMode(Enum):
  Standard = 40 # 15, 30, 40, game
  TieBreak = 6
  LongTieBreak = 10

class DefaultPlayerNames(Enum):
  Player1 = 1
  Player2 = 2

###################
# enumeratori [end]
###################

class Game:
  
  currentGameMode = CurrentGameMode.Standard
  
  playerWonThePoint = "" # può valere 1 o 2
  playerLoseThePoint = "" # vale l'altro valore della variabile precedente
  
  playedPoints = 0 # totale corrente dei punti giocati nel game
  score = [0, 0] # es. [40, 15], [50, 40] caso vantaggio player 1, oppure [9, 8] in un tie break
  set = None

  def __init__(self, currentGameMode = CurrentGameMode.Standard) -> None:
      self.currentGameMode = currentGameMode

  def getVisualScore(self):
    # punteggio nel game es. "40-15" oppure "0-4" nel tie break
    s = self.score
    return s[0] + "-" + s[1]

  def hasWonTheGame(self):
    i = self.playerWonThePoint - 1
    j = self.playerLoseThePoint - 1

    if self.currentGameMode == CurrentGameMode.Standard:
      if self.score[i] > CurrentGameMode.Standard and self.score[i] - self.score[j] > 10:
          return True
    else:
      # caso tie break o long tie break
      if self.score[i] > self.currentGameMode and self.score[i] - self.score[j] > 1:
          return True

    return False

  def newPoint(self, player): # player vale 1 o 2 a seconda del giocatore che ha fatto il punto
    self.playerWonThePoint = player
    self.playerLoseThePoint = 2 if self.playerWonThePoint == 1 else 1

    self.playedPoints += 1 # incremento il numero di punti giocati nel game

    if self.currentGameMode == CurrentGameMode.Standard:
      # aggiungo il 15 al giocatore che ha vinto il punto (che possono come sappiamo valere anche solo 10 punti)
      self.score[self.playerWonThePoint - 1] += 15 if self.score[self.playerWonThePoint] <= 15 else self.score[self.playerWonThePoint] + 10
    else: # caso tie break o long tie break
      self.score[self.playerWonThePoint - 1] += 1
    
class Set:
  
  setOrderNumber = 0 # numero ordinale che identifica il set che si sta giocando: il primo piuttosto che il secondo o il terzo, ecc.
  totGames = 0 # totale corrente dei game giocati
  
  visualScore = "" # punteggio nel set es. "4-2" oppure "6-6"
  score = [] # es. [3, 3]
  currentGameMode = CurrentGameMode.Standard
    
  def __init__(self, match, setOrderNumber = 1): #se non viene passato il parametro allora è il primo set
    self.setOrderNumber = setOrderNumber
    self.match = match
      
  # def getScore(self):
  #   return self.score

  def newPoint(self, player): # player vale "1" o "2" a seconda del giocatore che ha fatto il punto
    ret = False
    
    self.playerWonThePoint = player
    self.otherPlayer = "1" if self.playerWonThePoint == "2" else "2"
    
    if self.currentGameMode == CurrentGameMode.Standard: # 6 game per set
      
      # aggiungo il 15 al giocatore che ha vinto il punto
      self.scorecard[self.playerWonThePoint]["score"] += 15 if self.scorecard[self.playerWonThePoint]["score"] <= 15 else self.scorecard[self.playerWonThePoint]["score"] + 10
      
      self.updateVisualScoreCard()
      
      # vinto il game?
      if self.scorecard[self.playerWonThePoint]["score"] >= 50 \
        and self.scorecard[self.playerWonThePoint]["score"] - self.scorecard[self.otherPlayer]["score"] >= 20:
        
        # azzero lo score nel game di entrambi
        self.scorecard[self.playerWonThePoint]["score"] = 0
        self.scorecard[self.otherPlayer]["score"] = 0
        
        # un game in più
        self.scorecard[self.playerWonThePoint]["games"] += 1 
        
        self.updateVisualScoreCard()
        
        # vinto il set?
        if self.hasWonTheSet(self):
          self.scorecard[self.playerWonThePoint]["games"] = 0
          self.scorecard[self.otherPlayer]["games"] = 0
          
          # un set in più
          self.scorecard[self.playerWonThePoint]["sets"] += 1
          
          self.updateVisualScoreCard()
                        
          # vinto il match?
          if self.hasWonTheMatch(self):
            return True
          else: #vinto solo il set non ancora il match
            self.currentSet += 1 #nuovo set  
  
    return False

set = Set(2)
print("Set #", set.setOrderNumber)
print("player1 =", set.player1Name)
print("player2 =", set.player2Name)

set2 = Set(player2Name="Bonfiglio")
print("Set #", set2.setOrderNumber)
print("player1 =", set2.player1Name)
print("player2 =", set2.player2Name)


print("Set di prima #", set.setOrderNumber)
print("player1 =", set.player1Name)
print("player2 =", set.player2Name)

class Match:
  player1Name, player2Name = ""
  matchMode, numberOfGames, advantageMode, whenStartTieBreakInShortGames, startToServe = None
  currentGameMode = CurrentGameMode.Standard

  currentSetNumber = 1 # il numero ordinale del set corrente
  currentSet = Set(currentSetNumber) # il set corrente
  sets = [currentSet] # Lista di set del match

  def __init__(self
              , player1Name = DefaultPlayerNames.Player1.name
              , player2Name = DefaultPlayerNames.Player2.name
              , matchMode = MatchMode.On3Sets
              , numberOfGames = NumberOfGamesInSet.On4Games
              , advantageMode = AdvantageMode.NoAdv
              , whenStartTieBreakInShortGames = WhenStartTieBreakInShortGames.On3All
              , startToServe = 1):
    self.player1Name = player1Name
    self.player2Name = player2Name
    self.matchMode = matchMode
    self.numberOfGames = numberOfGames
    self.advantageMode = advantageMode
    self.whenStartTieBreakInShortGames = whenStartTieBreakInShortGames
    self.startToServe = startToServe
 
    # (player, [in game, in set, in match])
    self.talkingScoreBySet = [] # es: ['6-7(5)', '6-3', '10-8']

    self.currentSet = 0 #primo set
  
  def hasWonTheSet(self):
    # vinto il set?
    if self.scorecard[self.player]["games"] >= self.numberOfGames \
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
incontro = Match(player1 = "Andrea", player2 = "Emanuele", matchMode = MatchMode.On3SetsLTB, numberOfGames = NumberOfGamesInSet.Standard, advantageMode = AdvantageMode.NoAdv, startToServe = 1)
incontro.newPoint("1")
print(incontro.currentScore())


