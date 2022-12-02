-- 1.3a : Détruire les tables manquantes et modifier celles ci-dessous
DROP TABLE IF EXISTS LesEpreuves;
DROP TABLE IF EXISTS LesSportifsEQ;
DROP TABLE IF EXISTS LesInscriptions;
DROP TABLE IF EXISTS LesResultats;

DROP VIEW IF EXISTS LesAgesSportifs;
DROP VIEW IF EXISTS LesNbEquipiers;
--  3.3 : pensez à détruire vos triggers !
DROP TABLE IF EXISTS log;
DROP TRIGGER IF EXISTS on_inscriptions_insert;
DROP TRIGGER IF EXISTS on_inscriptions_delete_trigger;
DROP TRIGGER IF EXISTS on_inscriptions_update;
DROP TRIGGER IF EXISTS on_resultats_insert;
DROP TRIGGER IF EXISTS on_resultats_delete_trigger;
DROP TRIGGER IF EXISTS on_resultats_update;