import styled, { keyframes, css } from 'styled-components';
import LogoImage from '~/assets/logo-loading.png';

const PulseAnimation = keyframes`
  0% { 
    transform: scale(0.9) 
  }
  50% { 
    transform: scale(1.2) 
  }
  100% { 
    transform: scale(0.9) 
  }
`;

interface IWrapperProps {
  close: boolean
}

export const Wrapper = styled.div<IWrapperProps>`
  display: flex;
  height: 100vh;
  width: 100%;
  align-items: center;
  justify-content: center;
  transition: all 1s 1s ease-in-out;
  background: #27292C;
  position: fixed;
  top: 0;
  left: 0;
  
  ${props => props.close && css`
    transform: translateY(-100vh);
  `}
`;


interface ILogoProps {
  close?: boolean
}

export const Logo = styled.div<ILogoProps>`
  display: flex;
  width: 300px;
  height: 100px;
  background-image: url(${LogoImage});
  background-repeat: no-repeat;
  background-position: center;
  scale: 0.6;
  animation: ${PulseAnimation} 1.5s cubic-bezier(0.52, -0.01, 0.46, 1.01) infinite;
  transition: all 1s ease-in-out;

  ${props => props.close && css`
    transform: translateY(-100vh);
  `}
`;