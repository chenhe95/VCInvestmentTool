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
import {Card as SemanticCard, Image, Icon} from 'semantic-ui-react';
import withStyles from 'isomorphic-style-loader/lib/withStyles';
import s from './Card.css';

class Card extends React.Component {

  render() {
    return (
      <SemanticCard className={s.card}>
        <div className={s.imageWrapper}>
          <Image src={'https://assets-cdn.github.com/images/modules/logos_page/GitHub-Logo.png'}/>
        </div>
        <SemanticCard.Content>
          <SemanticCard.Header>
            Matthew
          </SemanticCard.Header>
          <SemanticCard.Meta>
        <span className='date'>
          Joined in 2015
        </span>
          </SemanticCard.Meta>
          <SemanticCard.Description>
            Matthew is a musician living in Nashville.
          </SemanticCard.Description>
        </SemanticCard.Content>
        <SemanticCard.Content extra>
          <a>
            <Icon name='user'/>
            21 Friends
          </a>
        </SemanticCard.Content>
      </SemanticCard>
    );
  }
}

export default withStyles(s)(Card);

