<template>
    <div v-for="Tab in Tabs" :key="Tab.id">
      <div v-for="Items in getList(Tab.id)" :key="Items.text">
        <Tab :name="Tab.name" />
      </div>
    </div>
</template>

<script>
import Tab from './components/Tab.vue'


export default {
  components: {
    Tab
  },
  data(){
    return {
      Tabs: [
        {name: "Todo", id: 1},
        {name: "In Progress", id: 2},
        {name: "Done", id: 3}
      ],
      
    }
  },
  setup(){

    const Todos = [
        {text: "Buy Milk", list: 1},
        {text: "Buy Bread", list: 1},
        {text: "Buy Eggs", list: 1},
        {text: "Buy Milk", list: 2},
        {text: "Buy Bread", list: 2},
        {text: "Buy Eggs", list: 2},
        {text: "Buy Milk", list: 3},
        {text: "Buy Bread", list: 3},
        {text: "Buy Eggs", list: 3}
      ]


    return {
      getList(id){
        return Todos.filter(item => item.list == id)
      }
    }
  }




}
</script>

<style>

</style>