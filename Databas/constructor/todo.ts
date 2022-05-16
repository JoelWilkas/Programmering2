export default class TodoTabs {
    todos: []
    name : string
    constructor(name: string){
        this.name = name
        this.todos = []



    }

    addTodo(this: any, todo: any){
        this.todos.push(todo)
    }


    
}