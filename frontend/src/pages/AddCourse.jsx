import React, { useState } from 'react'
import {  toast } from 'react-toastify';

export default function AddCourse() {

  const [name, setName] = useState("")
  const [price, setPrice] = useState(0)

  const formSubmit = (event)=>{
    event.preventDefault()

  fetch('http://127.0.0.1:5000/courses', {
  method: 'POST',
  body: JSON.stringify({
    name: name,
    price: price,

  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((res) => {
    if(res.id){
      toast.success("Course Added successfully")
    }
    else{
      toast.error("Error adding course")
    }

  });


  }

  return (
    <div>

<h4>Add New Course</h4>
<form onSubmit={formSubmit} className="max-w-sm mx-auto">
  <div className="mb-5">
    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title</label>
    <input type="text" onChange={(e)=> setName(e.target.value) } value={name} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Course Name" required />
  </div>
 
   <div className="mb-5">
    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
    <input type="number" onChange={(e)=> setPrice(e.target.value) } value={price} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Course Price" required />
  </div>
  
  <button type="submit" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
</form>

      


    </div>
  )
}
