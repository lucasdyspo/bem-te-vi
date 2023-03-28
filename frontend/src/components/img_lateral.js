import foto from "../imgs/daf5f17ee707b1643d1d9c4e34b97407.jpg"
import Shadow from "./shadow_back";
import './img_lateral.css'


function Iimg(props) {


    return ( <
        div style = {
            {
                backgroundImage: `url("https://via.placeholder.com/500")`
            }
        }
        className = "lateral" >

        <
        Shadow / >
        <
        div >
        <
        h3 > { props.title } < /h3> <
        p > { props.desc } < /p> < /
        div >


        <
        /div>
    )

}


export default Iimg;