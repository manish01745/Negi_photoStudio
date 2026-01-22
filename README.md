# Negi Photo Studio

A Django-based photography studio website for showcasing portfolios, services, and managing client inquiries.

## Features

- **Portfolio Management**: Display wedding, haldi, and birthday photography projects
- **Contact Form**: Clients can submit inquiries with automatic email notifications
- **Admin Panel**: Manage projects, images, and client submissions
- **Responsive Design**: Mobile-friendly interface
- **Email Integration**: Automated email notifications for both admin and clients

## Project Structure

```
photostudio/
├── photostudio/          # Main project settings
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── studio/              # Main app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # App URL patterns
│   └── admin.py         # Admin configuration
├── template/            # HTML templates
├── static/              # CSS, JS, images
├── media/               # User uploaded files
└── manage.py            # Django management script
```

## Models

### ContactForm
- Stores client inquiry submissions
- Fields: name, phone, email, date, location, budget, referrer, subject, message

### Project
- Photography project details
- Fields: title, description, date, location, category, slug
- Categories: Wedding, Haldi, Birthday

### ProjectImage
- Images associated with projects
- Foreign key relationship with Project

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/manish01745/Negi_photoStudio.git
cd Negi_photoStudio
```

2. **Create virtual environment**
```bash
python -m venv env_site
env_site\Scripts\activate  # On Windows
# source env_site/bin/activate  # On Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
Create a `.env` file in the project root and add:
```
SECRET_KEY=your-secret-key-here
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEBUG=True
```

5. **Run migrations**
```bash
cd photostudio
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the site.

## Email Configuration

The project uses Gmail SMTP for sending emails. To configure:

1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password
3. Update `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in settings.py or .env file

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`

You can manage:
- Contact form submissions
- Projects and their images
- User accounts

## URL Patterns

- `/` - Home page
- `/about` - About page
- `/services` - Services page
- `/portfolio` - Portfolio gallery
- `/portfolio/<slug>` - Individual project details
- `/contact` - Contact form
- `/pricing` - Pricing information
- `/testimonial` - Client testimonials

## Technologies Used

- **Backend**: Django 3.0.5
- **Database**: SQLite (development)
- **Email**: Gmail SMTP
- **Frontend**: HTML, CSS, JavaScript

## Security Notes

⚠️ **Important for Production:**
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Change the SECRET_KEY
- Use a production database (PostgreSQL/MySQL)
- Configure ALLOWED_HOSTS properly
- Use HTTPS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is private and proprietary.

## Contact

For any queries, contact: manish@isuremedia.com
