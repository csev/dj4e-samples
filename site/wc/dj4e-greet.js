import {html, css, LitElement} from 'https://cdn.jsdelivr.net/gh/lit/dist@2.4.0/core/lit-core.min.js';

// https://stackoverflow.com/questions/68614776/using-lit-with-javascript-and-no-build-tools

export class SimpleGreeting extends LitElement {

  static get properties() {
    return {
      name: {type: String}
    }
  }

  constructor() {
    super();
    this.name = 'Somebody';
  }

  // Don't use Shadow-DOM 
  createRenderRoot() { return this;}

  render() {
    return html`<p>Hello, ${this.name}!</p>`;
  }
}

customElements.define('dj4e-greeting', SimpleGreeting);

