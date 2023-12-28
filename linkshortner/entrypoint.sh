#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create a default user
DEFAULT_ADMIN_USERNAME=${DEFAULT_ADMIN_USERNAME}
DEFAULT_ADMIN_PASSWORD=${DEFAULT_ADMIN_PASSWORD}

if [ -n "$DEFAULT_ADMIN_USERNAME" ] && [ -n "$DEFAULT_ADMIN_PASSWORD" ]; then
    echo "Creating a default user..."
    python manage.py shell -c "
from django.contrib.auth.models import User;
if not User.objects.filter(username='$DEFAULT_ADMIN_USERNAME').exists():
    User.objects.create_superuser(username='$DEFAULT_ADMIN_USERNAME', password='$DEFAULT_ADMIN_PASSWORD')
    "
    else
        echo "User credentials not provided. Skipping user creation."
fi


# Start the Django app
exec "$@"
