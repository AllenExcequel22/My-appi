Instalación
pip install fastapi uvicorn sqlalchemy

Ejecutar
uvicorn main:app --reload

Qué hace esta API
CRUD Completo para Clientes, Productos, Ventas y Detalles de Ventas

Base de datos SQLite automática

Endpoints adicionales:

-Productos más vendidos

-Clientes con más compras

Documentación interactiva en: http://127.0.0.1:8000/docs

Base de datos
Archivo: evaluacion.db (se crea automáticamente al ejecutar)

Contiene datos de prueba insertados automáticamente

Tablas:

-clientes - Información de clientes

-productos - Catálogo de productos

-ventas - Registro de ventas

-detalles_ventas - Items de cada venta

Funcionalidades CRUD
- Crear, Leer, Actualizar, Eliminar en todas las entidades

- Relaciones completas entre tablas

- Validaciones de datos

- Consultas específicas y filtros
