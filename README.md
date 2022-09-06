# Cahier des charges

## Problèmes rencontrés

Dans le cadre de recherches incluant des problématiques de vie privée, il est parfois nécessaire de gérer les popup et bannières de gestion de ookies sur les sites à étudier, en effet il est intéressant d'observer l'impacte des choix de l'utilisateur sur le comportement du site.
Pour réaliser ces choix il existe une extension chrome, [Consent-O-matic](https://github.com/cavi-au/Consent-O-Matic) qui propose 5 types de cookies qu'il est possible d'accepter ou refuser dans les paramètres de l'extension. Malheureusement, cette extension utilise des templates uniques à un CMP (Consent Management Provider) à la fois et n'est donc par défaut pas suffisement général dans sa détection et son traitement des popup pour des applications à l'étude d'un grand nombre de sites qui peuvent avoir des CMP divers et variés. En effet il faudrait réaliser à la main des templates pour chaque CMP qui n'est pas utilisé par défaut.
De plus le temps d'execution de l'algorithme ne convient pas à une utilisation automatisée pour des fins de recherche sur un nombre de sites conséquent.

## But du projet

Suite à l'étude du besoin décrite ci-dessus, il est proposé de créer un outil permettant de gérer automatiquement tout type de popup de consentement au cookies sans avoir recours à une configuration manuelle.

Pour cela l'outil proposé devra :
- Détecter la présence d'une bannière de consentement
- En utilisant les préférences préalablement remplies par l'utilisateur :
	- Déterminer quels types de permissions peuvent être données
- Sur la bannière détecter les différents types de permissions demandées
- Intéragir avec la bannière pour appliquer les préférences déterminées

On ajoutera une contrainte sur la vitesse globale d'execution de l'outil dans le but de ne pas ralentir les tests automatiques pour lesquels il pourrait être utilisé.

Finalement, il serait idéalement utile d'incorporer l'outil dans un plugin [pupeteer](https://github.com/puppeteer/puppeteer) afin de faciliter et d'accélerer encore le processus de test automatique.
