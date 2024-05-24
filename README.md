
# MyShop

MyShop is a simple e-commerce web application built with Django, designed to showcase various skills and best practices in Django development. It provides basic functionalities for an online store, including product listings, user authentication, and an admin dashboard.

## Features

- User authentication and authorization
- Product catalog management
- Shopping cart functionality
- Order processing
- Responsive design
- Role-based functionalities

## Skills Demonstrated

- Django project structure and app organization
- User authentication with Django's built-in auth system
- CRUD operations with Django models and views
- Templating with Django templates
- Static and media file handling
- Custom admin panel enhancements
- Responsive web design with HTML, CSS, and JavaScript
- Handling file uploads
- Database migrations and management
- Django class-based views and function-based views
- Custom user model subclassing `AbstractUser`
- Using generic and functional views
- Overriding `form_valid` and `save()` methods to add extra tasks (e.g., assigning roles upon user signup)
- Implementing role-based functionalities

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Zaone999/MyShop.git
   cd MyShop
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scriptsctivate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Visit the homepage at `http://127.0.0.1:8000` to view the store and shop for products.
2. A pre-configured owner user is available in the database with the following credentials:
   - **Username:** admin
   - **Password:** admin

## Live Demo

Check out the live demo of the website at [MyShop on PythonAnywhere](https://zaone.pythonanywhere.com/).

## Project Structure

- `dashboard/` - Contains the admin dashboard views and templates.
- `media/` - Stores uploaded media files.
- `shoestore/` - The main Django project directory.
- `shop/` - Contains the core e-commerce app with models, views, and templates.
- `static/` - Contains static files (CSS, JavaScript, images).
- `templates/` - Global templates for the project.
- `users/` - Handles user authentication and profiles.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
