<template>
<v-select
  label="Para onde você quer ir?"
  :items="citys"
  v-model="citySearch"
></v-select>
<city-select :citySearch="citySearch" v-show="citySearch != ''"/>
</template>


<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import AccountsApi from "@/api/accounts.api.js"
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import CitySelect from './CitySelect.vue'




export default {
 name: "AtrractionsView",
 components: {CitySelect },
 setup() {
   const appStore = useAppStore()
   return { appStore }
 },
 computed: {
   ...mapState(useAccountsStore, ["loggedUser"]),
 },
 data() {
   return {
     loading: false,
     city: '',
     description: '',
     tourist_spot: '',
     url_image: '',
     show: false,
     show_plus:false,
     show_options:false,
     dialogm1:'',
     correct_id:'',
     visible: false,
     items: [],
     like: '',
	 citys: ['Aracaju', 'Belém', 'Belo Horizonte', 'Brasília', 'Curitiba', 'Natal', 'Boa vista', 'Rio de Janeiro', 'São Paulo' ],
	 citySearch:''
   }
 },
 emits: ["newTask"],
 mounted() {
     this.getTasks()
     AccountsApi.whoami().then((response) => {
     if (response.authenticated) {
       this.visible = true
     }
   })
   },
   computed: {
   ...mapState(useAccountsStore, ["loggedUser"]),
 },
 methods: {
   getTasks() {
     this.loading = true
     TasksApi.getTasks().then((data) => {
       this.items = data.todos
       this.loading = false
     })
   },
   deleteTask(id) {
     this.loading = true
     TasksApi.deleteTask(id).then((id) => {
       this.loading = false
       this.getTasks()
       this.$router.push({ name: 'tasks-list' })
     })
   },
   editTask(id){
     TasksApi.editTask(id).then((task_to_update) => {
       this.$emit("newTask", {
         id: 'task_to_update.id',
         city: 'task_to_update.city',
         touristSpot: 'task_to_update.tourist_spot',
         description: 'task_to_update.description',
         url_image: 'task_to_update.url_image'
       })
       this.$router.push({ name: 'new-task' })
   })
    
   },
   action(id){
     this.show_options = false
     if (this.dialogm1 == 'Edit'){
       this.editTask(id)
     }
     else if (this.dialogm1 == 'Delete'){
       this.deleteTask(id)
     }
   },
   openToast(id) {
     if(this.visible){
       this.show_options= !this.show_options
       this.correct_id = id 
     }
   },
 },
}
</script>
