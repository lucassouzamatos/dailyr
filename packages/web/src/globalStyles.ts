import { createGlobalStyle } from 'styled-components';

import MetropolisBoldFont from '~/assets/fonts/Metropolis-Bold.otf';
import MetropolisRegularFont from '~/assets/fonts/Metropolis-Regular.otf';
import MetropolisSemiBoldFont from '~/assets/fonts/Metropolis-SemiBold.otf';

export default createGlobalStyle`
  @font-face {
    font-family: MetropolisBold;
    src: url(${MetropolisBoldFont});
  }

  @font-face {
    font-family: MetropolisRegular;
    src: url(${MetropolisRegularFont});
  }

  @font-face {
    font-family: MetropolisSemiBold;
    src: url(${MetropolisSemiBoldFont});
  }

  * {
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
  }
  *:focus {
    outline: 0;
  }
  
  html,
  body,
  #root {
    min-height: 100vh;
  }
  body {
    font: 14px 'MetropolisRegular', sans-serif;
    background-color: #202225;
  }
`;
