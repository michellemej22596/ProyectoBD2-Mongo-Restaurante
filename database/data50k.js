const faker = require('faker');
const { MongoClient } = require('mongodb');

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
    const usuariosCollection = db.collection('Usuarios');  

    let restauranteId = 1;  // Empezamos el ID de restaurante desde 1
    let usuarioId = 1;      // Empezamos el ID de usuario desde 1
    let ordenId = 1;        // Empezamos el ID de orden desde 1
    let reseñaId = 1;       // Empezamos el ID de reseña desde 1
    let menuId = 1;         // Empezamos el ID de menú desde 1

    for (let i = 1; i <= 50000; i++) {
      console.log(`Creando restaurante ${i}...`);
      // Crear un restaurante con un ID manual y el campo location
      const restaurante = {
        _id: restauranteId,  // Asignamos el ID manual
        nombre: faker.company.companyName(),
        direccion: faker.address.streetAddress(),
        telefono: faker.phone.phoneNumber(),
        categoria: faker.random.arrayElement(['Pizza', 'Sushi', 'Burgers', 'Pasta', 'Mexicana']),
        location: {  // Nuevo campo de ubicación
          latitud: parseFloat(faker.address.latitude()),  // Generar latitud
          longitud: parseFloat(faker.address.longitude()) // Generar longitud
        },
        menu: [],  // Se llenará con los platillos
        reseñas: []  // Se llenará con las reseñas
      };

      // Insertar restaurante en la colección
      await restaurantesCollection.insertOne(restaurante);
      console.log(`Restaurante insertado con ID: ${restauranteId}`);

      // Crear 9 platillos para este restaurante con precios limitados a 150
      const menu = [];
      for (let j = 0; j < 9; j++) {
        menu.push({
          _id: menuId++, 
          nombre: faker.commerce.productName(), 
          descripcion: faker.lorem.sentence(), 
          precio: parseFloat(faker.commerce.price(10, 150)), 
          restaurante_id: restauranteId
        });
      }

      // Insertar platillos en la colección de menú
      await menuCollection.insertMany(menu);
      console.log(`9 platillos insertados para restaurante ID: ${restauranteId}`);

      // Crear un usuario de ejemplo con un ID manual
      const usuario = {
        _id: usuarioId++, // Asignamos el ID manual
        nombre: faker.name.findName(),
        email: faker.internet.email(),
        telefono: faker.phone.phoneNumber(),
        direccion: faker.address.streetAddress()
      };

      // Insertar usuario en la colección de usuarios
      const usuarioInsertado = await usuariosCollection.insertOne(usuario);
      console.log(`Usuario insertado con ID: ${usuarioId - 1}`);  // Restamos 1 ya que incrementamos antes de insertar

      // Crear una orden de ejemplo con los platillos embebidos
      const orden = {
        _id: ordenId++,  // Asignamos el ID manual
        usuario_id: usuarioId - 1,  // Asociamos la orden al usuario creado
        items: [
          { 
            nombre: menu[0].nombre, 
            descripcion: menu[0].descripcion, 
            precio: menu[0].precio, 
            cantidad: 2 
          },
          { 
            nombre: menu[1].nombre, 
            descripcion: menu[1].descripcion, 
            precio: menu[1].precio, 
            cantidad: 1 
          }
        ],
        total: (menu[0].precio * 2) + (menu[1].precio * 1), // Calculamos el total con los precios de los platillos
        estado: "pendiente",
        fecha: new Date()
      };

      // Insertar la orden en la colección de órdenes
      await ordenesCollection.insertOne(orden);
      console.log(`Orden insertada con ID: ${ordenId - 1}`);

      // Crear una reseña de ejemplo con los platillos embebidos
      const reseña = {
        _id: reseñaId++,  // Asignamos el ID manual
        usuario_nombre: usuario.nombre,  // Asociamos el nombre del usuario en vez de el ID
        restaurante_nombre: restaurante.nombre,  // Asociamos el nombre del restaurante en vez del ID
        platillos: [  // Los platillos ahora están embebidos
          {
            nombre: menu[0].nombre,
            descripcion: menu[0].descripcion,
            precio: menu[0].precio
          },
          {
            nombre: menu[1].nombre,
            descripcion: menu[1].descripcion,
            precio: menu[1].precio
          }
        ],
        calificacion: faker.datatype.number({ min: 1, max: 5 }),
        comentario: faker.lorem.sentence()
      };

      // Insertar la reseña en la colección de reseñas
      await reseñasCollection.insertOne(reseña);
      console.log(`Reseña insertada con ID: ${reseñaId - 1}`);

      // Incrementar el ID de restaurante para el siguiente ciclo
      restauranteId++;
    }

    console.log('Base de datos llena con 50,000 documentos.');
  } catch (error) {
    console.error('Error al llenar la base de datos:', error);
  } finally {
    await client.close();  // Cerrar la conexión a MongoDB
  }
}

populateDatabase();
