SEED_DATA: dict[int, dict] = {
    # ==================== CLIENTES ====================
    1: {
        "uuid": "cli-001",
        "nombre": "Ana García",
        "email": "ana@email.com", 
        "rut": "11.111.111-1",
        "created_at": "2024-01-15 10:00:00",
        "modified_at": "2024-01-15 10:00:00"
    },
    2: {
        "uuid": "cli-002", 
        "nombre": "Carlos López",
        "email": "carlos@email.com",
        "rut": "22.222.222-2",
        "created_at": "2024-01-15 10:00:00",
        "modified_at": "2024-01-15 10:00:00"
    },
    3: {
        "uuid": "cli-003",
        "nombre": "María Torres",
        "email": "maria@email.com",
        "rut": "33.333.333-3",
        "created_at": "2024-01-15 10:00:00",
        "modified_at": "2024-01-15 10:00:00"
    },

    # ==================== PRODUCTOS ====================
    4: {
        "uuid": "prod-001",
        "nombre": "Laptop Gamer",
        "categoria": "Tecnología",
        "precio": 800000,
        "created_at": "2024-01-10 08:00:00",
        "modified_at": "2024-01-10 08:00:00"
    },
    5: {
        "uuid": "prod-002",
        "nombre": "Mouse Inalámbrico", 
        "categoria": "Tecnología",
        "precio": 25000,
        "created_at": "2024-01-10 08:00:00",
        "modified_at": "2024-01-10 08:00:00"
    },
    6: {
        "uuid": "prod-003",
        "nombre": "Teclado Mecánico",
        "categoria": "Tecnología", 
        "precio": 50000,
        "created_at": "2024-01-10 08:00:00",
        "modified_at": "2024-01-10 08:00:00"
    },
    7: {
        "uuid": "prod-004",
        "nombre": "Monitor 24''",
        "categoria": "Tecnología",
        "precio": 150000,
        "created_at": "2024-01-10 08:00:00",
        "modified_at": "2024-01-10 08:00:00"
    },

    # ==================== VENTAS ====================
    8: {
        "uuid": "venta-001",
        "fecha": "2024-01-20 14:30:00",
        "total": 825000,  # Laptop + Mouse
        "created_at": "2024-01-20 14:30:00",
        "modified_at": "2024-01-20 14:30:00", 
        "cliente_id": 1  # Ana García
    },
    9: {
        "uuid": "venta-002",
        "fecha": "2024-01-21 16:45:00",
        "total": 200000,  # Monitor + Teclado
        "created_at": "2024-01-21 16:45:00",
        "modified_at": "2024-01-21 16:45:00", 
        "cliente_id": 2  # Carlos López
    },

    # ==================== DETALLES VENTAS ====================
    10: {
        "uuid": "det-001",
        "producto_id": 4,  # Laptop Gamer
        "venta_id": 8,     # Venta de Ana
        "precio": 800000,
        "descuento": 0,
        "cantidad": 1,
        "created_at": "2024-01-20 14:30:00",
        "modified_at": "2024-01-20 14:30:00"
    },
    11: {
        "uuid": "det-002", 
        "producto_id": 5,  # Mouse
        "venta_id": 8,     # Venta de Ana
        "precio": 25000,
        "descuento": 0,
        "cantidad": 1,
        "created_at": "2024-01-20 14:30:00",
        "modified_at": "2024-01-20 14:30:00"
    },
    12: {
        "uuid": "det-003",
        "producto_id": 7,  # Monitor
        "venta_id": 9,     # Venta de Carlos
        "precio": 150000,
        "descuento": 0,
        "cantidad": 1,
        "created_at": "2024-01-21 16:45:00",
        "modified_at": "2024-01-21 16:45:00"
    },
    13: {
        "uuid": "det-004",
        "producto_id": 6,  # Teclado
        "venta_id": 9,     # Venta de Carlos  
        "precio": 50000,
        "descuento": 0,
        "cantidad": 1,
        "created_at": "2024-01-21 16:45:00",
        "modified_at": "2024-01-21 16:45:00"
    }
}