import './Profile_name.css'



function Profile_name({nome, vulgo}) {
    return ( <
        div >
        <
        div id = 'flex' >
        <
        div className = 'blur_name' > < /div> <
        h1 > {nome} < /h1>
        <h3>{vulgo}</h3>

        <
        /div> <
        /div>
    )


}

export default Profile_name;