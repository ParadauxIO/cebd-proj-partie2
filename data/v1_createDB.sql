CREATE TABLE LesSportifsEQ
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  numEq NUMBER(4),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_CK3 CHECK(numEq > 0)
);

CREATE TABLE LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  nomDi VARCHAR2(25),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

-- 1.3 : Créer les tables manquantes et modifier celles ci-dessous
CREATE TABLE LesInscriptions
(
    numIn NUMBER(4),
    numEp NUMBER(3)
);

CREATE TABLE LesResultats
(
  numEp NUMBER(3),
  gold NUMBER(4),
  silver NUMBER(4),
  bronze number(4)
);

-- 1.4a : ajouter la définition de la vue LesAgesSportifs
CREATE VIEW LesAgesSportifs(numSp, nomSp, prenomSp, pays, categorieSp, dateNaisSp, ageSp)
AS
    SELECT numSp, nomSp, prenomSp, pays, categorieSp, dateNaisSp, strftime('%Y', 'now') - dateNaisSp AS ageSp FROM LesSportifsEQ;

-- 1.5a : ajouter la définition de la vue LesNbsEquipiers
CREATE VIEW LesNbEquipiers(numEq, nbEquipiersEq)
AS
    SELECT numEq, COUNT(numEq)
    FROM LesSportifsEQ
    WHERE numEq IS NOT NULL
    GROUP BY numEq;

-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)
