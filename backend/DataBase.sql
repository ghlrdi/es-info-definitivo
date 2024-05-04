CREATE TABLE users (
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(100) NOT NULL,
    email VARCHAR(100) PRIMARY KEY NOT NULL
);
CREATE TABLE orders (
    order_id INT UNIQUE  PRIMARY KEY,
    email VARCHAR(100) REFERENCES users(email),
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'active'

);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


CREATE TABLE cart_items (
    cart_item_id SERIAL PRIMARY KEY,
    user_email VARCHAR(100) REFERENCES users(email),
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);



CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255)
);

SELECT * FROM orders;
SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM order_items;
SELECT * FROM cart_items;

