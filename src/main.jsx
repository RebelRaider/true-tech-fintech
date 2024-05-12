import 'regenerator-runtime/runtime';
import React, {createContext} from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import MainPage from "./components/MainPage/MainPage.jsx";
import Store from "./store/store.js";
import MobileVersion from "./components/MobileVersion/MobileVersion.jsx";
import ChatPage from "./components/ChatPage/ChatPage.jsx";
const store = new Store();
export const Context = createContext({
    store,
});

const router = createBrowserRouter([
    {
        path: "/",
        element: <MainPage />,
    },
    {
        path: "/mobile",
        element: <MobileVersion />
    },
    {
        path: "/chat",
        element: <ChatPage />,
    }
])


ReactDOM.createRoot(document.getElementById('root')).render(
    <Context.Provider value={{store, router}}>
        <React.StrictMode>
            <RouterProvider router={router}/>
        </React.StrictMode>
    </Context.Provider>
)
