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
import s from './CompanyProfile.css';
import {Grid, Image, Divider, Header, Label, Statistic, Message} from 'semantic-ui-react';

class CompanyProfile extends React.Component {

  render() {
    return (
      <div>
        <Grid>
          <Grid.Row>
            <Grid.Column width={4}>
              <Image
                src={'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Dropbox_logo_2015.svg/2000px-Dropbox_logo_2015.svg.png'}/>
            </Grid.Column>
            <Grid.Column width={12}>
              <Header as='h3'>Mission Statement</Header>
              <p>
                Lorem ipsum dolor sit amet, vix appetere perfecto neglegentur ut. Ei cum accumsan phaedrum antiopam,
                illud
                blandit pro no, sit etiam antiopam te. Ne vel illum evertitur expetendis. Veri malis semper an vel, ne
                usu
                habeo efficiendi. Erant nobis incorrupte te his.
              </p>
            </Grid.Column>
          </Grid.Row>
          <Grid.Row>
            <Label className={s.label} color='grey' tag>Tag</Label>
            <Label className={s.label} color='grey' tag>Tag</Label>
            <Label className={s.label} color='grey' tag>Tag</Label>
            <Label className={s.label} color='grey' tag>Tag</Label>
            <Label className={s.label} color='grey' tag>Tag</Label>
            <Label className={s.label} color='grey' tag>Tag</Label>
            <Label className={s.label} color='grey' tag>Tag</Label>
          </Grid.Row>
          <Divider/>
          <Grid.Row centered>
            <Statistic.Group>
              <Statistic>
                <Statistic.Value>70%</Statistic.Value>
                <Statistic.Label>Uniqueness</Statistic.Label>
              </Statistic>
              <Statistic>
                <Statistic.Value>$40,000,00</Statistic.Value>
                <Statistic.Label>Revenue</Statistic.Label>
              </Statistic>
              <Statistic>
                <Statistic.Value>3</Statistic.Value>
                <Statistic.Label>Founders</Statistic.Label>
              </Statistic>
              <Statistic>
                <Statistic.Value>124</Statistic.Value>
                <Statistic.Label>Employees</Statistic.Label>
              </Statistic>
            </Statistic.Group>
          </Grid.Row>
          <Divider className={s.removeSpace}/>
        </Grid>
        <Header as='h3'>Responses</Header>
        <Message>
          <Message.Header>
            What is the question I have here?
          </Message.Header>
          <p>
            Lorem ipsum dolor sit amet, vix appetere perfecto neglegentur ut. Ei cum accumsan phaedrum antiopam,
            illud
            blandit pro no, sit etiam antiopam te. Ne vel illum evertitur expetendis. Veri malis semper an vel, ne
            usu
            habeo efficiendi. Erant nobis incorrupte te his.
          </p>
        </Message>
        <Message>
          <Message.Header>
            What is the question I have here?
          </Message.Header>
          <p>
            Lorem ipsum dolor sit amet, vix appetere perfecto neglegentur ut. Ei cum accumsan phaedrum antiopam,
            illud
            blandit pro no, sit etiam antiopam te. Ne vel illum evertitur expetendis. Veri malis semper an vel, ne
            usu
            habeo efficiendi. Erant nobis incorrupte te his.
          </p>
        </Message>
        <Message>
          <Message.Header>
            What is the question I have here?
          </Message.Header>
          <p>
            Lorem ipsum dolor sit amet, vix appetere perfecto neglegentur ut. Ei cum accumsan phaedrum antiopam,
            illud
            blandit pro no, sit etiam antiopam te. Ne vel illum evertitur expetendis. Veri malis semper an vel, ne
            usu
            habeo efficiendi. Erant nobis incorrupte te his.
          </p>
        </Message>
        <Divider hidden />
      </div>
    );
  }
}

export default withStyles(s)(CompanyProfile);
