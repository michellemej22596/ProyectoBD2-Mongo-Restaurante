const { MongoClient } = require('mongodb');

// URL de conexión a MongoDB
const uri = 'mongodb+srv://silvia:silvia@cluster0.a67fb.mongodb.net/Proyecto2?retryWrites=true&w=majority';
const dbName = 'Proyecto2';  // Nombre de base de datos

// Función para crear los índices
async function createIndexes() {
  const client = new MongoClient(uri);

  try {
    await client.connect();
    console.log("Conectado a MongoDB");

    const db = client.db(dbName);

    // Crear índices para la colección Restaurantes
    const restaurantesCollection = db.collection('Restaurantes');
    await restaurantesCollection.createIndex({ nombre: 1 });  // Índice para buscar por nombre
    console.log("Índice creado en 'nombre' de Restaurantes");
    
    // Índice para buscar por categoria
    await restaurantesCollection.createIndex({ categoria: 1 });
    console.log("Índice creado en 'categoria' de Restaurantes");

    // Índice para dirección 
    await restaurantesCollection.createIndex({ direccion: "text" });  // Índice de texto para dirección
    console.log("Índice de texto creado en 'direccion' de Restaurantes");

    // Crear índices para la colección Menu
    const menuCollection = db.collection('Menu');
    await menuCollection.createIndex({ restaurante_id: 1 });  // Índice para buscar por restaurante_id
    console.log("Índice creado en 'restaurante_id' de Menu");

    // Índice para buscar por precio
    await menuCollection.createIndex({ precio: -1 });
    console.log("Índice creado en 'precio' de Menu");

    // Índice multikey en "platillos.restaurante_id" (campo 'menu' es un array)
    await menuCollection.createIndex({ "platillos.restaurante_id": 1 });
    console.log("Índice multikey creado en 'platillos.restaurante_id' de Menu");

    // Crear índices para la colección Ordenes
    const ordenesCollection = db.collection('Ordenes');
    await ordenesCollection.createIndex({ usuario_id: 1, fecha: -1 });  // Índice compuesto por usuario_id y fecha
    console.log("Índice compuesto creado en 'usuario_id' y 'fecha' de Ordenes");

    // Índice para buscar por estado
    await ordenesCollection.createIndex({ estado: 1 });
    console.log("Índice creado en 'estado' de Ordenes");

    // Crear índices para la colección Reseñas
    const reseñasCollection = db.collection('Reseñas');
    await reseñasCollection.createIndex({ usuario_id: 1, restaurante_id: 1 });  // Índice para buscar por usuario_id y restaurante_id
    console.log("Índice creado en 'usuario_id' y 'restaurante_id' de Reseñas");

    // Índice para buscar por calificación
    await reseñasCollection.createIndex({ calificacion: -1 });
    console.log("Índice creado en 'calificacion' de Reseñas");

    // Índice de texto en 'comentario' de Reseñas para búsqueda de texto completo
    await reseñasCollection.createIndex({ comentario: "text" });
    console.log("Índice de texto creado en 'comentario' de Reseñas");

    // Crear índices para la colección Usuarios
    const usuariosCollection = db.collection('Usuarios');
    await usuariosCollection.createIndex({ email: 1 });  // Índice para buscar por email
    console.log("Índice creado en 'email' de Usuarios");

    // Índice para buscar por nombre
    await usuariosCollection.createIndex({ nombre: 1 });
    console.log("Índice creado en 'nombre' de Usuarios");

  } catch (error) {
    console.error("Error al crear índices:", error);
  } finally {
    await client.close();  // Cerrar la conexión
  }
}

// Llamar a la función para crear los índices
createIndexes();
