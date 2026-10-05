SELECT * FROM Customers;
SELECT CustomerName, City FROM Customers;

SELECT * FROM Customers WHERE Country = 'Germany';

SELECT CustomerName, City FROM Customers WHERE Country = 'France' AND City = 'Paris';


SELECT CustomerName, City FROM Customers ORDER BY City;

SELECT CustomerName, Country FROM Customers ORDER BY Country DESC;


SELECT TOP 5 * FROM Customers;


SELECT CustomerName, City FROM Customers WHERE Country = 'UK' ORDER BY CustomerName;

SELECT TOP 3 CustomerName, City, Country FROM Customers WHERE Country = 'Spain' ORDER BY City DESC;

SELECT TOP 10 * FROM Customers WHERE Country <> 'USA' ORDER BY CustomerName;

SELECT COUNT(*) FROM Products;

SELECT AVG(Price) FROM Products;

SELECT SUM(Quantity) FROM OrderDetails WHERE PRODUCTID = 1;

SELECT CategoryID, COUNT(*) FROM Products GROUP BY CategoryID;

SELECT CategoryID, AVG(Price) AS AVGPrice FROM Products GROUP BY CategoryID ORDER BY AvgPrice DESC;
