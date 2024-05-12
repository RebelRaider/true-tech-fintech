import {makeObservable, observable} from "mobx";
import MessageService from "../services/MessageService.js";


export default class Store {
    messages = [];
    Services = [];
    Action = [];
    NextTasks = [];
    constructor() {
        makeObservable(this, {
            messages: observable,
        });
    }
    setMessage(massages) {
        this.messages = massages;
    }
    setServices(servisec){
        this.Services = servisec;
    }
    setAction(action) {
        this.Action = action;
    }
    setNextTask(tasks) {
        this.NextTasks = tasks;
    }


    async getMessages(command, transcript) {
        try {
            const response = await MessageService.getMessages(command,transcript);
            this.setMessage(response.data);
        } catch(e) {
            console.error('Error getting messages', e);
        }
    }
    async getServices(){
        try {
            const response = await MessageService.getServices();
            this.setServices(response.data);
        } catch(e) {
            console.error('Error getting services', e);
        }
    }
    async CreateAction(action_id){
        try {
            const response = await MessageService.CreateAction(action_id);
            this.setAction(response.data);
        } catch(e) {
            console.error('Error getting services', e);
        }
    }
    async getNextTasks(id){
        try {
            const response = await MessageService.NextTasks(id);
            this.setNextTask(response.data);
        } catch(e) {
            console.error('Error getting services', e);
        }
    }
}
