Creating a Django app for tax calculation involves several steps. Below, I'll guide you through the process, including setting up the project, creating the models, views, serializers, and the API endpoints. Additionally, I'll cover setting up the admin interface and using Git for version control.

**Step 1: Set Up the Project**

Assuming you have Python and Django installed, open a terminal and run the following commands:

```bash
# Create a virtual environment (recommended)
python3 -m venv venv_tax_app
source venv_tax_app/bin/activate

# Install Django and other dependencies
pip install django djangorestframework psycopg2-binary
```

**Step 2: Create a New Django Project and App**

```bash
# Create a new Django project
django-admin startproject tax_project
cd tax_project

# Create a new Django app
python manage.py startapp tax_app
```

**Step 3: Define Models**

In the `models.py` file within the `tax_app` app, define the `TaxationScheme` model:

```python
# tax_app/models.py
from django.db import models

class TaxationScheme(models.Model):
    year = models.PositiveIntegerField(unique=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"TaxationScheme - {self.year}"
```

**Step 4: Set Up Admin Interface**

Register the `TaxationScheme` model with the Django admin interface:

```python
# tax_app/admin.py
from django.contrib import admin
from .models import TaxationScheme

admin.site.register(TaxationScheme)
```

**Step 5: Create Serializers**

Create a file named `serializers.py` in the `tax_app` directory:

```python
# tax_app/serializers.py
from rest_framework import serializers
from .models import TaxationScheme

class TaxationSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxationScheme
        fields = '__all__'
```

**Step 6: Create Views and API**

Create a file named `views.py` in the `tax_app` directory:

```python
# tax_app/views.py
from rest_framework import generics
from .models import TaxationScheme
from .serializers import TaxationSchemeSerializer

class FinancialYearList(generics.ListAPIView):
    queryset = TaxationScheme.objects.all()
    serializer_class = TaxationSchemeSerializer

class TaxCalculator(generics.CreateAPIView):
    serializer_class = TaxationSchemeSerializer

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        year = request.data.get('year')
        try:
            taxation_scheme = TaxationScheme.objects.get(year=year)
            tax = (taxation_scheme.tax_rate / 100) * amount
            return self.create(request, *args, **kwargs)
        except TaxationScheme.DoesNotExist:
            return Response({"error": "Taxation scheme not found for the specified year."}, status=status.HTTP_404_NOT_FOUND)
```

**Step 7: Create URLs**

Create a file named `urls.py` in the `tax_app` directory:

```python
# tax_app/urls.py
from django.urls import path
from .views import FinancialYearList, TaxCalculator

urlpatterns = [
    path('financial-years/', FinancialYearList.as_view(), name='financial-year-list'),
    path('tax-calculator/', TaxCalculator.as_view(), name='tax-calculator'),
]
```

**Step 8: Configure the Project URLs**

Edit the `urls.py` file in the `tax_project` directory:

```python
# tax_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tax_app.urls')),
]
```

**Step 9: Database Configuration**

Configure the PostgreSQL database settings in the project's `settings.py` file:

```python
# tax_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Step 10: Migrate and Create Superuser**

Run the following commands to apply the initial migrations and create a superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**Step 11: Run the Development Server**

```bash
python manage.py runserver
```

Now you can access the admin interface at http://127.0.0.1:8000/admin/ and the API endpoints at http://127.0.0.1:8000/api/.

**Step 12: Git Version Control**

Initialize a Git repository, create your initial commit, and push the code to a remote repository:

```bash
git init
git add .
git commit -m "Initial commit"
# Create a remote repository on GitHub or another platform
git remote add origin your_remote_repository_url
git push -u origin master
```

This is a basic outline to help you get started. You can further customize and enhance the application, add error handling, authentication, and more as needed.