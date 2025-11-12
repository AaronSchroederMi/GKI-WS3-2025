# Übungsblatt: Constraints

## CSP.01: Logikrätsel (2P)

Betrachten Sie die Variante des berühmten
[“Einstein-Rätsels”](https://de.wikipedia.org/wiki/Zebrar%C3%A4tsel) auf
Wikipedia.

Formulieren Sie das Problem als CSP (Variablen, Wertebereiche,
Constraints) zunächst auf dem Papier. Machen Sie sich klar, was die
Variablen und was deren Wertebereiche sind. Schreiben Sie die
Constraints als (unäre bzw. binäre) Relationen zwischen den Variablen
auf.

*Hinweis*: Machen Sie sich zunächst klar, was die Variablen und was
deren Wertebereiche sind. Schreiben Sie die Constraints als (unäre bzw.
binäre) Relationen auf.

> ### Zebrarätsel
> $`CSP: \{V, D, C\}`$
> 
> $`V = \{a, b, c, d, e\}`$  
> 
> $`D = \{`$  
> $`Haus=\{rot,grün,weiß,gelb,blau\}`$  
> $`Person=\{Engländer,Spanier,Ukrainer,Norweger,Japaner\}`$  
> $`Haustier=\{Hund,Schnecken,Fuchs,Pferd,Zebra\}`$  
> $`Getränk=\{Kaffee,Tee,Milch,Orangensaft,Wasser\}`$  
> $`Zigaretten=\{Old-Gold,Kools,Chesterfield,Lucky-Strike,Parliaments\}`$  
> $`\}`$ D gilt global für alle Klassen.
> Auch tritt jedes Element in der Domäne genau einmal Auf
> 
> $`C = \{`$  
>   $`c_1 = ((V), (rot, Engländer, *, *, *) )`$  
>   $`c_2 = ((V), (*, Spanier, Hund, *, *))`$  
>   $`c_3 = ((V), (grün, *, *, Kaffee, *)\; \& \; \text{direkt rechts vom weißen Haus})`$  
>   $`c_4 = ((V), (*, Ukrainer, *, Tee, *))`$  
>   $`c_5 = ((V), (*, *, Schnecken, *, Old-Gold))`$  
>   $`c_6 = ((V), (gelb, *, *, *, Kools)\; \& \;\text{neben Haus mit Pferd} )`$  
>   $`c_7 = ((V), (*, *, *, Milch, *)\; \& \; \text{Haus steht mittig})`$  
>   $`c_8 = ((V), (*, Norweger, *, *, *)\;\&\:\text{Haus steht ganz links}\;\&\;\text{neben blauem Haus})`$  
>   $`c_{9} = ((V), (*, *, *, *, Chesterfield))\;\&\;\text{neben Haus mit Fuchs}`$  
>   $`c_{10} = ((V), (*, *, *, Orangensaft, Lucky-Strike))`$  
>   $`c_{11} = ((V), (*, Japaner, *, *, Parliaments))`$  
> $`\}`$  

*Thema*: Formulierung von Problemen als CSP

## CSP.02: Framework für Constraint Satisfaction (3P)

Lösen Sie nun das obige Rätsel (aus CSP.01):

1.  Lösen Sie das Rätsel zunächst mit dem Basis-Algorithmus `BT_Search`
    aus der Vorlesung.

> | Struktur                                                                                                                                                                                                                                              | Konflikt? | Constraint |
>  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------
> | *, *, *, *, *                                                                                                                                                                                                                                         | nein      |          |
> | ...                                                                                                                                                                                                                                                   |           |          |
> | (rot, Norweger, Hund, Kaffee, Old-Gold), *, *, *, *                                                                                                                                                                                                   | ja        | c_1      |
> | (grün, Norweger, Schnecken, Kaffee, Old-Gold), *, *, *, *                                                                                                                                                                                             | ja        | c_3      |
> | (grün, Norweger, Schnecken, Kaffee, Old-Gold), <br/> (blau, Engländer, Hund, Tee, Lucky-Strike), *, *, *                                                                                                                                              | ja        | c_1, ... |
> | ...                                                                                                                                                                                                                                                   |           |          |
> | (grün, Norweger, Schnecken, Kaffee, Old-Gold), <br/> (blau, Spanier, Hund, Wasser, Chesterfield), *, *, *                                                                                                                                             | nein      |          |
> | (grün, Norweger, Schnecken, Kaffee, Old-Gold), <br/> (blau, Spanier, Hund, Wasser, Chesterfield), <br/> (rot, Engländer, Fuchs, Orangensaft, Lucky-Strike), *, *                                                                                      | ja        | c_7      |
> | ...                                                                                                                                                                                                                                                   |           |          |
> | (grün, Norweger, Schnecken, Kaffee, Old-Gold), <br/> (blau, Spanier, Hund, Wasser, Chesterfield), <br/> (weiß, Japaner, Fuchs, Milch, Parliaments), *, *                                                                                              | ja        | c_3      |
> | ...                                                                                                                                                                                                                                                   |           |          |
> | (gelb, Norweger, Fuchs, Wasser, Kools), <br/> (blau, Ukrainer, Pferd, Tee, Chesterfield), <br/> (weiß, Japaner, Zebra, Milch, Parliaments), *, *                                                                                                      | nein      |          |
> | (gelb, Norweger, Fuchs, Wasser, Kools), <br/> (blau, Ukrainer, Pferd, Tee, Chesterfield), <br/> (weiß, Japaner, Zebra, Milch, Parliaments), <br/> (grün, Spanier, Hund, Kaffee, Old-Gold), *                                                          | ja        | c_5      |
> | ...                                                                                                                                                                                                                                                   |           |          |
> | (gelb, Norweger, Fuchs, Wasser, Kools), <br/> (blau, Ukrainer, Pferd, Tee, Chesterfield), <br/> (weiß, Japaner, Zebra, Milch, Parliaments), <br/> (weiß, Spanier, Hund, Orangensaft, Lucky-Strike), *                                                 | nein      |          |
> | (gelb, Norweger, Fuchs, Wasser, Kools), <br/> (blau, Ukrainer, Pferd, Tee, Chesterfield), <br/> (rot, Engländer, Schenecken, Milch, Old-Gold), <br/> (weiß, Spanier, Hund, Orangensaft, Lucky-Strike), <br/>(grün, Japaner, Zebra, Kaffe, Parliament) | nein      |          |

2.  Erweitern Sie den Algorithmus um die Heuristiken MRV und
    Gradheuristik und lösen Sie das Problem erneut. Vergleichen Sie die
    Ergebnisse und die Laufzeit der beiden Experimente.

> \*, \*, \*, \*, \*  
> Wähle V mit MRV: c oder a  
> Wähle V mit LCV: ?  
> ...
> 
> Ich bin mir ein Wenig unsicher wie man hier den LCV berechnet, da ja alle Constraints (zumindest in meiner Modellierung), global wirken

3.  Wenden Sie vor dem Start von `BT_Search` den AC-3 an. Erhalten Sie
    damit bereits eine Lösung (bzw. Unlösbarkeit)? Falls nicht, wenden
    Sie anschließend den ergänzten Algorithmus aus Schritt (2) an.
    Vergleichen Sie wieder die Ergebnisse und die Laufzeiten.

> Es liefert eine Lösung da das Zebra Rätsel nur eine Lösung hat und somit die Constraints nur aller erfüllt werden können, wenn die richtige Lösung gefunden wurde

4.  Wenden Sie die *Min-Conflicts* Heuristik zur Lösung des Problems an.
    Vergleichen Sie wieder die Ergebnisse und die Laufzeiten.

> findet Lösung nur mit einer Gewissen Wahrscheinlichkeit. kann sich verhängen ist für dieses Problem etwas ungeeignet

Sie können dafür eine Handsimulation anwenden oder die Algorithmen
implementieren. Sie können gern auch die Java-Klassen im Paket
[`aima.core.search.csp`](https://github.com/aimacode/aima-java/tree/AIMA3e/aima-core/src/main/java/aima/core/search/csp)
bzw. die Python-Klassen in
[`csp.py`](https://github.com/aimacode/aima-python/blob/master/csp.py)
als Ausgangspunkt nutzen.[^1]

## CSP.03: Kantenkonsistenz mit AC-3 (1P)

Sei $`D=\lbrace 0, \ldots, 5 \rbrace`$, und ein Constraintproblem
definiert durch

$$
\langle
    \lbrace v_1, v_2, v_3, v_4 \rbrace,
    \lbrace D_{v_1} = D_{v_2} = D_{v_3} = D_{v_4} = D \rbrace,
    \lbrace c_1, c_2, c_3, c_4 \rbrace
\rangle
$$

mit

- $`c_1=\left((v_1,v_2), \lbrace (x,y) \in D^2 | x+y = 3 \rbrace\right)`$,
- $`c_2=\left((v_2,v_3), \lbrace (x,y) \in D^2 | x+y \le 3 \rbrace\right)`$,
- $`c_3=\left((v_1,v_3), \lbrace (x,y) \in D^2 | x \le y \rbrace\right)`$
  und
- $`c_4=\left((v_3,v_4), \lbrace (x,y) \in D^2 | x \ne y \rbrace\right)`$.

1.  Zeichnen Sie den Constraint-Graph

> [![](https://mermaid.ink/img/pako:eNpVkM1OxCAUhV8F79Z2wt9AS5yVLnXj0pAYIsy00UKDrVE7fXcB6yRuLpzzcS5wF3gJ1oGCUzRjh-4ftf94JrnQXFguXPviorquz3m9RgmjA2JntJ2jG6OFMXSzQfY_mOzkXQAr4OqQDQ5VekNvQU1xdhUMLg4mS1i0R0jD1LnBaVBpa0181aD9mjKj8U8hDH-xGOZTB-po3t6TmkdrJnfXm_S74eJG562Lt2H2EygiSw9QC3wmRflu3wrGCZYMt0TwCr5AUS52kjSCMN42eC8FXyv4LtfinZRtw2SLBRNYUEErcLafQnz4HWyZ7_oDDplrow?type=png)](https://mermaid.live/edit#pako:eNpVkM1OxCAUhV8F79Z2wt9AS5yVLnXj0pAYIsy00UKDrVE7fXcB6yRuLpzzcS5wF3gJ1oGCUzRjh-4ftf94JrnQXFguXPviorquz3m9RgmjA2JntJ2jG6OFMXSzQfY_mOzkXQAr4OqQDQ5VekNvQU1xdhUMLg4mS1i0R0jD1LnBaVBpa0181aD9mjKj8U8hDH-xGOZTB-po3t6TmkdrJnfXm_S74eJG562Lt2H2EygiSw9QC3wmRflu3wrGCZYMt0TwCr5AUS52kjSCMN42eC8FXyv4LtfinZRtw2SLBRNYUEErcLafQnz4HWyZ7_oDDplrow)
> [![](https://mermaid.ink/img/pako:eNpVkM1OxCAUhV8F79Z2wt9AS5yVLnXj0pAYYplpkyk0SI3a6bsLWCdxc-Gcj3OBu8Cb7ywoOAUz9ejxWbuPV5ILzYXlwrUrLqrr-pLXW5QwOiB2Qds5ujFaGEN3G2T_g8lO3hWwAm4O2eBQpTcMHagYZlvBaMNosoRFO4Q0xN6OVoNK284ezXyOGrRbU2wy7sX78S8Z_HzqQR3N-T2peepMtA-DSR8cr26wrrPh3s8ugiKs9AC1wGdSlO_2rWCcYMlwSwSv4AsU5WInSSMI422D91LwtYLvci3eSdk2TLZYMIEFFbQC2w3Rh6ff2ZYRrz-V-Gzi?type=png)](https://mermaid.live/edit#pako:eNpVkM1OxCAUhV8F79Z2wt9AS5yVLnXj0pAYYplpkyk0SI3a6bsLWCdxc-Gcj3OBu8Cb7ywoOAUz9ejxWbuPV5ILzYXlwrUrLqrr-pLXW5QwOiB2Qds5ujFaGEN3G2T_g8lO3hWwAm4O2eBQpTcMHagYZlvBaMNosoRFO4Q0xN6OVoNK284ezXyOGrRbU2wy7sX78S8Z_HzqQR3N-T2peepMtA-DSR8cr26wrrPh3s8ugiKs9AC1wGdSlO_2rWCcYMlwSwSv4AsU5WInSSMI422D91LwtYLvci3eSdk2TLZYMIEFFbQC2w3Rh6ff2ZYRrz-V-Gzi)

2.  Wenden Sie den AC-3-Algorithmus auf das CSP an. Geben Sie den
    Zustand der Queue und das Ergebnis von `ARC_Reduce`, d.h. den
    Ergebniszustand des aktuellen $`D_i`$, für jede Iteration des
    Algorithmus an.

> result wir wie folgt dargestellt ($`v_1`$, $`v_2`$, $`v_3`$, $`v_4`$)
> ```
>  0. result: ([1-5],[1-5],[1-5],[1-5]);  Queue: [(v_1, v_2, c_1), (v_1, v_2, c_3), (v_2, v_3, c_2), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_3, v_2, c_2), (v_3, v_4, c_4), (v_4, v_3, c_4)]
>  1. result: ([1|2],[1-5],[1-5],[1-5]);  Queue: [(v_1, v_3, c_3), (v_2, v_3, c_2), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_3, v_2, c_2), (v_3, v_4, c_4), (v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3)]
>  2. result: ([1|2],[1-5],[1-5],[1-5]);  Queue: [(v_2, v_3, c_2), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_3, v_2, c_2), (v_3, v_4, c_4), (v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3)]
>  3. result: ([1|2],[1|2],[1-5],[1-5]);  Queue: [(v_2, v_1, c_1), (v_3, v_1, c_3), (v_3, v_2, c_2), (v_3, v_4, c_4), (v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2)]
>  4. result: ([1|2],[1|2],[1-5],[1-5]);  Queue: [(v_3, v_1, c_3), (v_3, v_2, c_2), (v_3, v_4, c_4), (v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2)]
>  5. result: ([1|2],[1|2],[1-5],[1-5]);  Queue: [(v_3, v_2, c_2), (v_3, v_4, c_4), (v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2)]
>  6. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_3, v_4, c_4), (v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2), (v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
>  7. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_4, v_3, c_4), (v_2, v_1, c_1), (v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2), (v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
>  8. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_2, v_1, c_1), (v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2), (v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
>  9. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_3, v_1, c_3), (v_1, v_2, c_1), (v_3, v_2, c_2), (v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
> 10. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_1, v_2, c_1), (v_3, v_2, c_2), (v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
> 11. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_3, v_2, c_2), (v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
> 12. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_2, v_3, c_2), (v_1, v_3, c_3), (v_4, v_3, c_4)]
> 13. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_1, v_3, c_3), (v_4, v_3, c_4)]
> 14. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: [(v_4, v_3, c_4)]
> 15. result: ([1|2],[1|2],[1|2],[1-5]);  Queue: []
> > ```

*Thema*: Handsimulation des AC-3-Algorithmus

## CSP.04: Forward Checking und Kantenkonsistenz (1P)

Betrachten Sie erneut das CSP aus der vorigen Aufgabe und die Zuweisung
$`\alpha = \lbrace v_1 \to  2 \rbrace`$.

1.  Erzeugen Sie Kantenkonsistenz in $`\alpha`$. Geben Sie hierzu die
    Wertebereiche der Variablen vor und nach dem Erzeugen der
    Kantenkonsistenz an.

    *Hinweis*: Sie dürfen annehmen, dass der Wertebereich von Variablen
    mit bereits zugewiesenen Werten nur aus dem zugewiesenen Wert
    besteht, während unbelegte Variablen den vollen Wertebereich haben.

    *Hinweis*: Sie müssen zur Lösung dieser Teilaufgabe nicht den AC-3
    nutze.

> 0. v_1 (2), v_2 ([1-5]), v_3 ([1-5])
> 1. v_1 (2), v_2 (1), v_3 (2)  
> (v_4 wäre dann hier [1|3-5])


2.  Führen Sie Forward-Checking in $`\alpha`$ aus. Vergleichen Sie das
    Ergebnis mit (1).

> 0. v_1 (2), v_2 ([1-5]), v_3 ([1-5])
> 1. v_1 (2), v_2 (1), v_3 ([2-5])  
> (v_4 wäre dann hier [1-5])

*Thema*: Kantenkonsistenz und Forward Checking verstehen

## CSP.05: Planung von Indoor-Spielplätzen (3P)

Sie sind für die Planung von Indoor-Spielplätzen zuständig.

Ein Spielplatz hat eine rechteckige Form, etwa 40x100 m. Zur
Vereinfachung wird diese Fläche in ein gleichmäßiges Raster unterteilt,
beispielsweise 10x10 cm. Es gibt am Rand mehrere Türen (normaler
Eingang, Notausgänge).

Auf dieser Grundfläche sollen verschiedene Spielgeräte angeordnet
werden, beispielsweise Go-Kart-Bahnen, Hüpfburgen und Kletterberge.
Diese Spielgeräte haben selbst eine rechteckige Grundfläche, wobei die
Abmessungen rastergenau sein sollen (also Vielfache der Rastergröße).
Weiterhin gibt es eine Bar, die als größerer rechteckiger Bereich
modelliert werden kann (keine Unterscheidung in Tresen plus Tische plus
Stühle o.ä. notwendig).

Die Aufgabe besteht darin, die Spielgeräte und den Bar-Bereich nach
bestimmten Randbedingungen anzuordnen. Zu diesen Vorgaben gehört, dass
sich die Spielgeräte nicht überlappen oder berühren, dass bestimmte
Sicherheitsabstände eingehalten werden (1m zw. den Spielgeräten), dass
Entspannungszonen eingerichtet werden und dass Sichtlinien gewährleistet
sind (z.B. sollten die Aktivitäten am Kletterberg vom Barbereich aus
beobachtet werden können). Die Bar ist bevorzugt direkt am Eingang zu
finden. Notausgänge dürfen nicht verstellt werden.

Abstrahieren Sie das gegebene Problem angemessen und geben Sie eine
geeignete Modellierung als CSP an. Definieren Sie sich ein paar
Spielgeräte und lösen Sie das Problem mit Hilfe von *MAC* und
*Min-Conflicts*.

> CSP = $`(V, D, C)`$
> 
>$`V = \{Eingang, Notausgang, Bar, Hüpfburg, GoKartBahn, Kletterberg\}`$
> 
> $`D = ((Position),(Dimensionen)) = \{`$  
>           $`D_{Eingang} = \{((0, [1-99]), (0, 1)), (([1-39], 0),(1, 0)),((40, [1-99]), (0, 1)), (([1-39], 100),(1, 0))\}`$,  
>           $`D_{Notausgang} = ((20, 0), (2,0))`$,  
>           $`D_{Bar} = \{(([0-10], [0-80]),(30, 20)), (([0-20], [0-70]),(20, 30))\}`$,  
>           $`D_{Hüpfburg} = \{(([0-35],[0-95]),(5, 5))\}`$,  
>           $`D_{GoKartBahn} = \{(([0-25],[0-80]),(15, 20)), (([0-20],[0-85]),(20, 15))\}`$,  
>           $`D_{Kletterberg} = \{(([0-10],[0-70]),(30, 30))\}`$  
> $`\}`$
> 
> $`C = \{`$  
>          $`c_1 = ((v_1 \in V,v_2 \in (V/v_1)), \text{1 Meter Abstand})`$,  
>          $`c_2 = (Eingang, Bar), \text{nicht mehr als 5 Meter entfernt})`$,  
>          $`c_3 = (Bar, Kletterberg), \text{in Sichtfeld sein (alias: nicht mehr als 5 Meter entfernt)})`$,   
> $`\}`$
> 
> 1 Meter Abstand: `(v_1.posX - 1 >= v_2.posX + v_2.sizeX || v_1.posX + v_1.sizeX <= v_2.posX - 1) && (v_1.posY - 1 >= v_2.posY + v_2.sizeY || v_1.posY + v_1.sizeY <= v_2.posY - 1)`  
> nicht mehr als 5 Meter entfernt: `(v_1.posX - 5 <= v_2.posX + v_2.sizeX || v_1.posY + v_1.sizeY >= v_2.posY - 5) && (v_1.posY - 5 <= v_2.posY + v_2.sizeY || v_1.posY + v_1.sizeY >= v_2.posY - 5)`

> ### MAC
>|   Eingang    |  Notausgang  |                           Bar                            |   Hüpfburg   |   GoKartBahn   |  Kletterberg   | Domänenreduzierung (vereinfacht) |
>|:------------:|:------------:|:--------------------------------------------------------:|:------------:|:--------------:|:--------------:|----------------------------------|
>|  D_Eingang   | (20,0),(2,0) | D_Bar <br/>(- mit höchstens 5 Meter Abstand von Eingang) |  D_Hüpfburg  |  D_GoKartBahn  | D_Kletterberg  | Umkreis von Notausgang           |
>| (18,0),(1,0) |      "       |                           ...                            |     ...      |      ...       |      ...       | Umkreis von Eingang              |
>|      "       |      "       |                      (0,2),(30, 20)                      |     ...      |      ...       |      ...       | Umkreis von Bar                  |
>|      "       |      "       |                            "                             | (31,0),(5,5) |      ...       |      ...       | Umkreis von Hüpfburg             |
>|      "       |      "       |                            "                             |      "       |      ...       | (0,23),(30,30) | Umkreis von Kletterberg          |
>|      "       |      "       |                            "                             |      "       | (0,54),(20,15) |       "        |                                  |

> ### Min-Conflict
> 
>|   Eingang    |  Notausgang  |      Bar       |   Hüpfburg   |   GoKartBahn    |   Kletterberg   |                                                                         Probleme |
>|:------------:|:------------:|:--------------:|:------------:|:---------------:|:---------------:|---------------------------------------------------------------------------------:|
>| (0,67),(0,1) | (20,0),(2,0) | (8,29),(20,30) | (4,10),(5,5) | (7,53),(20,15)  | (7,12),(30,30)  | c_2, c_1 (Bar, GoKartBahn),<br/>(Kletterberg, Bar),<br/>(Kletterberg, Hüpfburg), |
>|      "       |      "       | (5,70),(20,30) |      "       |        "        |        "        |                                                 c_3, c_1 (Kletterberg, Hüpfburg) |
>|      "       |      "       |       "        |      "       |        "        | (10,37),(30,30) |                                                    c_1 (Kletterberg, GoKartBahn) |
>|      "       |      "       |       "        |      "       | (25,37),(20,15) |        "        |                                                                                  |
>| (0,67),(0,1) | (20,0),(2,0) | (5,70),(20,30) | (4,10),(5,5) | (25,37),(20,15) | (10,37),(30,30) |                                                                                  |
>

*Thema*: Modellierung eines Real-World-Problems

## Bonus: DSL für Constraint Solving: MiniZinc (2P)

[MiniZinc](https://www.minizinc.org/) ist eine *Domain Specific
Language* (DSL) zum Modellieren von Constraint- und
Optimierungs-Problemen.

Schauen Sie sich das
[Tutorial](https://docs.minizinc.dev/en/stable/part_2_tutorial.html) an.
Stellen Sie das Einstein-Rätsel oder das Spielplatz-Problem in MiniZinc
dar. Nutzen Sie zur Ausführung einen der im
[Playground](https://play.minizinc.dev) angebotenen Solver. Vergleichen
Sie die Modellierung und die Laufzeiten mit Ihren Ergebnissen aus den
vorigen Aufgaben.

*Thema*: DSL zur Formulierung von Constraint-Problemen