import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation } from 'swiper/modules';
import { homeSlide } from '../../Data'; 

import 'swiper/css';
import 'swiper/css/navigation';
import './home.css'

import ScrollLink from '@components/link/ScrollLink.jsx'
import { FaArrowLeft, FaArrowRight, FaArrowCircleRight } from "react-icons/fa";


import parse from 'html-react-parser';

const Home = () => {
  return (
    <section className="home">
    <Swiper
    speed={2000}
      modules={[Navigation]} 
      navigation={{
        nextEl: '.next-btn',
        prevEl: '.prev-btn',
      }} 
    >
      {homeSlide.map(({ img, title, description }, index) => {
        return (
          <SwiperSlide className='home-slide section' style={{ backgroundImage: `url(${img})`, backgroundSize: 'cover', }} key={index}>
            <div className='home-data container'>
              <h3 className='home-subtitle'>Welcome to Alfa Gourmand</h3>
              <h1 className="home-title">{parse(title)}</h1>

              <p className='home-description'>{description}</p>
              <div className='home-buttons'>
                <ScrollLink 
                  to='about' 
                  name='Abput more' 
                  className='button' 
                  icon={<FaArrowCircleRight className='button-icon' />}
                />
                <ScrollLink 
                  to='menu' 
                  name='Check Menu' 
                  className='button home-button' 
                  icon={<FaArrowCircleRight className='button-icon' />}
                />
              </div>
            </div>
          </SwiperSlide>          
        );
      })}

      <button className='swiper-btn prev-btn'>
        <FaArrowLeft />
      </button>

      <button className='swiper-btn next-btn'>
        <FaArrowRight />
      </button>

      

    </Swiper>
    </section>
  )
}
export default Home

