/**
 * React Starter Kit (https://www.reactstarterkit.com/)
 *
 * Copyright © 2014-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import React from 'react';
import cx from 'classnames';
import withStyles from 'isomorphic-style-loader/lib/withStyles';
import s from './Navigation.css';
import Link from '../Link';
import { Image, Dropdown } from 'semantic-ui-react';
import profile from './profile.jpg';

class Navigation extends React.Component {
  render() {
    const trigger = <Image avatar src={profile} />;
    const options = [
      { key: 'user', text: 'Account', icon: 'user' },
      { key: 'settings', text: 'Settings', icon: 'settings' },
      { key: 'sign-out', text: 'Sign Out', icon: 'sign out' },
    ];
    return (
      <div size={'big'} className={s.root} role="navigation">
        <Dropdown trigger={trigger} options={options} pointing='top right' icon={null} />
      </div>
    );
  }
}

export default withStyles(s)(Navigation);
