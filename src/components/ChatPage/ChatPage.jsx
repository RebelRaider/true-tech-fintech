import styles from "./ChatPage.module.css";
import Right from '../../assets/Right.svg'
import Voice from '../../assets/Voice.svg'
import {Link} from "react-router-dom";
import Search from '../../assets/Search.svg'
import React, {useContext, useState} from "react";
import {Positions, Sizes, TextToSpeech, useTts} from 'tts-react'
import {Context} from "../../main.jsx";
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';


const ChatPage = () => {
    const [UserMassage, setUserMassage] = useState([
        'Привет, как дела'
    ]);
    const [UserCommand, setUserCommand] = useState([

    ])
    const {store} = useContext(Context);
    const [messages, setMessages] = useState([
        "Вас приветствует МТС Ассистент, чем могу помочь?"
    ]);

    const startListening = () => SpeechRecognition.startListening({
        language: 'ru-RU'
    });

    const commands = [
        {
            command: ['Проверить баланс','Отправить платеж','Cовершить перевод'],
            callback: (command) => getMessages(command, transcript),
            isFuzzyMatch: true,
            fuzzyMatchingThreshold: 0.2,
            bestMatchOnly: true
        }
    ]
    const {transcript, browserSupportsSpeechRecognition } = useSpeechRecognition({ commands })

    const getMessages = (command, transcript) => {
        store.getMessages(command, transcript).then((response) => {
            setUserMassage(store.messages)
        }).catch((error) => {
            console.error(error)
        })
    }

    return (
        <div className={styles.MainContainer}>
            <div className={styles.SectorContainer}>
                <div className={styles.HeaderContainer}>
                    <div className={styles.Icon}>
                        <Link to={"/mobile"}><img src={Right} width={20} height={20}/></Link>
                    </div>
                    <div className={styles.TextDecoration}>
                        <div className={styles.RedText}>МТС</div>Ассистент
                    </div>
                </div>
                <main className={styles.ContainerMain}>
                    {messages.map((msg, index) => (
                        <div key={`message-${index}`} className={styles.LeftMessage}>
                            {msg}
                        </div>
                    ))}
                    {UserMassage.map((msg, index) => (
                        <div key={`transcript-${index}`} className={styles.RightMessage}>
                            {msg}
                        </div>
                    ))}
                </main>
                <div className={styles.BottomContainer}>
                    {UserCommand}
                    <input className={styles.input}></input>
                    <img src={Search} width={35} className={styles.Icon}></img>
                    <img src={Voice} className={styles.Icon} onClick={startListening}></img>
                </div>
        </div>
        </div>
    )
}

export default ChatPage;