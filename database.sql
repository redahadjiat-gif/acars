CREATE TABLE vehicles_vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marque VARCHAR(100),
    modele VARCHAR(100),
    annee INTEGER,
    prix DECIMAL(10,2),
    kilometrage INTEGER,
    carburant VARCHAR(50),
    transmission VARCHAR(50),
    description TEXT,
    image VARCHAR(255),
    disponible BOOLEAN DEFAULT 1
);