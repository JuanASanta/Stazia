# Stazia

API gestor de reservas multi-tenant con Django Rest Framework

## Stack
- Django
- Django REST Framework
- PostgreSQL
- Docker

## Features (WIP)
- Atenticación con JWT
- Aislación por Tenant
- Gestión de reservas
- Documentación API

## Modelos
- Tenant (id, name, slug)
- User (id, email, tenant_id, phone)
- Property (id, tenant_id)
- Reservation (id, property_id, customer_name, customer_email, state(pending, confirmed, cancelled, checked_id, checked_out))
  
## Comando para correrlo
- docker compose up --build