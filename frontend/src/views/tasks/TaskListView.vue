<template>
  <v-container >
    <v-row no-gutters>
      <v-col v-if="visible  ">
        <v-tooltip
          v-model="show_plus"
          location="top right"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              icon
              v-bind="props"
              :to="{ name: 'favs-list' } "
            >
              <v-icon color="grey-lighten-1" >
                mdi-plus {{ this.loggedUser_ }}
              </v-icon>
            </v-btn>
            <v-btn value="favorites"
              class="ma-4 pb-7 pt-5"
              :to="{ name: 'new-task' } "
            >
              <v-icon>mdi-heart</v-icon>

              Favoritos
            </v-btn>
            <!-- <v-text-field
              v-model="search"
              label="Busque uma cidade"
              class="pa-7"
            ></v-text-field> -->
          </template>
          <span>New tourist spot</span>
        </v-tooltip>
      </v-col>  
      <v-spacer></v-spacer>
      <v-responsive width="100%"></v-responsive>
      
        <v-col cols="3" v-for="item in items" :key="item.id" justify="center" :search="search">
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
            <v-card  min-width="600" class="mx-auto">
              <v-card-title>Select Option</v-card-title>
              <v-divider></v-divider>
              <v-card-text style="height: 80px;" >
                <v-radio-group
                  v-model="dialogm1"
                  column
                >
                  <!-- <v-radio
                    label="Edit"
                    value="Edit"
                  ></v-radio> -->
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
                  Close
                </v-btn>
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="action(correct_id)"
                >
                  Save 
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
          <v-col>
            <v-btn 
            icon
            @click="item.like = !item.like"
            :color="item.like ? 'pink' : 'gray'"
            >
              <v-icon 
                icon="mdi-heart" 
                @click="item.updateColor"></v-icon>
            </v-btn>
          </v-col>
          <v-card-actions>
            <v-btn
              color="pink"
              variant="text"
              @click="item.done = !item.done"
            >
              Explore 
            </v-btn>

            <v-spacer></v-spacer>

            <v-btn
              :icon="item.done ? 'mdi-chevron-up' : 'mdi-chevron-down'"
              @click="item.done = !item.done"
            ></v-btn>
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
      show: false,
      show_plus:false,
      show_options:false,
      dialogm1:'',
      correct_id:'',
      visible: false,
      items: [],
      colorBtn: "pink",
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
    updateColor(){
      this.colorBtn="blue"
    }
  },
}
</script>

