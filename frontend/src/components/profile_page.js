import './profile_page.css'
import Profile_name from './Profile_name';
import Ballons_profile from './ballons_profile';
import Img_profile from './img_profile';



function Profile() {

    const data = [{"id":5,"friends":1,"arts_realizatas":3,"users_collaborators":1,"nome":"sabrina hungaro","vulgo":"sassa","similarity":null,"pathphoto":"","register":12}][0]

    console.log(data)
    return ( 
        <div>
            <div className = 'capa' >
                <div className = 'margin' >
                    <Profile_name nome={data.nome} vulgo={data.vulgo}/>
                </div>

                <div>
                    <Img_profile image={data.pathphoto}/>
                </div> <div>
                    <Ballons_profile/>
                </div>


                </div> 
                <ol className = 'op' >
                    <li> {data.arts_realizatas + data.users_collaborators} Arts </li> 
                    <li> {data.friends} followers </li> 
                    <li> instagram </li> 
                    <li> Linkedin </li> 
                </ol>

        </div>


    )


}

export default Profile;