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
        label="City"
        required
        ></v-text-field>
        
        <v-text-field
        v-model="touristSpot"
        :rules="Rules"
        label="Tourist Spot"
        required
        ></v-text-field>
        
        <v-text-field
        v-model="description"
        label="Description"
        required
        ></v-text-field>
        
        <v-col cols="12" class="d-flex align-center justify-center mt-5">
            <input type="file" accept="image/jpeg" @change="upload" />
        </v-col>
        
        <v-btn
        :disabled="!valid"
        color="teal lighten-3"
        class="mr-4"
        @click="addNewTask()"
        :to="{ name: 'tasks-list'}"
      >
      Validate
    </v-btn>
    
    <v-btn
    color="blue lighten-5"
    class="mr-4"
    @click="reset"
    >
    Reset Form
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
  data: () => ({
    valid: true,
    city: '',
    Rules: [
      v => !!v || 'Required',
    ],
    touristSpot: '',
    description: '',
    profilePicture: ''
  }),

  methods: {
    reset () {
      this.$refs.form.reset()
    },
    upload(event) {
      const input = event.target;
      if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.profilePicture = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
      }
    },
    addNewTask(task) {
        task = {
            city: this.city,
            touristSpot: this.touristSpot,
            description:this.description,
            profilePicture: this.profilePicture
        }
        this.$refs.form.validate()
        this.loading = true
        TasksApi.addNewTask(task.city, task.touristSpot, this.description).then((task) => {
        this.appStore.showSnackbar(`Nova tarefa adicionada #${task.id}`)
        this.getTasks()
        this.loading = false
        console.log("oi")
      })
    },
  },
}
</script>