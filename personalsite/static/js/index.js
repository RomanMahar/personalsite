import _ from 'lodash';

import {} from '../less/styles.less'

function component() {
  var element = document.createElement('div');

  // Lodash, currently included via a script, is required for this line to work
  element.innerHTML = _.join(['Haxlo', 'Spacepack'], ' ');

  return element;
}

document.body.appendChild(component());