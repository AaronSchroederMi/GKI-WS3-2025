# Übungsblatt: Entscheidungsbäume (Decision Tree Learner DTL)

## Bonus: Starke vs. Schwache KI (2P)

Recherchieren Sie und diskutieren Sie folgende Punkte:

- Ist ein System wie ChatGPT “intelligent”? Was ist der Kern des
  Systems?
- Gibt es Systeme, die intelligent sind? Was tun diese, wie arbeiten
  sie?
- Brauchen wir wirklich Intelligenz in Systemen? Reicht auch schwache
  KI, d.h. reichen intelligent *wirkende* Systeme?
- Absicht vs. Auswirkung: vorteilhafte Anwendungen vs. Unfälle
  (Robustheit und falsche Korrelationen, Fairness, Sicherheit)
  vs. Missbrauch (Spam, Betrug, Spear-Phishing, Desinformation)
  vs. doppelte Verwendung (“*dual use*”: Raketen, Kernkraft,
  Genbearbeitung, …) vs. *Bias* (Voreingenommenheit)

*Thema*: Schwache vs. starke KI, Auswirkungen und Nutzen

## DTL.01: Entscheidungsbäume mit CAL3 und ID3 (6P)

Es ist wieder Wahlkampf: Zwei Kandidaten O und M bewerben sich um die
Kanzlerschaft. Die folgende Tabelle zeigt die Präferenzen von sieben
Wählern.

| Nr. | Alter      | Einkommen | Bildung  | Kandidat |
|:----|:-----------|:----------|:---------|:---------|
| 1   | $`\ge 35`$ | hoch      | Abitur   | O        |
| 2   | $`< 35`$   | niedrig   | Master   | O        |
| 3   | $`\ge 35`$ | hoch      | Bachelor | M        |
| 4   | $`\ge 35`$ | niedrig   | Abitur   | M        |
| 5   | $`\ge 35`$ | hoch      | Master   | O        |
| 6   | $`< 35`$   | hoch      | Bachelor | O        |
| 7   | $`< 35`$   | niedrig   | Abitur   | M        |

Trainieren Sie nacheinander mit den Verfahren CAL3 (3P) und ID3 (3P) auf
der obigen Trainingsmenge je einen Entscheidungsbaum. Nutzen Sie für
CAL3 dabei die Schwellen $`S_1=4`$ und $`S_2=0.7`$.

Sie können dafür eine Handsimulation anwenden oder die Algorithmen
implementieren. Sie können gern auch die Java-Klassen im Paket
[`aima.core.learning`](https://github.com/aimacode/aima-java/blob/AIMA3e/aima-core/src/main/java/aima/core/learning/learners/DecisionTreeLearner.java)
bzw. die Python-Klassen in
[`learning.py`](https://github.com/aimacode/aima-python/blob/master/learning.py)
als Ausgangspunkt nutzen.

> ### CAL3
> Alter = $`x_1`$ ; Einkommen = $`x_3`$ ; Bildung = $`x_3`$  
> $`x_1`$: Ausprägung 2  
> $`x_2`$: Ausprägung 2  
> $`x_3`$: Ausprägung 3
> 0. $`*`$
> ---
> 1. $`/01/`$
> 2. $`/02/`$
> 3. $`/02,M1/`$
> 4. $`/02,M2/`$ --> $`x_1(/M1/, *)`$
> 5. $`x_1(/O1,M1/, *)`$
> 6. $`x_1(/O1,M1/,/O1/)`$
> 7. $`x_1(/O1,M1/, /O1,M1/)`$
> ---
> 1. $`x_1(/O2,M1/, /O1,M1/)`$
> 2. $`x_1(/O2,M1/, /O2,M1/)`$
> 3. $`x_1(/O2,M2/, /O2,M1/)`$ --> $`x_1(x_2(/M1/, *), /O2,M1/)`$
> 4. $`x_1(x_2(/M1/, /M1/), /O2,M1/)`$
> 5. $`x_1(x_2(/O1,M1/, /M1/), /O2,M1/)`$
> 6. $`x_1(x_2(/O1,M1/, /M1/), /O3,M1/)`$ --> $`x_1(x_2(/O1,M1/, /M1/), O)`$
> 7. $`x_1(x_2(/O1,M1/, /M1/), O)`$ (**Fehler**)
> ---
> 1. $`x_1(x_2(/O2,M1/, /M1/), O)`$
> 2. $`x_1(x_2(/O2,M1/, /M1/), O)`$
> 3. $`x_1(x_2(/O2,M2/, /M1/), O)`$ --> $`x_1(x_2(x_3(*,*,/M1/), /M1/), O)`$
> 4. $`x_1(x_2(x_3(*,*,/M1/), /M2/), O)`$
> 5. $`x_1(x_2(x_3(*,/O1/,/M1/), /M2/), O)`$
> 6. $`x_1(x_2(x_3(*,/O1/,/M1/), /M2/), O)`$
> 7. $`x_1(x_2(x_3(*,/O1/,/M1/), /M2/), O)`$ (**Fehler**)
> ---
> 1. $`x_1(x_2(x_3(/O1/,/O1/,/M1/), /M2/), O)`$
> 2. $`x_1(x_2(x_3(/O1/,/O1/,/M1/), /M2/), O)`$
> 3. $`x_1(x_2(x_3(/O1/,/O1/,/M2/), /M2/), O)`$
> 4. $`x_1(x_2(x_3(/O1/,/O1/,/M2/), /M3/), O)`$
> 5. $`x_1(x_2(x_3(/O1/,/O2/,/M2/), /M3/), O)`$
> 6. $`x_1(x_2(x_3(/O1/,/O2/,/M2/), /M3/), O)`$
> 7. $`x_1(x_2(x_3(/O1/,/O2/,/M2/), /M3/), O)`$ (**Fehler**)
> ---
> 1. $`x_1(x_2(x_3(/O2/,/O2/,/M2/), /M3/), O)`$
> 2. $`x_1(x_2(x_3(/O2/,/O2/,/M2/), /M3/), O)`$
> 3. $`x_1(x_2(x_3(/O2/,/O2/,/M3/), /M3/), O)`$
> 4. $`x_1(x_2(x_3(/O2/,/O2/,/M2/), /M4/), O)`$ --> $`x_1(x_2(x_3(/O2/,/O2/,/M2/), M), O)`$
> 5. $`x_1(x_2(x_3(/O2/,/O3/,/M2/), M), O)`$
> 6. $`x_1(x_2(x_3(/O2/,/O3/,/M2/), M), O)`$
> 7. $`x_1(x_2(x_3(/O2/,/O3/,/M2/), M), O)`$ (**Fehler**)
> ---
> 1. $`x_1(x_2(x_3(/O3/,/O3/,/M2/), M), O)`$
> 2. $`x_1(x_2(x_3(/O3/,/O3/,/M2/), M), O)`$
> 3. $`x_1(x_2(x_3(/O3/,/O3/,/M3/), M), O)`$
> 4. $`x_1(x_2(x_3(/O3/,/O3/,/M3/), M), O)`$
> 5. $`x_1(x_2(x_3(/O3/,/O4/,/M3/), M), O)`$ --> $`x_1(x_2(x_3(/O3/,O,/M3/), M), O)`$
> 6. $`x_1(x_2(x_3(/O3/,O,/M3/), M), O)`$
> 7. $`x_1(x_2(x_3(/O3/,O,/M3/), M), O)`$ (**Fehler**)
> ---
> 1. $`x_1(x_2(x_3(/O4/,O,/M3/), M), O)`$ --> $`x_1(x_2(x_3(O,O,/M3/), M), O)`$
> 2. $`x_1(x_2(x_3(O,O,/M3/), M), O)`$
> 3. $`x_1(x_2(x_3(O,O,/M4/), M), O)`$ --> $`x_1(x_2(x_3(O,O,M), M), O)`$
> 
> Trainingsfehler = 1/7 < 1 - $`S_2`$

> ### ID3
>
> #### 0 ID3({1,2,3,4,5,6,7}, {$`x_1, x_2, x_3`$}, O)
> 
> $`H(S) = -\sum_k p_k \log_2 p_k = -((4/7*log_24/7) + (3/7*log_23/7)) = 0.98522`$ (Bit)  
> $`R(S, A)\sum_{v \in \mathop{\text{Values}}(A)} \frac{|S_v|}{|S|} H(S_v)`$  
> 
> $`R(S, x_1) = 4/7 * (-(2/4*log_22/4+2/4log_22/4)) + 3/7 * (-(2/3*log_22/3+1/3log_21/3)) = 0.96498`$ (Bit)  
> $`R(S, x_2) = 4/7 * (-(3/4*log_23/4+1/4*log_21/4))+ 3/7 * (-(1/3*log_21/3+2/3*log_22/3)) = 0.85714`$ (Bit)
> $`R(S, x_3) = 3/7 * (-(1/3*log_21/3 + 2/3*log_22/3)) + 2/7 * (-(2/2*log_22/2))+ 2/7 * (-(1/2*log_21/2+1/2*log_21/2)) = 0.67926`$ (Bit)
> 
> $`Gain(S, x_1) = 0.98522 - 0.96498 = 0.02024`$ (Bit)  
> $`Gain(S, x_2) = 0.98522 - 0.85714 = 0.12808`$ (Bit)  
> $`Gain(S, x_3) = 0.98522 - 0.67926 = 0.30596`$ (Bit)
> 
> $`x_3(*,*,*)`$
> 
> #### 3.1 ID3({1,4,7}, {$`x_1,x_2`$}, M)
> 
> $`H(S) = -\sum_k p_k \log_2 p_k = -((1/3*log_21/3) + (2/3*log_22/3)) = 0.91829`$ (Bit)
> 
> $`R(S, x_1) = 2/3 * (-(1/2*log_21/2+1/2log_21/2)) + 1/3 * (-(1/1log_21/1)) = 0.66666`$ (Bit)   
> $`R(S, x_2) = 1/3 * (-(1/1*log_21/1))+ 2/3 * (-(1/2*log_21/2+1/2*log_21/2)) = 0.66666`$ (Bit)
> 
> $`Gain(S, x_1) = 0.91829 - 0.66666 = 0.25163`$ (Bit)  
> $`Gain(S, x_2) = 0.91829 - 0.66666 = 0.25163`$ (Bit)
> 
> $`x_3(x_1(*,*),*,*)`$
> 
> #### 1.1 ID3({1, 4}, {x_2}, OM)
> 
> $`x_3(x_1(x_2(*,*),*),*,*)`$
> 
> #### 2.1 ID3({1}, {x_2}, O)
> Alle Beispiele haben dieselbe Klasse (O)
> 
> $`x_3(x_1(x_2(O,*),*),*,*)`$
> 
> #### 2.1 ID3({4}, {x_2}, M)
> Alle Beispiele haben dieselbe Klasse (M)
> 
> $`x_3(x_1(x_2(O,M),*),*,*)`$
> 
> #### 1.2 ID3({7}, {x_2}, M)
> Alle Beispiele haben dieselbe Klasse (M)
> 
> $`x_3(x_1(x_2(O,M),M),*,*)`$
> 
> #### 3.2 ID3({2,5}, {$`x_1,x_2`$}, O)
> Alle Beispiele haben dieselbe Klasse (O)
> 
> $`x_3(x_1(x_2(O,M),M),O,*)`$
> 
> #### 3.3 ID3({3,6}, {$`x_1,x_2`$}, OM)
> 
> $`H(S) = -\sum_k p_k \log_2 p_k = -((1/2*log_21/2) + (1/2*log_21/2)) = 1`$ (Bit)
>
> $`R(S, x_1) = 1/2 * (-(1/1*log_21/1)) + 1/2 * (-(1/1log_21/1)) = 0`$ (Bit)   
> $`R(S, x_2) = 2/2 * (-(1/2*log_21/2+1/2log_21/2)) = 1`$ (Bit)
>
> $`Gain(S, x_1) = 1 - 0 = 1`$ (Bit)  
> $`Gain(S, x_2) = 1 - 1 = 0`$ (Bit)
> 
> $`x_3(x_1(x_2(O,M),M),O,x_1(*,*))`$
> 
> #### 1.1 ID3({3}, {x_2}, M)
> Alle Beispiele haben dieselbe Klasse (M)
> 
> $`x_3(x_1(x_2(O,M),M),O,x_1(M,*))`$
> 
> #### 1.2 ID3({6}, {x_2}, O)
> Alle Beispiele haben dieselbe Klasse (O)
> 
> $`x_3(x_1(x_2(O,M),M),O,x_1(M,O))`$

## DTL.02: Pruning (1P)

Vereinfachen Sie schrittweise den Baum

$$
x_3(x_2(x_1(C,A), x_1(B,A)), x_1(x_2(C,B), A))
$$

> Allgemeine Transformationsregel
> 
> 1. $`x_3(x_2(x_1(C,A), x_1(B,A)), x_1(x_2(C,B), A))`$ --> $`x_3(x_1(x_2(C,B), x_2(A,A)), x_1(x_2(C,B), A))`$
> 
> $`x_2(A,A)`$ ist ein redundanter Test
> 
> 2. $`x_3(x_1(x_2(C,B), x_2(A,A)), x_1(x_2(C,B), A))`$ --> $`x_3(x_1(x_2(C,B), A), x_1(x_2(C,B), A))`$
> 
> Allgemeine Transformationsregel
> 
> 3. $`x_3(x_1(x_2(C,B), A), x_1(x_2(C,B), A))`$ --> $`x_1(x_3(x_2(C,B), x_2(C,B)), x_3(A, A))`$
> 
> $`x_3(A,A)`$ ist ein redundanter Test
> $`x_3(x_2(C,B), x_2(C,B))`$ ist ein redundanter Test
> 
> 4. $`x_1(x_3(x_2(C,B), x_2(C,B)), x_3(A, A))`$ --> $`x_1(x_2(C,B), A)`$
> 

so weit wie möglich.

Nutzen Sie die linearisierte Schreibweise. Geben Sie die jeweils
verwendete Regel an.

*Thema*: Anwendung der Transformations- und Pruning-Regeln

## DTL.03: Machine Learning mit Weka (3P)

Weka
([waikato.github.io/weka-wiki/](https://waikato.github.io/weka-wiki/))
ist eine beliebte Sammlung von (in Java implementierten) Algorithmen aus
dem Bereich des Maschinellen Lernens. Laden Sie sich das Tool in der
aktuellen stabilen Version herunter und machen Sie sich mit der
beiliegenden Dokumentation vertraut.

Laden Sie sich die Beispieldatensätze “Zoo” (`zoo.csv`) und “Restaurant”
(`restaurant.csv`) aus dem AIMA-Repository
([github.com/aimacode/aima-data](https://github.com/aimacode/aima-data))
herunter.[^2] Zum Laden der Beispieldatensätze in Weka müssen die
`.csv`-Dateien eine Kopfzeile mit den Namen der Attribute haben. Passen
Sie die Dateien entsprechend an und laden Sie diese im Reiter
“Pre-Process” mit “Open file …”.

*Hinweis*: Wenn Sie *Weka 3.6* einsetzen, sind alle für dieses Blatt
erforderlichen Algorithmen bereits vorhanden. In neueren Versionen
müssen Sie in der Weka-Haupt-GUI den Paketmanager unter “Tools” starten
und dort nach einem Paket suchen, welches ID3 enthält, und dieses Paket
nachinstallieren.

1.  Training mit J48 (1P)

    Wechseln Sie auf den Reiter “Classify” und wählen Sie mit dem Button
    “Choose” den Entscheidungsbaum-Lerner J48 aus. (Dies ist eine
    Java-Implementierung von C4.5. Die ID3-Implementierung funktioniert
    für den `zoo.csv`-Datensatz leider nicht …)

    Lernen Sie für die beiden Datensätze je einen Entscheidungsbaum. Wie
    sehen die Bäume aus? Wie hoch ist jeweils die Fehlerrate für den
    Trainingssatz? (Stellen Sie unter “Test options” den Haken auf “Use
    training set”.) Interpretieren Sie die **Confusion Matrix**.

2.  ARFF-Format (1P)

    Lesen Sie in der beiliegenden Doku zum Thema “ARFF” nach. Dabei
    handelt es sich um ein spezielles Datenformat, womit man Weka
    mitteilen kann, welche Attribute es gibt und welchen Typ diese haben
    und welche Werte auftreten dürfen.
    ([Link](https://waikato.github.io/weka-wiki/formats_and_processing/arff/))

    Erklären Sie die Unterschiede zwischen “nominal”, “ordinal” (bzw.
    “numeric”) und “string”.

    Konvertieren Sie den Zoo- und Restaurantdatensatz in das
    ARFF-Format. Beachten Sie, dass die ID3-Implementierung von Weka
    nicht mit bestimmten Attributtypen umgehen kann.

3.  Training mit ID3 und J48 (1P)

    Trainieren Sie für die im letzten Schritt erstellten Datensätze (Zoo
    und Restaurant) im ARFF-Format erneut Entscheidungsbäume. Nutzen Sie
    diesmal sowohl ID3 als auch J48.

    Vergleichen Sie wieder die Ergebnisse (Entscheidungsbäume,
    Fehlerraten, Confusion Matrix) untereinander und mit den Ergebnissen
    aus dem J48-Lauf mit den `.csv`-Dateien.

*Thema*: Kennenlernen von Weka