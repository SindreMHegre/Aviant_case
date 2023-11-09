# Aviant_case

This repo contains everything related to Sindre Meyer Hegre's interview case for Aviant. It models the interface for a restaurant to be used to read and change orders, opening hours and statistics

## Installation

The only packed needed is in requirements, it's named flask

## Usage

python3 main.py

http://localhost:5000/

### Restaurants.py

This file has the classes and methods used for the backend

Classes:
- OrderStatus
- Order
- Restaurant

### Webpage.py

This file has the functions used in the frontend, togheter with the html templates in templates. The frontend is structured as follows:
- Home
    - Statistics
    - Orders
    - Opening Hours
