# Stazia

SaaS de gestión para hostales, pensiones y pisos turísticos.

## Stack
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Tailwind CSS

## Features (WIP)
- Multi-tenancy con Row Level Security
- Gestión de reservas
- Panel de administración

## Modelos
- Tenant (id, name, slug)
- User (id, email, tenant_id, phone)
- Property (id, tenant_id)
- Reservation (id, tenant_id, property_id, customer_name, customer_email)