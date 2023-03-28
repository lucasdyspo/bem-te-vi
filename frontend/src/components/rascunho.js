import React from 'react'
import './rascunho.css'


const Rasc = () => {
    const eve = (e) => {
        console.log(e)
        console.log('é issumemo')
        return (

            <
            div > < h1 > eu aamo voce < /h1></div >
        )

    }
    return ( <
        div className = "rasc"
        onClick = { eve } >
        <
        h1 > texxxxto < /h1> <
        div className = 'window' / >


        <
        /div>
    )
}


export default Rasc;