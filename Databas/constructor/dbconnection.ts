import { Todo } from '../interfaces/todo'
import mysql = require('mysql');

const con = mysql.createPool({
    host: "localhost",
    user: "root",
    password: "",
    database: "todo"
});


export default con;
