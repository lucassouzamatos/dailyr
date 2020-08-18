import React from 'react';

import Enzyme, { mount } from 'enzyme';
import EnzymeAdapter from 'enzyme-adapter-react-16';

import { Loading } from '~/components';

Enzyme.configure({ adapter: new EnzymeAdapter() });

describe('<Loading /> unit test', () => {
  const wrapper = props => mount(<Loading {...props} />);

  it('should show by default', () => {
    expect(getComputedStyle(wrapper({ visible: true }).getDOMNode())
      .getPropertyValue('transform'))
      .not.toBe('translateY(-100vh)');
  })

  it('should hide if visible modifies to false', () => {
    expect(getComputedStyle(wrapper({ visible: false }).getDOMNode())
      .getPropertyValue('transform'))
      .toBe('translateY(-100vh)');
  });
});