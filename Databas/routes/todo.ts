import express, { Request, Response } from 'express'
import TodoTabs from '../constructor/todo'

import con from '../constructor/dbconnection'

let router = express.Router();

const myTabs: any[] = []

router.get('/', (req: Request, res: Response) =>{
    


    con.connect((err) => {
        if (err) res.send(err)
        

        con.query('SELECT * FROM todo', (err, result, fields) => {
            if (err) res.send(err)
            
            let tabs = ["Todo", "Doing", "Done"]
            tabs.forEach(tab => {
                let x = new TodoTabs(tab)
                result.forEach((y: any) => {
                    if (tab == y.progress) x.addTodo({
                        id: y.id,
                        content: y.content,
                    })
                })
                myTabs.push(x)
            });

            

            
            console.log(myTabs[0].todos)
            res.render('index', { tabs: myTabs })
            
        })
    })
    
    

})



export default router;