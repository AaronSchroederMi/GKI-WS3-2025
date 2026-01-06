# Übungsblatt: Backpropagation

## NN.Backprop.01: Gewichtsupdates für versteckte Schichten (2P)

In der Vorlesung wurde(n) die Gewichtsupdates bei der Backpropagation
für die Ausgabeschicht und die davor liegende letzte versteckte Schicht
hergeleitet, wobei in der Ausgabeschicht die Sigmoid und in der
versteckten Schicht die ReLU Aktivierungsfunktionen eingesetzt wurden.
Leiten Sie die Gewichtsupdates für die erste versteckte Schicht (für ein
Netz mit zwei echten versteckten Schichten) her. Verwenden Sie dabei die
Sigmoid Funktion als Aktivierung in allen Schichten.

*Thema*: Verständnis Backpropagation

> Ableitung Schicht 3: $`\delta^{(3)}_k=\frac{\partial E}{\partial W^{(3)}_k}=(\hat{y}k-yk)*\sigma'(z^{(3)}_k)`$  
> Ableitung Schicht 3: $`\frac{\partial E}{\partial W^{(3)}_{kj}}=\delta^{(3)}_k*a^{(2)}_j`$  
> Ableitung Schicht 2: $`\delta^{(2)}_i=\sum_k{W^{(3)}_{ki} \delta^{(3)}_k*\sigma'(z^{(2)}_i)}`$  
> Ableitung Schicht 2: $`\frac{\partial E}{\partial W^{(2)}_{ij}}=\delta^{(2)}_i*a^{(1)}_j`$  
> Ableitung Schicht 1: $`\delta^{(1)}_i=\sum_m{W^{(2)}_{mi}\delta^{(2)}_m*\sigma'(z^{(1)}_i)}`$  
> Ableitung schicht 1: $`\frac{\partial E}{\partial W^{(1)}_{ij}}=\delta^{(1)}_i*x_j`$  

## NN.Backprop.02: Forward- und Backpropagation (2P)

Betrachten Sie das folgende MLP mit zwei Schichten mit insgesamt zwei
Zellen. Die Gewichte sind an den Kanten angegeben. Das Netz erhält den
skalaren Input $`x`$ und berechnet daraus die Ausgabe $`y`$. Beide
Zellen verwenden die Aktivierungsfunktion
$`\sigma(z) = \frac{1}{ 1 + e^{-z} }`$.

<p align="center"><picture><source media="(prefers-color-scheme: light)" srcset="images/mlp_light.png"><source media="(prefers-color-scheme: dark)" srcset="images/mlp_dark.png"><img src="images/mlp.png" width="50%"></picture></p><p align="center">Abbildung
1</p>

- (1P) Berechnen Sie die Ausgabe $`y`$ für die Eingabe
  $`(x,y_T)=(0, 0.5)`$. Wie groß ist der Fehler?

- (1P) Berechnen Sie die partiellen Ableitungen für die Gewichte. Wie
  lauten die Gewichtsupdates für das obige Trainingsbeispiel? Setzen Sie
  $`\alpha = 0.01`$.

## NN.Backprop.03: MLP und Backpropagation (6P)

Implementieren Sie ein Feedforward MLP mit mindestens einer versteckten
Schicht. Nutzen Sie die Cross-Entropy Verlustfunktion.

- (2P) Implementieren Sie die Forwärtspropagation. Nutzen Sie als
  Aktivierungsfunktion in der Ausgangsschicht
  $`g(z) = \frac{1}{ 1 + e^{-z} }`$ und in der versteckten Schicht
  $`g(z) = ReLU(z)`$.

- (2P) Implementieren Sie das Backpropagations-Verfahren zum
  Aktualisieren der Gewichte. Achten Sie insbesondere darauf, die
  bereits berechneten partiellen Ableitungen der jeweils hinteren
  Schicht wieder zu verwenden (und nicht jeweils erneut zu berechnen!),
  d.h. propagieren Sie die Fehler von hinten nach vorn durch das Netz.

- (2P) Trainieren Sie das Netz für den Iris-Datensatz (iris.csv) aus dem
  [AIMA-Repository](https://github.com/aimacode/aima-data) und nutzen
  Sie dabei die Variante des stochastischen Gradientenabstiegs. Messen
  Sie pro Epoche (also nach jedem Durchlauf durch den kompletten
  Datensatz) den Trainingsfehler. Zeichnen Sie den Trainingsfehler als
  Diagramm über den Epochen auf.

Falls der Trainingsfehler nach einigen tausend Epochen nicht gegen einen
Wert nahe Null strebt, erweitern Sie Ihr Netz (beispielsweise eine
versteckte Schicht mehr oder mehr Zellen in der schon existierenden
versteckten Schicht, …) und trainieren Sie es erneut. Nach wievielen
Epochen ist der Trainingsfehler fast Null?

*Thema*: Verständnis MLP und Backpropagation, Gefühl für nötige Größe
des Netzes

------------------------------------------------------------------------

<img src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" width="10%">

Unless otherwise noted, this work is licensed under CC BY-SA 4.0.

<blockquote><p><sup><sub><strong>Last modified:</strong> 6672880 (markdown: switch to leaner yaml header (#438), 2025-08-09)<br></sub></sup></p></blockquote>
