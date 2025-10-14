# Bonus
### Recherchieren Sie, welche Probleme bereits mittels Computer- bzw. Robotereinsatz gelöst werden können und welche aktuell noch ungelöst sind.
#### Gelöst
- Geplante Produktionslinien (Wiederkehrende Bedingungen, strukturiertes statisches Umfeld)
- Sensorik: Oberflachenanalyse, Sortierung, Farberkennung
- Assistenzsysteme im straßenverkehr: Spurhalte-, Limiter-, Lenkassistenten
- Sprachverarbeitung: Speech to Text, Text to Speech, auch im Sinne der Vervollständigung (LLMs)
- Prozessoptimierung durch ML-Modelle
#### Ungelöst
- adaptive Roboter für unstrukturierte Dynamische Umgebungen (Ziel: i.d.r Humanoid)
- LLM Halluzinationen (Das Datenproblem)
  - Trainingsprozesse die primär durch Compute statt Datensatzgrößen skalierbar sind
- Fortgesetzte Lernprozesse in ML-Modellen die über Fine-Tuning und In-context learning hinausgehen
- Menschenähnliches Räumliches verständnis (Objekt) <-- könnte gegen argumentiert werden
- P-NP

Vor allem in hinblick auf die Lernprozesse in ML-Modellen ist der Daten aufwand enorm,  
wobei der Mensch ein weniger Daten intensiven Lernprozess zu haben scheint.

### Recherchieren und diskutieren Sie Auswirkungen auf die Gesellschaft durch die KI, etwa durch autonomes Fahren oder durch Large Language Models (LLM).
Häufig wird im Zusammenhang mit KI von Innovation und effizienten Lösungen gesprochen.
Dabei müssen jedoch die steigenden Strom- und Datenkosten durch Machine-Learning-Rechenzentren berücksichtigt werden.
Maschinelles Lernen ist nicht billig. Sei es ein LLM, ein Bild- oder gar ein Videoerzeugungsmodell wie Sora.
Das Training und der Betrieb dieser Modelle sind teuer und übersteigen in manchen Fällen sogar den Energieverbrauch ganzer Länder.
Aber das ist es ja alles wert. So zumindest die Hoffnung der Unternehmen, die unzählige Milliarden in die Entwicklung dieser Technologie stecken.
Vielleicht ja sogar zurecht.

Sollten sie sich hierbei jedoch irren, hätte das enorme Konsequenzen, nicht nur für die Tech-Giganten, sondern auch für den gesamten Aktienmarkt.
Der Wert des S&P 500 besteht zunehmend und größtenteils aus der Hoffnung auf KI.
Sollte dieses Vertrauen jemals verschwinden, werden der Markt und mit ihm auch Renten und Rücklagen (z. B. 401(k)-Konten) den Preis dafür zahlen.

Doch sollten die Modelle tatsächlich funktionsfähig, ökonomisch und produktivitätssteigernd sein, stellt sich die Frage, ob Arbeitsplätze künftig immer seltener werden und Arbeitstüchtigkeit bzw. Erwerbsarbeit vielleicht eines Tages der Vergangenheit angehören. (Weit in die Zukunft gedacht.)

Für den Moment sind KI-Modelle, insbesondere LLMs in aller Munde. Sie generieren fröhlich vor sich hin. In einigen Feldern ist dieser Anstieg der
Produktivtät sicherlich spürbar keine Frage. Jedoch gibt es auch einen Anstieg von sogenanntem Arbeits-Slob.
Dieser fördert nicht die Produktivität ganz im Gegenteil: Manche Arbeiter sind zunehmend irritiert von Dokumenten,
die auf den ersten Blick plausibel wirken, bei genauerem Hinsehen jedoch

- Artikel enthalten, die gar nicht verkauft werden,
- Preise nennen, die nie angeboten wurden, oder
- Zahlen ausweisen, die das Unternehmen nicht korrekt widerspiegeln.

Das soll kein Schwarzmalen sein, doch dieses Rennen nach immer mehr Innovation im Bereich der KI wirkt übereilt und nicht unbedingt ökonomisch sinnvoll.
Auch das ständige Rufen nach „AGI“ und der fehlende Plan für einen klaren Return on Investment (ROI) sind bedenklich und wirken ehrlich gesagt fragen auf.
Dennoch sehe ich Machine Learning und KI-Modelle, zumindest im Konzept, als unglaubliche Chance, die langfristig immer komplexere und variablere Aufgaben lösen kann.
Nach allem was ich gelesen, gehört und gesehen habe, ist für den Moment, die nahe Zukunft jedoch ungewiss.
# Search.01: Problemformalisierung, Zustandsraum
### 1. Formalisieren Sie das Problem (Zustände, Aktionen, Start- und Endzustand).
**Zustände:**
1. Start: 1 Pferde, 3 Orks, 3 Elben; Ziel: 0 Pferde, 0 Orks, 0 Elben| <-- **<span style="color: green;">Startzustand</span>**
2. Start: 1 Pferde, 3 Orks, 0 Elben; Ziel: 0 Pferde, 0 Orks, 3 Elben 
3. Start: 1 Pferde, 2 Orks, 3 Elben; Ziel: 0 Pferde, 1 Orks, 0 Elben 
4. Start: 1 Pferde, 2 Orks, 2 Elben; Ziel: 0 Pferde, 1 Orks, 1 Elben 
5. Start: 1 Pferde, 2 Orks, 0 Elben; Ziel: 0 Pferde, 1 Orks, 3 Elben 
6. Start: 1 Pferde, 1 Orks, 3 Elben; Ziel: 0 Pferde, 2 Orks, 0 Elben 
7. Start: 1 Pferde, 1 Orks, 1 Elben; Ziel: 0 Pferde, 2 Orks, 2 Elben 
8. Start: 1 Pferde, 1 Orks, 0 Elben; Ziel: 0 Pferde, 2 Orks, 3 Elben 
9. Start: 0 Pferde, 2 Orks, 3 Elben; Ziel: 1 Pferde, 1 Orks, 0 Elben
10. Start: 0 Pferde, 2 Orks, 2 Elben; Ziel: 1 Pferde, 1 Orks, 1 Elben
11. Start: 0 Pferde, 2 Orks, 0 Elben; Ziel: 1 Pferde, 1 Orks, 3 Elben 
12. Start: 0 Pferde, 1 Orks, 3 Elben; Ziel: 1 Pferde, 2 Orks, 0 Elben
13. Start: 0 Pferde, 1 Orks, 1 Elben; Ziel: 1 Pferde, 2 Orks, 2 Elben
14. Start: 0 Pferde, 1 Orks, 0 Elben; Ziel: 1 Pferde, 2 Orks, 3 Elben
15. Start: 0 Pferde, 0 Orks, 3 Elben; Ziel: 1 Pferde, 3 Orks, 0 Elben
16. Start: 0 Pferde, 0 Orks, 0 Elben; Ziel: 1 Pferde, 3 Orks, 3 Elben| <-- **<span style="color: green;">Endzustand</span>**
- Start: 1 Pferde, 3 Orks, 2 Elben; Ziel: 0 Pferde, 0 Orks, 1 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 3 Orks, 1 Elben; Ziel: 0 Pferde, 0 Orks, 2 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 2 Orks, 1 Elben; Ziel: 0 Pferde, 1 Orks, 2 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 1 Orks, 2 Elben; Ziel: 0 Pferde, 2 Orks, 1 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 0 Orks, 3 Elben; Ziel: 0 Pferde, 3 Orks, 0 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 0 Orks, 2 Elben; Ziel: 0 Pferde, 3 Orks, 1 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 0 Orks, 1 Elben; Ziel: 0 Pferde, 3 Orks, 2 Elben | **<span style="color: red;">Invalid</span>**
- Start: 1 Pferde, 0 Orks, 0 Elben; Ziel: 0 Pferde, 3 Orks, 3 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 3 Orks, 3 Elben; Ziel: 1 Pferde, 0 Orks, 0 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 3 Orks, 2 Elben; Ziel: 1 Pferde, 0 Orks, 1 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 3 Orks, 1 Elben; Ziel: 1 Pferde, 0 Orks, 2 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 3 Orks, 0 Elben; Ziel: 1 Pferde, 0 Orks, 3 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 2 Orks, 1 Elben; Ziel: 1 Pferde, 1 Orks, 2 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 1 Orks, 2 Elben; Ziel: 1 Pferde, 2 Orks, 1 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 0 Orks, 2 Elben; Ziel: 1 Pferde, 3 Orks, 1 Elben | **<span style="color: red;">Invalid</span>**
- Start: 0 Pferde, 0 Orks, 1 Elben; Ziel: 1 Pferde, 3 Orks, 2 Elben | **<span style="color: red;">Invalid</span>**

**Aktionen:**
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
Invalide Zustände sind hier nicht mehr aufgeführt
```
Nodes: (Pferd, Orks_links, Elben_links)
Pferd: 1 = links, 0 = rechts
```
[![](https://mermaid.ink/img/pako:eNp9lVFv2jAUhf9K5KpTKwVk30uAROpetmgvnajaPU28RLOBaCFBwWjtgP--JMTxxUZDCnLy6Zx7j-3ER_arkoolbF1nu03w_Losg-D-PnjTWa2DT8G3KiuCvf4o8nIdtKwdq-BFLDDFYJUXRXK3WsnmF-51Xf1WyZ1E7MejP7nUmwR271TKFzzlvVTKVjxIIQNP2iptU1rt25umvkj5w8PLkwgXzZU-8cfHAQgKBAFIAQ4ArBVcWUEKFAABSIG1QmuFV1ZoFUgU3WS0gDeAE0ULkAKrEFYhrhR9cu4k5yY5d5Jzk5w7yblJzp3k3CTnNHm_PD_qrNznOq9KskbBaPT5JEaL0eupT2uXybD0P9AwQRh2DAgTDqMF0a5yr_ObAa9RQRg49cBjJIRtBoZGbzWDXkGf2YJg95fjaRtFLwQQhp4OHUZC0ILomeJlyfs32dg-n_qZdFhne4Fmbq7gwKwQPVN0GNWhfS8cHQ6ewqsHN5jfp9mIQBg6jAQ088bJLrXNoMPEjYB2l_qe4IWwAa92olvQwvRGQfRMkYXNgZBLluj6oEK2VfU2a2_ZsfscM71RW7VkSTOUapUdCr1ky_LcyHZZ-bOqtkZZV4f1hiWrrNg3d4edbL7gX_OsOW22w9NalVLVX6pDqVkyj6dx58KSI3tnCcBsLOZxhPM4nqOAeBKyj_ZxNI5nE4Q4av4jnE3PIfvbFebjGKJoPoFoOp3EXMwgZErmuqq_X4667sQ7_wN7UM4r?type=png)](https://mermaid.live/edit#pako:eNp9lVFv2jAUhf9K5KpTKwVk30uAROpetmgvnajaPU28RLOBaCFBwWjtgP--JMTxxUZDCnLy6Zx7j-3ER_arkoolbF1nu03w_Losg-D-PnjTWa2DT8G3KiuCvf4o8nIdtKwdq-BFLDDFYJUXRXK3WsnmF-51Xf1WyZ1E7MejP7nUmwR271TKFzzlvVTKVjxIIQNP2iptU1rt25umvkj5w8PLkwgXzZU-8cfHAQgKBAFIAQ4ArBVcWUEKFAABSIG1QmuFV1ZoFUgU3WS0gDeAE0ULkAKrEFYhrhR9cu4k5yY5d5Jzk5w7yblJzp3k3CTnNHm_PD_qrNznOq9KskbBaPT5JEaL0eupT2uXybD0P9AwQRh2DAgTDqMF0a5yr_ObAa9RQRg49cBjJIRtBoZGbzWDXkGf2YJg95fjaRtFLwQQhp4OHUZC0ILomeJlyfs32dg-n_qZdFhne4Fmbq7gwKwQPVN0GNWhfS8cHQ6ewqsHN5jfp9mIQBg6jAQ088bJLrXNoMPEjYB2l_qe4IWwAa92olvQwvRGQfRMkYXNgZBLluj6oEK2VfU2a2_ZsfscM71RW7VkSTOUapUdCr1ky_LcyHZZ-bOqtkZZV4f1hiWrrNg3d4edbL7gX_OsOW22w9NalVLVX6pDqVkyj6dx58KSI3tnCcBsLOZxhPM4nqOAeBKyj_ZxNI5nE4Q4av4jnE3PIfvbFebjGKJoPoFoOp3EXMwgZErmuqq_X4667sQ7_wN7UM4r)
# Search.02: Suchverfahren (Würzburg zu München)
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
1.  h(n) <= h*(n). Soll heißen h(n) muss eine Unterschätzung oder Gleichsetzung der Optimallösung sein.
2. h(n) >= 0 für jeden Knoten
3. h(n) = 0 für jeden Zielknoten

Dies gilt zu überprüfen:

- [ ] h(n) <= h*(n)

 h*(n) errechnet durch die Wegkosten

|           | Restwegschätzung | Restwegkosten |           Bedingung erfüllt           |
|:---------:|:----------------:|:-------------:|:-------------------------------------:|
| Augsburg  |        0         |      84       |                  Ja                   |
|  Erfurt   |       400        |      456      |                  Ja                   |
| Frankfurt |       100        |      487      |                  Ja                   |
| Karlsruhe |        10        |      334      |                  Ja                   |
|  Kassel   |       460        |      502      |                  Ja                   |
| Mannheim  |       200        |      414      |                  Ja                   |
|  München  |        0         |       0       |                  Ja                   |
| Nürnberg  |       537        |      167      | <span style="color: red;">Nein</span> |
| Stuttgart |       300        |      350      |                  Ja                   |
| Würzburg  |       170        |      270      |                  Ja                   |

-[x] h(n) >= 0 für jeden Knoten  
-[x] h(n) = 0 für jeden Zielknoten (Augsburg könnte eine suboptimale schätzung sein ist, aber dennoch valide)

Die Nürnberg wegschätzung muss also angepasst werden (Vorschlag: 150) und
damit ist der h(n) Datensatz zulässig was für die A* Tree-Search variante ausreichend ist
## 3. A*
```
Queue [Wü(0+170)];                                                      Begegnete Elemente []
Queue [WüEr(186+400), WüFr(217+100), (WüNü(103+150))];                  Begegnete Elemente [Wü]
Queue [WüEr(186+400), WüNüSt(286+300), WüFr(217+100), WüNüMü(270+0)];   Begegnete Elemente [Wü, Nü]

Ziel erreicht über Wü-Nü-Mü (Optimale Lösung)
```

|              | Durchläufe | Datenstruktur größe | Begegneten Elementen | Variante     | Optimale Lösung |
|:------------:|:----------:|:-------------------:|:--------------------:|--------------|:---------------:|
| Tiefensuche  |     5      |      Stack: 3       |          4           | Graph-Search |      Nein       |
| Breitensuche |     7      |      Queue: 4       |          6           | Graph-Search |       Ja        |
|      A*      |     3      |      Queue: 4       |          2           | Tree-Search  |       Ja        |
# Search.03: Dominanz
### 1. Was bedeutet *“Eine Heuristik $`h_1(n)`$ dominiert eine Heuristik $`h_2(n)`$”*? 
Eine Heuristik dominiert eine andere Heuristik, wenn sie für alle Nodes n einen Größeren oder gleich großen Schätzwert angibt.  
Des Weiteren dürfen $`h_1(n)`$ und $`h_2(n)`$ nicht identisch sein.
### 2. Wie wirkt sich die Nutzung einer dominierenden Heuristik $`h_1(n)`$ in A\* aus (im Vergleich zur Nutzung einer Heuristik $`h_2`$, die von $`h_1`$ dominiert wird)?
Eine Heuristik die näher an der optimalen Lösung $`h^*(n)`$ liegt, während sie immer noch zulässig ist, wird ihre weiter entfernten Heuristiken dominieren.  
Das heißt, sie wird zumindest eine gleich gute Lösung, wenn nicht sogar ein besseres Liefern.
### 3. Geben Sie selbstgewählte Beispiele an.
Zwischen Städten reisen; Annahme $`h_1(n)`$, $`h_2(n)`$ sind zulässig  
$`h_1(n)`$: Luftlinie zwischen zwei Standorten  
$`h_2(n)`$: pessimistische wegschätzung

Es wird hier also $`h_2(n)`$ eine bessere Lösung als $`h_1(n)`$ liefern
# Search.04: Beweis der Optimalität von A*
Wenn $h$ zulässig ist und $`C^*`$ die optimale Lösung ist, so muss $`h`$ eine Lösung liefern die $`C^*`$ entspricht.

Nehmen wir an das $`A^*`$ eine suboptimale Lösung $`C`$ findet. Hierfür müssten zwei Bedingungen erfüllt sein.
1. Dieser suboptimale Weg $`C`$ muss > $`C^*`$ sein (Alias suboptimal)
2. Der Weg $`C`$ muss vor $`C^*`$ entdeckt werden (Sonst endet ja der Algorithmus)

Dies ist widersprüchlich da $A^*$ Knoten nach $`min(f(n)=g(n)+h(n))`$ expandiert. Es ist also nicht möglich das $`C`$ zuerst expandiert wird,  
da $`C`$ hierfür eine geringere $`f(n)`$ besitzen müsste.  
Also wird bei zulässiger Heuristik immer $`C^*`$ vor $`C`$ untersucht.