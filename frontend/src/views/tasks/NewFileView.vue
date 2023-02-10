<template>
    <v-container>

        <v-form
        ref="form"
        v-model="valid"
        lazy-validation
        >
        <v-text-field
        v-model="city"
        :rules="Rules"
        label="City/Country"
        required
        @keyup.enter="login()"
        ></v-text-field>
        
        <v-text-field
        v-model="touristSpot"
        :rules="Rules"
        label="Tourist Spot"
        required
        @keyup.enter="login()"
        ></v-text-field>
        
        <v-text-field
        v-model="description"
        label="Description"
        required
        @keyup.enter="login()"
        ></v-text-field>

        <v-text-field
        v-model="url_image"
        label="Image URL"
        required
        @keyup.enter="login()"
        ></v-text-field>
        
        
        
        <v-btn
        :disabled="!valid"
        color="teal lighten-3"
        class="mr-4"
        @click="addNewTask()"
      >
      Validate
    </v-btn>
    
    <v-btn
    color="red lighten-5"
    class="mr-4"
    @click="reset"
    >
    Reset Form
    </v-btn>

    <v-btn
      color="purple lighten-5"
      class="mr-4"
      :to="{ name: 'tasks-list' }"
      >
      Return
    </v-btn>
</v-form>
</v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"

export default {
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  props: {
    newTask: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    valid: true,
    city: '',
    Rules: [
      v => !!v || 'Required',
    ],
    touristSpot: '',
    description: '',
    url_image: ''
  }),

  methods: {
    reset () {
      this.$refs.form.reset()
    },
    addNewTask(task) {
        task = {
            city: this.city,
            touristSpot: this.touristSpot,
            description:this.description,
            url_image: this.url_image
        }
        this.$refs.form.validate()
        this.loading = true
        TasksApi.addNewTask(task.city, task.touristSpot, task.description, task.url_image).then((task) => {
        // this.getTasks()
        this.loading = false
        console.log("oi")
        this.$router.push({ name: 'tasks-list' })
      })
    },
  },
}
</script>