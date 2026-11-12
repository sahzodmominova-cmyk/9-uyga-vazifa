CREATE DATABASE onlayn_buyurtmalar;
USE onlayn_buyurtmalar;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mijoz VARCHAR(100),
    mahsulot VARCHAR(100),
    miqdor INT,
    narx DECIMAL(12,2),
    status VARCHAR(50)
);

INSERT INTO orders (mijoz, mahsulot, miqdor, narx, status)
VALUES
('Ali', 'Kompyuter', 2, 8000000, 'Yangi'),
('Vali', 'Telefon', 1, 5000000, 'Yetkazildi'),
('Hasan', 'Monitor', 3, 1500000, 'Bekor qilingan'),
('Husan', 'Klaviatura', 2, 200000, 'Yangi');

UPDATE orders
SET status = 'Yetkazildi'
WHERE id = 1;

DELETE FROM orders
WHERE status = 'Bekor qilingan';

SELECT *,
       (miqdor * narx) AS umumiy_narx
FROM orders;