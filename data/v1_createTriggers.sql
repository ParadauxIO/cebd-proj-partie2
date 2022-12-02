-- TODO 3.3 Créer un trigger pertinent
CREATE TRIGGER on_inscriptions_insert BEFORE INSERT ON LesInscriptions
BEGIN
    INSERT INTO log(message) VALUES ("Tentative d'ajout d'une nouvelle entrée aux inscriptions : " || new.numIn);
END;

CREATE TRIGGER on_inscriptions_delete_trigger AFTER DELETE ON LesInscriptions
BEGIN
    INSERT INTO log (message) VALUES ("Supprimé " || old.numIn);
END;

CREATE TRIGGER on_inscriptions_update AFTER UPDATE ON LesInscriptions
BEGIN
    INSERT INTO log(message) VALUES ("Mise à jour des inscriptions :" || old.numIn);
END;

CREATE TRIGGER on_resultats_insert BEFORE INSERT ON LesResultats
BEGIN
    INSERT INTO log(message) VALUES ("Tentative d'ajout d'une nouvelle entrée aux résultats : " || new.numEp);
END;

CREATE TRIGGER on_resultats_delete_trigger AFTER DELETE ON LesResultats
BEGIN
    INSERT INTO log (message) VALUES ("Supprimé " || old.numEp);
END;

CREATE TRIGGER on_resultats_update AFTER UPDATE ON LesResultats
BEGIN
    INSERT INTO log(message) VALUES ("Mise à jour des résultats :" || old.numEp);
END;