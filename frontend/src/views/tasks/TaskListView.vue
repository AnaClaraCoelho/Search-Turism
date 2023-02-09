<template>
  <v-container >
    <v-row no-gutters>
      <v-col >
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
      <v-responsive width="100%"></v-responsive>
      <v-col>  
        <v-sheet class="pa-3 ma-3">
        <v-card 
          max-width="900"
          class="mx-auto"
          shaped outlined>
          <div class="d-flex flex-no-wrap justify-space-between">
                <div> 
                  <v-card-title>
                    Top western road trips
                  </v-card-title>
                  
                  <v-card-subtitle>
                    1,000 miles of wonder
                  </v-card-subtitle>
                  
                  <v-card-actions>
                    <v-btn
                    color="pink lighten-5"
                    text
                    @click="show = !show"
                    >
                    Explore
                    <v-spacer></v-spacer>
                    <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                  </v-btn>
                  
                  <v-spacer></v-spacer>
              </v-card-actions>
              
              <v-expand-transition>
                <div v-show="show">
                  <v-divider></v-divider>
                  
                  <v-card-text>
                    I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                  </v-card-text>
                </div>
              </v-expand-transition>
            </div>
            <v-avatar class="ma-3" size="125" rounded="0">
              <v-img
              src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              height="200px"
              ></v-img>
            </v-avatar>
          </div>
        </v-card>
      </v-sheet>
      </v-col>
      <v-responsive width="100%"></v-responsive>
      <v-col>
        <v-sheet class="pa-3 ma-3">
        <v-row v-for="item in items" :key="item.id"  justify="center"  >
          <v-col cols="10" >
            <task :task="item" max-width="900"/>
            <v-responsive width="100%"></v-responsive>
          </v-col >
        </v-row>
      </v-sheet>
      </v-col>
    </v-row>
        
      
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import Task from "@/components/Task.vue"
import TaskForm from "@/components/TaskForm.vue"

export default {
  name: "TasksList",
  components: { Task, TaskForm },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      show: false,
      show_plus:false,
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
    
  },
}
</script>

<style scoped>
.v-container.fill-height {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
}
</style>
