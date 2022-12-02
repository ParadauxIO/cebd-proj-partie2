-- TODO 3.3 Créer un trigger pertinent
CREATE TRIGGER on_inscriptions_insert BEFORE INSERT ON LesInscriptions
BEGIN
    INSERT INTO log(message) VALUES ('Tentative d''ajout d''une nouvelle entree aux inscriptions : ' || new.numIn);
END;

CREATE TRIGGER on_inscriptions_delete_trigger AFTER DELETE ON LesInscriptions
BEGIN
    INSERT INTO log (message) VALUES ('Supprime ' || old.numIn);
END;

CREATE TRIGGER on_inscriptions_update AFTER UPDATE ON LesInscriptions
BEGIN
    INSERT INTO log(message) VALUES ('Mise a jour des inscriptions :' || old.numIn);
END;

CREATE TRIGGER on_resultats_insert BEFORE INSERT ON LesResultats
BEGIN
    INSERT INTO log(message) VALUES ('Essayer d''ajouter d''une nouvelle entree aux resultats : ' || new.numEp);
END;

CREATE TRIGGER on_resultats_delete_trigger AFTER DELETE ON LesResultats
BEGIN
    INSERT INTO log (message) VALUES ('Supprime ' || old.numEp);
END;

CREATE TRIGGER on_resultats_update AFTER UPDATE ON LesResultats
BEGIN
    INSERT INTO log(message) VALUES ('Mise a jour des resultats :' || old.numEp);
END;