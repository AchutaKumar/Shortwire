# URL Shortener

A production-oriented Django URL shortener service with a REST API for creating short links, redirecting them, and collecting click statistics.

## Features

- Create short links from long URLs
- Redirect short codes to their original destinations
- Track click activity and basic analytics
- Expose API endpoints for shorten, redirect, and stats operations
- Include a simple landing page for the web UI

## Tech Stack

- Python 3.11+
- Django
- Django REST Framework
- MySQL
- python-decouple

## Project Structure

- config/ — Django project settings and URL configuration
- shortener/ — URL shortening app with models, services, views, serializers, and templates

## Local Development

1. Create and activate a virtual environment

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies

   ```bash
   pip install django djangorestframework python-decouple mysqlclient
   ```

3. Create a local environment file

   Create a `.env` file in the project root with values such as:

   ```env
   SECRET_KEY=change-me
   DB_NAME=url_shortener
   DB_USER=root
   DB_PASSWORD=your-password
   DB_HOST=localhost
   DB_PORT=3306
   BASE_URL=http://localhost:8000
   ```

4. Run database migrations

   ```bash
   python manage.py migrate
   ```

5. Start the development server

   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser at http://localhost:8000/

## API Endpoints

- POST /api/shorten — create a short URL
- GET /api/stats/<short_code> — fetch click statistics
- GET /<short_code> — redirect to the original URL

## Testing

Run the test suite with:

```bash
python manage.py test shortener.tests
```

## Production-Ready Plan

The project is structured for production readiness with the following checklist:

### 1. Environment-based configuration
- Store secrets and database settings in environment variables.
- Never commit real credentials to source control.

### 2. Secure deployment settings
- Set `DEBUG=False` in production.
- Restrict `ALLOWED_HOSTS` to your real domain names.
- Use a strong `SECRET_KEY` and HTTPS everywhere.

### 3. Database and persistence
- Use a managed MySQL or PostgreSQL service in production.
- Keep database backups and monitor storage growth.

### 4. Reliability and operations
- Run the app behind a production WSGI server such as Gunicorn.
- Place the app behind a reverse proxy such as Nginx.
- Configure logging, monitoring, and alerting.

### 5. Security hardening
- Add rate limiting for the shorten endpoint.
- Validate and sanitize user input thoroughly.
- Consider CAPTCHA or abuse protection for public-facing endpoints.

### 6. Scalability
- Add caching for redirect lookups and stats queries.
- Introduce background tasks for analytics processing if traffic grows.
- Use a CDN or edge caching for static assets.

## Next Steps

- Add authentication for admin-only actions.
- Add rate limiting and abuse protection.
- Add Docker support for easier deployment.
- Add CI/CD pipelines for automated testing and deployment.
Commit at 2026-06-24T12:47:46.116654
Commit at 2026-08-22T08:22:21.507779
Commit at 2026-03-04T01:05:27.746545
Commit at 2026-02-10T16:36:13.923065
Commit at 2026-06-25T16:14:55.161495
Commit at 2026-01-19T03:54:27.348265
Commit at 2025-11-02T13:54:06.521506
Commit at 2026-10-08T19:40:21.724976
Commit at 2026-07-10T18:28:49.902974
Commit at 2026-01-27T01:08:23.146098
Commit at 2026-01-04T16:53:05.282929
Commit at 2025-12-06T00:21:37.480218
Commit at 2026-05-26T08:06:40.766737
Commit at 2025-11-02T18:14:19.026274
Commit at 2026-04-11T06:01:17.295176
Commit at 2026-09-17T16:07:34.447146
Commit at 2025-12-26T19:14:10.634711
Commit at 2026-03-11T08:03:08.829295
Commit at 2026-08-09T01:49:18.057398
Commit at 2026-08-02T20:57:11.225562
Commit at 2026-07-13T01:13:09.414438
Commit at 2025-12-22T16:06:54.611737
Commit at 2026-10-13T12:01:28.764338
Commit at 2026-04-17T09:04:28.039235
Commit at 2025-11-14T18:57:25.238846
Commit at 2026-01-29T09:09:53.394252
Commit at 2025-12-16T23:43:26.580821
Commit at 2026-04-15T22:08:38.750462
Commit at 2026-08-07T07:19:07.924885
Commit at 2026-01-12T20:40:59.118740
Commit at 2026-06-19T02:24:57.295928
Commit at 2026-09-12T10:08:28.521015
Commit at 2026-02-11T18:05:08.757105
Commit at 2026-01-13T00:36:10.974277
Commit at 2026-06-08T19:49:14.251863
Commit at 2026-06-03T02:25:02.446929
Commit at 2026-01-18T17:52:43.680592
Commit at 2026-01-25T10:59:13.858482
Commit at 2026-10-02T19:13:25.131156
Commit at 2026-06-10T15:14:25.352978
Commit at 2025-10-19T02:21:53.526200
Commit at 2026-06-27T12:54:36.706647
Commit at 2026-10-01T10:29:15.964287
Commit at 2026-06-11T22:13:06.202663
Commit at 2025-12-10T18:22:59.468671
Commit at 2026-07-18T02:31:21.791555
Commit at 2026-01-10T02:26:31.128668
Commit at 2026-08-23T14:18:41.378179
Commit at 2026-07-21T02:16:41.615315
Commit at 2026-02-19T14:18:06.942412
Commit at 2026-01-22T11:25:11.698908
Commit at 2026-03-03T02:54:03.029357
Commit at 2025-12-11T21:26:33.234050
Commit at 2026-03-25T06:49:37.430040
Commit at 2026-07-10T13:09:43.597406
Commit at 2026-09-01T13:25:08.835482
Commit at 2026-03-31T04:17:07.060000
Commit at 2026-08-08T23:26:44.329652
Commit at 2026-04-23T06:39:19.495515
Commit at 2026-03-28T17:55:48.656861
Commit at 2026-03-08T13:49:49.866815
