import './hgs.css'
import Box_direita from './box_direita'




export default function Hgs() {
    let datas
    let nos

    const url = 'http://localhost:8000/home/api/v1/highlights/'
    async function getHGs(){
        const response = await fetch(url)
        console.log(response)
        const data = await response.json();
        console.log((data))
        



        const Box = data.map(
            (post)=> console.dir(post)
        )



        


        

    }

    datas = getHGs()
    console.log((datas))
    

    



    return(
        <div className='hgs'>


        {console.log(datas)}
{/*             
            
            {datas.products.map((post) => {
                <Box_direita title={post.title} content={post.content}/>
            })} */}


            {/* {datas.map(function(data) {
                return (
                    <Box_direita title='piiiinto' content='aai q tudo/>
                )
            })} */}


            <Box_direita/>
            {/* {Box} */}
        </div>
    )


}