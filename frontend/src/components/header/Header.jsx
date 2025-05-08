import LogoHeader from '@assets/LogoHeader.png'
import { navLinks } from '../../Data'
import ScrollLink from '@components/link/ScrollLink.jsx'
import { FaArrowCircleRight } from "react-icons/fa";
import { CgMenuLeft } from "react-icons/cg";

import './../header/header.css'

const Header = () => {
    return (
      <header className='header'>
        <nav className='nav container'>
          <a href="/" className='nav-logo'>
            <img src={LogoHeader} alt="Logo" className='nav-logo-img' />  
          </a>

          <div className='nav-menu'>
            <ul className='nav-list'>
              {navLinks.map((navLink, index) => {
                return (
                  <li className='nav-item' key={index}>
                    <ScrollLink 
                      to={navLink} 
                      name={navLink} 
                      className='nav-link' 
                    />
                  </li>
                );
              })}
            </ul>
          </div>

          <div className='nav-buttons'>
            <ScrollLink 
              to='reservation' 
              name='Reseñas' 
              className='button' 
              icon={<FaArrowCircleRight className='button-icon' />}
            />

            <CgMenuLeft className='nav-toggler' />
          </div> 
        </nav>
      </header>
    )
  }
  export default Header