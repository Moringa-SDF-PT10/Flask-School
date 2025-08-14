import React, { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { toast } from 'react-toastify'

export default function EditStudent() 
{
    const navigate =useNavigate()

    const [houses, setHouses] = useState([])

      const [full_name, setFullname] = useState("")
      const [boarding_house, setBoarding_house] =useState("")
      const [ age, setAge] = useState(0)
      const [ email, setEmail] = useState("")
      const  [bio, setBio] = useState("")

    const [student, setStudent] = useState({})
    const {id} = useParams()

    useEffect(()=>{
              fetch(`http://localhost:5000/student/${id}`)
              .then((response) => response.json())
              .then((data) =>{
                  setStudent(data)

                  setFullname(data.full_name)
                  setAge(data.age)
                  setBoarding_house(data.boarding_house)
                  setEmail(data.email)
                  setBio(data.bio)
                
                  })
              .catch((error) => toast.error("Error fetching students:", error));
        
    }, [id])

      // fetch houses
      useEffect(() => {
        fetch("http://localhost:5000/houses")
        .then( res => res.json() )
        .then((data)=>{
          setHouses(data)
          console.log("Houses ",data)
          
        })
      }, []);


    function onEditStudent(e){
           e.preventDefault();
            fetch(`http://localhost:5000/students/${id}`, {
             method: "PATCH",
             headers: { "Content-Type": "application/json" },
             body: JSON.stringify({
                boarding_house:boarding_house, email:email, 
                bio:bio, full_name:full_name, age:age
             })
           })
           .then((res) => res.json())
           .then((res) => {
             console.log(res);

             if(res.age){
                navigate("/addstudent")
                 toast.success("Student updated successfully");
             }
             else{
               toast.error("Error updating student")
       
             }
             
       
           })
           .catch((error) => toast.error("Error updating student:", error));


    }

  return (
    <div>
        <h1>Edit Student {id}</h1>
               {/* Form */}
        <form
          onSubmit={onEditStudent}
          className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8"
        >
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Full Name"
            value={full_name}
            onChange={(e) => setFullname( e.target.value )}
            required
          />
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Age"
            type="number"
            value={age}
            onChange={(e) => setAge( e.target.value )}
            required
          />
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail( e.target.value )}
          />
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Bio"
            value={bio}
            onChange={(e) => setBio( e.target.value )}
          />

          <div>
              <label className="block text-sm font-medium text-gray-700"> Boarding House  </label>
              <select
                className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
                value={boarding_house}
                onChange={(e) => setBoarding_house( e.target.value )}
              >
                <option value={boarding_house}>{boarding_house}</option> 
                {
                  houses && houses.map((house)=>(
                    <option value={house.id}>{house.name} ({house.mascot})</option>

                  ))
                }
              
              </select>
          </div>

          <button
            type="submit"
            className="md:col-span-2 bg-blue-500 text-white rounded-lg py-2 font-semibold hover:bg-blue-600 transition duration-200"
          >
            Save Student
          </button>
        </form>

      
    </div>
  )
}
