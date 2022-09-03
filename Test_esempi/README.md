# Esempi di test con i due framework più utilizzati con Python
Per configurare l'ambiente di test di VS Code ed eseguirli, bisogna aprire come root directory la cartella contenente questo stesso file (nonché, ovviamente, gli script python di prova). <br>
VS Code, infatti, non riesce ad individuare il file di test qualora inseriti in sottocartelle. <br>
Aprire quindi la Command Palette (Ctrl-Shift-P) e selezionare `"Python: Configure Tests"`. 
Dopodiché in ordine: 
- il framework di testing: `unittest` o `pytest`
- la directory dove cercare i file di test: `". Root directory"`
- come pattern per identificare i file che contengono i test: `"test_*.py Python files beginning with test_"` (perché semplicemente questo è lo standard di nomenclatura che ho scelto)