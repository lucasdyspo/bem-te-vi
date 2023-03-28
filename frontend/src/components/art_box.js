import foto from "../imgs/euzin.jpeg";





function Art_box({number, title}) {

   


    return(<>
    
    

        <div className="box_image" >

           
            
            
            <img src = { foto } className="d-flex"/> 
                
                
                        <div className = 'art_title'> {title}</div>
                        <div className = 'name_page'> </div>
                        <h1 className = 'n_page' > {number} </h1> 
                        
                       
                        

                    
                   
                
                
          

                   
        </div>
        </>

    )

}

export default Art_box