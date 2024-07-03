contact : boubacar.timera@efrei.net
date : 03/07/2024

---

# Le titanic : aurait-on pu prévoir à l'avance qui allait survivre ?
---

## But du notebook

Dans ce Notebook, nous allons faire l'étude du tristement célèbre jeu de données [des passagers du titanic](https://www.kaggle.com/c/titanic).

A partir d'un descriptif des passagers au moment où ils sont montés à bord, est-il possible de prédire qui allait s'en sortir ?

---

## Information

Le but de ce Notebook est d'étudier les données. On va utiliser pour cela quelques bibliothèques : pandas pour les manipulations de données, numpy pour les opérations mathématiques et plotly pour faire nos graphes. Des bibliothèques alternatives existent pour la visualisation de données (matplotlib, seaborn, bokeh...). numpy et pandas sont par contre des standards dans l'industrie.

Pour la Data Science, le standard de l'industrie est scikit-learn (tensorflow ou pytorch pour le deep learning). Nous les utiliserons dès les prochains cours.

---

## Données 

Utilisez les données qui sont dans le github. Si jamais vous n'y arrivez pas, vous pouvez récupérer les données en cliquant sur [ce lien](https://www.kaggle.com/c/titanic).

**Descriptif des données :**

|Variable | Definition |	Key |
|---|---|---|
|survival |	Survival |	0 = No, 1 = Yes |
|pclass 	Ticket class |	1 = 1st, 2 = 2nd, 3 = 3rd |
|sex |	Sex 	| |
|Age |	Age in years | | 	
|sibsp |	# of siblings / spouses aboard the Titanic | 	|
|parch |	# of parents / children aboard the Titanic 	| |
|ticket |	Ticket number 	| |
|fare |	Passenger fare 	| |
|cabin |	Cabin number 	| |
|embarked | 	Port of Embarkation |	C = Cherbourg, Q = Queenstown, S = Southampton |

Variable Notes

pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.
