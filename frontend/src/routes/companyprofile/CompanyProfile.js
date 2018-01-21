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
import {Grid, Image, Divider, Header, Label, Statistic, Message, Loader} from 'semantic-ui-react';


const withCommas = (x) => x.replace(/\B(?=(\d{3})+(?!\d))/g, ",");

class CompanyProfile extends React.Component {

  static propTypes = {
    id: PropTypes.string.isRequired
  };


  state = {
    loaded: false,
    company: {}
  };


  componentDidMount() {
    fetch(`http://localhost:5000/company_digest/${this.props.id}`)
      .then(x => x.json())
      .then(company => this.setState({company: company, loaded: true}));
  }

  /**
   * {
  "name": "asdsadsda",
  "founder": "aaaa",
  "revenue": "sdasad",
  "employees": "sdsds",
  "tags": [
    "money",
    "people"
  ],
  "uniqueness": 0.35,
  "logo": "zxcxzcxczzxz ds",
  "id": 4349647296,
  "responses": []
}
   */
  render() {
    if (this.state.loaded) {
      const { company } = this.state;
      return (
        <div>
          <Grid>
            <Grid.Row>
              <Grid.Column width={4}>
                <Image
                  src={company.logo}/>
              </Grid.Column>
              <Grid.Column width={12}>
                <Header as='h3'>Mission Statement</Header>
                <p>{company.model}</p>
                <p>{company.tagline}</p>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              {company.tags.map(tag => <Label className={s.label} color='grey' tag>{tag}</Label>)}
            </Grid.Row>
            <Divider/>
            <Grid.Row centered>
              <Statistic.Group>
                <Statistic>
                  <Statistic.Value>{Math.floor(company.uniqueness * 100)}%</Statistic.Value>
                  <Statistic.Label>Uniqueness</Statistic.Label>
                </Statistic>
                <Statistic>
                  <Statistic.Value>${withCommas(company.revenue)}</Statistic.Value>
                  <Statistic.Label>Revenue</Statistic.Label>
                </Statistic>
                <Statistic>
                  <Statistic.Value>{withCommas(company.founder)}</Statistic.Value>
                  <Statistic.Label>Founders</Statistic.Label>
                </Statistic>
                <Statistic>
                  <Statistic.Value>{withCommas(company.employees)}</Statistic.Value>
                  <Statistic.Label>Employees</Statistic.Label>
                </Statistic>
              </Statistic.Group>
            </Grid.Row>
            <Divider className={s.removeSpace}/>
          </Grid>
          <Header as='h3'>Responses</Header>
          <Message>
            <Message.Header>
              Tell us in one or two sentences something about each founder that shows a high level of ability.
            </Message.Header>
            <p>
              Alexis is currently writing 80page Honors thesis on 20th century German history, taking a 21 credit hour semester (7 classes), acting in the lead role of a student film, preparing for an International Business German exam in April, fulfilling the final requirements for his dual-concentration degree in the McIntire School of Commerce and planning a startup software company.

              Andy: [redacted]

              Steve: Steve was hired out of high school to work as a programmer/systems administrator for a local software company (Image Matters LLC).
            </p>
          </Message>
          <Message>
            <Message.Header>
              Tell us in one or two sentences something about each founder that shows he or she is an "animal," in the sense described in How to Start a Startup.
            </Message.Header>
            <p>
              Animals? We're a freaking zoo.

              Andy: When Paul described the type of person whom he believes is an animal at his "How to Start a Startup" talk, Andy was the first person of whom I (Steve) thought.

              Steve: Steve regularly works extra hours at his current programming job, even when over-time isn't an option (i.e. working for free) to fix nagging bugs. At school, Steve often works late nights with Computer Science friends helping them get assignments working.

              Alexis: See current schedule. When it comes to design, Alexis literally won't rest until every pixel is aligned--sleep deprivation is the status quo and when it comes to working in general, coffee makes sure he's the last one to go to sleep at night and the first one up in the morning.
            </p>
          </Message>
          <Message>
            <Message.Header>
              For founders who are hackers: what cool things have you built? (Extra points for urls of demos or screenshots.)
            </Message.Header>
            <p>
              Steve: Steve is currently working on his undergraduate thesis, which is a web application written in Lisp. Other notable projects include a rigid-body simulator to lay out graphs and a distributed raytracer. (Some screenshots from the raytracer are at http://www.people.virginia.edu/~slh6d/raytracer/ ).

              Andy: I wrote a set of php scripts to accept an image, find barcodes, decode the barcode, and look up prices on amazon. (Note: Paul, if you recall from when we spoke in Cambridge, this was something we spoke about).

              Alexis: He's done our logo. View at
            </p>
          </Message>
          <Divider hidden/>
        </div>
      )
    } else {
      return (
        <div style={{height: '70vh', width: '100%'}}>
          <Loader active inline='centered'/>
        </div>
      )
    }
  }
}

export default withStyles(s)(CompanyProfile);
