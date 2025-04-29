// upload.js
const express = require('express');
const multer = require('multer');
const connectToDB = require('./mongodbConnection');  // Importar la conexión a MongoDB

const app = express();
const port = 3000;

// Configuración de multer para manejar la subida de archivos en memoria
const storage = multer.memoryStorage();
const upload = multer({ storage });

// Endpoint para subir archivos
app.post('/upload', upload.single('file'), async (req, res) => {
  try {
    const bucket = await connectToDB();  // Conectarse a la base de datos
    
    // Crear un stream de subida de GridFS
    const uploadStream = bucket.openUploadStream(req.file.originalname);
    uploadStream.end(req.file.buffer);  // Subir el archivo desde el buffer de memoria
    
    uploadStream.on('finish', () => {
      res.send('Archivo subido con éxito');
    });
  } catch (error) {
    console.error('Error al subir archivo:', error);
    res.status(500).send('Error al subir archivo');
  }
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
