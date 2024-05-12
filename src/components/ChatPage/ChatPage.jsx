import styles from "./ChatPage.module.css";
import Right from '../../assets/Right.svg'
import Voice from '../../assets/Voice.svg'
import {Link} from "react-router-dom";
import Search from '../../assets/Search.svg'
import React, {useContext, useEffect, useState} from "react";
import {Positions, Sizes, TextToSpeech, useTts} from 'tts-react'
import {Context} from "../../main.jsx";
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';


const ChatPage = () => {
    const [service, setService] = useState([]);
    const [action, setAction] = useState([]);
    const [NextTasks, setNextTasks] = useState([]);

    const Yznati = "a7148524-e33b-4a07-a07e-c5ce1a7a65f6"
    const Otpravka = "05857344-6834-4439-8f15-fdbbb00e839f"
    const Plateshi = "5f80435e-5a24-4415-89fe-1f1462373caa"

    const [allMessages, setAllMessages] = useState([
        { text: "Вас приветствует МТС Ассистент, чем могу помочь?" +
                "Доступные команды: Проверить баланс Отправка платежей Совершить перевод" , from: 'assistant' },
    ]);

    const [UserCommand, setUserCommand] = useState([
    ])
    const {store} = useContext(Context);

    const startListening = () => SpeechRecognition.startListening({
        language: 'ru-RU'
    });


    const commands = [
        {
            command: ['Проверить баланс'],
            callback: (command) => getAction(Yznati),
            isFuzzyMatch: true,
            fuzzyMatchingThreshold: 0.2,
            bestMatchOnly: true
        },
        {
            command: ['Отправить платеж'],
            callback: (command) => getAction(Otpravka),
            isFuzzyMatch: true,
            fuzzyMatchingThreshold: 0.2,
            bestMatchOnly: true
        },
        {
            command: ['Cовершить перевод'],
            callback: (command) => getAction(Plateshi),
            isFuzzyMatch: true,
            fuzzyMatchingThreshold: 0.2,
            bestMatchOnly: true
        },


    ]
    const {transcript, resetTranscript,finalTranscript } = useSpeechRecognition({ commands })

    const getMessages = (command, transcript) => {
        store.getMessages(command, transcript).then((response) => {
            setUserMassage(store.messages)
        }).catch((error) => {
            console.error(error)
        })
    }

    const getAction = (action_id) => {
        store.CreateAction(action_id).then((response) => {
            setAction(store.Action);
            store.getNextTasks(store.Action.id).then(() =>{
                setNextTasks(store.NextTasks);
                store.NextTasks.forEach(task => {
                    setAllMessages(allMessages => [...allMessages, { text: task.name, from: 'assistant' }]);
                });
            }).catch((error) => {
                console.error(error)
            })
        }).catch((error) => {
            console.error(error)
        })
    }

    useEffect(() => {
        // Добавляем сообщение в allMessages, когда transcript обновляется
        if (finalTranscript.trim() !== "") {
            setAllMessages(allMessages => [...allMessages, { text: finalTranscript, from: 'user' }]);
            resetTranscript(); // Опционально сбросить transcript после добавления
        }
    }, [finalTranscript, resetTranscript]);

    const sendMessage = (text) => {
        setAllMessages(prev => [...prev, { text, from: 'user' }]);
    };

    useEffect(()=> {
        handleServices()
    },[]);

    const handleServices = ( ) => {
        store.getServices().then((response) => {
            const serviceNames = response.map(service => service.name);
            setService(serviceNames);
        }).catch((error) => {
            console.error(error)
        })
    }
    useEffect(() => {
        service.forEach(svc => {
            setAllMessages(allMessages => [...allMessages, { text: svc, from: 'assistant' }]);
        });
    }, [service]);



    const renderMessage = (msg, index) => {
        if (msg.from === 'assistant') {
            return (
                <div  className={msg.from === 'user' ? styles.RightMessage : styles.LeftMessage}>
                <TextToSpeech
                    key={index}
                    markTextAsSpoken
                    align="vertical"
                    size="small"
                    position="tl"
                    lang="ru-RU"
                    autoPlay
                >
                    <p>{msg.text}</p>
                </TextToSpeech>
                </div>
            );
        } else {
            return (
                <div key={index} className={msg.from === 'user' ? styles.RightMessage : styles.LeftMessage}>
                    {msg.text}
                </div>
            );
        }
    };

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
                    {allMessages.map(renderMessage)}
                </main>
                <div className={styles.BottomContainer}>
                    {UserCommand}
                    <input className={styles.input} onKeyPress={e => e.key === 'Enter' && sendMessage(e.target.value)}></input>
                    <img src={Search} width={35} className={styles.Icon}></img>
                    <img src={Voice} className={styles.Icon} onClick={startListening}></img>
                </div>
        </div>
        </div>
    )
}

export default ChatPage;