# Bonus
# Search.01: Problemformalisierung, Zustandsraum
### 1. Formalisieren Sie das Problem (Zustände, Aktionen, Start- und Endzustand).
Zustände:
1. Start: 1 Pferde, 3 Orks, 3 Elben; Ziel: 0 Pferde, 0 Orks, 0 Elben <-- <span style="color: green;">Startzustand</span>
- Start: 1 Pferde, 3 Orks, 2 Elben; Ziel: 0 Pferde, 0 Orks, 1 Elben <span style="color: red;">Invalid</span>
- Start: 1 Pferde, 3 Orks, 1 Elben; Ziel: 0 Pferde, 0 Orks, 2 Elben <span style="color: red;">Invalid</span>
2. Start: 1 Pferde, 3 Orks, 0 Elben; Ziel: 0 Pferde, 0 Orks, 3 Elben 
3. Start: 1 Pferde, 2 Orks, 3 Elben; Ziel: 0 Pferde, 1 Orks, 0 Elben 
4. Start: 1 Pferde, 2 Orks, 2 Elben; Ziel: 0 Pferde, 1 Orks, 1 Elben 
- Start: 1 Pferde, 2 Orks, 1 Elben; Ziel: 0 Pferde, 1 Orks, 2 Elben <span style="color: red;">Invalid</span>
5. Start: 1 Pferde, 2 Orks, 0 Elben; Ziel: 0 Pferde, 1 Orks, 3 Elben 
6. Start: 1 Pferde, 1 Orks, 3 Elben; Ziel: 0 Pferde, 2 Orks, 0 Elben 
- Start: 1 Pferde, 1 Orks, 2 Elben; Ziel: 0 Pferde, 2 Orks, 1 Elben <span style="color: red;">Invalid</span>
7. Start: 1 Pferde, 1 Orks, 1 Elben; Ziel: 0 Pferde, 2 Orks, 2 Elben 
8. Start: 1 Pferde, 1 Orks, 0 Elben; Ziel: 0 Pferde, 2 Orks, 3 Elben 
- Start: 1 Pferde, 0 Orks, 3 Elben; Ziel: 0 Pferde, 3 Orks, 0 Elben <span style="color: red;">Invalid</span>
- Start: 1 Pferde, 0 Orks, 2 Elben; Ziel: 0 Pferde, 3 Orks, 1 Elben <span style="color: red;">Invalid</span>
- Start: 1 Pferde, 0 Orks, 1 Elben; Ziel: 0 Pferde, 3 Orks, 2 Elben <span style="color: red;">Invalid</span>
- Start: 1 Pferde, 0 Orks, 0 Elben; Ziel: 0 Pferde, 3 Orks, 3 Elben <span style="color: red;">Invalid</span>
- Start: 0 Pferde, 3 Orks, 3 Elben; Ziel: 1 Pferde, 0 Orks, 0 Elben <span style="color: red;">Invalid</span>
- Start: 0 Pferde, 3 Orks, 2 Elben; Ziel: 1 Pferde, 0 Orks, 1 Elben <span style="color: red;">Invalid</span>
- Start: 0 Pferde, 3 Orks, 1 Elben; Ziel: 1 Pferde, 0 Orks, 2 Elben <span style="color: red;">Invalid</span>
- Start: 0 Pferde, 3 Orks, 0 Elben; Ziel: 1 Pferde, 0 Orks, 3 Elben <span style="color: red;">Invalid</span>
9. Start: 0 Pferde, 2 Orks, 3 Elben; Ziel: 1 Pferde, 1 Orks, 0 Elben
10. Start: 0 Pferde, 2 Orks, 2 Elben; Ziel: 1 Pferde, 1 Orks, 1 Elben
- Start: 0 Pferde, 2 Orks, 1 Elben; Ziel: 1 Pferde, 1 Orks, 2 Elben <span style="color: red;">Invalid</span>
11. Start: 0 Pferde, 2 Orks, 0 Elben; Ziel: 1 Pferde, 1 Orks, 3 Elben 
12. Start: 0 Pferde, 1 Orks, 3 Elben; Ziel: 1 Pferde, 2 Orks, 0 Elben
- Start: 0 Pferde, 1 Orks, 2 Elben; Ziel: 1 Pferde, 2 Orks, 1 Elben <span style="color: red;">Invalid</span>
13. Start: 0 Pferde, 1 Orks, 1 Elben; Ziel: 1 Pferde, 2 Orks, 2 Elben
14. Start: 0 Pferde, 1 Orks, 0 Elben; Ziel: 1 Pferde, 2 Orks, 3 Elben
15. Start: 0 Pferde, 0 Orks, 3 Elben; Ziel: 1 Pferde, 3 Orks, 0 Elben
- Start: 0 Pferde, 0 Orks, 2 Elben; Ziel: 1 Pferde, 3 Orks, 1 Elben <span style="color: red;">Invalid</span>
- Start: 0 Pferde, 0 Orks, 1 Elben; Ziel: 1 Pferde, 3 Orks, 2 Elben <span style="color: red;">Invalid</span>
16. Start: 0 Pferde, 0 Orks, 0 Elben; Ziel: 1 Pferde, 3 Orks, 3 Elben  <-- <span style="color: green;">Endzustand</span>

Aktionen:
  - (2-0-R) 2 Orks reiten rechts
  - (2-E-R) 2 Elben reiten rechts
  - (1-OE-R) 1 Ork und Elbe reiten rechts
  - (1-O-R) 1 Ork reitet rechts 
  - (1-E-R) 1 Elbe reitet rechts
  - (2-O-L) 2 Orks reiten links
  - (2-E-L) 2 Elben reiten links
  - (1-OE-L) 1 Ork und Elbe reiten links
  - (1-O-L) 1 Ork reitet links
  - (1-E-L) 1 Elbe reitet links
### 2. Skizzieren Sie den Problemgraph.
Invalide Zusände sind hier nichtmehr aufgeführt
```
Nodes: (Pferd, Orks_links, Elben_links)
Pferd: 1 = links, 0 = rechts
```
[![](https://mermaid.ink/img/pako:eNp9lVFv2jAUhf9K5KpTKwVk30uAROpetmgvnajaPU28RLOBaCFBwWjtgP--JMTxxUZDCnLy6Zx7j-3ER_arkoolbF1nu03w_Losg-D-PnjTWa2DT8G3KiuCvf4o8nIdtKwdq-BFLDDFYJUXRXK3WsnmF-51Xf1WyZ1E7MejP7nUmwR271TKFzzlvVTKVjxIIQNP2iptU1rt25umvkj5w8PLkwgXzZU-8cfHAQgKBAFIAQ4ArBVcWUEKFAABSIG1QmuFV1ZoFUgU3WS0gDeAE0ULkAKrEFYhrhR9cu4k5yY5d5Jzk5w7yblJzp3k3CTnNHm_PD_qrNznOq9KskbBaPT5JEaL0eupT2uXybD0P9AwQRh2DAgTDqMF0a5yr_ObAa9RQRg49cBjJIRtBoZGbzWDXkGf2YJg95fjaRtFLwQQhp4OHUZC0ILomeJlyfs32dg-n_qZdFhne4Fmbq7gwKwQPVN0GNWhfS8cHQ6ewqsHN5jfp9mIQBg6jAQ088bJLrXNoMPEjYB2l_qe4IWwAa92olvQwvRGQfRMkYXNgZBLluj6oEK2VfU2a2_ZsfscM71RW7VkSTOUapUdCr1ky_LcyHZZ-bOqtkZZV4f1hiWrrNg3d4edbL7gX_OsOW22w9NalVLVX6pDqVkyj6dx58KSI3tnCcBsLOZxhPM4nqOAeBKyj_ZxNI5nE4Q4av4jnE3PIfvbFebjGKJoPoFoOp3EXMwgZErmuqq_X4667sQ7_wN7UM4r?type=png)](https://mermaid.live/edit#pako:eNp9lVFv2jAUhf9K5KpTKwVk30uAROpetmgvnajaPU28RLOBaCFBwWjtgP--JMTxxUZDCnLy6Zx7j-3ER_arkoolbF1nu03w_Losg-D-PnjTWa2DT8G3KiuCvf4o8nIdtKwdq-BFLDDFYJUXRXK3WsnmF-51Xf1WyZ1E7MejP7nUmwR271TKFzzlvVTKVjxIIQNP2iptU1rt25umvkj5w8PLkwgXzZU-8cfHAQgKBAFIAQ4ArBVcWUEKFAABSIG1QmuFV1ZoFUgU3WS0gDeAE0ULkAKrEFYhrhR9cu4k5yY5d5Jzk5w7yblJzp3k3CTnNHm_PD_qrNznOq9KskbBaPT5JEaL0eupT2uXybD0P9AwQRh2DAgTDqMF0a5yr_ObAa9RQRg49cBjJIRtBoZGbzWDXkGf2YJg95fjaRtFLwQQhp4OHUZC0ILomeJlyfs32dg-n_qZdFhne4Fmbq7gwKwQPVN0GNWhfS8cHQ6ewqsHN5jfp9mIQBg6jAQ088bJLrXNoMPEjYB2l_qe4IWwAa92olvQwvRGQfRMkYXNgZBLluj6oEK2VfU2a2_ZsfscM71RW7VkSTOUapUdCr1ky_LcyHZZ-bOqtkZZV4f1hiWrrNg3d4edbL7gX_OsOW22w9NalVLVX6pDqVkyj6dx58KSI3tnCcBsLOZxhPM4nqOAeBKyj_ZxNI5nE4Q4av4jnE3PIfvbFebjGKJoPoFoOp3EXMwgZErmuqq_X4667sQ7_wN7UM4r)
# Search.02: Suchverfahren (Wüzburg zu München)
## 1. Tiefensuche
```
Stack [(Wü)];                                   Begegnete Elemente []
Stack [(WüEr), WüFr, WüNü];                     Begegnete Elemente [Wü]
Stack [(WüFr), WüNü];                           Begegnete Elemente [Wü, Er] <-- keine neuen Elemente (Sackgasse)
Stack [(WüFrKa), WüFrMa, WüNü];                 Begegnete Elemente [Wü, Er, Fr]
Stack [(WüFrKaMü), WüFrMa, WüNü];               Begegnete Elemente [Wü, Er, Fr, Ka]

Ziel erreicht über Wü-Fr-Ka-Mü
```
## 2. Breitensuche
```
Queue [(Wü)];                                   Begegnete Elemente []
Queue [WüNü, WüFr, (WüEr)];                     Begegnete Elemente [Wü]
Queue [WüNü, (WüFr)];                           Begegnete Elemente [Wü, Er] <-- keine neuen Elemente (Sackgasse)
Queue [WüFrMa, WüFrKa, (WüNü)];                 Begegnete Elemente [Wü, Er, Fr]
Queue [WüNüSt, WüNüMü, WüFrMa, (WüFrKa)];       Begegnete Elemente [Wü, Er, Fr, Nü]
Queue [WüFrKaMü, WüNüSt, WüNüMü, (WüFrMa)];     Begegnete Elemente [Wü, Er, Fr, Nü, Ka]
Queue [WüFrMaKa, WüFrKaMü, WüNüSt, (WüNüMü)];   Begegnete Elemente [Wü, Er, Fr, Nü, Ka, Ma]

Ziel erreicht über Wü-Nü-Mü (Optimale Lösung)
```
### Ist h(n) zulässig für A*?
1.  h(n) <= h*(n). Soll heißen h(n) muss eine Unterschäzung oder Gleichsetzung der Optimallösung sein.
2. h(n) >= 0 für jeden Knoten
3. h(n) = 0 für jeden Zielknoten

Dies gilt zu überprüfen:
-[ ] h(n) <= h*(n) <span style="color: red;">Invalid</span>

 h*(n) errechnet durch die Wegkosten

|            | Restwegschätzung | Restwegkosten |           Bedingung erfüllt           |
|:----------:|:----------------:|:-------------:|:-------------------------------------:|
|  Ausburg   |        0         |      84       |                  Ja                   |
|   Erfurt   |       400        |      456      |                  Ja                   |
| Frankfuhrt |       100        |      487      |                  Ja                   |
| Karlsruhe  |        10        |      334      |                  Ja                   |
|   Kassel   |       460        |      502      |                  Ja                   |
|  Mannheim  |       200        |      414      |                  Ja                   |
|  München   |        0         |       0       |                  Ja                   |
|  Nünberg   |       537        |      167      | <span style="color: red;">Nein</span> |
| Stuttgart  |       300        |      350      |                  Ja                   |
|  Würburg   |       170        |      270      |                  Ja                   |

-[x] h(n) >= 0 für jeden Knoten
-[x] h(n) = 0 für jeden Zielknoten (Ausburg könnte eine suboptimale schätzung sein ist, aber dennoch valide)

Die Nünberg wegschätzung muss also angepasst werden (Vorschlag: 150) und
damit ist der h(n) Datensatz Zulässig was für die A* Tree-Search variante ausreichend ist
## 3. A*
```
Queue [Wü(0+170)];                                       Begegnete Elemente []
Queue [WüEr(186+400), WüFr(217+100), (WüNü(103+150))];   Begegnete Elemente [Wü]
Queue [WüEr(186+400), WüNüSt(286+300), WüFr(217+100), WüNüMü(270+0)];   Begegnete Elemente [Wü, Nü]

Ziel erreicht über Wü-Nü-Mü (Optimale Lösung)
```
# Search.03: Dominanz
# Search.04: Beweis der Optimalität von A*