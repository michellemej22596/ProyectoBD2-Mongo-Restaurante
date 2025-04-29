// mongodbConnection.js
const { MongoClient, GridFSBucket } = require('mongodb');

// Conexión a la base de datos MongoDB
const uri = 'mongodb+srv://silvia:silvia@cluster0.a67fb.mongodb.net/Proyecto2?retryWrites=true&w=majority';
const dbName = 'Proyecto2';  // Nombre de tu base de datos

const client = new MongoClient(uri);


async function connectToDB() {
  try {
    await client.connect();  // Conectar a MongoDB
    console.log("Conectado a MongoDB");

    const db = client.db(dbName);  // Seleccionamos la base de datos
    const bucket = new GridFSBucket(db, { bucketName: 'fs' });  // Configuración de GridFS
    
    return bucket;
  } catch (error) {
    console.error('Error al conectar a MongoDB:', error);
  }
}

module.exports = connectToDB;
