#############
# enumeratori
#############

from enum import Enum

# For match
class Match_Mode(Enum):
  On3Sets = 3
  On3SetsLTB = 3
  On5Sets = 5

class Match_DefaultPlayerNames(Enum):
  Player1 = 1
  Player2 = 2

# For sets
class Set_NumberOfGamesToWin(Enum):
  On6Games = 6 
  On4Games = 4
  OnLongTieBreak = 1

class Set_WhenStartTieBreak(Enum):
  On6All = 6
  On4All = 4
  On3All = 3

class Set_CurrentMode(Enum):
  NormalSet = 1
  LongTieBreak = 2

# For games
class Game_AdvantageMode(Enum):
  ClassicAdv = 40 # classic advantages
  NoAdv = 40 # killer point
  NoAdvAfter1stDeuce = 50 # killer point after 1st deuce

class Game_CurrentMode(Enum):
  StandardGame = 40 # 15, 30, 40, game
  TieBreakGame = 6
  LongTieBreakGame = 9

#############
# Classe Game
#############

class Game:
  
  currentGameMode = None
  advantageMode = None
  
  playerWonThePoint = 0 # può valere 1 o 2
  playerLoseThePoint = 0 # vale l'altro valore della variabile precedente
  
  playedPoints = 0 # totale corrente dei punti giocati nel game
  score = [] # es. [40, 15], [50, 40] caso vantaggio player 1, oppure [9, 8] in un tie break
  set = None

  #------------
  # Costruttore
  #------------
  def __init__(self, currentGameMode = Game_CurrentMode.StandardGame, advantageMode = Game_AdvantageMode.ClassicAdv) -> None:
    self.currentGameMode = currentGameMode
    self.advantageMode = advantageMode
    score = [0, 0]  # si parte: 0 a 0

  def getVisualScore(self):
    # punteggio nel game es. "40-15" oppure "0-4" nel tie break
    s = self.score
    return s[0] + "-" + s[1]

  def hasWonTheGame(self):
    i = self.playerWonThePoint - 1
    j = self.playerLoseThePoint - 1

    # verifico se è un game normale e non un (long) tie break
    if self.currentGameMode == Game_CurrentMode.StandardGame:
      # game normale
      # verifico quindi se il vincitore del punto ha superato il punto 40
      if self.score[i] > Game_CurrentMode.StandardGame:
        # superato il punto 40
        # se vige la regola del no-adv, allora il game l'ha vinto
        if self.advantageGameMode == Game_AdvantageMode.NoAdv:
          return True
        # se vige la regola del no-adv dopo il primo deuce e supera quindi il punto 50, allora il game l'ha vinto
        if self.advantageGameMode == Game_AdvantageMode.NoAdvAfter1stDeuce and self.score[i] > Game_AdvantageMode.NoAdvAfter1stDeuce:
            return True
        # se invece vie la regola classica dei vantaggi, il game lo vince se c'è una differenza di 20 col punteggio dell'avversario
        if self.score[i] - self.score[j] > 10:
          return True
    else:
      # se è invece un tie break o long tie break
      # il game lo vince se c'è una differenza di 2 col punteggio dell'avversario
      if self.score[i] > self.currentGameMode and self.score[i] - self.score[j] > 1:
          return True

    return False

  def newPoint(self, player): # player vale 1 o 2 a seconda del giocatore che ha fatto il punto
    self.playerWonThePoint = player
    self.playerLoseThePoint = 2 if self.playerWonThePoint == 1 else 1

    i = self.playerWonThePoint - 1
    j = self.playerLoseThePoint - 1

    self.playedPoints += 1 # incremento il numero di punti giocati nel game

    if self.currentGameMode == Game_CurrentMode.StandardGame:
      # aggiungo il 15 al giocatore che ha vinto il punto (che possono come sappiamo valere anche solo 10 punti)
      self.score[i] += 15 if self.score[i] <= 15 else self.score[j] + 10
    else: 
      # caso tie break o long tie break: aggiungo un semplice punticino
      self.score[i] += 1

############
# Classe Set
############
class Set:
  numberOfGamesToWin = None
  whenStartTieBreak = None
  currentMode = None

  totGames = 0 # totale corrente dei game giocati
  
  visualScore = "" # punteggio nel set es. "4-2" oppure "6-6"
  score = [0, 0] # es. [4, 2] oppure [6, 6]
  
  cur_GameMode = None
  game = None # il game corrente
  numberOfGamesToWin = 0 # numero di game previsti per vincere il set

  #------------
  # Costruttore
  #------------  
  def __init__(self, numberOfGamesToWin = Set_NumberOfGamesToWin.On6Games, whenStartTieBreak = Set_WhenStartTieBreak.On6all, currentMode = Set_CurrentMode.StandardSet): 
    self.numberOfGamesToWin = numberOfGamesToWin
    self.whenStartTieBreak = whenStartTieBreak
    self.currentMode = currentMode

    self.newGame()
      
  def newGame(self):
    # verifico che tipo di set devono giocare
    if self.currentMode == Set_CurrentMode.NormalSet:
      # caso set normale inteso come no long tie break (potrebbe essere a 6 o a 4 game quindi)
      # verifico quindi quanti game sono necessari per vincere
      if (self.score == [6, 6]) \
        or (self.whenStartTieBreak == Set_WhenStartTieBreak.On3All and self.score == [3, 3]) \
        or (self.whenStartTieBreak == Set_WhenStartTieBreak.On4All and self.score == [4, 4]):   
          self.game = Game(Game_CurrentMode.TieBreakGame)
      else:
        # istanzio il nuovo game standard
        self.game = Game(Game_CurrentMode.StandardGame)
    else:
      # se devono giocare il long tie break
      self.game = Game(Game_CurrentMode.LongTieBreakGame)
    
    # incremento il numero di game giocati nel set
    self.totGames += 1 
  
  def hasWonTheSet(self):
    # se nessuno ha ancora vinto un punto, restituisco ovviamente False
    if self.game.playerWonThePoint == 0:
      return False

    i = self.game.playerWonThePoint - 1
    j = self.game.playerLoseThePoint - 1 
    
    #NumberOfGamesInSet(Enum): 
    #WhenStartTieBreakInShortGames(Enum):

    # se è un game standard
    if self.game.currentGameMode == Game_CurrentMode.StandardGame:
      if self.match.
      if self.score[i] > Game_CurrentMode.StandardGame and self.score[i] - self.score[j] > 10:
          return True
    else:
      # caso tie break o long tie break
      return True

  def hasWonTheSet(self):
    i = self.game.playerWonThePoint - 1
    j = self.game.playerLoseThePoint - 1

    if self.score[i]["games"] >= self.numberOfGamesToWin \
      and self.score[i]["games"] - self.score[j]["games"] == 2:
      return True
    return False

##############
# Classe Match
##############
class Match:
  player1Name, player2Name = ""
  matchMode, numberOfGames, advantageMode, whenStartTieBreakInShortGames, startToServe = None

  currentGameMode = Game_CurrentMode.Standard
  setId = 0 # identificato del set, il numero ordinale del set corrente
  set = None # il set corrente
  sets = [] # Lista di set del match

  ######
  # init
  ######
  def __init__(self
              , player1Name = Match_DefaultPlayerNames.Player1.name
              , player2Name = Match_DefaultPlayerNames.Player2.name
              , matchMode = Match_Mode.On3Sets
              , numberOfGames = Set_NumberOfGamesToWin.On4Games
              , advantageMode = Game_AdvantageMode.NoAdv
              , whenStartTieBreakInShortGames = WhenStartTieBreakInShortGames.On3All
              , startToServe = 1):
    self.player1Name = player1Name
    self.player2Name = player2Name
    self.matchMode = matchMode
    self.numberOfGames = numberOfGames
    self.advantageMode = advantageMode
    self.whenStartTieBreakInShortGames = whenStartTieBreakInShortGames
    self.startToServe = startToServe
    
    self.setId = 1 
    self.set = Set(self.setId) # parte il primo set
    self.sets = [self.set]

    self.game = self.set.game

  def newSet(self) :
    self.setId += 1
  def newPoint(self, player):    
    ''' 
    restituisce True se ultimo punto del match
    '''
    # aggiungo un punto nel game al vincitore del punto
    self.game.newPoint(player)
    i = self.game.playerWonThePoint - 1
    j = self.game.playerLoseThePoint - 1
    
    # vinto il game?
    if self.game.hasWonTheGame():
      if self.set.hasWonTheSet():
        if self.hasWonTheMatch():
          return True 
        # se il match non si è chiuso ma ha vinto solo un set
        self.newSet()
      # se il set non si è ancora chiuso ma ha vinto solo un game
      self.set.score[i] += 1


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
            self.set += 1 #nuovo set  
    
    #elif self.currentGameMode == CurrentGameMode.TieBreak:
    #  pass

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
 
#########   
## inizio
#########
incontro = Match(player1 = "Andrea", player2 = "Emanuele", matchMode = Match_Mode.On3SetsLTB, numberOfGames = Set_NumberOfGamesToWin.Standard, advantageMode = Game_AdvantageMode.NoAdv, startToServe = 1)
incontro.newPoint("1")
print(incontro.currentScore())


