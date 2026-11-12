CREATE DATABASE kuryerlar;
USE kuryerlar;

CREATE TABLE couriers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ism VARCHAR(100),
    telefon VARCHAR(20),
    hudud VARCHAR(100),
    buyurtmalar_soni INT
);

INSERT INTO couriers (ism, telefon, hudud, buyurtmalar_soni)
VALUES
('Ali', '901112233', 'Fargona', 15),
('Vali', '902223344', 'Toshkent', 8),
('Hasan', '903334455', 'Fargona', 20),
('Husan', '904445566', 'Andijon', 12),
('Olim', '905556677', 'Namangan', 5);

SELECT * FROM couriers WHERE buyurtmalar_soni > 10;

SELECT * FROM couriers WHERE hudud = 'Fargona';

SELECT * FROM couriers
ORDER BY buyurtmalar_soni DESC
LIMIT 1;