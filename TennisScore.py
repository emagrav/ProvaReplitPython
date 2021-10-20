from enum import Enum

class Match_Mode(Enum):
  On3Sets = 3
  On3SetsLTB = 3
  On5Sets = 5

class Match_DefaultPlayerNames(Enum):
  Player1 = 1
  Player2 = 2

class Set_WhenStartTieBreak(Enum):
  On6All = 6
  On4All = 4
  On3All = 3

class Set_Mode(Enum):
  On6Games = 6 
  On4Games = 4

class Game_AdvantageMode(Enum):
  ClassicAdv = 40 # classic advantages
  NoAdv = 40 # killer point
  NoAdvAfter1stDeuce = 50 # killer point after 1st deuce

class Game_Mode(Enum):
  StandardGame = 40 # 15, 30, 40, game
  TieBreakGame = 6
  LongTieBreakGame = 9

class Game: 
  gameMode = None
  advantageMode = None
  
  playerWonThePoint = 0 # può valere 1 o 2
  playerLoseThePoint = 0 # vale l'altro valore della variabile precedente
  
  playedPoints = 0 # totale corrente dei punti giocati nel game
  score = [] # es. [40, 15] ovvero [50, 40] 50 è da considerarsi vantaggio , oppure [9, 8] in un tie break
  
  def __init__(self, gameMode = Game_Mode.StandardGame, advantageMode = Game_AdvantageMode.ClassicAdv) -> None:
    self.gameMode = gameMode
    self.advantageMode = advantageMode
    score = [0, 0]  # si parte da 0 a 0

  def getVisualScore(self):
    # punteggio nel game es. "40-15" oppure "0-4" nel tie break
    s = self.score

    if s[0] > s[1] and s[0] > 40:
      primo = "Adv"
      secondo = "40"
    if s[1] > s[0] and s[1] > 40:
      primo = "40"
      secondo = "Adv"
    if s[0] == s[1] and s[0] > 40:
      primo = secondo = "40"

    return primo + "-" + secondo

  def hasWonTheGame(self):
    i = self.playerWonThePoint - 1
    j = self.playerLoseThePoint - 1

    # verifico se è un game normale e non un (long) tie break
    if self.gameMode == Game_Mode.StandardGame:
      # verifico quindi se il vincitore del punto ha superato il punteggio di 40
      if self.score[i] > 40:
        # se vige la regola del no-adv, allora il game l'ha vinto
        if self.advantageGameMode == Game_AdvantageMode.NoAdv:
          return True
        # se vige la regola del no-adv dopo il primo deuce e supera quindi il punteggio di 50, allora il game l'ha vinto
        if self.advantageGameMode == Game_AdvantageMode.NoAdvAfter1stDeuce and self.score[i] > 50:
            return True
        # se invece vige la regola classica dei vantaggi, il game lo vince se c'è una differenza di 20 col punteggio dell'avversario
        if self.score[i] - self.score[j] > 10:
          return True
    else:
      # caso tie break o long tie break
      # il game lo vince se c'è una differenza di 2 col punteggio dell'avversario
      if self.score[i] > self.gameMode and self.score[i] - self.score[j] > 1:
          return True

    return False

  def newPoint(self, player): 
    """
    player vale 1 o 2 a seconda del giocatore che ha fatto il punto
    """
    self.playerWonThePoint = player
    self.playerLoseThePoint = 2 if self.playerWonThePoint == 1 else 1

    i = self.playerWonThePoint - 1
    j = self.playerLoseThePoint - 1

    self.playedPoints += 1 # incremento il numero di punti giocati nel game

    # verifico se la modalità del game corrente è standard
    if self.gameMode == Game_Mode.StandardGame:
      # in tal caso aggiungo il 15 al giocatore che ha vinto il punto (che possono come sappiamo valere anche solo 10 punti)
      self.score[i] += 15 if self.score[i] <= 15 else self.score[j] + 10
    else: 
      # caso tie break o long tie break: aggiungo un semplice punticino
      self.score[i] += 1

class Set:
  """
  Gestisce tutto quanto di competenza del set
  """
  whenStartTieBreak = None
  mode = None
  advantageMode = None

  totGames = 0 # totale corrente dei game giocati
  
  visualScore = "" # punteggio nel set es. "4-2" oppure "6-6"
  score = [0, 0] # es. [4, 2] oppure [6, 6]
  
  game = None # il game corrente

  def __init__(self, LTB = False, mode = Set_Mode.On6Games, whenStartTieBreak = Set_WhenStartTieBreak.On6All, advantageMode = Game_AdvantageMode.ClassicAdv): 
    
    if LTB:
      self.newGame(True)
      return

    self.mode = mode
    self.whenStartTieBreak = whenStartTieBreak
    self.advantageMode = advantageMode

     # parte il primo gioco del set
    self.newGame()
      
  def newGame(self, LTB = False):
    if LTB:
      self.game = Game(Game_Mode.LongTieBreakGame)
    else:
      # caso set normale (potrebbe essere a 6 o a 4 game quindi)
      # verifico quindi quanti game sono necessari per vincere
      if (self.score == [6, 6]) \
        or (self.whenStartTieBreak == Set_WhenStartTieBreak.On3All and self.score == [3, 3]) \
        or (self.whenStartTieBreak == Set_WhenStartTieBreak.On4All and self.score == [4, 4]):   
          # istanzio il nuovo game con punti da tie break
          self.game = Game(Game_Mode.TieBreakGame)
      else:
        # se non devo istanziare un tie break, istanzio il nuovo game con punti standard
        self.game = Game(Game_Mode.StandardGame)
    
    # incremento il numero di game giocati nel set
    self.totGames += 1

  def hasWonTheSet(self):
     # se nessuno ha ancora vinto un punto, restituisco ovviamente False
    if self.game.playerWonThePoint == 0:
      return False

    i = self.game.playerWonThePoint - 1
    j = self.game.playerLoseThePoint - 1

    # se è un game standard
    if self.game.gameMode == Game_Mode.StandardGame:
      # verifico se la differenza è di 2 game qualora raggiunto o superato il numero di game per vincere dal player
      if (self.game.score[i] >= self.mode.value) and (self.game.score[i] - self.game.score[j] == 2):
        return True
    
    # se è un tie break vince il set così come se è un long tie break (in questo caso ha vinto il match)
    if self.game.gameMode == Game_Mode.TieBreakGame or self.game.gameMode == Game_Mode.LongTieBreakGame:
      return True
    
    return False

class Match:
  '''
  Il match di tennis
  '''
  player1Name = ""
  player2Name = ""
  
  matchMode = None
  numberOfGames = None
  advantageMode = None
  whenStartTieBreak = None
  startToServe = 0

  set = None # il set corrente
  sets = [] # Lista dei set del match

  def __init__(self, player1Name = Match_DefaultPlayerNames.Player1.name, player2Name = Match_DefaultPlayerNames.Player2.name, matchMode = Match_Mode.On3Sets, setMode = Set_Mode.On6Games, advantageMode = Game_AdvantageMode.ClassicAdv, whenStartTieBreak = Set_WhenStartTieBreak.On6All, startToServe = 1):
    '''
    gli input servono per definire le regole del punteggio
    '''
    # cerco contraddizioni nei parametri passati
    if whenStartTieBreak == Set_WhenStartTieBreak.On6All and setMode != Set_Mode.On6Games:
      raise Exception("Il tie break non può iniziare sul 6 pari se il numero di game in un set è inferiore") 
    if whenStartTieBreak == Set_WhenStartTieBreak.On4All and setMode == Set_Mode.On6Games:
      raise Exception("Il tie break non può iniziare sul 4 pari se il numero di game in un set è impostato a 6") 
    if whenStartTieBreak == Set_WhenStartTieBreak.On3All and setMode == Set_Mode.On6Games:
      raise Exception("Il tie break non può iniziare sul 3 pari se il numero di game in un set è impostato a 6") 
    
    self.player1Name = player1Name
    self.player2Name = player2Name
    self.matchMode = matchMode
    self.setMode = setMode
    self.advantageMode = advantageMode
    self.whenStartTieBreak = whenStartTieBreak
    self.startToServe = startToServe
    
    self.newSet() # parte il primo set e il primo game ovviamente

  def newSet(self):
    # se il match prevede il long tie break al posto del terzo set
    if self.matchMode == Match_Mode.On3SetsLTB:
      # e se i set finora giocati sono 2
      if len(self.sets) == 2:
        self.set = Set(True)
      else:
        # allora si giocano il terzo secondo quanto stabilito nel costruttore 
        self.set = Set(self.setMode)
    
    self.sets.append(self.set)

  def hasWonTheMatch(self):
    i = self.set.game.playerWonThePoint - 1
    j = self.set.game.playerLoseThePoint - 1

    # vinto il match?
    # se il numero di set vinti coincide con quello definito inizialmente
    if self.set.score[i] == self.matchMode.value:
      # fine partita, vinta
      return True
    # se invece non è stato raggiunto ancora il limite ma ci sono due set di differenza per match a 3 set ovvero tre set per match a 5 set
    if (self.set.score[i] - self.set.score[j] == 2) and (self.matchMode.value == 3): 
        return True
    if (self.set.score[i] - self.set.score[j] == 3) and (self.matchMode.value == 5): 
        return True
    
    return False  

  def newPoint(self, player) -> bool:    
    '''
    Aggiunge un punto al giocatore in input

      player -> Il giocatore che ha fatto il punto. Può valere 1 o 2
      return -> bool: True se ultimo punto del match
    '''
    # aggiungo un punto nel game al vincitore del punto
    self.set.game.newPoint(player)

    i = self.set.game.playerWonThePoint - 1
    j = self.set.game.playerLoseThePoint - 1
    
    # vinto il game?
    if self.set.game.hasWonTheGame():
      if self.set.hasWonTheSet():
        if self.hasWonTheMatch():
          return True 
        # se il match non si è chiuso ma ha vinto solo un set
        self.newSet()
      else:
        # non ha vinto il set ma solo un game
        self.set.score[i] += 1     

    return False
 
#########   
## inizio
#########
incontro = Match(player1Name = "Andrea", player2Name = "Emanuele", matchMode = Match_Mode.On3SetsLTB, setMode = Set_Mode.On4Games, advantageMode = Game_AdvantageMode.NoAdv, whenStartTieBreak=Set_WhenStartTieBreak.On3All, startToServe = 1)
incontro.newPoint(1)
print(incontro.currentScore())


