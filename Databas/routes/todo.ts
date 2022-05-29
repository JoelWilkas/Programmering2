import express, { Request, response, Response } from 'express'
import TodoTabs from '../constructor/todo'

import con from '../constructor/dbconnection'

let router = express.Router();

router.use(express.static('public'))
router.use('/css', express.static(__dirname + 'public/css'))
router.use('/js', express.static(__dirname + 'app.js'))


import bodyParser from 'body-parser'
router.use(bodyParser.urlencoded({ limit: "100mb", extended: true }))
router.use(express.urlencoded({ extended: true}))



let myTabs: any[] = []

router.get('/', (req: Request, res: Response) =>{
    myTabs = []

    con.getConnection((err) => {
        if (err) res.send(err)
        con.query('SELECT * FROM todo', (err, result, fields) => {
            if (err) res.send(err)
            
            

            let tabs = ["Todo", "Doing", "Done"]
            tabs.forEach(tab => {
                let x = new TodoTabs(tab)
                for (let y in myTabs)
                {
                    if(x.name == myTabs[y].name) return
                }
                result.forEach((y: any) =>
                {
                    let existing = false
                    myTabs.forEach(currentTab => {
                        for (let a in currentTab.todos)    
                        {
                            if (currentTab.todos[a].id == y.id) existing = true
                        }
                        
                    });
                    if (tab == y.progress && !existing) x.addTodo({
                        id: y.id,
                        content: y.content,
                    })
                    

                })




                myTabs.push(x)
            });
            res.render('index', { tabs: myTabs })
            
        })
        
    })
})


router.post('/', (req: Request, res : Response) => {
    res.header("Access-Control-Allow-Origin", "*")
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
    res.header("Access-Control-Allow-Methods", "PUT, POST, GET, DELETE, OPTIONS")

    

    con.getConnection((err) => {
        if (err) res.sendStatus(404)
        con.query('INSERT INTO todo (content) VALUES (?)', [req.body.content], (err, result, fields) =>
        {

            res.redirect(303, '/')
        })


    })
})


router.get('/:id', (req: Request, res: Response) =>{
    con.getConnection((err) => {
        if (err) res.sendStatus(404)
        con.query('DELETE FROM todo WHERE id = ?', [req.params.id], (err, result, fields) =>
        {
            if (err) res.sendStatus(404)
            res.redirect(303, '/')
        })
    })
})


router.put('/', (req, res) =>
{
    let data = Object.keys(req.body)[0].split('|')
    con.query(`UPDATE todo SET progress = '${data[1]}' WHERE id = '${data[2]}'`, (err) =>
    {   
        if(err) console.error(err)
    })
    
    res.redirect(303, '/')
    

})



export default router;