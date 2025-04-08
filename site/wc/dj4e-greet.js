import { html, LitElement } from "https://cdn.jsdelivr.net/npm/lit@3.2.1/+esm";

export class SimpleGreeting extends LitElement {

  static properties =  {
    name: { type: String }
  };

  constructor() {
    super();
    this.name = 'Somebody';
  }

  // Inherit CSS from enclosing document
  createRenderRoot() { return this;}

  render() {
    return html`<p>Hello, ${this.name}!</p>`;
  }
}

customElements.define('dj4e-greeting', SimpleGreeting);

