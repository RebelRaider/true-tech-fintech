import axios from 'axios';




export default class MessageService {
    static async getMessages(command, transcript) {
        return axios.post('', {command, transcript}, {headers: {'Content-Type': 'application/json'}})
    }
    static async getServices() {
        return axios.get('https://188.124.37.121.sslip.io:8000/api/v1/action_template/root_actions')
    }
    static async CreateAction(action_id) {
        const userId = "84bc07d5-af3d-43e0-9b66-88dbe959b963"
        return axios.post('https://188.124.37.121.sslip.io:8000/api/v1/active_action/',{user_id:userId,action_id:action_id}, {headers: {'Content-Type': 'application/json'}})
    }
    static async NextTasks(id) {
        return axios.get(`https://188.124.37.121.sslip.io:8000/api/v1/active_action/next_tasks/${id}`)
    }
    static async doAll(id,nextID,transcript) {
        return axios.post(`https://188.124.37.121.sslip.io:8000/api/v1/active_action/do_all/${id}`, {next_node_id:nextID, value: transcript}, {headers: {'Content-Type': 'application/json'}})
    }
}