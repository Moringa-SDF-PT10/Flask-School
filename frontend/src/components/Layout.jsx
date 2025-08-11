import React from 'react'
import { Outlet } from 'react-router-dom'
import Navbar from "./Navbar"
import Footer from './Footer'
import { ToastContainer } from 'react-toastify';


export default function Layout() 
{
  return (
    <div>
        <Navbar />

        <div className='mx-12 p-4  min-h-[90vh]'>
         <Outlet /> {/*render the current route selected */}
        </div>
        <ToastContainer />

        <Footer />
        
        
    </div>
  )
}
