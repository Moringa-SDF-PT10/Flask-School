import { useState } from 'react'
import {BrowserRouter, Route, Routes} from "react-router-dom"
import Layout from './components/Layout'
import NoPage from './pages/NoPage'
import AddCourse from './pages/AddCourse'
import AddStudent from './pages/AddStudent'
import Home from './pages/Home'
import AddBoardingHouse from './pages/AddBoardingHouse'
import EditStudent from './pages/EditStudent'


function App() {


  return (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path='/addstudent' element={<AddStudent />} />
        <Route path='/student/:id' element={<EditStudent />} />
        <Route path='/addcourse' element={<AddCourse />} />
        <Route path='/addboardinghouse' element={<AddBoardingHouse />} />
        <Route path='*' element={<NoPage />} />
      
      </Route>
    </Routes>  
  </BrowserRouter>
  )
}

export default App
