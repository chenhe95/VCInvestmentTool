/**
 * React Starter Kit (https://www.reactstarterkit.com/)
 *
 * Copyright © 2014-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import React from 'react';
import PropTypes from 'prop-types';
import withStyles from 'isomorphic-style-loader/lib/withStyles';
import s from './Home.css';
import { Button, Header } from 'semantic-ui-react';

class Home extends React.Component {
  static propTypes = {
    news: PropTypes.arrayOf(
      PropTypes.shape({
        title: PropTypes.string.isRequired,
        link: PropTypes.string.isRequired,
        content: PropTypes.string,
      }),
    ).isRequired,
  };

  render() {
    return (
      <div className={s.root}>
        <h1 className={s.header}>WHICH ARE YOU?</h1>
        <div>
          <Button onClick={() => window.location.pathname = '/form'} inverted={'true'} size={'massive'} color={'violet'}>COMPANY</Button>
          <Button onClick={() => window.location.pathname = '/vchome'} inverted={'true'} size={'massive'} color={'violet'}>INVESTOR</Button>
        </div>
      </div>
    );
  }
}

export default withStyles(s)(Home);
