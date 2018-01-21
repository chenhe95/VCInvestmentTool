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
import {Grid, Input, Button, Icon, Pagination, Sticky, Loader} from 'semantic-ui-react';
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
    grid: true,
    loading: true,
    companies: []
  };

  componentDidMount() {
    fetch('http://localhost:5000/company_all_digest')
      .then(x => x.json())
      .then(json => this.setState({companies: json, loading: false}))
  }

  render() {
    let content;
    if (this.state.loading) {
      content = (
        <div style={{width: '100%', height: '60vh'}}>
          <Loader active inline='centered'/>
        </div>
      );
    } else {
      content = (
        <Grid centered columns={'equal'}>
          { this.state.companies.map(company => <Card {...company}/>) }
        </Grid>
      )
    }

    return (
      <div>
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
        {content}
        <Pagination className={s.paginator} defaultActivePage={1} totalPages={3}/>
      </div>
    );
  }
}

export default withStyles(s)(VCHome);
