import { Todo } from '../interfaces/todo'
import mysql = require('mysql');

const con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "todo"
});


export default con;