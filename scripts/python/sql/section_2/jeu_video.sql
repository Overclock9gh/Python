-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  Dim 27 sep. 2020 à 20:15
-- Version du serveur :  10.3.17-MariaDB
-- Version de PHP :  7.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `jeu_video`
--

-- --------------------------------------------------------

--
-- Structure de la table `artefacts`
--

CREATE TABLE `artefacts` (
  `id` int(11) NOT NULL,
  `possesseur_id` int(11) NOT NULL,
  `poids` float DEFAULT NULL,
  `element` varchar(255) DEFAULT NULL,
  `attaque_bonus` varchar(255) DEFAULT NULL,
  `defense_bonus` varchar(255) DEFAULT NULL,
  `pouvoir_special` varchar(255) DEFAULT NULL,
  `annee_de_conception` date NOT NULL DEFAULT '0476-01-01'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `artefacts`
--

INSERT INTO `artefacts` (`id`, `possesseur_id`, `poids`, `element`, `attaque_bonus`, `defense_bonus`, `pouvoir_special`, `annee_de_conception`) VALUES
(1, 1, 20, '20', 'vent', '3', '20', '0000-00-00'),
(2, 2, 15, '10', 'électricité', '20', '10', '0000-00-00');

-- --------------------------------------------------------

--
-- Structure de la table `heros`
--

CREATE TABLE `heros` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `affinite` varchar(255) DEFAULT NULL,
  `attaque` int(11) DEFAULT NULL,
  `defense` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `heros`
--

INSERT INTO `heros` (`id`, `nom`, `prenom`, `age`, `affinite`, `attaque`, `defense`) VALUES
(1, 'Iwatani', 'Naofumi', 20, 'potion', 0, 6),
(2, 'Motoyasu', 'Kitamura', 21, 'feu', 10, 7);

-- --------------------------------------------------------

--
-- Structure de la table `partenaires`
--

CREATE TABLE `partenaires` (
  `id` int(11) NOT NULL,
  `chef_id` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `affinite` varchar(255) DEFAULT NULL,
  `support_bonus` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `partenaires`
--

INSERT INTO `partenaires` (`id`, `chef_id`, `nom`, `prenom`, `affinite`, `support_bonus`) VALUES
(1, '1', 'Filo', 'Raphtalia', 'vent', 35),
(2, '2', 'Malty', 'Melromarc', 'magie', 25);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `artefacts`
--
ALTER TABLE `artefacts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pouvoir_special` (`pouvoir_special`);

--
-- Index pour la table `heros`
--
ALTER TABLE `heros`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `partenaires`
--
ALTER TABLE `partenaires`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `artefacts`
--
ALTER TABLE `artefacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `heros`
--
ALTER TABLE `heros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `partenaires`
--
ALTER TABLE `partenaires`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
