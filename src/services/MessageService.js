import axios from 'axios';

export default class MessageService {
    static async getMessages(command, transcript) {
        return axios.post('', {command, transcript}, {headers: {'Content-Type': 'application/json'}})
    }
}