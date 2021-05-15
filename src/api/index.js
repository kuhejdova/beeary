import axios from "axios";
import { baseUrl } from "../variables.js";

export function authenticate(userData) {
  return axios.post(`${baseUrl}/login/`, userData);
}

export function register(userData) {
  return axios.post(`${baseUrl}/register/`, userData);
}
