CREATE DATABASE ombor;
USE ombor;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    narx DECIMAL(12,2),
    miqdor INT,
    kategoriya VARCHAR(100)
);

INSERT INTO products (nom, narx, miqdor, kategoriya)
VALUES
('Kompyuter', 8000000, 5, 'Texnika'),
('Telefon', 5000000, 10, 'Texnika'),
('Daftar', 5000, 100, 'Kanselyariya'),
('Ruchka', 3000, 50, 'Kanselyariya'),
('Monitor', 1500000, 8, 'Texnika'),
('Sumka', 150000, 12, 'Aksessuar');

SELECT kategoriya, COUNT(*) AS mahsulotlar_soni
FROM products
GROUP BY kategoriya;

SELECT kategoriya, SUM(narx * miqdor) AS umumiy_qiymat
FROM products
GROUP BY kategoriya;

SELECT * FROM products
WHERE narx > 100000;