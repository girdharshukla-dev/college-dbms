CREATE TABLE Farmers (
    farmer_id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_name VARCHAR(100) NOT NULL,
    village VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE Crops (
    crop_id INT AUTO_INCREMENT PRIMARY KEY,
    crop_name VARCHAR(100) NOT NULL,
    season VARCHAR(50)
);

CREATE TABLE Markets (
    market_id INT AUTO_INCREMENT PRIMARY KEY,
    market_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_id INT NOT NULL,
    crop_id INT NOT NULL,
    market_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (farmer_id) REFERENCES Farmers(farmer_id),
    FOREIGN KEY (crop_id) REFERENCES Crops(crop_id),
    FOREIGN KEY (market_id) REFERENCES Markets(market_id)
);
