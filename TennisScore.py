class MatchMode:
  On3Sets = 1
  On3SetsLTB = 2
  On5Sets = 3

class SetsGamesMode:
  Standard = 1 #On6Games
  On4Games = 2

class GameMode:
  Standard = 1 # with classic advantages
  NoAdv = 2
  NoAdvAfter1stAdv = 3

class WhenStartTieBreakInShortGames:
  On4All = 1
  On3All = 2

class CurrentGameMode
  Standard = 1 # 15, 30, 40, game
  TieBreak = 2
  LongTieBreak = 3

class Match:
  # (player, [in game, in set, in match])
  score1 = (1, [0, 0, 0])
  score2 = (2, [0, 0, 0])

  def __init__(self, player1, player2, matchMode = MatchMode.On3Sets, setsGamesMod = SetsGamesMode.Standard, whenStartTieBreakInShortGames = WhenStartTieBreakInShortGames.On3All, startToServe):
    self.player1 = player1
    self.player2 = player2
    self.matcMode = matchMode
    self.startToServe = startToServe
  
  def punto(player):
    if self.matchMode == MatchMode.3Sets
    
incontro = Match(player1 = "Andrea", player2 = "Emanuele", matchMode = MatchMode.On3SetsLTB, setsGameMode = SetsGamesMode.Standard, gameMode = GameMode.NoAdv, startToServe = 1)

