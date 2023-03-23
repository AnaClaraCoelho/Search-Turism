import api from "./config.js"
import apiHelpers from "./helpers.js"

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
  likeSpot: (id) => {
    console.log('Bati na API', id)
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/like", id)
        .then((response) => {
          return resolve(response)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  unlikeSpot: (id) => {
    console.log('Bati na API', id)
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/unlike", id)
        .then((response) => {
          return resolve(response)
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
  }
}
