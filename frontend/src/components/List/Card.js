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
import {Card as SemanticCard, Image, Icon, Label} from 'semantic-ui-react';
import withStyles from 'isomorphic-style-loader/lib/withStyles';
import s from './Card.css';

class Card extends React.Component {


  static propTypes = {
    name: PropTypes.string.isRequired,
    founder: PropTypes.string.isRequired,
    revenue: PropTypes.string.isRequired,
    employees: PropTypes.string.isRequired,
    model: PropTypes.string.isRequired,
    tagline: PropTypes.string.isRequired,
    tags: PropTypes.arrayOf(PropTypes.string).isRequired,
    uniqueness: PropTypes.number.isRequired,
    logo: PropTypes.string.isRequired,
    id: PropTypes.string.isRequired,
    responses: PropTypes.arrayOf(PropTypes.string).isRequired,
  };


  render() {
    return (
      <SemanticCard href={`/vc/company/${this.props.id}`} className={s.card}>
        <div className={s.imageWrapper}>
          <Image src={this.props.logo.trim()}/>
        </div>
        <SemanticCard.Content>
          <SemanticCard.Header>
            {this.props.name}
          </SemanticCard.Header>
          <SemanticCard.Meta>
        <span className='date'>
          It is {Math.floor(this.props.uniqueness) * 100}% unique.
        </span>
          </SemanticCard.Meta>
          <SemanticCard.Description>
            {this.props.model}
          </SemanticCard.Description>
        </SemanticCard.Content>
        <SemanticCard.Content extra>
          {this.props.tags.slice(0, 2).map(tag => (
            <Label>
              {tag}
            </Label>
          ))}
        </SemanticCard.Content>
      </SemanticCard>
    );
  }
}

export default withStyles(s)(Card);

