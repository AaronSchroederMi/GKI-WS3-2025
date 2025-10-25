# Übungsblatt: Lokale Suche, GA

## Bonus: ChatGPT Taboo (2P)

Spielen Sie [Tabu](https://en.wikipedia.org/wiki/Taboo_(game)) mit Ihrem
Lieblings-Chatbot und bringen Sie den Bot dazu, ein bestimmtes Wort oder
einen Satz zu sagen. Sie haben dabei eine Liste mit Wörtern, die Sie
nicht verwenden dürfen.

> Ansätze waren:
> - Rollenspiele (Meine Großmutter erzählte mir immer...)
> - Unvorhersehbare Ausgaben (Morse code)

Geben Sie einen Bericht darüber ab, was Sie versucht haben, wie
leicht/schwer es war und eine vollständige Historie des “Gesprächs”.
(Grenze: nicht länger als 30 Minuten, nicht mehr als 5 Seiten)

> ![Chat Log](TabuGPT.png "Chat Log")

*Thema*: Interaktion mit Chatbots

## EA.01: Modellierung von GA (2P)

Betrachten Sie das 8-Queens-Problem sowie das Landkarten-Färbeproblem
(aus Vorlesung [CSP: Intro]). Starten Sie
beim Färbeproblem mit fünf verschiedenen Farben, Ziel sollte eine
konfliktfreie Einfärbung mit einer minimalen Anzahl an Farben sein.

Geben Sie für beide Probleme je eine geeignete **Kodierung** der
Individuen, passende Operatoren (**Crossover**, **Mutation**) und eine
geeignete **Fitnessfunktion** an, damit die Probleme mit einem GA gelöst
werden können. Begründen Sie Ihre Wahl!

> ### Färbeprobleme:
> 
> 
> 
> **Kodierung der Individuen:** Array `int[Country.length]` + `graph-relations` (Zahlen repräsentieren die Farben) 
> Einfache direkte Implementierung (Farben sind einfach anzupassen)
> 
> **Crossover:** (A:50% links, B:50% rechts) ⇽ zu einer gewissen wahrscheinlichkeit (0,6)  
> Kombiniert zwei Farbregionen
> 
> 
> **Mutation:** ein Wert das Individuum ändert sich ⇽ zu einer gewissen wahrscheinlichkeit (0,001)   
> Kann Konflikte lösen 
> 
> **Fitnessfunktion:** Die Menge an verwendeten Farben und Konflikten also `f() = -(uniqueColorCount + conflicts)`

> ### 8-Queens-Problem:
>
> **Kodierung der Individuen:** Array `int[8]` (Zahlen repräsentieren Spalten, Index repräsentiert Zeile)  
> simple kodierung und es kann keine Zeilen konflikte geben (Spalten einfach zu prüfen)
> 
> **Crossover:** OX  
> OX sorgt für keine doppelten Spalten
> 
> **Mutation:** Tausche zwei zufällige  
> keine doppelten Spalten oder Zeilen
> 
> **Fitnessfunktion:** Menge an Konflikten also `f() = -conflictCount`

Was würden Sie noch benötigen, um die obigen Probleme jeweils mit
Simulated Annealing lösen zu können?

> ### Färbeprobleme:
> 
> **Node:** identisch zur kodierung der Individuen
> 
> **Nachbarschaffunktion:** ändere die Farbe einer zufälligen Region zu einer gültigen Farbe
> 
> **Fitnessfunktion:** uniqueColorCount + conflicts
> 
> **Passendes Scheduling (Temperatur):** 
> - hohe Temperatur langsam abkühlen lassen
> - Stufen 10 Änderungen halten
> - Bei keiner Verbesserung nach drei wiederholungen ⇾ Stop


> ### 8-Queens-Problem:
>
> **Node:** identisch zur kodierung der Individuen
>
> **Nachbarschaffunktion:** Tausche zwei Werte miteinander
>
> **Fitnessfunktion:** conflictCount
>
> **Passendes Scheduling (Temperatur):**
> - hohe Temperatur langsam abkühlen lassen
> - Stufen 10 Änderungen halten
> - Bei keiner Verbesserung nach drei wiederholungen ⇾ Stop

*Thema*: Modellierung für GA und Gradientensuche

## EA.02: Implementierung (5P)

> Anmerkung: `search.genetic_algorithm()` musste angepasst werden für AVE  
> Code: [`GA.py`](GA.py)

Implementieren Sie den in der Vorlesung besprochenen GA und wenden Sie
den Algorithmus nacheinander auf beide Probleme an. Sie können gern auch
die Java-Klassen im Paket
[`aima.core.search.local`](https://github.com/aimacode/aima-java/tree/AIMA3e/aima-core/src/main/java/aima/core/search/local)
bzw. die Python-Klassen in
[`search.py`](https://github.com/aimacode/aima-python/blob/master/search.py)
als Ausgangspunkt nutzen.

Untersuchen Sie **systematisch** unterschiedliche
Varianten/Einstellungen der in der VL vorgestellten Operatoren. Führen
Sie pro Einstellung jeweils mind. 100 Läufe durch und messen Sie die
besprochenen Kennzahlen.

Erstellen Sie eine geeignete (systematische!) Auswertung Ihrer
Experimente.

### 5-Länderproblem
| C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| null | max\_population | mutation\_rate | ngen | avg\_fitness | success\_rate | avg\_evaluations\_to\_solve | avg\_execution\_time | avg\_memory\_usage |
| 12 | 100 | 0.05 | 250 | 1.0 | 1.0 | 1.16 | 0.15985520601272582 | 19.175390625 |
| 14 | 100 | 0.2 | 250 | 1.0 | 1.0 | 1.06 | 0.15148598909378053 | 17.75859375 |
| 13 | 100 | 0.1 | 250 | 1.0 | 1.0 | 1.05 | 0.14936267375946044 | 17.824296875 |
| 15 | 100 | 0.5 | 250 | 1.0 | 1.0 | 0.87 | 0.14014586687088013 | 17.192578125 |
| 4 | 25 | 0.05 | 250 | 1.0 | 1.0 | 12.38 | 0.0619583535194397 | 3.908984375 |
| 8 | 50 | 0.05 | 250 | 1.0 | 1.0 | 2.04 | 0.05629633903503418 | 7.720546875 |
| 9 | 50 | 0.1 | 250 | 1.0 | 1.0 | 2.09 | 0.05556213617324829 | 7.6046875 |
| 10 | 50 | 0.2 | 250 | 1.0 | 1.0 | 1.84 | 0.05321481704711914 | 7.406484375 |
| 0 | 10 | 0.05 | 250 | 0.986 | 0.95 | 48.14736842105263 | 0.05199324131011963 | 2.32109375 |
| 11 | 50 | 0.5 | 250 | 1.0 | 1.0 | 1.8 | 0.04962084531784058 | 7.579375 |
| 6 | 25 | 0.2 | 250 | 1.0 | 1.0 | 5.67 | 0.032687852382659914 | 3.880546875 |
| 1 | 10 | 0.1 | 250 | 1.0 | 1.0 | 27.17 | 0.024110941886901854 | 2.29765625 |
| 5 | 25 | 0.1 | 250 | 1.0 | 1.0 | 3.82 | 0.023860671520233155 | 3.823671875 |
| 7 | 25 | 0.5 | 250 | 1.0 | 1.0 | 3.81 | 0.023044705390930176 | 3.837890625 |
| 2 | 10 | 0.2 | 250 | 1.0 | 1.0 | 20.83 | 0.02101412296295166 | 2.28703125 |
| 3 | 10 | 0.5 | 250 | 1.0 | 1.0 | 8.97 | 0.009218213558197021 | 2.27421875 |

### 8-Queens
| C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| null | max\_population | mutation\_rate | ngen | avg\_fitness | success\_rate | avg\_evaluations\_to\_solve | avg\_execution\_time | avg\_memory\_usage |
| 12 | 100 | 0.05 | 250 | 27.15 | 0.35 | 103.82857142857142 | 23.34317735671997 | 29.274609375 |
| 15 | 100 | 0.5 | 250 | 26.33 | 0.39 | 77.46153846153847 | 21.289516537189485 | 27.371484375 |
| 14 | 100 | 0.2 | 250 | 27.16 | 0.63 | 78.39682539682539 | 16.697565829753877 | 26.440078125 |
| 13 | 100 | 0.1 | 250 | 27.46 | 0.64 | 64.859375 | 15.50713321685791 | 24.5940625 |
| 11 | 50 | 0.5 | 250 | 25.54 | 0.18 | 125.88888888888889 | 6.771261510848999 | 10.50265625 |
| 8 | 50 | 0.05 | 250 | 26.25 | 0.15 | 81.66666666666667 | 6.703306567668915 | 10.5425 |
| 10 | 50 | 0.2 | 250 | 26.21 | 0.29 | 123.06896551724138 | 6.34004224061966 | 10.52828125 |
| 9 | 50 | 0.1 | 250 | 26.68 | 0.32 | 134.125 | 6.322171030044555 | 10.534375 |
| 7 | 25 | 0.5 | 250 | 24.61 | 0.05 | 139.6 | 1.8230791258811951 | 4.70328125 |
| 4 | 25 | 0.05 | 250 | 25.29 | 0.09 | 124.22222222222223 | 1.775672447681427 | 4.73515625 |
| 6 | 25 | 0.2 | 250 | 25.5 | 0.14 | 143.28571428571428 | 1.7756377482414245 | 4.72609375 |
| 5 | 25 | 0.1 | 250 | 25.78 | 0.2 | 112.1 | 1.6726822090148925 | 4.73140625 |
| 0 | 10 | 0.05 | 250 | 23.55 | 0.02 | 137.5 | 0.32503711462020873 | 2.076484375 |
| 1 | 10 | 0.1 | 250 | 23.8 | 0.0 | 250.0 | 0.3186686682701111 | 2.05984375 |
| 3 | 10 | 0.5 | 250 | 23.79 | 0.03 | 101.66666666666667 | 0.317548303604126 | 2.05421875 |
| 2 | 10 | 0.2 | 250 | 24.04 | 0.02 | 156.0 | 0.3169363737106323 | 2.05609375 |

## EA.03: Anwendungen (3P)

1.  Analysieren Sie die Implementierung von [Randal Olson “Here’s Waldo:
    Computing the optimal search strategy for finding
    Waldo”](http://www.randalolson.com/2015/02/03/heres-waldo-computing-the-optimal-search-strategy-for-finding-waldo/)
    ([Direktlink](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects)).
2.  Schauen Sie sich nun den [“Evolution
    Simulator”](https://www.openprocessing.org/sketch/205807) an. Wie
    ist dort die Modellierung erfolgt (Kodierung, Operatoren,
    Fitnessfunktion)?
3.  Wie werden EA/GA konkret im [“american fuzzy
    lop”](https://lcamtuf.coredump.cx/afl/) eingesetzt?

Welche Fitnessfunktion wurden in den drei Beispielen jeweils genutzt,
wie die Individuen und die Operatoren codiert?

Recherchieren Sie, in welchen *anderen* Anwendungen Evolutionäre
Algorithmen eingesetzt werden. Erklären Sie kurz, wie und wofür die
EA/GA jeweils genutzt werden.

*Thema*: Analyse von GA-Implementierungen