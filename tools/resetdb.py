#!/usr/bin/env python
"""
Script to reset database and delete migration files.
This script:
1. Connects to the database defined in settings.py (auto-detected)
2. Drops all tables in the database
3. Deletes all migration files (except __init__.py) in all */migrations/ folders

Can be run from any directory within a Django project.
"""

import os
import sys
import django
from pathlib import Path


def find_django_project_root():
    """Find the Django project root by looking for manage.py."""
    # Start from current working directory
    current = Path.cwd().resolve()
    
    # Walk up the directory tree looking for manage.py
    for path in [current] + list(current.parents):
        manage_py = path / 'manage.py'
        if manage_py.exists():
            return path
    
    raise FileNotFoundError(
        "Could not find manage.py. Please run this script from within a Django project directory."
    )


def find_settings_module(project_root):
    """Find the settings.py file and determine the module path."""
    # Common patterns for settings.py location
    settings_patterns = [
        'config/settings.py',
        'settings.py',
        'project/settings.py',
        'mysite/settings.py',
    ]
    
    # Also check for any directory containing settings.py
    for settings_file in project_root.rglob('settings.py'):
        # Skip if it's in a virtual environment or other common ignore locations
        rel_path = settings_file.relative_to(project_root)
        if any(part in str(rel_path) for part in ['.venv', 'venv', '.env', '__pycache__', '.git']):
            continue
        
        # Convert to module path (e.g., config/settings.py -> config.settings)
        module_path = str(rel_path.with_suffix('')).replace('/', '.').replace('\\', '.')
        return module_path
    
    # Try common patterns
    for pattern in settings_patterns:
        settings_file = project_root / pattern
        if settings_file.exists():
            module_path = str(Path(pattern).with_suffix('')).replace('/', '.').replace('\\', '.')
            return module_path
    
    raise FileNotFoundError(
        f"Could not find settings.py in {project_root}. "
        "Common locations: config/settings.py, settings.py, project/settings.py"
    )


def setup_django():
    """Setup Django environment by finding project root and settings."""
    # Find Django project root
    project_root = find_django_project_root()
    print(f"Found Django project at: {project_root}")
    
    # Add project root to Python path
    sys.path.insert(0, str(project_root))
    
    # Find settings module
    settings_module = find_settings_module(project_root)
    print(f"Using settings module: {settings_module}")
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    
    # Setup Django
    django.setup()
    
    return project_root


# Setup Django environment
PROJECT_ROOT = setup_django()
from django.conf import settings
from django.db import connection


def drop_all_tables():
    """Drop all tables in the database."""
    print("Dropping all tables...")
    
    with connection.cursor() as cursor:
        # Get all table names
        if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
            # Disable foreign key constraints for SQLite
            cursor.execute("PRAGMA foreign_keys = OFF;")
            
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = [row[0] for row in cursor.fetchall()]
            
            # Drop each table
            for table in tables:
                print(f"  Dropping table: {table}")
                cursor.execute(f"DROP TABLE IF EXISTS {table};")
            
            # Re-enable foreign key constraints
            cursor.execute("PRAGMA foreign_keys = ON;")
        else:
            # For MySQL, disable foreign key checks
            if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
                cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            
            # For PostgreSQL, we need to drop tables in the right order or use CASCADE
            # Use Django's connection introspection
            table_names = connection.introspection.table_names()
            for table_name in table_names:
                print(f"  Dropping table: {table_name}")
                if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql':
                    cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
                else:
                    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            
            # Re-enable foreign key checks for MySQL
            if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
                cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    
    print("All tables dropped successfully.")


def delete_migration_files(project_root):
    """Delete all migration files except __init__.py in all migrations folders."""
    print("\nDeleting migration files...")
    
    # Find all migrations folders in the project root
    migrations_folders = list(project_root.rglob('migrations'))
    
    if not migrations_folders:
        print("  No migrations folders found.")
        return
    
    deleted_count = 0
    for migrations_folder in migrations_folders:
        if not migrations_folder.is_dir():
            continue
        
        print(f"  Processing: {migrations_folder}")
        
        # Delete all .py files except __init__.py
        for file_path in migrations_folder.glob('*.py'):
            if file_path.name != '__init__.py':
                print(f"    Deleting: {file_path}")
                file_path.unlink()
                deleted_count += 1
        
        # Also delete .pyc files in __pycache__ if they exist
        pycache_folder = migrations_folder / '__pycache__'
        if pycache_folder.exists():
            for file_path in pycache_folder.glob('*.pyc'):
                print(f"    Deleting: {file_path}")
                file_path.unlink()
                deleted_count += 1
    
    print(f"\nDeleted {deleted_count} migration files.")


def main():
    """Main function to reset database and migrations."""
    print("=" * 60)
    print("Database and Migration Reset Script")
    print("=" * 60)
    
    # Confirm before proceeding
    response = input("\nThis will DELETE ALL TABLES and ALL MIGRATION FILES!\nAre you sure you want to continue? (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted.")
        return
    
    try:
        # Drop all tables
        drop_all_tables()
        
        # Delete migration files
        delete_migration_files(PROJECT_ROOT)
        
        print("\n" + "=" * 60)
        print("Reset completed successfully!")
        print("=" * 60)
        print("\nNext steps:")
        print("  1. Run: python manage.py makemigrations")
        print("  2. Run: python manage.py migrate")
        print("  3. Run: python manage.py createsuperuser (if needed)")
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

