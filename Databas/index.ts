import express, { Request, Response } from 'express'
import router from './routes/todo'




const app = express()

app.use('/', router)
app.use(express.static(__dirname + "/public/"));


app.set('view engine', 'ejs');








app.listen(8080, () =>
{
    console.log("ready!")
} )