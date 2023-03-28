import React, { useState, useEffect } from 'react';



function Example() {
    // const setDatas = useState([]);
    var dados = 0
  
    
      async function fetchData() {
        const response = await fetch('http://localhost:8000/home/api/v1/highlights/')
  
      
        
        
        
        const data = await response.json();
        // console.log((data));
        dados = data
        console.log((dados));
        return dados
      }
  
     const lo = fetchData()
     
    

    

   
    
  
    return (
      <section>
      <div>
        <h1>{dados.id}</h1>
        <h1>ooooooooooooi</h1>
      </div>
  
      </section>
    );
  }
export default Example;