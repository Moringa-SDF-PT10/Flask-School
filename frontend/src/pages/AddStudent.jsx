import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";

export default function AddStudent() {
  const [onChange, setOnChange] = useState(false)

  const [students, setStudents] = useState([]);
  const [houses, setHouses] = useState([])
  const [form, setForm] = useState({
    full_name: "",
    boarding_house: "", 
    age: "",
    email: "",
    bio: ""
  });

  // fetch student
  useEffect(() => {
      fetch("http://localhost:5000/students")
      .then((response) => response.json())
      .then((data) => setStudents(data))
      .catch((error) => toast.error("Error fetching students:", error));

     fetch("http://localhost:5000/houses")
    .then( res => res.json() )
    .then((data)=>{
      setHouses(data)
      console.log("Houses ",data)
      
    })
  }, [onChange]);


  console.log(students);
  console.log('====================================');

  // === add student
  const onAddStudent = (e) => {
    e.preventDefault();
     fetch("http://localhost:5000/students", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    })
    .then((res) => res.json())
    .then((res) => {
      
      if(res.id){
          setOnChange(!onChange)
          toast.success("Student added successfully");
          setForm({ full_name: "", age: "", email: "", bio: "", boarding_house: "" });
      }
      else{
        toast.error("Error adding student")

      }
      

    })
    .catch((error) => toast.error("Error adding student:", error));
  };

  // === delete student
  const deleteStudent = async (id) => {
    fetch("http://localhost:5000/students/" + id, {
      method: "DELETE"
    })
    .then((res) => res.json())
    .then((res) => {
        if(res.success){
             setOnChange(!onChange)
              toast.success(res.success);
        }
        else{
          toast.error("Error deleting student")
        }
   
    })
    .catch((error) => toast.error("Error deleting student:", error));
  };
    


  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow-lg p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">Add Student</h2>

        {/* Form */}
        <form
          onSubmit={onAddStudent}
          className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8"
        >
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Full Name"
            value={form.full_name}
            onChange={(e) => setForm({ ...form, full_name: e.target.value })}
            required
          />
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Age"
            type="number"
            value={form.age}
            onChange={(e) => setForm({ ...form, age: e.target.value })}
            required
          />
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Email"
            value={form.email}
            onChange={(e) => setForm({ ...form, email: e.target.value })}
          />
          <input
            className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
            placeholder="Bio"
            value={form.bio}
            onChange={(e) => setForm({ ...form, bio: e.target.value })}
          />

          <div>
              <label className="block text-sm font-medium text-gray-700"> Boarding House  </label>
              <select
                className="border rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 outline-none"
                value={form.boarding_house}
                onChange={(e) => setForm({ ...form, boarding_house: e.target.value })}
              >
                <option value="">Select Boarding House</option> 
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
            Add Student
          </button>
        </form>

        {/* Students Table */}
        <h2 className="text-xl font-semibold text-gray-700 mb-4">
          Students List
        </h2>
        <div className="overflow-x-auto">
          <table className="min-w-full bg-white border border-gray-200 rounded-lg overflow-hidden shadow">
            <thead className="bg-gray-200 text-gray-700">
              <tr>
                <th className="py-2 px-4 border-b">ID</th>
                <th className="py-2 px-4 border-b">Full Name</th>
                <th className="py-2 px-4 border-b">Age</th>
                <th className="py-2 px-4 border-b">Email</th>
                <th className="py-2 px-4 border-b">Bio</th>
                <th className="py-2 px-4 border-b">Boarding House</th>
                <th className="py-2 px-4 border-b">Action</th>
              </tr>
            </thead>
            <tbody>
              {students.map((s, index) => (
                <tr
                  key={s.id}
                  className={index % 2 === 0 ? "bg-gray-50" : "bg-white"}
                >
                  <td className="py-2 px-4 border-b">{s.id}</td>
                  <td className="py-2 px-4 border-b">{s.full_name}</td>
                  <td className="py-2 px-4 border-b">{s.age}</td>
                  <td className="py-2 px-4 border-b">{s.email}</td>
                  <td className="py-2 px-4 border-b">{s.bio}</td>
                  <td className="py-2 px-4 border-b">{s.boarding_house}</td>
                  <td className="flex gap-2 py-2 px-4 border-b text-center">
                    <button
                      onClick={() => deleteStudent(s.id)}
                      className="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 transition duration-200"
                    >
                      Delete
                    </button>

                    <Link to={`/student/${s.id}`} className="border px-3 py-1">Edit Student</Link>
                  </td>
                </tr>
              ))}
              {students.length === 0 && (
                <tr>
                  <td
                    colSpan="6"
                    className="text-center py-4 text-gray-500 italic"
                  >
                    No students found
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
