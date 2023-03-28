import "./App.css";
import ImagemG from './components/imagemG';
// import a from "./components/00.json";
// import { useState, useEffect } from "react";
import Comments_box from "./components/arts_pages";
import Profile from "./components/profile_page";
import Box_direita from "./components/box_direita";
import Example from "./components/exapi";
// import CustomersList from "./components/teste";
// import Appi from "./components/exapi";
// import Hgs from "./components/hgs";
import { BrowserRouter, Routes, Route, Link} from 'react-router-dom'
import bootstrap from "bootstrap";


function App() {
    // const it = a
    // console.log(it.Arts[0].id)
    // const dic = it.Arts[0]
    // console.log(dic)
    // const [mousePosition, setmousePosition] = useState({
    //     x: 0,
    //     y: 0
    // });
    // console.log(mousePosition)
    // useEffect(() => {
    //     const mouseMove = e => {
    //         // console.log(e)

    //     }
    //     window.addEventListener("mousemove", mouseMove)
    //     return () => {
    //         window.removeEventListener('mousemove', mouseMove)
    //     }
    // }, []);

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"></link>
    



    return ( 

    
        <div className = "App" >
        


            {/* <Profile/> */}
            <Comments_box/>
            {/* <Hgs/> */}
            {/* <a href='http://localhost:8000/art/teste/6/comments/'> */}
            {/* <div>
                <h2>sssss</h2>
               
                <h1> xexo gerral chatuba de mesquita </h1>
                <h2>posososos</h2>
            </div>
            </a> */}
            {/* <CustomersList/> */}

            {/* <Box_direita/> */}
            {/* <Appi/> */}

            {/* <ImagemG/> */}
            {/* <div> */}
            {/* <section> */}
            {/* <Shadow/> */}
            {/* <h1>oooooooooooooooooooooooooooooooooooooooooooooooooooooiaiaakskaksk</h1> */}
           
            {/* <Example/> */}
            {/* </section> */}
            {/* </div> */}
        </div>
    );
}

export default App;