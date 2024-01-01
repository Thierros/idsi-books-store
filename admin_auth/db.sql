CREATE TABLE Auteur (
    author_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    pays VARCHAR(255)
);

CREATE TABLE Domaine (
    domaine_id INT PRIMARY KEY,
    domaine_name VARCHAR(255)
);

CREATE TABLE Livre (
    livre_id INT PRIMARY KEY,
    title VARCHAR(255),
    isbn VARCHAR(20),
    publication_date DATE,
    language VARCHAR(50),
    nb_page INT,
    prix_unitaire DECIMAL(10, 2),
    Qte_stock INT,
    domaine_id INT,
    FOREIGN KEY (domaine_id) REFERENCES Domaine(domaine_id)
);

CREATE TABLE Exemplaire (
    exemplaire_id INT PRIMARY KEY,
    exemplaire_number VARCHAR(50),
    edition_number INT,
    etat VARCHAR(50),
    disponible BOOLEAN,
    livre_id INT,
    editeur_id INT,
    FOREIGN KEY (livre_id) REFERENCES Livre(livre_id),
    FOREIGN KEY (editeur_id) REFERENCES Editeur(editeur_id)
);

CREATE TABLE Editeur (
    editeur_id INT PRIMARY KEY,
    editeur_name VARCHAR(255),
    pays VARCHAR(255)
);

CREATE TABLE Classe (
    classe_id INT PRIMARY KEY,
    classe_name VARCHAR(255),
    classe_niveau VARCHAR(50),
    effectif INT
);

CREATE TABLE ECUE (
    ecue_id INT PRIMARY KEY,
    ecue_name VARCHAR(255),
    classe_id INT,
    FOREIGN KEY (classe_id) REFERENCES Classe(classe_id)
);

CREATE TABLE Livre_ECUE (
    livre_id INT,
    ecue_id INT,
    PRIMARY KEY (livre_id, ecue_id),
    FOREIGN KEY (livre_id) REFERENCES Livre(livre_id),
    FOREIGN KEY (ecue_id) REFERENCES ECUE(ecue_id)
);

CREATE TABLE Emprunt (
    emprunt_id INT PRIMARY KEY,
    date_emprunt DATE,
    delais INT,
    date_remise DATE,
    etat_remise VARCHAR(50),
    exemplaire_id INT,
    user_id INT,
    FOREIGN KEY (exemplaire_id) REFERENCES Exemplaire(exemplaire_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE User (
    user_id INT PRIMARY KEY,
    username VARCHAR(150),
    password VARCHAR(128),
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    email VARCHAR(255),
    is_student BOOLEAN
);

CREATE TABLE Etudiant (
    matricule VARCHAR(50) PRIMARY KEY,
    user_id INT,
    classe_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (classe_id) REFERENCES Classe(classe_id)
);
