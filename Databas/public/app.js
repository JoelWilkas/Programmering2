let draggables = document.querySelectorAll(".draggable")
let containers = document.querySelectorAll(".container")




draggables.forEach(draggable => {
    draggable.addEventListener('dragstart', (e) => {
        draggable.classList.add('dragging')
    })



    draggable.addEventListener('dragend', async () => {
        const res = await axios.put('/', 
        
        
        `${draggable.childNodes[3].innerHTML}|${target}|${draggable.childNodes[1].innerHTML}`
             


        , {
    Headers: {
        'content-type': 'text/json'
        
        }

    })
    res.data.headers['Content-Type']
    })
})


let target = ""

containers.forEach(container => {


    container.addEventListener('dragover', async e => {
        e.preventDefault()
        const draggable = document.querySelector(".dragging")
        
        container.appendChild(draggable)
        
        draggable.addEventListener('dragend', async (e) => {
            e.preventDefault()
            draggable.classList.remove('dragging')
            





            
        })
    })
    container.addEventListener('dragenter', () => {
        target = container.children[0].innerHTML
    })


})