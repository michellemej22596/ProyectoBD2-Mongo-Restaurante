const { MongoClient } = require('mongodb');
const faker = require('faker');

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

      // Crear un array de operaciones de bulk para los restaurantes
      const bulkOps = [
        { insertOne: { document: restaurante } }
      ];

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

      // Crear las operaciones de inserción para los platillos
      menu.forEach(platillo => {
        bulkOps.push({ insertOne: { document: platillo } });
      });

      // Crear un usuario de ejemplo
      const usuario = {
        _id: usuarioId++, 
        nombre: faker.name.findName(),
        email: faker.internet.email(),
        telefono: faker.phone.phoneNumber(),
        direccion: faker.address.streetAddress()
      };

      // Agregar la operación de inserción del usuario al bulkOps
      bulkOps.push({ insertOne: { document: usuario } });

      // Crear una orden de ejemplo
      const orden = {
        _id: ordenId++,  
        usuario_id: usuarioId - 1,
        items: [
          { nombre: menu[0].nombre, descripcion: menu[0].descripcion, precio: menu[0].precio, cantidad: 2 },
          { nombre: menu[1].nombre, descripcion: menu[1].descripcion, precio: menu[1].precio, cantidad: 1 }
        ],
        total: (menu[0].precio * 2) + (menu[1].precio * 1),
        estado: "pendiente",
        fecha: new Date()
      };

      // Agregar la operación de inserción de la orden
      bulkOps.push({ insertOne: { document: orden } });

      // Crear una reseña de ejemplo
      const reseña = {
        _id: reseñaId++,  
        usuario_nombre: usuario.nombre,  
        restaurante_nombre: restaurante.nombre,  
        platillos: [
          { nombre: menu[0].nombre, descripcion: menu[0].descripcion, precio: menu[0].precio },
          { nombre: menu[1].nombre, descripcion: menu[1].descripcion, precio: menu[1].precio }
        ],
        calificacion: faker.datatype.number({ min: 1, max: 5 }),
        comentario: faker.lorem.sentence()
      };

      // Agregar la operación de inserción de la reseña
      bulkOps.push({ insertOne: { document: reseña } });

      // Ejecutar el bulkWrite para insertar todos los documentos de una sola vez
      await restaurantesCollection.bulkWrite(bulkOps);
      console.log(`Documentos insertados en lote para restaurante ID: ${restauranteId}`);

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
