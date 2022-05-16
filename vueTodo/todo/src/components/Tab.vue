<template>
    <h1>{{name}}</h1>
    
    <!-- <div class="drop-zone">
        <div v-for="item in items" :key="item.id" draggable="true" class="drag-el" @dragstart="onDragStart($event, item)">
            <p>{{item.text}}</p>
        </div>
    </div> -->


</template>

<script>



export default {
    props: {
        name: {
            type: String,
            required: true
        },
        items: {
            type: Array,
            required: false
        }
    },
    // methods: {
    //     onDragStart(e, item){
    //         console.log(item)
    //         e.dataTransfer.dropEffect = "move"
    //         e.dataTransfer.effectAllowed = 'move';
    //     },
    //     onDragOver(e){
    //         e.preventDefault();
    //         e.dataTransfer.dropEffect = 'move';
    //     },
    //     onDrop(e, list){
    //         const itemID = event.dataTransfer.getData('itemID');
    //         const item = this.items.find(item => item.id == itemID);
    //         // item.list = 
    //     }
    // }
}
</script>

<style scoped>
    .drag-el{
        cursor: pointer;
    }
</style>