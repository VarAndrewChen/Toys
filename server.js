const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname, './')))

app.listen(8091,() => {
    console.log('App listening at http://localhost:8091/')
})