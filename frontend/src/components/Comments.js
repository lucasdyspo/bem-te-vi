import foto from "../imgs/euzin.jpeg";




function Comments({content, posted}) {



    return(

        <div className = 'comments container' >

                        <div className='text-start'>
                             <h1 className=""> eu memo </h1>
                            <img className = "profile" src = { foto }/> 
                           
                            <br></br>
                            <p id='posted'> {posted}</p>
                        </div> 
                        
                        <div className="container-sm">
                        <p> {content}´pki</p>
                        
                        </div>
            </div> 
     )

};

export default Comments;