// download.js
const express = require('express');
const fs = require('fs');
const connectToDB = require('./mongodbConnection');  // Importar la conexión a la base de datos

const app = express();
const port = 3000;

// Endpoint para descargar archivos
app.get('/download/:filename', async (req, res) => {
  try {
    const bucket = await connectToDB();  // Conectar a la base de datos
    
    // Obtener el stream de descarga por nombre de archivo
    const downloadStream = bucket.openDownloadStreamByName(req.params.filename);
    
    // Transferir el archivo al cliente
    downloadStream.pipe(res);
    
    downloadStream.on('end', () => {
      console.log('Archivo descargado');
    });
  } catch (error) {
    console.error('Error al descargar archivo:', error);
    res.status(500).send('Error al descargar archivo');
  }
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
