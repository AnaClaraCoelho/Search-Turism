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
  } 
}
