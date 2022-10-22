import axios from "axios";

const ApiService = axios.create({
    //baseURL:'https://open-finances-api.herokuapp.com/api',
    baseURL:'http://localhost:8000/api'
})

export default ApiService