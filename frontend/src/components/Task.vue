<template>
<div>
  <v-card>
    <v-card-text>
      <div>#{{ task.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ task.description }}
        <p class="ma-0 pa-0 text-h5 text--primary">{{ task.city }}</p>
        <p class="ma-0 pa-0 text-h5 text--primary">{{ task.url_image }}</p>
        <p class="ma-0 pa-0 text-h5 text--primary">{{ task.touristSpot }}</p>
        <p class="ma-0 pa-0 text-h5 text--primary">{{ task.like }}</p>
      </p>
    </v-card-text>
  </v-card>
</div>
</template>

<script>
export default {
  name: "TasksModel",
  props: {
    task: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
}
</script>
