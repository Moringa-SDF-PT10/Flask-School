import { useEffect, useState } from "react"
import { toast } from "react-toastify";


export default function Home() 
{
  const [courses, setCourses] = useState([])
  
  useEffect(()=>{    

    fetch('http://127.0.0.1:5000/courses')
    .then((response) => response.json())
    .then((data) => {
       setCourses(data)
    console.log("data", data);
    }
    
    );

  }, [])

  // delete function
  const deleteCourse = (id)=>{
    fetch(`http://127.0.0.1:5000/courses/${id}`, {
  method: 'DELETE',
   })
  .then((response) => response.json())
  .then((res) => {
    console.log(res);
    
         if(res.success){
           toast.success(res.success)
         }
         else{
           toast.error("Error deleting course!")
         }
  
  });

  }

  return (
    <div>
      <h1 className="text-2xl font-bold ">Courses ({courses.length})</h1>

      {
        courses && courses.length <1 &&
        <p>No courses at the moment!</p>
      }

      <div className="grid grid-cols-4 gap-4">
      {
        courses && courses.map((course)=>(
          <div className="border rounded p-3">
            <h3>{course.title}</h3>
            <h3>Price : {course.price}</h3>
            <h5>No. Enrolled {course.students.length}</h5>
            <button onClick={()=> deleteCourse(course.id)} className="bg-red-600 text-white px-2 py-1 text-sm">Delete</button>
          </div>
        ))
      }
      </div>

    </div>
  )
}
