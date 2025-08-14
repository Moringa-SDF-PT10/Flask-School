import { useState } from 'react'
import {  toast } from 'react-toastify';

export default function AddBoardingHouse() {

  const [name, setName] = useState("")
  const [mascot, setMascot] = useState("")

  const formSubmit = (event)=>{
    event.preventDefault()

    fetch("http://localhost:5000/houses", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({name:name, mascot:mascot })
    })
    .then( res => res.json() )
    .then((data)=>{
      if(data.name){
          toast.success("House added successfully")

          setMascot("")
          setName("")
      }
      else{
                  toast.error("Error adding boarding house ")

      }
      
    })

  }



  return (
    <div>

    <h4 className='text-3xl font-bold text-center'>Add New Boarding House</h4>
    <form onSubmit={formSubmit} className="bg-gray-300 p-3 max-w-sm mx-auto text-lg font-semibold">
      <div className='flex flex-col mb-4'>
        <label className=''>Name</label>
        <input type='name' placeholder='Enter house name' onChange={(e)=> setName(e.target.value)} />
      </div>
      <div className='flex flex-col mb-4'>
        <label className=''>Mascot</label>
        <input type='name' placeholder='Enter mascote' onChange={(e)=> setMascot(e.target.value)} />
      </div>

      <button type='submit' className='px-4 py-2 bg-blue-600 text-white'>Save</button>
      
    </form>

      


    </div>
  )
}
