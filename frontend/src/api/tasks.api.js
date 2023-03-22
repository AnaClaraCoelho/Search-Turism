import api from "./config.js"
import apiHelpers from "./helpers.js"
import axios from 'axios'

export default {
  getTasks: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/tasks/list")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addNewTask: (city, touristSpot, description, url_image) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/add", apiHelpers.dataToForm({ city, touristSpot, description, url_image }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  deleteTask: (id) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/delete", {id})
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  editTask: (city, touristSpot, description, url_image) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/edit",apiHelpers.dataToForm({ city, touristSpot, description, url_image }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addFavs: (like)  => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/like", apiHelpers.dataToForm({like}))
        .then(response => {
      return resolve(response.data)
      // atualizar o estado do botão de curtir/descurtir
    })
    .catch((error) => {
      return reject(error)
      })
    })
  }
}
