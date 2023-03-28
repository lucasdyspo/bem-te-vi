div >
<section>
    <MyForm/>
    <Drop/>
</section>
</div>


<nav>
    <div>
        <img className="profile" src={ foto }/> </div>
    <div>
        <div>
            <h4> salve
                <h4>
                    <article>opaaa</article>
        </div>
    </div>
</nav>




function Example() {
    const setData = useState(null);
  
    useEffect(() => {
      async function fetchData() {
        const response = await fetch('http://localhost:8000/art/bb/');
        
        
        
        const data = await response.json();
        console.log(data);
        setData(data);
        
      }
  
      fetchData();
    }, []);
    
  
    return (
      <section>
      <div>
        <h1>ooooooooooooi</h1>
      </div>
  
      </section>
    );
  }