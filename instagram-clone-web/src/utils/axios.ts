import axios from 'axios'

export const BASE_URL = 'http://localhost:8000/'

export const AxiosInstance = axios.create({
  baseURL: BASE_URL,
})
