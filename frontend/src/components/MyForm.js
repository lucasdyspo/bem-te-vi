import { useState } from "react";
import "./MyForm.css";
import { FaInstagram, FaFacebook, FaLinkedin, FaHandPointUp, FaBitcoin, FaHeart, FaHandHolding, FaPeopleArrows, FaSeedling, FaUsers, FaThumbsUp, FaRegStickyNote } from "react-icons/fa"

/*6 - controlled inputs */
function MyForm({like, rating, props}) {
    const domain = 'http://localhost:8000/'
    const appl = 'login/profile/'
    let id = '1/'
    console.log(props)


    return (

        <div>
            <ul>
                <li>{rating}</li>
                <li>
                    <div className = "btn">
                    </div> <FaInstagram />
                </li> 

                <a href='http://127.0.0.1:8000/art/teste/6/comments/'><li className = "btn"> <FaHeart/> </li></a>
                <a href={domain + appl + id}> <li>   <FaRegStickyNote/> </li> </a>
                <li> <h6 className="like">{like}</h6> <FaThumbsUp/> </li>  
                <li> <FaUsers/> </li> 
            
            </ul> 
        </div>
    );
};

export default MyForm;