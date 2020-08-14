import React, { useState, useEffect } from 'react';

import { Wrapper, Logo } from './Loading.styles';

interface ILoadingProps {
  visible: boolean;
}

const Loading : React.FC<ILoadingProps> = ({ visible }) => {
  const [close, setClose] = useState<boolean>(false);

  useEffect(() => { 
    !visible && setClose(true);
  }, [visible])

  return (
    <Wrapper close={close}>
      <Logo />
    </Wrapper>
  )
}

export default Loading;