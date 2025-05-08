import "./App.css"

import About from '@components/about/About.jsx'
import Features from '@components/features/Features.jsx'
import Footer from '@components/footer/footer.jsx'
import Gallery from '@components/gallery/Gallery.jsx'
import Header from '@components/header/header.jsx'
import Home from '@components/home/Home.jsx'
import Menu from '@components/menu/Menu.jsx'
import Testimonials from '@components/testimonials/Testimonials.jsx'





const App = () => {
  return (
    <>
    <Header />
    <Home />
    <Features />    
    <About />
    <Menu />
    <Gallery />
    <Testimonials />
    <Footer /> 
    
    </>
  )
}
export default App