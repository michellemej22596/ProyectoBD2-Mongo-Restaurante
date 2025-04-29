const faker = require('faker');
const { MongoClient, ObjectId } = require('mongodb');

// Configurar el idioma de Faker a español
faker.locale = "es";  // Establecer el idioma a español

// Conexión a la base de datos MongoDB
const uri = 'mongodb+srv://silvia:silvia@cluster0.a67fb.mongodb.net/Proyecto2?retryWrites=true&w=majority';
const dbName = 'Proyecto2';  // Nombre de base de datos

const client = new MongoClient(uri);

async function populateDatabase() {
  try {
    await client.connect();  // Conectar a MongoDB
    console.log("Conectado a MongoDB");

    const db = client.db(dbName);  // Obtener la base de datos
    const restaurantesCollection = db.collection('Restaurantes');
    const menuCollection = db.collection('Menu');
    const ordenesCollection = db.collection('Ordenes');
    const reseñasCollection = db.collection('Reseñas');
    const usuariosCollection = db.collection('Usuarios');  // Nueva colección de usuarios

    for (let i = 1; i <= 50000; i++) {
      console.log(`Creando restaurante ${i}...`);
      // Crear un restaurante
      const restaurante = {
        nombre: faker.company.companyName(),
        direccion: faker.address.streetAddress(),
        telefono: faker.phone.phoneNumber(),
        categoria: faker.random.arrayElement(['Pizza', 'Sushi', 'Burgers', 'Pasta', 'Mexicana']),
        menu: [],  // Se llenará con los platillos
        reseñas: []  // Se llenará con las reseñas
      };

      // Insertar restaurante en la colección
      const restauranteInsertado = await restaurantesCollection.insertOne(restaurante);
      const restauranteId = restauranteInsertado.insertedId;
      console.log(`Restaurante insertado con ID: ${restauranteId}`);

      // Crear platillos para este restaurante
      const menu = [
        { nombre: "Platillo 1", descripcion: faker.lorem.sentence(), precio: faker.commerce.price(), restaurante_id: restauranteId },
        { nombre: "Platillo 2", descripcion: faker.lorem.sentence(), precio: faker.commerce.price(), restaurante_id: restauranteId },
        { nombre: "Platillo 3", descripcion: faker.lorem.sentence(), precio: faker.commerce.price(), restaurante_id: restauranteId }
      ];

      // Insertar platillos en la colección de menú
      await menuCollection.insertMany(menu);
      console.log(`3 platillos insertados para restaurante ID: ${restauranteId}`);

      // Crear un usuario de ejemplo
      const usuario = {
        nombre: faker.name.findName(),
        email: faker.internet.email(),
        telefono: faker.phone.phoneNumber(),
        direccion: faker.address.streetAddress()
      };

      // Insertar usuario en la colección de usuarios
      const usuarioInsertado = await usuariosCollection.insertOne(usuario);
      const usuarioId = usuarioInsertado.insertedId;
      console.log(`Usuario insertado con ID: ${usuarioId}`);

      // Crear una orden de ejemplo
      const orden = {
        usuario_id: usuarioId,  // Asociamos la orden al usuario creado
        items: [
          { platillo_id: menu[0]._id, cantidad: 2, precio: menu[0].precio },
          { platillo_id: menu[1]._id, cantidad: 1, precio: menu[1].precio }
        ],
        total: menu[0].precio * 2 + menu[1].precio,
        estado: "pendiente",
        fecha: new Date()
      };

      // Insertar la orden en la colección de órdenes
      await ordenesCollection.insertOne(orden);
      console.log(`Orden insertada para restaurante ID: ${restauranteId}`);

      // Crear una reseña de ejemplo
      const reseña = {
        usuario_id: usuarioId,  // Asociamos la reseña al usuario creado
        restaurante_id: restauranteId,
        platillo_id: menu[0]._id,  // Puedes asociar las reseñas a los platillos también
        calificacion: faker.datatype.number({ min: 1, max: 5 }),
        comentario: faker.lorem.sentence()
      };

      // Insertar la reseña en la colección de reseñas
      await reseñasCollection.insertOne(reseña);
      console.log(`Reseña insertada para restaurante ID: ${restauranteId}`);
    }

    console.log('Base de datos llena con 50,000 documentos.');
  } catch (error) {
    console.error('Error al llenar la base de datos:', error);
  } finally {
    await client.close();  // Cerrar la conexión a MongoDB
  }
}

populateDatabase();
