<template>
  <v-container >
    <v-row no-gutters>
      <v-col v-if="loggedUser" >
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
                mdi-plus
              </v-icon>
            </v-btn>
          </template>
          <span>New tourist spot</span>
        </v-tooltip>
      </v-col>  
      <v-spacer></v-spacer>
      <v-responsive width="100%"></v-responsive>
      
        <v-col cols="3" v-for="item in items" :key="item.id"  justify="center" >
            <v-card
              class="mx-auto my-12"
              max-width="374"
            >
          <v-img
            :src="item.url_image"
            height="250px"
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
              <v-card-text style="height: 100px;" >
                <v-radio-group
                  v-model="dialogm1"
                  column
                >
                  <v-radio
                    label="Edit"
                    value="Edit"
                  ></v-radio>
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
          >
            {{ item.tourist_spot }}
          </v-card-title>

          <v-card-subtitle>
            {{ item.city }}
          </v-card-subtitle>

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

              <v-card-text>
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
import { mapState } from "pinia"
import TasksApi from "@/api/tasks.api.js"
import TaskForm from "@/components/TaskForm.vue"
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
      show: false,
      show_plus:false,
      show_options:false,
      dialogm1:'',
      correct_id:'',
      items: [],
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      this.loading = true
      TasksApi.getTasks().then((data) => {
        this.items = data.todos
        this.loading = false
      })
    },
    deleteTask(task) {
      this.loading = true
      TasksApi.deleteTask(task).then((task) => {
        this.loading = false
        this.getTasks()
        this.$router.push({ name: 'tasks-list' })
      })
    },
    action(id){
      this.show_options = false
      if (this.dialogm1 == 'Edit'){
        console.log(this.dialogm1)
      }
      else if (this.dialogm1 == 'Delete'){
        this.deleteTask(id)
      }
    },
    openToast(id) {
      if(this.loggedUser){
        this.show_options= !this.show_options
        this.correct_id = id  
      }

    },
  },
}
</script>

