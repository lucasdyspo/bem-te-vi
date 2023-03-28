/* eslint-disable react/jsx-pascal-case */
import './popup.css'
import Header_popup from "./header_popup";
import { FaFacebook, FaSuperpowers } from "react-icons/fa"

const Popup = () => {


    return ( <
        div className = "popup" >
        <
        div >
        <
        Header_popup / >

        <
        div >
        <
        form action = "#" >

        <
        input type = 'text'
        placeholder = 'title'
        name = "commit" / >
        <
        input id = 'content'
        type = 'text'
        placeholder = "make your commentary"
        name = 'content' / >
        <
        div >
        <
        FaFacebook / >
        <
        FaSuperpowers / >
        <
        /div>


        <
        /form> <
        /div>


        <
        /div>

        <
        /div>


    )

}
export default Popup;