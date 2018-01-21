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
import s from './VCHome.css';
import {Grid, Input, Button, Icon, Pagination, Sticky} from 'semantic-ui-react';
import Card from '../../components/List/Card';

class VCHome extends React.Component {
  static propTypes = {
    news: PropTypes.arrayOf(
      PropTypes.shape({
        title: PropTypes.string.isRequired,
        link: PropTypes.string.isRequired,
        content: PropTypes.string,
      }),
    ).isRequired,
  };

  state = {
    grid: true
  };

  render() {
    return (
      <div>
        <Sticky/>
        <div className={s.options}>
          <Input
            className={s.search}
            icon={{name: 'search', circular: true, link: true}}
            placeholder='Search...'
          />
          <Button.Group className={s.displayMode}>
            <Button icon active={this.state.grid}>
              <Icon name='grid layout'/>
            </Button>
            <Button icon active={!this.state.grid}>
              <Icon name='list layout'/>
            </Button>
          </Button.Group>
        </div>
        <Sticky/>
        <Grid centered columns={'equal'}>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
          <Card/>
        </Grid>
        <Pagination className={s.paginator} defaultActivePage={5} totalPages={10}/>
      </div>
    );
  }
}

export default withStyles(s)(VCHome);
