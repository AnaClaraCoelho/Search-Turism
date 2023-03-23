<template>
  <v-container >
  <v-row>
    <v-col>
      <v-text-field
        v-model="searchWord"
        color="deep-orange darken-1"
        :loading="loading"
        placeholder="Find a tourist spot..."
        append-inner-icon="mdi-magnify"
      />
    </v-col>
    <v-col v-if="visible  ">
      <v-tooltip
        v-model="show_plus"
        location="top right"
      >
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            v-bind="props"
            :to="{ name: 'new-task' } "
          >
            <v-icon color="grey-lighten-1" >
              mdi-plus {{ this.loggedUser_ }}
            </v-icon>
          </v-btn>
        </template>
        <span>New tourist spot</span>
      </v-tooltip>
    </v-col>  
  </v-row> 
  <v-row>
  <v-col cols="3" v-for="item in searchedSpots" :key="item.id"  justify="center" >
    <v-card
      class="mx-auto my-12"
      max-width="374"
    >
      <v-img
        :src="item.url_image"
        height="250px"
        v-model="url_image"
        cover
        @click="openToast(item.id)"
      >
    </v-img>
    <v-dialog
      v-model="show_options"
    >
      <v-card  min-width="600" class="mx-auto" >
        <v-card-title>Select Option</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 80px;" >
          <v-radio-group
            v-model="dialogm1"
            column
          >
            <v-radio
              label="Delete"
              value="Delete"
            ></v-radio>
          </v-radio-group>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="show_options = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="blue-darken-1"
            variant="text"
            @click="action(correct_id)"
          >
            Confirm 
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


  <v-card-title
  v-model="tourist_spot"
  >
    {{ item.tourist_spot }}
  </v-card-title>

  <v-card-subtitle v-model="city">
    {{ item.city }}
  </v-card-subtitle>

  <v-card-actions>
    <v-btn
      :append-icon="item.done ? 'mdi-chevron-up' : 'mdi-chevron-down'"
      @click="item.done = !item.done"
      color="orange"
    >
      Read more
    </v-btn>

    <v-spacer></v-spacer>
    <v-btn
      color="pink"
      variant="text" 
      @click="likeSpot(item.id)"
    >
      <v-icon icon="mdi-heart"></v-icon>
      {{ item.like }}
    </v-btn>
  </v-card-actions>

  <v-expand-transition>
    <div v-show="item.done">
      <v-divider></v-divider>

      <v-card-text v-model="description">
        {{ item.description }}
      </v-card-text>
    </div>
  </v-expand-transition>
</v-card>
<v-responsive width="100%"></v-responsive>
    </v-col >
  </v-row>

</v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import TaskForm from "@/components/TaskForm.vue"
import AccountsApi from "@/api/accounts.api.js"
import { mapState } from "pinia"

import { useAccountsStore } from "@/stores/accountsStore"


export default {
  name: "TasksList",
  components: {  TaskForm },
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
      like: undefined,
      show: false,
      show_plus:false,
      show_options:false,
      dialogm1:'',
      correct_id:'',
      visible: false,
      items: [],
      searchWord: '',
      searchLoading: false,
      like: true,
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
    searchedSpots() {
      return this.items.filter((e) => {
        return e.tourist_spot .toLowerCase().includes(this.searchWord.toLowerCase());
      });
    },
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
    likeSpot(id) {
      
      if(this.like === true) {
        TasksApi.likeSpot(id)
        .then(() => {
          this.getTasks()
        })
        .then(this.like = !this.like)
      }
      else {
        TasksApi.unlikeSpot(id)
        .then(() => {
          this.getTasks()
        })
        .then(this.like = !this.like)
      }
    }
  },
} 
</script>

