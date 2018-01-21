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
import s from './Form.css';
import Particles from 'react-particles-js';
import {
  Sticky,
  Container,
  Header,
  Divider,
  Button,
  Transition,
} from 'semantic-ui-react';

class Form extends React.Component {
  particleConfig = {
    "particles": {
      "number": {
        "value": 80,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": "#9d9d9d"
      },
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0,
          "color": "#000000"
        },
        "polygon": {
          "nb_sides": 5
        },
        "image": {
          "src": "img/github.svg",
          "width": 100,
          "height": 100
        }
      },
      "opacity": {
        "value": 0.5,
        "random": false,
        "anim": {
          "enable": false,
          "speed": 1,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 3,
        "random": true,
        "anim": {
          "enable": false,
          "speed": 40,
          "size_min": 0.1,
          "sync": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#ffffff",
        "opacity": 0.4,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 2,
        "direction": "none",
        "random": false,
        "straight": false,
        "out_mode": "out",
        "bounce": false,
        "attract": {
          "enable": false,
          "rotateX": 600,
          "rotateY": 1200
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": false,
          "mode": "repulse"
        },
        "onclick": {
          "enable": false,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 400,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 400,
          "size": 40,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true
  };

  state = {
    phase: 0,
    questions: [
      'What is your company name?',
      'What is your company logo?',
      "What is your company's tagline?",
      'What is your business model?',
      'What are your main KPIs?',
      'How much money have you made so far?',
      'How many founders are you?',
      'How many employees do you have so far?',
      'How much are you planning to raise?',
    ],
    responses: {
      '0': '',
      '1': '',
      '2': '',
      '3': '',
      '4': '',
      '5': '',
      '6': '',
      '7': '',
      '8': '',
      '9': '',
    },
  };

  increment = () => this.setState({ phase: this.state.phase + 1 });

  deincrement = () => this.setState({ phase: this.state.phase - 1 });

  onChange = event => {
    const { responses } = this.state;
    responses[this.getQuestion()] = event.target.value;
    this.setState({ responses });
    console.log(responses);
  };

  onSubmit = () => {
    fetch('http://localhost:5000/startup_registration', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.state.responses),
    });
    this.setState({ phase: -1 });
  };

  getQuestion = () => this.state.phase - 2;

  render() {
    return (
      <div>
        <Transition visible={this.state.phase === -1} animation="fly right">
          <div>
            <Container className={s.container}>
              <Header textAlign="center" color="violet" as="h1" inverted>
                SUBMIT!
              </Header>
              <p style={{ 'font-size': '20px', color: 'white' }}>
                Someone will hopefully be in contact with you soon after we
                properly analyze the data and see how you match up with our
                fund!
              </p>
            </Container>
          </div>
        </Transition>
        <Transition
          visible={this.state.phase === 0}
          animation="fly right"
          onComplete={this.increment}
        >
          <div>
            <Container className={s.container}>
              <Header textAlign="center" color="violet" as="h1" inverted>
                STARTUP APPLICATION
              </Header>
              <Divider hidden clearing />
              <Button
                color="violet"
                inverted
                size="massive"
                onClick={this.increment}
              >
                Begin
              </Button>
            </Container>
          </div>
        </Transition>
        <Transition visible={this.getQuestion() >= 0}>
          <div className={s.questioner}>
            <h1 className={s.question}>
              {this.state.questions[this.getQuestion()]}
            </h1>
            <div className={s.content}>
              <textarea
                value={this.state.responses[this.getQuestion()]}
                onChange={this.onChange}
                autoFocus
              />
            </div>
            <div className={s.footer}>
              <div>
                <Button
                  disabled={this.getQuestion() <= 0}
                  onClick={this.deincrement}
                  size="big"
                  attached="left"
                  icon="left chevron"
                />
                <Button
                  disabled={
                    this.getQuestion() >= this.state.questions.length - 1
                  }
                  onClick={this.increment}
                  size="big"
                  attached="right"
                  icon="right chevron"
                />
                <Button
                  onClick={this.onSubmit}
                  inverted
                  disabled={
                    this.getQuestion() !== this.state.questions.length - 1
                  }
                  style={{ 'margin-left': '15px' }}
                  color="violet"
                  size="big"
                >
                  Submit
                </Button>
              </div>
            </div>
          </div>
        </Transition>
        <Particles className={s.canvas} params={this.particleConfig} />
      </div>
    );
  }
}

export default withStyles(s)(Form);
