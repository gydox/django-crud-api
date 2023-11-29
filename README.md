# Django REST Project: Location and Item Management API

This Django project provides a RESTful API for managing locations and items. It utilizes Django REST Framework to create API endpoints for performing CRUD operations on locations and items.

## Getting Started

To get this project running on your local machine, follow these steps:

### Prerequisites

- Python (3.x)
- Django
- Django REST Framework

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/django-rest-location-item.git
   cd django-rest-location-item
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

The server will start running at `http://127.0.0.1:8000/`.

## API Endpoints

### Locations

- **List/Create Locations:**

  Endpoint: `/api/locations/`

  - HTTP Method: GET (list all locations) / POST (create a new location)
  - Returns a list of locations or creates a new location.

- **Retrieve/Update/Delete Location:**

  Endpoint: `/api/locations/<location_id>/`

  - HTTP Method: GET (retrieve) / PUT (update) / DELETE (delete)
  - Retrieve, update, or delete a specific location by its ID.

### Items

- **List/Create Items:**

  Endpoint: `/api/items/`

  - HTTP Method: GET (list all items) / POST (create a new item)
  - Returns a list of items or creates a new item.

- **Retrieve/Update/Delete Item:**

  Endpoint: `/api/items/<item_id>/`

  - HTTP Method: GET (retrieve) / PUT (update) / DELETE (delete)
  - Retrieve, update, or delete a specific item by its ID.

## Views Overview

### `LocationList` (List/Create Locations)
- Endpoint: `/api/locations/`
- Provides a list of locations or creates a new location.

### `LocationDetail` (Retrieve/Update/Delete Location)
- Endpoint: `/api/locations/<location_id>/`
- Retrieves, updates, or deletes a specific location by its ID.

### `ItemList` (List/Create Items with Location Filtering)
- Endpoint: `/api/items/`
- Lists items or creates a new item. Allows filtering items by location.

### `ItemDetail` (Retrieve/Update/Delete Item)
- Endpoint: `/api/items/<item_id>/`
- Retrieves, updates, or deletes a specific item by its ID.

## Usage

Use any API client (e.g., Postman) or make HTTP requests to the above endpoints to interact with the API. You can perform CRUD operations on locations and items as described in the API documentation.

Feel free to explore and modify the project according to your needs.
