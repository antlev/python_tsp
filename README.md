# Rapport Projet Python

Etant dans une filière Big Data, ou l’optimisation est le coeur de notre formation, j’ai décidé de faire un algorithme génétique permettant de résoudre un problème de voyageur de commerce.

En informatique, le problème du voyageur de commerce, ou problème du commis voyageur, est un problème d'optimisation qui, étant donné une liste de villes, et des distances entre toutes les paires de villes, détermine un plus court chemin qui visite chaque ville une et une seule fois et qui termine dans la ville de départ.

Le programme a été écrit en python 3.x

## Installation
Décompresser le dossier compressé à l’endroit de votre choix.

## Execution
Executer le main du programme.

## IHM
Lors du lancement du programme une fenêtre avec le menu principale s’ouvre.
Cette fenêtre permet de choisir le nombre de ville composant le problème du voyageur du commerce les paramètres de l’algorithme génétique.
Appuyer sur “Run” pour ouvrir un nouvelle fenêtre prêt à lancer l’algorithme correctement paramétré sur le problème du voyageur de commerce donné. Il est possible de lancer plusieurs problèmes en parallèle.


## Structure du programme

Le programme est développé en orienté objet.

Nous disposons de 4 classes : 
* IHM : contient tous les éléments de l’IHM et la thread principale
* TSP : permet de gérer une fenêtre et de lancer un problème du voyageur de commerce
* Genetic : workflow de l’algorithme, générique.
* Chromosome: contient les spécificités du problème pour l'algorithme génétique


### Ressources web utilisées pour le projet : 
Technique de crossover PMX : 
http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/PMXCrossoverOperator.aspx
