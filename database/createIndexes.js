const { MongoClient } = require('mongodb');
const faker = require('faker');

// URL de conexión a MongoDB
const uri = 'mongodb+srv://silvia:silvia@cluster0.a67fb.mongodb.net/Proyecto2?retryWrites=true&w=majority';
const dbName = 'Proyecto2';  // Nombre de base de datos

const client = new MongoClient(uri);

// Función para agregar el campo de ubicación y crear índices
async function addLocationFieldAndCreateIndexes() {
  try {
    await client.connect();
    console.log("Conectado a MongoDB");

    const db = client.db(dbName);

    // Actualizar todos los documentos para agregar el campo location (latitud, longitud)
    const restaurantesCollection = db.collection('Restaurantes');

    // Actualizar todos los documentos para agregar el campo location
    await restaurantesCollection.updateMany(
      {},
      {
        $set: {
          location: [  // Se crea el array con latitud y longitud
            parseFloat(faker.address.latitude()),  // Generar latitud como número
            parseFloat(faker.address.longitude())  // Generar longitud como número
          ]
        }
      }
    );
    console.log("Campo 'location' actualizado en todos los documentos de Restaurantes");

    // Crear el índice geoespacial 2dsphere en el campo location
    await restaurantesCollection.createIndex({ location: "2dsphere" });
    console.log("Índice geoespacial 2dsphere creado en 'location' de Restaurantes");

    // Crear otros índices para la colección Restaurantes
    await restaurantesCollection.createIndex({ nombre: 1 });  // Índice para buscar por nombre
    console.log("Índice creado en 'nombre' de Restaurantes");

    await restaurantesCollection.createIndex({ categoria: 1 });  // Índice para buscar por categoria
    console.log("Índice creado en 'categoria' de Restaurantes");

    await restaurantesCollection.createIndex({ direccion: "text" });  // Índice de texto para dirección
    console.log("Índice de texto creado en 'direccion' de Restaurantes");

    // Crear índices para la colección Menu
    const menuCollection = db.collection('Menu');
    await menuCollection.createIndex({ restaurante_id: 1 });  // Índice para buscar por restaurante_id
    console.log("Índice creado en 'restaurante_id' de Menu");

    await menuCollection.createIndex({ precio: -1 });  // Índice para buscar por precio
    console.log("Índice creado en 'precio' de Menu");

    await menuCollection.createIndex({ "platillos.restaurante_id": 1 });  // Índice multikey
    console.log("Índice multikey creado en 'platillos.restaurante_id' de Menu");

    // Crear índices para la colección Ordenes
    const ordenesCollection = db.collection('Ordenes');
    await ordenesCollection.createIndex({ usuario_id: 1, fecha: -1 });  // Índice compuesto por usuario_id y fecha
    console.log("Índice compuesto creado en 'usuario_id' y 'fecha' de Ordenes");

    await ordenesCollection.createIndex({ estado: 1 });  // Índice para buscar por estado
    console.log("Índice creado en 'estado' de Ordenes");

    // Crear índices para la colección Reseñas
    const reseñasCollection = db.collection('Reseñas');
    await reseñasCollection.createIndex({ usuario_id: 1, restaurante_id: 1 });  // Índice para usuario_id y restaurante_id
    console.log("Índice creado en 'usuario_id' y 'restaurante_id' de Reseñas");

    await reseñasCollection.createIndex({ calificacion: -1 });  // Índice para calificación
    console.log("Índice creado en 'calificacion' de Reseñas");

    await reseñasCollection.createIndex({ comentario: "text" });  // Índice de texto para comentario
    console.log("Índice de texto creado en 'comentario' de Reseñas");

    // Crear índices para la colección Usuarios
    const usuariosCollection = db.collection('Usuarios');
    await usuariosCollection.createIndex({ email: 1 });  // Índice para buscar por email
    console.log("Índice creado en 'email' de Usuarios");

    await usuariosCollection.createIndex({ nombre: 1 });  // Índice para buscar por nombre
    console.log("Índice creado en 'nombre' de Usuarios");

  } catch (error) {
    console.error("Error al agregar 'location' y crear índices:", error);
  } finally {
    await client.close();  // Cerrar la conexión
  }
}

// Llamar a la función para agregar el campo 'location' y crear los índices
addLocationFieldAndCreateIndexes();
