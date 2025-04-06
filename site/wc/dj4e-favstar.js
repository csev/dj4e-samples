import {html, css, LitElement} from 'https://cdn.jsdelivr.net/gh/lit/dist@2.4.0/core/lit-core.min.js';

// https://stackoverflow.com/questions/68614776/using-lit-with-javascript-and-no-build-tools

export class DJ4EFavoriteStar extends LitElement {

  static get properties() {
    return {
      fav: {type: String}
    }
  }

  constructor() {
    super();
    this.fav = false;
  }

  // Don't use Shadow-DOM 
  createRenderRoot() { return this;}

  render() {
    return this.fav == 'true'
    ? html`<span class="fa-stack" style="vertical-align: middle;">
        <i class="fa fa-star fa-stack-1x" style="color: orange;"></i>
        <i class="fa fa-star-o fa-stack-1x"></i>
        </span>`
    : html`<span class="fa-stack" style="vertical-align: middle;">
        <i class="fa fa-star fa-stack-1x" style="display: none; color: orange;"></i>
        <i class="fa fa-star-o fa-stack-1x"></i>
        </span>`
    ;
  }
}

customElements.define('dj4e-favstar', DJ4EFavoriteStar);

