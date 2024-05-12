import {makeObservable, observable} from "mobx";
import MessageService from "../services/MessageService.js";


export default class Store {
    messages = [];
    constructor() {
        makeObservable(this, {
            messages: observable,
        });
    }
    setMessage(massages) {
        this.messages = massages;
    }


    async getMessages(command, transcript) {
        try {
            const response = await MessageService.getMessages(command,transcript);
            this.setMessage(response.data);
        } catch(e) {
            console.error('Error getting messages', e);
        }
    }
}
