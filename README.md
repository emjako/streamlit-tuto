# Projet Streamlit

Une application web interactive basée sur Streamlit. Ce projet démontre comment créer une application complète intégrant des visualisations de données, une analyse statistique, du logging, des tests unitaires et une pipeline CI/CD avec GitHub Actions.

## Table des Matières
- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du Projet](#structure-du-projet)
- [Tests Unitaires](#tests-unitaires)
- [CI/CD](#cicd)
- [Pistes d'Amélioration](#pistes-damélioration)
- [Licence](#licence)

## Introduction

Ce projet a été développé pour illustrer les capacités de Streamlit dans la création d'applications web interactives sans nécessiter de compétences poussées en développement web. L'application propose deux pages principales :

- **Visualisation de données :** Affichage interactif des données générées, incluant des graphiques réalisés avec Matplotlib et des graphiques interactifs avec des widgets de filtrage.
- **Analyse de données :** Calcul de statistiques descriptives et réalisation d'une régression linéaire simple pour démontrer une analyse de données basique.

## Fonctionnalités

- **Navigation multi-pages :** Utilisation de la barre latérale pour basculer entre la visualisation et l'analyse.
- **Visualisations interactives :** Graphiques dynamiques réalisés avec Matplotlib et intégrés dans l'application grâce à Streamlit.
- **Analyse statistique :** Affichage des statistiques descriptives et calcul d'une régression linéaire sur les données.
- **Logging :** Suivi de l'exécution du code via le module `logging` pour faciliter le débogage.
- **Tests unitaires :** Vérification du bon fonctionnement des principales fonctionnalités à l'aide de `pytest`.
- **CI/CD :** Pipeline d'intégration
