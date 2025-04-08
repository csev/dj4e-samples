import { html, LitElement } from "https://cdn.jsdelivr.net/npm/lit@3.2.1/+esm";

// https://stackoverflow.com/questions/68614776/using-lit-with-javascript-and-no-build-tools

export class SimpleGreeting extends LitElement {

  static properties =  {
    name: { type: String }
  };

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

