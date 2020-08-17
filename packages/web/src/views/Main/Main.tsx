import React, { useState, useEffect } from 'react';

import { Loading } from '~/components';

export default function Main() {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    /**
     * temporary implementation
     */
    setTimeout(() => {
      setVisible(false);
    }, 5000);
  }, [])

  return (
    <Loading visible={visible} />
  )
}