# Übungsblatt: Overfitting & MLP

## NN.MLP.01: Perzeptron-Netze (2P)

Konstruieren Sie ein Netz mit drei Perzeptrons, welches für zwei
Eingabevariablen $`x_1`$ und $`x_2`$ die in der folgenden Abbildung
blau-grau dargestellten Bereiche mit +1 klassifiziert. Benutzen Sie die
$`\mathop{\text{sign}}`$-Funktion als Aktivierungsfunktion.

<p align="center"><picture><source media="(prefers-color-scheme: light)" srcset="/img.png"><source media="(prefers-color-scheme: dark)" srcset="images/perzeptron_netz_dark.png"><img src="images/perzeptron_netz.png" width="50%"></picture></p><p align="center">Abbildung
1</p>

> Schicht 1: $`0b_1 = 2; 0w_1 = -1; 0w_2 = 0`$  
> Schicht 1: $`1b_1 = 3; 1w_1 = 0; 1w_2 = -1`$  
> Schicht 2: $`b_1 = -1; w_1 = 1; w_2 = 1`$

## NN.MLP.02: Vorwärtslauf im MLP (2P)

Gegeben sei ein MLP mit 25 Zellen in der Eingangsschicht, 64 Zellen in
der ersten versteckten Schicht, 32 Zellen in der zweiten versteckten
Schicht und 4 Zellen in der Ausgabeschicht (die Bias-Zellen nicht
mitgezählt). In allen Zellen wird die ReLU Aktivierungsfunktion
verwendet.

- Was sind die Dimensionen der Gewichtsmatrizen $`W^{[1]}`$, $`W^{[2]}`$
  und $`W^{[3]}`$ und der Bias-Vektoren $`b^{[1]}`$, $`b^{[2]}`$ und
  $`b^{[3]}`$?

> $`W^{[1]} = 1600\;(R^{64*25})`$  
> $`W^{[2]} = 2048\;(R^{32*64})`$  
> $`W^{[3]} = 128\;(R^{4*32})`$  
> $`b^{[1]} = 64\;(R^{64*1})`$   
> $`b^{[2]} = 32\;(R^{32*1})`$  
> $`b^{[3]} = 4\;(R^{4*1})`$  

- Wie wird die Ausgabe berechnet? Schreiben Sie den Vorwärtslauf in
  Matrix-Notation auf. Wie könnte man die Ausgabe deuten; welches
  Problem könnte durch dieses Netzwerk möglicherweise gelöst werden?


> $`z^{[1]} = W^{[1]}x+b^{[1]}`$  
> $`a^{[1]} = ReLu(z^{[1]})`$
> 
> $`z^{[2]} = W^{[2]}a^{[1]}+b^{[2]}`$  
> $`a^{[2]} = ReLu(z^{[2]})`$
> 
> $`z^{[3]} = W^{[3]}a^{[2]}+b^{[3]}`$  
> $`a^{[3]} = ReLu(z^{[3]})`$
> 
> Eine Klassifizierung eines Unregelmäßigen Cluster wäre hier gut möglich, wobei dieses Modell nicht nur Binär klassifiziert

## NN.MLP.03: Tensorflow Playground (6P)

Benutzen Sie den [Neural Network
Playground](https://playground.tensorflow.org/), um die unten gelisteten
Experimente durchzuführen. Achten Sie bei allen Experimenten auf das
Verhalten der Trainings- und Testkosten. Sie können mit Hilfe der
Checkbox unter der Ausgabezelle (ganz rechts, unten) die Testdaten ein-
und ausblenden. Der Play-Knopf startet dabei das Training und der
Reload-Knopf setzt das Netzwerk zurück.

1.  (1P) Trainieren Sie ein **logistisches Regressionsmodell** zunächst
    auf dem “**Gaussian**” Datensatz (linear separierbarer Datensatz
    links-unten), danach auf den anderen Datensätzen.

>|              | Entscheidungsgrenze | Trainingskosten | Testkosten | Konvergenzgeschwindigkeit | Konsistenz des Ergebnisses | Hidden Layers | Anmerkung                 |
>|--------------|---------------------|-----------------|------------|---------------------------|----------------------------|---------------|---------------------------|
>| Gaussian     | lineare Grenze      | 0.000           | 0.000      | ca. 0.300                 | wiederholbar               |               |                           |
>| Circle       | lineare Grenze      | 0.501           | 0.510      | ca. 0.030                 | wiederholbar               |               | Priorisiert inneren Kreis |
>| Exclusive or | lineare Grenze      | 0.502           | 0.529      | ca. 0.030                 | wiederholbar               |               | Priorisiert Orange Daten  |
>| Spiral       | linare Grenze       | 0.464           | 0.499      | ca. 0.030                 | wiederholbar               |               |                           |


2.  (3P) Trainieren Sie ein **MLP** mit

    1. einer versteckten Schicht mit 2 Neuronen, 
    2. einer versteckten Schicht mit 3 Neuronen, 
    3. einer versteckten Schicht mit 5 Neuronen, 
    4. zwei versteckten Schichten mit jeweils 5 Neuronen pro Schicht 
    5. drei versteckten Schichten mit jeweils 7 Neuronen pro Schicht 
    6. vier versteckten Schichten mit jeweils 7 Neuronen pro Schicht

    auf dem kreisförmigen (**Circle**) und auf dem spiralförmigen
    (**Spiral**) Datensatz, mehrmals mit jeweils den
    Aktivierungsfunktionen ReLU, tanh und Sigmoid. Hat die Auswahl der
    Aktivierungsfunktion einen Einfluss auf die Form der
    Entscheidungsgrenze oder die Geschwindigkeit der Berechnung?

>| Circle       | Entscheidungsgrenze                        | Trainingskosten | Testkosten | Konvergenzgeschwindigkeit | Konsistenz des Ergebnisses | Hidden Layers                                                                   | Anmerkung                                          |
>|--------------|--------------------------------------------|-----------------|------------|---------------------------|----------------------------|---------------------------------------------------------------------------------|----------------------------------------------------|
>| i. ReLu      | unregelmäßiges Rechteck (wächst unendlich) | ca. 0.233       | ca. 0.320  | ca. 0.200                 | nicht wiederholbar         | einfarbig                                                                       | seperiert Unregelmäßig; Overfitting                |
>| i. Tanh      | Parable                                    | ca. 0.226       | ca. 0.242  | ca. 0.600                 | nicht wiederholbar         | Linearegrenze                                                                   | seperiret Unregelmäßig; Resistenter zu Overfitting |
>| i. Sigmoid   | Parable                                    | ca. 0.229       | ca. 0.290  | ca. 0.400                 | nicht wiederholbar         | einfarbig                                                                       | seperiert Unregelmäßig; Overfitting                |
>| ii. ReLu     | unregelmäßiges Rechteck (6-Eck möglich)    | ca. 0.000       | ca. 0.003  | ca. 1.000                 | wiederholbar (-ish)        | einfarbig                                                                       | kann sich kurz verhängen                           |
>| ii. Tanh     | abgerundetes Dreieck                       | ca. 0.001       | ca. 0.004  | ca. 5.000                 | wiederholbar (-ish)        | Linearegrenze                                                                   |                                                    |
>| ii. Sigmoid  | abgerundetes Dreieck                       | ca. 0.001       | ca. 0.006  | ca. 7.000                 | wiederholbar (-ish)        | einfarbig                                                                       | kann sich kurz verhängen                           |
>| iii. ReLu    | unregelmäßiges Vieleck                     | ca. 0.000       | ca. 0.005  | ca. 2.000                 | wiederholbar (-ish)        | einfarbig                                                                       |                                                    |
>| iii. Tanh    | abgerundeteres Dreieck                     | ca. 0.001       | ca. 0.003  | ca. 2.000                 | wiederholbar (-ish)        | Linearegrenze                                                                   |                                                    |
>| iii. Sigmoid | abgerundeteres Dreieck                     | ca. 0.001       | ca. 0.003  | ca. 5.000                 | wiederholbar (-ish)        | einfarbig                                                                       | kann sich kurz verhängen                           |
>| iv. ReLu     | unregelmäßiges Vieleck                     | ca. 0.000       | ca. 0.000  | ca. 2.000                 | wiederholbar (-ish)        | einfarbig                                                                       |                                                    |
>| iv. Tanh     | abgerundeteres Dreieck                     | ca. 0.000       | ca. 0.001  | ca. 1.500                 | wiederholbar (-ish)        | Linearegrenze; unregelmäßige Formen                                             |                                                    |
>| iv. Sigmoid  | abgerundeteres Dreieck                     | ca. 0.001       | ca. 0.002  | ca. 3.000                 | wiederholbar (-ish)        | einfarbig                                                                       | kann sich kurz verhängen                           |
>| v. ReLu      | unregelmäßiges Vieleck                     | ca. 0.000       | ca. 0.000  | ca. 0.500                 | wiederholbar (-ish)        | einfarbig                                                                       |                                                    |
>| v. Tanh      | abgerundetereres Dreieck                   | ca. 0.000       | ca. 0.000  | ca. 0.600                 | wiederholbar (-ish)        | Linearegrenze; unregelmäßige Formen; unregelmäßige Formen                       |                                                    |
>| v. Sigmoid   | abgerundetereres Dreieck                   | ca. 0.001       | ca. 0.000  | ca. 5.000                 | wiederholbar (-ish)        | einfarbig                                                                       | kann sich kurz verhängen                           |
>| vi. ReLu     | unregelmäßiges Vieleck                     | ca. 0.000       | ca. 0.000  | ca. 0.300                 | wiederholbar (-ish)        | einfarbig                                                                       |                                                    |
>| vi. Tanh     | abgerundetereres Dreieck                   | ca. 0.000       | ca. 0.000  | ca. 0.500                 | wiederholbar (-ish)        | Linearegrenze; unregelmäßige Formen; unregelmäßige Formen; unregelmäßige Formen |                                                    |
>| vi. Sigmoid  | abgerundetereres Dreieck                   | ca. 0.500       | ca. 0.500  | ca. 10.000                | nicht wiederholbar         | einfarbig                                                                       | kann sich daurhaft verhängen                       |                            

> Spiral wird sich ähnlich verhalten, wobei eine Spiral Klassifizierung komplexere Modelle Benötigt

3.  (2P) Setzen Sie nun den **Noise-Level auf 15** und wiederholen Sie
    die Experimente. Wann kann von einer Überanpassung gesprochen
    werden?

> Sigmoid: empfindlich gegen Noise
> Tanh: tendenziell Robuster
> ReLu: am robustesten 

Sprechen Sie für alle Experimente die folgenden Punkte an:

- Wie verhält sich die Entscheidungsgrenze?
- Was können Sie über Trainings- und Testkosten sagen? Entsteht eine
  Überanpassung?
- Wie schnell wird die Entscheidungsgrenze berechnet?
- Können alle Datenpunkte jedes mal korrekt klassifiziert werden? Warum?
- Untersuchen und vergleichen Sie die Ausgaben der Zellen in den
  versteckten Schichten, in dem Sie die Maus über die jeweilige Zelle
  bewegen. Bemerken Sie einen wesentlichen Unterschied in den Ausgaben
  der ersten Schicht im Vergleich zu der letzten Schicht?

------------------------------------------------------------------------

<img src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" width="10%">

Unless otherwise noted, this work is licensed under CC BY-SA 4.0.

<blockquote><p><sup><sub><strong>Last modified:</strong> 302e9ce (homework: rescale images (NN-MLP), 2025-08-18)<br></sub></sup></p></blockquote>
